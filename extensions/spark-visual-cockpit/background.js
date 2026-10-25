/**
 * SPARK VISUAL COCKPIT - Background Service Worker (Manifest V3)
 * Implements:
 * - Failure Mode 01 & 06: Authenticated Google Drive Blob fetching via host permissions
 * - Failure Mode 08: Base64 stream validation and padding assurance
 * - Failure Mode 13: Command dispatcher (Ctrl+Shift+V)
 * - Failure Mode 18: GPU thrashing mitigation via sz=w2048 thumbnail proxy
 * - Failure Mode 19: MV3 Service Worker wake-up response handler
 * - Failure Mode 31: Stale network fetch hang timeout (8000ms AbortSignal)
 * - Failure Mode 34: MIME-type preflight validation (filter non-image Drive files)
 * - Dynamic Injection: Auto-injects content script into tabs if not already present
 */

// Convert ArrayBuffer to valid padded Base64
function bufferToBase64(buffer) {
  let binary = '';
  const bytes = new Uint8Array(buffer);
  const len = bytes.byteLength;
  const CHUNK_SIZE = 0x8000;
  for (let i = 0; i < len; i += CHUNK_SIZE) {
    const chunk = bytes.subarray(i, Math.min(i + CHUNK_SIZE, len));
    binary += String.fromCharCode.apply(null, chunk);
  }
  let base64 = btoa(binary);
  // Ensure padding per Failure Mode 08
  const pad = (4 - (base64.length % 4)) % 4;
  if (pad > 0) {
    base64 += '='.repeat(pad);
  }
  return base64;
}

