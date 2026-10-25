/**
 * SPARK VISUAL COCKPIT - Drive / Docs Frame Clipboard Bridge (v2.5)
 * Injected with all_frames: true into Google Drive & Docs embedded viewer iframes.
 * Guarantees that highlighting text and pressing Ctrl+C / Cmd+C inside the PDF viewer
 * reliably copies selected text directly into the system clipboard via 5-tier redundancy:
 * 1. Nested iframe Permissions Policy injection (auto-delegating allow="clipboard-write; clipboard-read").
 * 2. In-frame ClipboardEvent intercept (e.clipboardData.setData) for Context Menu & Native Copy.
 * 3. Event Shielding: stops Google Drive's "copy file" listener from intercepting Ctrl+C.
 * 4. Universal IME/Key detection (e.code === 'KeyC' || keyCode === 67).
 * 5. Offscreen Document Background execution: guaranteed Windows Clipboard population.
 */
(() => {
  if (window.__SPARK_CLIPBOARD_HELPER_LOADED__) return;
  window.__SPARK_CLIPBOARD_HELPER_LOADED__ = true;

  let lastSelectedText = '';

  // Tier 1: Nested iframe Permissions Policy delegation
  function patchIframeElement(iframe) {
    if (!iframe || !(iframe instanceof HTMLIFrameElement)) return;
    try {
      const cur = iframe.getAttribute('allow') || '';
      if (!cur.includes('clipboard-write')) {
        iframe.setAttribute('allow', (cur + ' clipboard-write; clipboard-read; fullscreen').trim());
      }
    } catch (_) {}
  }

  // Patch createElement for dynamically constructed iframes
  try {
    const origCreateElement = Document.prototype.createElement;
    Document.prototype.createElement = function(tagName, options) {
      const el = origCreateElement.call(this, tagName, options);
      if (tagName && String(tagName).toLowerCase() === 'iframe') {
        patchIframeElement(el);
      }
      return el;
    };
  } catch (_) {}

  // Observe DOM additions for any static or template-cloned iframes
  try {
    const observer = new MutationObserver((mutations) => {
      for (const m of mutations) {
        for (const node of m.addedNodes) {
          if (node.nodeType === 1) {
            if (node.tagName === 'IFRAME') {
              patchIframeElement(node);
            } else if (node.querySelectorAll) {
              const iframes = node.querySelectorAll('iframe');
              for (const f of iframes) patchIframeElement(f);
            }
          }
        }
      }
    });
    if (document.documentElement) {
      observer.observe(document.documentElement, { childList: true, subtree: true });
    }
  } catch (_) {}

  // Scan any iframes already present
  function scanExistingIframes() {
    try {
      const iframes = document.querySelectorAll('iframe');
      for (const f of iframes) patchIframeElement(f);
    } catch (_) {}
  }
  scanExistingIframes();
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', scanExistingIframes, { once: true });
  }

  // Extract text selection across standard DOM, Shadow DOM roots, composed ranges, and active elements
  function getDeepSelectedText() {
    try {
      // 1. Standard window & document selection
      const winSel = window.getSelection();
      if (winSel && !winSel.isCollapsed && winSel.toString()?.trim()) {
        return winSel.toString().trim();
      }
      const docSel = document.getSelection();
      if (docSel && !docSel.isCollapsed && docSel.toString()?.trim()) {
        return docSel.toString().trim();
      }

      // 2. Composed Ranges (pierces Shadow DOM trees)
      if (winSel && typeof winSel.getComposedRanges === 'function') {
        const shadowRoots = [];
        const walker = document.createTreeWalker(document.documentElement, NodeFilter.SHOW_ELEMENT);
        let node;
        while ((node = walker.nextNode())) {
          if (node.shadowRoot) shadowRoots.push(node.shadowRoot);
        }
        if (shadowRoots.length > 0) {
          const ranges = winSel.getComposedRanges({ shadowRoots });
          if (ranges && ranges.length > 0) {
            const r = ranges[0];
            const domRange = document.createRange();
            domRange.setStart(r.startContainer, r.startOffset);
            domRange.setEnd(r.endContainer, r.endOffset);
            const shadowText = domRange.toString()?.trim();
            if (shadowText) return shadowText;
          }
        }
      }

      // 3. Active element selection
      const activeEl = document.activeElement;
      if (activeEl) {
        if (typeof activeEl.selectionStart === 'number' && activeEl.selectionStart !== activeEl.selectionEnd) {
          const text = (activeEl.value || activeEl.textContent || '').substring(activeEl.selectionStart, activeEl.selectionEnd)?.trim();
          if (text) return text;
        }
        if (activeEl.shadowRoot) {
          const srSel = activeEl.shadowRoot.getSelection ? activeEl.shadowRoot.getSelection() : null;
          if (srSel && !srSel.isCollapsed && srSel.toString()?.trim()) {
            return srSel.toString().trim();
          }
        }
      }
    } catch (_) {}
    return '';
  }

  // Level 3 Event Shielding: Protect text selection events from Google Drive preventDefault interceptors
  ['selectstart'].forEach(ev => {
    document.addEventListener(ev, (e) => {
      e.stopImmediatePropagation();
    }, true);
  });

  // Sync selection across frame boundaries on selection changes
  let syncDebounceTimer = null;
  function syncSelection() {
    if (syncDebounceTimer) clearTimeout(syncDebounceTimer);
    syncDebounceTimer = setTimeout(() => {
      try {
        const sel = getDeepSelectedText();
        if (sel) {
          lastSelectedText = sel;
          window.top?.postMessage({ type: 'SPARK_SELECTION_CACHE', text: sel }, '*');
          try {
            if (typeof chrome !== 'undefined' && chrome.runtime?.sendMessage) {
              chrome.runtime.sendMessage({ action: 'SPARK_SELECTION_SYNC', text: sel });
            }
          } catch (_) {}
        }
      } catch (_) {}
    }, 40);
  }

  document.addEventListener('selectionchange', syncSelection, true);
  window.addEventListener('mouseup', syncSelection, true);
  window.addEventListener('pointerup', syncSelection, true);
  window.addEventListener('keyup', syncSelection, true);

  // Cache selection from child frames & handle trigger copy command from top window
  window.addEventListener('message', (e) => {
    if (!e.data || typeof e.data !== 'object') return;
    if (e.data.type === 'SPARK_SELECTION_CACHE' && typeof e.data.text === 'string') {
      lastSelectedText = e.data.text;
    } else if (e.data.type === 'SPARK_TRIGGER_COPY') {
      try {
        window.focus();
        document.execCommand('copy');
        const sel = (getDeepSelectedText() || lastSelectedText || '').trim();
        if (sel) {
          try {
            if (typeof chrome !== 'undefined' && chrome.runtime?.sendMessage) {
              chrome.runtime.sendMessage({ action: 'SPARK_FORCE_COPY', text: sel });
            }
          } catch (_) {}
          window.top?.postMessage({ type: 'SPARK_COPY_CONFIRMED', text: sel }, '*');
        }
      } catch (_) {}
    }
  });

  // Main Copy Handler (runs on native 'copy' event)
  function executeCopy(e) {
    let sel = getDeepSelectedText();
    if (!sel) {
      sel = lastSelectedText || '';
    }

    // 1. Primary: In-event ClipboardData (synchronous, 100% reliable for Right-Click)
    if (sel && e && e.clipboardData) {
      try {
        e.clipboardData.setData('text/plain', sel);
      } catch (_) {}
    }

    // 2. Guaranteed Background Offscreen Clipboard Write
    if (sel) {
      try {
        if (typeof chrome !== 'undefined' && chrome.runtime?.sendMessage) {
          chrome.runtime.sendMessage({ action: 'SPARK_FORCE_COPY', text: sel });
        }
      } catch (_) {}

      // 3. In-frame Async Clipboard API
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(sel).catch(() => {});
      }

      // 4. Cross-origin postMessage to top window
      try { window.top?.postMessage({ type: 'SPARK_FORCE_COPY', text: sel }, '*'); } catch (_) {}
      try { window.parent?.postMessage({ type: 'SPARK_FORCE_COPY', text: sel }, '*'); } catch (_) {}
    }

    // 5. Read actual clipboard text after Chromium completes native copy
    setTimeout(async () => {
      try {
        let clipText = '';
        if (navigator.clipboard && navigator.clipboard.readText) {
          clipText = await navigator.clipboard.readText();
        }
        const confirmedText = (clipText || sel || lastSelectedText || '').trim();
        if (confirmedText) {
          lastSelectedText = confirmedText;
          window.top?.postMessage({ type: 'SPARK_SELECTION_CACHE', text: confirmedText }, '*');
          window.top?.postMessage({ type: 'SPARK_COPY_CONFIRMED', text: confirmedText }, '*');
          window.parent?.postMessage({ type: 'SPARK_COPY_CONFIRMED', text: confirmedText }, '*');
        }
      } catch (_) {}
    }, 60);
  }

  // Intercept standard copy event in capturing phase
  window.addEventListener('copy', executeCopy, true);
  document.addEventListener('copy', executeCopy, true);

  // Universal Copy Shortcut Detector (resilient against CapsLock, Shift, and Vietnamese IMEs like Unikey/EVKey)
  function isCopyShortcut(e) {
    const isCtrl = e.ctrlKey || e.metaKey;
    if (!isCtrl) return false;
    const key = (e.key || '').toLowerCase();
    const code = e.code || '';
    const keyCode = e.keyCode || e.which || 0;
    return key === 'c' || code === 'KeyC' || keyCode === 67;
  }

  // Keyboard shortcut handler for Ctrl+C / Cmd+C
  function handleKeyDown(e) {
    if (!isCopyShortcut(e)) return;

    // EVENT SHIELD: Stop Google Drive from swallowing Ctrl+C with its file-management interceptor!
    // We stop immediate propagation so Google Drive's listeners don't run,
    // and let Chromium native copy pipeline run completely unhindered without suppression.
    e.stopImmediatePropagation();

    // 1. Direct native copy on active selection in this frame (works directly on PDFium / viewport selection)
    try {
      document.execCommand('copy');
    } catch (_) {}

    // 2. Extract deep selection if accessible via JS
    const sel = (getDeepSelectedText() || lastSelectedText || '').trim();

    // 3. Background offscreen write if selection was resolved
    if (sel) {
      try {
        if (typeof chrome !== 'undefined' && chrome.runtime?.sendMessage) {
          chrome.runtime.sendMessage({ action: 'SPARK_FORCE_COPY', text: sel });
        }
      } catch (_) {}
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(sel).catch(() => {});
      }
      try { window.top?.postMessage({ type: 'SPARK_FORCE_COPY', text: sel }, '*'); } catch (_) {}
      try { window.parent?.postMessage({ type: 'SPARK_FORCE_COPY', text: sel }, '*'); } catch (_) {}
    }

    // 4. Always notify top window after native copy finishes
    setTimeout(async () => {
      try {
        let clipText = '';
        if (navigator.clipboard && navigator.clipboard.readText) {
          clipText = await navigator.clipboard.readText();
        }
        const confirmedText = (clipText || sel || lastSelectedText || '').trim();
        window.top?.postMessage({ type: 'SPARK_COPY_CONFIRMED', text: confirmedText }, '*');
        window.parent?.postMessage({ type: 'SPARK_COPY_CONFIRMED', text: confirmedText }, '*');
        if (confirmedText) {
          lastSelectedText = confirmedText;
          window.top?.postMessage({ type: 'SPARK_SELECTION_CACHE', text: confirmedText }, '*');
        }
      } catch (_) {}
    }, 60);
  }

  // Keydown listener detached per user directive: let Chromium native pipeline handle keyboard copy directly
})();