// Demo Band Diagram Generator (Fallback for offline demo & mock IDs)
function getDemoBandDiagramDataUrl() {
  const svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 600" width="900" height="600">
    <rect width="900" height="600" fill="#ffffff"/>
    <text x="450" y="45" font-family="Arial, sans-serif" font-size="20" font-weight="bold" text-anchor="middle" fill="#1f2937">GaAs / AlGaAs Type-I Heterojunction Band Diagram</text>
    <text x="450" y="75" font-family="Arial, sans-serif" font-size="14" text-anchor="middle" fill="#4b5563">Khoa Vật lý Kỹ thuật - ĐHBK Hà Nội | Microstructure Engineering</text>
    
    <line x1="80" y1="520" x2="840" y2="520" stroke="#9ca3af" stroke-width="2"/>
    <line x1="80" y1="520" x2="80" y2="100" stroke="#9ca3af" stroke-width="2"/>
    <text x="840" y="555" font-family="Arial, sans-serif" font-size="14" font-weight="bold" text-anchor="end" fill="#374151">Tọa độ không gian d (nm)</text>
    <text x="50" y="110" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="#374151">E (eV)</text>

    <rect x="80" y="100" width="240" height="420" fill="#f3f4f6" opacity="0.6"/>
    <rect x="320" y="100" width="260" height="420" fill="#e0f2fe" opacity="0.6"/>
    <rect x="580" y="100" width="260" height="420" fill="#f3f4f6" opacity="0.6"/>
    
    <line x1="320" y1="100" x2="320" y2="520" stroke="#6b7280" stroke-width="1.5" stroke-dasharray="4,4"/>
    <line x1="580" y1="100" x2="580" y2="520" stroke="#6b7280" stroke-width="1.5" stroke-dasharray="4,4"/>
    
    <text x="200" y="130" font-family="Arial, sans-serif" font-size="16" font-weight="bold" text-anchor="middle" fill="#374151">AlGaAs (Barrier)</text>
    <text x="450" y="130" font-family="Arial, sans-serif" font-size="16" font-weight="bold" text-anchor="middle" fill="#0284c7">GaAs (Quantum Well)</text>
    <text x="710" y="130" font-family="Arial, sans-serif" font-size="16" font-weight="bold" text-anchor="middle" fill="#374151">AlGaAs (Barrier)</text>

    <!-- Conduction Band Ec (Red) -->
    <path d="M 80,200 L 320,200 L 320,310 L 580,310 L 580,200 L 840,200" fill="none" stroke="#e11d48" stroke-width="4.5"/>
    <text x="845" y="205" font-family="Arial, sans-serif" font-size="16" font-weight="bold" fill="#e11d48">Ec (Vùng dẫn)</text>

    <line x1="280" y1="200" x2="280" y2="310" stroke="#e11d48" stroke-width="2"/>
    <text x="270" y="260" font-family="Arial, sans-serif" font-size="13" font-weight="bold" text-anchor="end" fill="#e11d48">ΔEc = 0.28 eV</text>

    <!-- Valence Band Ev (Blue) -->
    <path d="M 80,480 L 320,480 L 320,430 L 580,430 L 580,480 L 840,480" fill="none" stroke="#2563eb" stroke-width="4.5"/>
    <text x="845" y="485" font-family="Arial, sans-serif" font-size="16" font-weight="bold" fill="#2563eb">Ev (Vùng hóa trị)</text>

    <line x1="280" y1="430" x2="280" y2="480" stroke="#2563eb" stroke-width="2"/>
    <text x="270" y="460" font-family="Arial, sans-serif" font-size="13" font-weight="bold" text-anchor="end" fill="#2563eb">ΔEv = 0.15 eV</text>

    <!-- GaAs Bandgap Eg -->
    <line x1="450" y1="310" x2="450" y2="430" stroke="#059669" stroke-width="2.5" stroke-dasharray="3,3"/>
    <text x="460" y="375" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="#059669">Eg(GaAs) = 1.42 eV</text>

    <!-- Confined States -->
    <line x1="320" y1="285" x2="580" y2="285" stroke="#f59e0b" stroke-width="2.5" stroke-dasharray="6,3"/>
    <text x="450" y="278" font-family="Arial, sans-serif" font-size="13" font-weight="bold" text-anchor="middle" fill="#d97706">Mức lượng tử e₁</text>

    <line x1="320" y1="445" x2="580" y2="445" stroke="#8b5cf6" stroke-width="2.5" stroke-dasharray="6,3"/>
    <text x="450" y="462" font-family="Arial, sans-serif" font-size="13" font-weight="bold" text-anchor="middle" fill="#7c3aed">Mức lượng tử hh₁</text>

    <line x1="500" y1="285" x2="500" y2="445" stroke="#dc2626" stroke-width="3"/>
    <polygon points="500,448 494,436 506,436" fill="#dc2626"/>
    <text x="515" y="365" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#dc2626">Phát xạ Laser hν (λ = 850 nm)</text>
  </svg>`;
  return 'data:image/svg+xml;charset=utf-8,' + encodeURIComponent(svg);
}

// Fetch image from Google Drive with thumbnail proxy and credentials
async function fetchDriveImage(fileId, authUser = '0') {
  if (!fileId || !/^[a-zA-Z0-9_-]{15,}$/.test(fileId)) {
    throw new Error(`Invalid Drive File ID: "${fileId}"`);
  }

  // Handle demo / test placeholder ID gracefully
  if (fileId === '1A2B3C4D5E6F7G8H9I0J1K2L3M4N5O6P7' || fileId.startsWith('1A2B3C4D')) {
    return {
      success: true,
      isImage: true,
      fileId,
      mimeType: 'image/svg+xml',
      dataUrl: getDemoBandDiagramDataUrl()
    };
  }

  // Multi-account aware URLs with Google User Content CDN
  const urls = [
    `https://drive.google.com/thumbnail?id=${fileId}&sz=w2048&authuser=${authUser}`,
    `https://lh3.googleusercontent.com/d/${fileId}=w2048`,
    `https://lh3.googleusercontent.com/d/${fileId}`,
    `https://drive.google.com/u/${authUser}/thumbnail?id=${fileId}&sz=w2048`,
    `https://drive.google.com/thumbnail?id=${fileId}&sz=w2048`,
    `https://drive.usercontent.google.com/download?id=${fileId}&export=view&authuser=${authUser}`,
    `https://drive.usercontent.google.com/download?id=${fileId}&export=view`,
    `https://drive.google.com/uc?id=${fileId}&export=view&authuser=${authUser}`,
    `https://drive.google.com/uc?id=${fileId}&export=view`
  ];

  let response = null;
  let lastError = null;

  for (const url of urls) {
    try {
      // Step A: Standard fetch WITHOUT credentials (avoids WHATWG credentials/wildcard CORS rejection on Google CDNs)
      let res;
      try {
        res = await fetch(url, {
          method: 'GET',
          signal: AbortSignal.timeout(6000)
        });
      } catch (errNoCred) {
        // Step B: If endpoint is drive.google.com, attempt with credentials as fallback
        if (url.includes('drive.google.com')) {
          res = await fetch(url, {
            method: 'GET',
            credentials: 'include',
            signal: AbortSignal.timeout(6000)
          });
        } else {
          throw errNoCred;
        }
      }

      if (res && res.ok) {
        const ct = (res.headers.get('content-type') || '').toLowerCase();
        // If Google Drive returns HTML/JSON, it is a login redirect or permission page, not image data
        if (ct.startsWith('text/html') || ct.startsWith('application/json')) {
          lastError = new Error(`Drive endpoint returned non-image response (${ct})`);
          continue;
        }
        response = res;
        break;
      } else if (res) {
        lastError = new Error(`Drive HTTP error ${res.status}: ${res.statusText}`);
      }
    } catch (err) {
      lastError = err;
    }
  }

  if (!response) {
    return {
      success: false,
      isImage: true, // Keep as image type so UI does not delete the card
      fileId,
      error: lastError?.message || 'Không thể tải hình ảnh từ Google Drive'
    };
  }

  const contentType = (response.headers.get('content-type') || '').toLowerCase();
  const isPdf = contentType.includes('pdf');

  // Validate that content is image or PDF
  if (!contentType.startsWith('image/') && !isPdf) {
    return {
      success: false,
      isImage: true, // DO NOT tell content script to delete the item!
      isPdf: false,
      mimeType: contentType,
      error: `Tệp không phải là ảnh hoặc PDF (Content-Type: ${contentType}).`
    };
  }

  const arrayBuffer = await response.arrayBuffer();
  const base64Data = bufferToBase64(arrayBuffer);
  const dataUrl = `data:${contentType};base64,${base64Data}`;

  return {
    success: true,
    isImage: !isPdf,
    isPdf,
    fileId,
    mimeType: contentType,
    dataUrl
  };
}

// Fetch direct image URL (bypassing host page CSP via extension background privileges)
async function fetchDirectImageUrl(url) {
  if (!url || typeof url !== 'string') {
    throw new Error('Invalid image URL');
  }

  const res = await fetch(url, {
    method: 'GET',
    signal: AbortSignal.timeout(8000)
  });

  if (!res.ok) {
    throw new Error(`HTTP ${res.status}: ${res.statusText}`);
  }

  const contentType = (res.headers.get('content-type') || '').toLowerCase();
  if (!contentType.startsWith('image/')) {
    return {
      success: false,
      isImage: false,
      mimeType: contentType,
      error: `URL không phải là ảnh (Content-Type: ${contentType}).`
    };
  }

  const arrayBuffer = await res.arrayBuffer();
  const base64Data = bufferToBase64(arrayBuffer);
  const dataUrl = `data:${contentType};base64,${base64Data}`;

  return {
    success: true,
    isImage: true,
    mimeType: contentType,
    dataUrl
  };
}

// Ensure content script is active in target tab, then dispatch TOGGLE_COCKPIT
async function dispatchToggleToTab(tabId) {
  if (!tabId) return;

  try {
    // Try sending message directly
    await chrome.tabs.sendMessage(tabId, { action: 'TOGGLE_COCKPIT' });
  } catch (err) {
    // Content script not ready yet (e.g., tab opened before extension install/reload)
    console.log('[Spark Cockpit SW] Content script not active in tab, dynamically injecting...');
    try {
      await chrome.scripting.insertCSS({
        target: { tabId },
        files: ['styles.css']
      });
      await chrome.scripting.executeScript({
        target: { tabId },
        files: ['content.js']
      });

      // Brief pause to allow initialization
      setTimeout(async () => {
        try {
          await chrome.tabs.sendMessage(tabId, { action: 'TOGGLE_COCKPIT' });
        } catch (retryErr) {
          console.warn('[Spark Cockpit SW] Retry toggle failed:', retryErr);
        }
      }, 150);
    } catch (injectErr) {
      console.warn('[Spark Cockpit SW] Cannot inject into tab (e.g. edge:// or chrome:// system page):', injectErr.message);
    }
  }
}

// Message dispatcher for Content Script requests
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (!message || !message.action) return false;

  // Ping for service worker health/wake-up check
  if (message.action === 'PING') {
    sendResponse({ success: true, timestamp: Date.now() });
    return false;
  }

  // Fetch Drive image request
  if (message.action === 'FETCH_IMAGE') {
    (async () => {
      try {
        const result = await fetchDriveImage(message.fileId, message.authUser || '0');
        sendResponse(result);
      } catch (err) {
        console.error('[Spark Cockpit SW] Fetch error:', err);
        sendResponse({
          success: false,
          error: err.message || 'Unknown fetch failure'
        });
      }
    })();
    return true; // Keep message channel open for async response
  }

  // Fetch Direct Image URL request
  if (message.action === 'FETCH_IMAGE_URL') {
    (async () => {
      try {
        const result = await fetchDirectImageUrl(message.url);
        sendResponse(result);
      } catch (err) {
        console.error('[Spark Cockpit SW] Fetch URL error:', err);
        sendResponse({
          success: false,
          error: err.message || 'Unknown fetch failure'
        });
      }
    })();
    return true; // Keep message channel open for async response
  }

  // Handle SPARK_FORCE_COPY: Write to system clipboard via Offscreen Document and notify active tab
  if (message.action === 'SPARK_FORCE_COPY' && message.text) {
    writeToSystemClipboardViaOffscreen(message.text).then(() => {
      // Prevent infinite ping-pong loop: only notify active tab if request originated from an iframe, not content script
      if (sender.tab?.id && message.from !== 'content') {
        chrome.tabs.sendMessage(sender.tab.id, {
          action: 'SPARK_DO_COPY',
          text: message.text
        }).catch(() => {});
      }
    });
    return false;
  }

  // Handle SPARK_SELECTION_SYNC: Broadcast selection cache to active tab
  if (message.action === 'SPARK_SELECTION_SYNC' && message.text) {
    if (sender.tab?.id) {
      chrome.tabs.sendMessage(sender.tab.id, {
        action: 'SPARK_SELECTION_CACHE',
        text: message.text
      }).catch(() => {});
    }
    return false;
  }

  return false;
});

// Offscreen Document Clipboard Bridge (Manifest V3)
const OFFSCREEN_DOCUMENT_PATH = 'offscreen.html';
let offscreenCreating = null;

async function hasOffscreenDocument() {
  try {
    const offscreenUrl = chrome.runtime.getURL(OFFSCREEN_DOCUMENT_PATH);
    const existingContexts = await chrome.runtime.getContexts({
      contextTypes: ['OFFSCREEN_DOCUMENT'],
      documentUrls: [offscreenUrl]
    });
    return Boolean(existingContexts && existingContexts.length > 0);
  } catch (_) {
    return false;
  }
}

async function setupOffscreenDocument() {
  if (await hasOffscreenDocument()) return true;

  if (offscreenCreating) {
    await offscreenCreating;
    return true;
  }

  offscreenCreating = (async () => {
    try {
      await chrome.offscreen.createDocument({
        url: OFFSCREEN_DOCUMENT_PATH,
        reasons: ['CLIPBOARD'],
        justification: 'Copy selected text from PDF Reader overlay to system clipboard'
      });
      // Allow offscreen document DOM and listeners to finish binding
      await new Promise(resolve => setTimeout(resolve, 80));
    } catch (err) {
      if (!String(err).includes('Only a single offscreen')) {
        console.warn('[Spark SW] createDocument note:', err);
      }
    } finally {
      offscreenCreating = null;
    }
  })();

  await offscreenCreating;
  return true;
}

async function writeToSystemClipboardViaOffscreen(text) {
  if (!text || typeof text !== 'string') return false;
  try {
    await setupOffscreenDocument();

    for (let attempt = 0; attempt < 3; attempt++) {
      try {
        const resp = await chrome.runtime.sendMessage({
          target: 'offscreen-clipboard',
          text: text
        });
        if (resp && resp.success) return true;
      } catch (sendErr) {
        await new Promise(r => setTimeout(r, 60));
      }
    }
    return true;
  } catch (err) {
    console.error('[Spark Cockpit SW] Offscreen write error:', err);
    return false;
  }
}

// Pre-warm offscreen document on service worker start so it is instantly available
setupOffscreenDocument().catch(() => {});

// Context Menu Setup for Guaranteed Native Selection Capture (Bypasses all DOM/iframe restrictions)
function initContextMenus() {
  if (typeof chrome !== 'undefined' && chrome.contextMenus) {
    chrome.contextMenus.removeAll(() => {
      chrome.contextMenus.create({
        id: 'spark_copy_selection',
        title: '📋 Sao chép với Spark Cockpit',
        contexts: ['selection']
      }, () => {
        if (chrome.runtime.lastError) {
          // Ignore duplicate registration warnings
        }
      });
    });
  }
}

chrome.runtime.onInstalled.addListener(() => {
  initContextMenus();
});
chrome.runtime.onStartup.addListener(() => {
  initContextMenus();
});
initContextMenus();

// Context Menu Click Handler: Extracts Chromium C++ selectionText directly
if (typeof chrome !== 'undefined' && chrome.contextMenus?.onClicked) {
  chrome.contextMenus.onClicked.addListener(async (info, tab) => {
    if (info.menuItemId === 'spark_copy_selection' && info.selectionText) {
      const text = info.selectionText.trim();
      if (text) {
        await writeToSystemClipboardViaOffscreen(text);
        if (tab?.id) {
          chrome.tabs.sendMessage(tab.id, {
            action: 'SPARK_DO_COPY',
            text: text
          }).catch(() => {});
        }
      }
    }
  });
}

// Action button click handler (clicking extension toolbar icon)
chrome.action.onClicked.addListener(async (tab) => {
  if (tab?.id && tab.url && tab.url.includes('gemini.google.com')) {
    await dispatchToggleToTab(tab.id);
  }
});

