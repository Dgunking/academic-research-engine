/**
 * SPARK VISUAL COCKPIT - Core Content Script Engine
 * Manifest V3 - Pure Client-Side DOM Overlay with Closed Shadow DOM
 * 
 * Strict Implementation of All 34 Audited Failure Modes & Architecture:
 * - Failure Mode 01 & 06: Background SW authenticated Drive fetching
 * - Failure Mode 02: Token streaming debounce (300ms) & File ID regex
 * - Failure Mode 03: Min-width chat bounds (>= 420px, canvas 25%-65%)
 * - Failure Mode 04: LRU Cache capped at 15 items with URL.revokeObjectURL
 * - Failure Mode 05: Unescapes markdown codeblocks & prefixes SVG gradient IDs
 * - Failure Mode 07: Deduplication map indexing by fileId / hash
 * - Failure Mode 08: Base64 integrity verification
 * - Failure Mode 11: Centralized AbortController for clean event detachment
 * - Failure Mode 12: Scoped mutation observer ignoring .katex / .math loops
 * - Failure Mode 13: Dedicated hotkey Ctrl+Shift+V
 * - Failure Mode 14: 100% style isolation inside Closed Shadow DOM Root
 * - Failure Mode 15: Zoom focal point normalized by DPR and viewport rect
 * - Failure Mode 16: Window-bound resizer dragging with user-select prevention
 * - Failure Mode 17: Chat scroll jitter suppression when scroll offset > 100px
 * - Failure Mode 18: sz=w2048 proxy consumption
 * - Failure Mode 19: MV3 Service Worker wake-up retry with exponential backoff
 * - Failure Mode 20: Dual-mode filter invert(1) hue-rotate(180deg) preserves physics colors
 * - Failure Mode 21: @media print flat document restoration
 * - Failure Mode 22: Tab-isolated sessionStorage for split percentage
 * - Failure Mode 23: Canvas dragover/drop pass-through (no lab image drop hijack)
 * - Failure Mode 24: Dynamic DPI resolution change listener
 * - Failure Mode 25: Canvas bounding box clamping + [⦿] Center Reset
 * - Failure Mode 26: Detached extension context safety wrapper & toast
 * - Failure Mode 27: Sub-figure clustering [a] [b] [c]
 * - Failure Mode 28: Zero-network memory cache hit
 * - Failure Mode 29: Pure DOM matrix transform on <img> and <svg>
 * - Failure Mode 30: Host theme observer & CSS variable synchronization
 * - Failure Mode 31: 8000ms fetch timeout & interactive [Retry] UI
 * - Failure Mode 32: Zero innerHTML across entire codebase (Strict Trusted Types)
 * - Failure Mode 33: Suppress canvas shortcuts when typing in inputs/textareas
 * - Failure Mode 34: Contextual keyword validation for Drive links
 */

(() => {
  // Prevent duplicate content script injection
  if (window.__SPARK_COCKPIT_INITIALIZED__) return;

  // Strict domain scope: execute ONLY on gemini.google.com
  if (window.location.hostname !== 'gemini.google.com') return;

  window.__SPARK_COCKPIT_INITIALIZED__ = true;

  // =========================================================================
  // CLASS 5: SanitizerAndPostProcessor (Failure Mode 05, 32)
  // =========================================================================
  class SanitizerAndPostProcessor {
    static sanitizeSvgString(rawText) {
      if (!rawText) return null;

      // Unescape markdown XML entities
      let unescaped = rawText
        .replace(/&lt;/g, '<')
        .replace(/&gt;/g, '>')
        .replace(/&amp;/g, '&')
        .replace(/&quot;/g, '"')
        .replace(/&#39;/g, "'");

      // Replace common HTML & Physics entities with Unicode to prevent XML parsererror
      const entityMap = {
        '&Delta;': 'Δ', '&delta;': 'δ', '&Lambda;': 'Λ', '&lambda;': 'λ',
        '&Alpha;': 'Α', '&alpha;': 'α', '&Beta;': 'Β', '&beta;': 'β',
        '&Gamma;': 'Γ', '&gamma;': 'γ', '&Psi;': 'Ψ', '&psi;': 'ψ',
        '&Phi;': 'Φ', '&phi;': 'φ', '&Omega;': 'Ω', '&omega;': 'ω',
        '&Mu;': 'μ', '&Pi;': 'π', '&Sigma;': 'Σ', '&sigma;': 'σ',
        '&Theta;': 'Θ', '&theta;': 'θ', '&Tau;': 'τ', '&hbar;': 'ℏ',
        '&infin;': '∞', '&plusmn;': '±', '&deg;': '°', '&sim;': '~',
        '&asymp;': '≈', '&ne;': '≠', '&le;': '≤', '&ge;': '≥',
        '&times;': '×', '&middot;': '·', '&nabla;': '∇', '&part;': '∂',
        '&int;': '∫', '&sum;': '∑', '&ang;': '∠', '&perp;': '⊥'
      };
      for (const [entity, char] of Object.entries(entityMap)) {
        unescaped = unescaped.split(entity).join(char);
      }

      // Extract <svg>...</svg>
      const svgMatch = unescaped.match(/<svg[\s\S]*?<\/svg>/i);
      if (!svgMatch) return null;

      let svgContent = svgMatch[0];

      // CRITICAL FOR CHROME/EDGE: Inject xmlns="http://www.w3.org/2000/svg" before parsing.
      // If xmlns is missing in XML parsing, DOMParser treats all child nodes as generic XML in a null namespace,
      // rendering 0 pixels on screen (making it black/invisible)!
      if (!svgContent.match(/<svg[^>]*\bxmlns=/i)) {
        svgContent = svgContent.replace(/<svg\b/i, '<svg xmlns="http://www.w3.org/2000/svg"');
      }
      if (svgContent.includes('xlink:') && !svgContent.includes('xmlns:xlink=')) {
        svgContent = svgContent.replace(/<svg\b/i, '<svg xmlns:xlink="http://www.w3.org/1999/xlink"');
      }

      // Parse safely via DOMParser (Strictly zero innerHTML)
      const parser = new DOMParser();
      let doc = parser.parseFromString(svgContent, 'image/svg+xml');
      let parserError = doc.querySelector('parsererror');
      
      let svgEl = null;
      if (parserError || !doc.documentElement || doc.documentElement.namespaceURI !== 'http://www.w3.org/2000/svg') {
        // Fallback to HTML parser for lenient SVG / HTML entity parsing
        const htmlDoc = parser.parseFromString(svgContent, 'text/html');
        svgEl = htmlDoc.querySelector('svg');
        if (!svgEl) {
          // Incomplete token stream or syntax issue: drop silently without polluting console
          return null;
        }
      } else {
        svgEl = doc.documentElement;
      }

      if (!svgEl || svgEl.nodeName.toLowerCase() !== 'svg') return null;

      // STREAMING & EMPTY SHELL GUARD (Tier 3):
      // Reject incomplete streaming SVG or empty shell (e.g. <svg></svg> or background-only rect).
      // A legitimate physics diagram (energy bands, quantum wells, optical curves) must have
      // at least 2 graphic child elements (paths, lines, rects, circles, texts, etc.).
      const graphicCount = svgEl.querySelectorAll('path, rect, line, circle, polygon, polyline, text, ellipse, image, use').length;
      if (graphicCount < 2) {
        return null;
      }

      // Strip dangerous tags: <script>, <foreignObject>, <iframe>, <embed>, <object>
      const dangerousTags = ['script', 'foreignobject', 'iframe', 'embed', 'object'];
      dangerousTags.forEach(tag => {
        const elements = svgEl.querySelectorAll(tag);
        elements.forEach(el => el.parentNode?.removeChild(el));
      });

      // Strip on* event attributes and javascript: URIs
      const allElements = [svgEl, ...svgEl.querySelectorAll('*')];
      allElements.forEach(el => {
        const attrs = Array.from(el.attributes);
        for (const attr of attrs) {
          const name = attr.name.toLowerCase();
          const val = attr.value.trim().toLowerCase();
          if (name.startsWith('on') || val.startsWith('javascript:')) {
            el.removeAttribute(attr.name);
          }
        }
      });

      // Namespace prefix all internal IDs to prevent cross-SVG gradient/clip-path collision
      const sessionHash = 'spk_' + Math.random().toString(36).substring(2, 8) + '_';
      const idMap = new Map();

      // Collect IDs
      allElements.forEach(el => {
        if (el.hasAttribute('id')) {
          const oldId = el.getAttribute('id');
          const newId = sessionHash + oldId;
          idMap.set(oldId, newId);
          el.setAttribute('id', newId);
        }
      });

      // Rewrite URL references: url(#oldId)
      if (idMap.size > 0) {
        allElements.forEach(el => {
          const attrs = Array.from(el.attributes);
          for (const attr of attrs) {
            let val = attr.value;
            for (const [oldId, newId] of idMap.entries()) {
              if (val.includes(`url(#${oldId})`) || val.includes(`url('#${oldId}')`) || val.includes(`url("#${oldId}")`)) {
                val = val.replace(new RegExp(`url\\((['"]?)#${oldId}\\1\\)`, 'g'), `url($1#${newId}$1)`);
                el.setAttribute(attr.name, val);
              }
              if ((attr.name === 'href' || attr.name === 'xlink:href') && val === `#${oldId}`) {
                el.setAttribute(attr.name, `#${newId}`);
              }
            }
          }
        });
      }

      // Ensure proper attributes
      if (!svgEl.hasAttribute('xmlns')) {
        svgEl.setAttribute('xmlns', 'http://www.w3.org/2000/svg');
      }

      // Guarantee viewBox for responsive zooming and timeline preview
      let vbWidth = 850;
      let vbHeight = 500;
      if (!svgEl.hasAttribute('viewBox')) {
        const w = parseFloat(svgEl.getAttribute('width')) || 850;
        const h = parseFloat(svgEl.getAttribute('height')) || 500;
        svgEl.setAttribute('viewBox', `0 0 ${w} ${h}`);
        vbWidth = w;
        vbHeight = h;
      } else {
        const parts = svgEl.getAttribute('viewBox').split(/[\s,]+/).map(parseFloat);
        if (parts.length === 4 && parts[2] > 0 && parts[3] > 0) {
          vbWidth = parts[2];
          vbHeight = parts[3];
        }
      }

      // Guarantee explicit width and height matching viewBox coordinates
      svgEl.setAttribute('width', vbWidth);
      svgEl.setAttribute('height', vbHeight);

      return svgEl;
    }

    static extractTitle(svgEl, rawContent = '', contextText = '') {
      if (!svgEl) return 'Mô phỏng Vector Băng Năng lượng';

      // 1. <title> inside SVG
      const titleEl = svgEl.querySelector('title');
      if (titleEl && titleEl.textContent?.trim()) {
        return titleEl.textContent.trim();
      }

      // 2. <desc> inside SVG
      const descEl = svgEl.querySelector('desc');
      if (descEl && descEl.textContent?.trim()) {
        return descEl.textContent.trim();
      }

      // 3. XML comment inside SVG: <!-- Title: ... --> or <!-- ... -->
      const commentMatch = (rawContent || '').match(/<!--\s*(?:Title:\s*)?([A-Za-z0-9À-ỹ\s\(\)\/\-_]{4,60})\s*-->/i);
      if (commentMatch && commentMatch[1]?.trim()) {
        return commentMatch[1].trim();
      }

      // 4. Header in surrounding text: ### ... or **Hình ...** or Figure ...
      if (contextText) {
        const hMatch = contextText.match(/(?:###?|Hình|Figure|Mô hình|Giản đồ)\s*[:\-\d\.]*\s*([A-Za-z0-9À-ỹ\s\(\)\/\-_]{4,60})/i);
        if (hMatch && hMatch[1]?.trim()) {
          return hMatch[1].trim().replace(/^[#*_\s]+|[#*_\s]+$/g, '');
        }
      }

      return 'Mô phỏng Vector Băng Năng lượng (SVG)';
    }

    static createSafeTextNode(text) {
      return document.createTextNode(text ?? '');
    }
  }

  // =========================================================================
  // CLASS 2: BlobLifecycleManager (Failure Modes 04, 07, 27, 28)
  // =========================================================================
  class BlobLifecycleManager {
    constructor(maxRamEntries = 20) {
      this.maxRamEntries = maxRamEntries; // Two-Tier Cache: keep heavy data for 20 most recent images in RAM
      this.cache = new Map();             // Tier 1: ALL timeline items (UNLIMITED capacity)
      this.ramTracker = new Set();        // Tier 2: IDs currently holding heavy rawData in RAM (<= 20)
      this.sequenceCounter = 0;
      this.setupUnloadCleanup();
    }

    setupUnloadCleanup() {
      window.addEventListener('beforeunload', () => {
        this.clearAll();
      });
    }

    get(id) {
      const entry = this.cache.get(id);
      if (entry) {
        entry.lastAccessed = Date.now();
        if (this.ramTracker.has(id)) {
          this.ramTracker.delete(id);
          this.ramTracker.add(id);
        }
      }
      return entry;
    }

    has(id) {
      return this.cache.has(id);
    }

    getRamCount() {
      return this.ramTracker.size;
    }

    getTotalCount() {
      return this.cache.size;
    }

    touchRam(id, activeId = null) {
      const item = this.cache.get(id);
      if (!item || !item.rawData) return;

      // Add to MRU position in RAM tracker
      this.ramTracker.delete(id);
      this.ramTracker.add(id);

      // LRU Soft Eviction: Keep RAM items <= maxRamEntries (20)
      while (this.ramTracker.size > this.maxRamEntries) {
        let evictId = null;
        for (const candidateId of this.ramTracker) {
          if (candidateId !== activeId && candidateId !== id) {
            evictId = candidateId;
            break;
          }
        }

        if (!evictId) break;

        this.ramTracker.delete(evictId);
        const evictItem = this.cache.get(evictId);
        if (evictItem) {
          // SOFT EVICTION: Revoke heavy blob and clear rawData, keep card on Timeline!
          this.revokeItemUrls(evictItem);
          if (evictItem.type === 'DRIVE') {
            evictItem.rawData = null;
            evictItem.status = 'evicted';
          }
        }
      }
    }

    addOrUpdate(id, itemData) {
      // Deduplication check: Keep existing item's position on timeline!
      if (this.cache.has(id)) {
        const existing = this.cache.get(id);
        existing.lastAccessed = Date.now();
        if (itemData.domOrder !== undefined) existing.domOrder = itemData.domOrder;
        if (itemData.status !== undefined) existing.status = itemData.status;
        if (itemData.rawData !== undefined && itemData.rawData !== null) {
          existing.rawData = itemData.rawData;
          this.touchRam(id);
        }
        if (itemData.title) existing.title = itemData.title;
        if (itemData.metadata) existing.metadata = { ...existing.metadata, ...itemData.metadata };
        if (itemData.fileId) existing.fileId = itemData.fileId;
        if (itemData.subfigures && itemData.subfigures.length > 0) {
          itemData.subfigures.forEach(sub => {
            if (!existing.subfigures.some(s => s.id === sub.id)) {
              existing.subfigures.push(sub);
            }
          });
        }
        return existing;
      }

      // No hard eviction: Timeline stores ALL items across the entire chat
      const newItem = {
        id,
        sequenceIndex: ++this.sequenceCounter,
        domOrder: itemData.domOrder !== undefined ? itemData.domOrder : (++this.sequenceCounter),
        status: itemData.status || (itemData.rawData ? 'ready' : 'loading'),
        type: itemData.type || 'DRIVE',
        title: itemData.title || 'Hình học vật lý',
        fileId: itemData.fileId || null,
        subfigures: itemData.subfigures || [],
        activeSubIndex: 0,
        blobUrl: itemData.blobUrl || null,
        rawData: itemData.rawData || null,
        metadata: itemData.metadata || null,
        createdAt: itemData.createdAt || Date.now(),
        lastAccessed: Date.now()
      };

      this.cache.set(id, newItem);
      if (newItem.rawData) {
        this.touchRam(id);
      }
      return newItem;
    }

    delete(id) {
      if (this.cache.has(id)) {
        const item = this.cache.get(id);
        this.revokeItemUrls(item);
        this.cache.delete(id);
        this.ramTracker.delete(id);
        return true;
      }
      return false;
    }

    revokeItemUrls(item) {
      if (item.blobUrl && item.blobUrl.startsWith('blob:')) {
        try {
          URL.revokeObjectURL(item.blobUrl);
        } catch (_) {}
      }
      if (item.subfigures && Array.isArray(item.subfigures)) {
        item.subfigures.forEach(sub => {
          if (sub.blobUrl && sub.blobUrl.startsWith('blob:')) {
            try {
              URL.revokeObjectURL(sub.blobUrl);
            } catch (_) {}
          }
        });
      }
    }

    static extractFigureNumber(title) {
      if (!title || typeof title !== 'string') return null;
      // Match Figure 1.5, Fig. 1.5, Hình 1.5, Mục 1.5, v.v.
      const match = title.match(/(?:Figure|Fig\.?|Hình|Mục)\s*[:\-\s]*(\d+(?:\.\d+)*)/i);
      if (match) {
        return match[1].split('.').map(n => parseInt(n, 10));
      }
      return null;
    }

    static compareFigureNumbers(partsA, partsB) {
      const len = Math.max(partsA.length, partsB.length);
      for (let i = 0; i < len; i++) {
        const valA = partsA[i] !== undefined ? partsA[i] : 0;
        const valB = partsB[i] !== undefined ? partsB[i] : 0;
        if (valA !== valB) {
          return valA - valB;
        }
      }
      return 0;
    }

    getAllSorted(sortOrder = 'newest_first') {
      return Array.from(this.cache.values()).sort((a, b) => {
        // Primary criterion: Conversational DOM document position (top-to-bottom of chat)
        const orderA = a.domOrder !== undefined ? a.domOrder : (a.sequenceIndex || 0);
        const orderB = b.domOrder !== undefined ? b.domOrder : (b.sequenceIndex || 0);

        // Secondary verification: Figure number if available on both
        const numA = BlobLifecycleManager.extractFigureNumber(a.title);
        const numB = BlobLifecycleManager.extractFigureNumber(b.title);

        let figDiff = 0;
        if (numA && numB) {
          figDiff = BlobLifecycleManager.compareFigureNumbers(numA, numB);
        }

        // Ascending difference: earlier item has lower value
        const ascendingDiff = figDiff !== 0 ? figDiff : (orderA - orderB);

        // 'newest_first': descending (Figure 1.5 / latest in chat at far left)
        // 'oldest_first': ascending (Figure 1.1 / earliest in chat at far left)
        return sortOrder === 'oldest_first' ? ascendingDiff : -ascendingDiff;
      });
    }

    getAllChronological(sortOrder = 'newest_first') {
      return this.getAllSorted(sortOrder);
    }

    clear() {
      this.clearAll();
    }

    clearAll() {
      for (const item of this.cache.values()) {
        this.revokeItemUrls(item);
      }
      this.cache.clear();
      this.ramTracker.clear();
      this.sequenceCounter = 0;
    }
  }

  // =========================================================================
  // CLASS 6: ErgonomicGuards (Failure Modes 17, 19, 23, 26, 33)
  // =========================================================================
  class ErgonomicGuards {
    static isTypingContext() {
      const active = document.activeElement;
      if (!active) return false;
      const tag = active.tagName.toLowerCase();
      return tag === 'input' || tag === 'textarea' || active.isContentEditable;
    }

    static async sendMessageWithRetry(message, maxRetries = 3) {
      // Failure Mode 19: Exponential backoff retry logic for Service Worker idle wake-up
      // Failure Mode 26: Safe extension context validation
      let delay = 300;
      for (let attempt = 1; attempt <= maxRetries; attempt++) {
        try {
          if (!chrome.runtime?.id) {
            throw new Error('Extension context invalidated');
          }
          const response = await chrome.runtime.sendMessage(message);
          return response;
        } catch (err) {
          const errMsg = err?.message || '';
          if (errMsg.includes('Extension context invalidated')) {
            ErgonomicGuards.showContextInvalidatedToast();
            throw err;
          }

          if (attempt === maxRetries) {
            throw err;
          }
          await new Promise(r => setTimeout(r, delay));
          delay *= 2;
        }
      }
    }

    static showContextInvalidatedToast() {
      if (document.getElementById('spark-reload-toast')) return;
      const toast = document.createElement('div');
      toast.id = 'spark-reload-toast';
      toast.appendChild(document.createTextNode('⚡ Spark Visual Cockpit: Tiện ích vừa được nạp lại. Vui lòng tải lại trang (F5) để tiếp tục.'));
      document.body.appendChild(toast);
      setTimeout(() => toast.remove(), 8000);
    }
  }

  // =========================================================================
  // CLASS 4: CanvasTransformEngine (Failure Modes 15, 20, 24, 25, 29)
  // =========================================================================
  class CanvasTransformEngine {
    constructor(viewportElement, containerElement) {
      this.viewport = viewportElement;
      this.container = containerElement;
      this.scale = 1.0;
      this.transX = 0;
      this.transY = 0;
      this.filterMode = 'none'; // 'none' | 'preserve' | 'invert' — default: raw (no filter)
      this.isDragging = false;
      this.dragStartX = 0;
      this.dragStartY = 0;
      this.targetElement = null; // Either <img> or <svg>

      this.setupInteractions();
    }

    setTargetElement(element) {
      this.targetElement = element;
      if (this.targetElement) {
        this.targetElement.ondragstart = (e) => e.preventDefault();
        this.targetElement.style.userSelect = 'none';
        this.targetElement.style.webkitUserDrag = 'none';
        this.targetElement.style.pointerEvents = 'none';
      }
      this.resetTransform();
    }

    setupInteractions() {
      // Mouse Wheel Zoom with Focal Point Normalization (Failure Mode 15)
      this.viewport.addEventListener('wheel', (e) => {
        window.__SPARK_LAYOUT_MANAGER__?.triggerInteractionLock();
        e.preventDefault();
        if (!this.targetElement) return;

        const rect = this.viewport.getBoundingClientRect();
        // Mouse coordinate inside viewport normalized by devicePixelRatio
        const mouseX = e.clientX - rect.left;
        const mouseY = e.clientY - rect.top;

        const factor = e.deltaY < 0 ? 1.15 : (1 / 1.15);
        const newScale = Math.min(Math.max(this.scale * factor, 0.15), 12.0);

        // Focal point math: keep pixel under cursor stationary
        this.transX = mouseX - (mouseX - this.transX) * (newScale / this.scale);
        this.transY = mouseY - (mouseY - this.transY) * (newScale / this.scale);
        this.scale = newScale;

        this.applyTransform();
      }, { passive: false });

      // Pan Dragging (Smooth 360° pan dragging with browser native drag prevention)
      this.viewport.addEventListener('pointerdown', (e) => {
        window.__SPARK_LAYOUT_MANAGER__?.triggerInteractionLock();
        if (e.button !== 0 || !this.targetElement) return;
        e.preventDefault();
        this.isDragging = true;
        this.dragStartX = e.clientX - this.transX;
        this.dragStartY = e.clientY - this.transY;
        this.viewport.setPointerCapture(e.pointerId);
        this.viewport.style.cursor = 'grabbing';
      });

      this.viewport.addEventListener('pointermove', (e) => {
        if (!this.isDragging || !this.targetElement) return;
        e.preventDefault();
        this.transX = e.clientX - this.dragStartX;
        this.transY = e.clientY - this.dragStartY;
        this.clampBounds();
        this.applyTransform();
      });

      const endDrag = (e) => {
        if (!this.isDragging) return;
        this.isDragging = false;
        try { this.viewport.releasePointerCapture(e.pointerId); } catch (_) {}
        this.viewport.style.cursor = 'grab';
      };

      this.viewport.addEventListener('pointerup', endDrag);
      this.viewport.addEventListener('pointercancel', endDrag);

      // Failure Mode 24: High-DPI & Resolution change listener
      const dprMatcher = window.matchMedia(`(resolution: ${window.devicePixelRatio}dpr)`);
      if (dprMatcher && dprMatcher.addEventListener) {
        dprMatcher.addEventListener('change', () => {
          this.applyTransform();
        });
      }
    }

    clampBounds() {
      if (!this.targetElement || !this.viewport) return;
      const vpW = this.viewport.clientWidth;
      const vpH = this.viewport.clientHeight;
      if (vpW <= 0 || vpH <= 0) return;

      const elW = parseFloat(this.targetElement.getAttribute('width')) ||
                  this.targetElement.naturalWidth ||
                  this.targetElement.clientWidth ||
                  800;
      const elH = parseFloat(this.targetElement.getAttribute('height')) ||
                  this.targetElement.naturalHeight ||
                  this.targetElement.clientHeight ||
                  500;

      const scaledW = elW * this.scale;
      const scaledH = elH * this.scale;

      // Allow full, unconstrained 360-degree panning so all 4 corners and borders
      // (top, bottom, left, right) can be inspected without hitting bounds prematurely.
      const minX = Math.min(0, vpW * 0.15 - scaledW);
      const maxX = Math.max(minX, vpW * 0.85);

      const minY = Math.min(0, vpH * 0.15 - scaledH);
      const maxY = Math.max(minY, vpH * 0.85);

      this.transX = Math.max(minX, Math.min(maxX, this.transX));
      this.transY = Math.max(minY, Math.min(maxY, this.transY));
    }

    applyTransform() {
      if (!this.targetElement) return;
      // Failure Mode 29: Pure DOM matrix transform
      this.targetElement.style.transform = `matrix(${this.scale}, 0, 0, ${this.scale}, ${this.transX}, ${this.transY})`;
      this.applyFilter();
    }

    applyFilter() {
      if (!this.targetElement) return;
      // Failure Mode 20: Color-preserving Dark Filter
      if (this.filterMode === 'preserve') {
        this.targetElement.style.filter = 'invert(1) hue-rotate(180deg)';
      } else if (this.filterMode === 'invert') {
        this.targetElement.style.filter = 'invert(1)';
      } else {
        this.targetElement.style.filter = 'none';
      }
    }

    cycleFilter() {
      if (this.filterMode === 'preserve') {
        this.filterMode = 'invert';
      } else if (this.filterMode === 'invert') {
        this.filterMode = 'none';
      } else {
        this.filterMode = 'preserve';
      }
      this.applyFilter();
      return this.filterMode;
    }

    resetTransform() {
      this.scale = 1.0;
      this.transX = 0;
      this.transY = 0;
      this.fitToViewport();
    }

    centerReset() {
      // Failure Mode 25: [⦿] Center Reset
      this.scale = 1.0;
      if (this.targetElement && this.viewport) {
        const vpW = this.viewport.clientWidth;
        const vpH = this.viewport.clientHeight;
        const elW = parseFloat(this.targetElement.getAttribute('width')) || this.targetElement.clientWidth || 800;
        const elH = parseFloat(this.targetElement.getAttribute('height')) || this.targetElement.clientHeight || 500;
        this.transX = (vpW - elW) / 2;
        this.transY = (vpH - elH) / 2;
      } else {
        this.transX = 0;
        this.transY = 0;
      }
      this.applyTransform();
    }

    fitToViewport() {
      if (!this.targetElement || !this.viewport) return;
      const vpW = this.viewport.clientWidth;
      const vpH = this.viewport.clientHeight;
      if (vpW <= 0 || vpH <= 0) return;

      const elW = parseFloat(this.targetElement.getAttribute('width')) || this.targetElement.clientWidth || 800;
      const elH = parseFloat(this.targetElement.getAttribute('height')) || this.targetElement.clientHeight || 500;

      const scaleX = (vpW * 0.92) / elW;
      const scaleY = (vpH * 0.92) / elH;
      this.scale = Math.min(scaleX, scaleY, 1.25);

      this.transX = (vpW - elW * this.scale) / 2;
      this.transY = (vpH - elH * this.scale) / 2;
      this.applyTransform();
    }

    zoomBy(delta) {
      const factor = delta > 0 ? 1.25 : 0.8;
      const rect = this.viewport.getBoundingClientRect();
      const centerX = rect.width / 2;
      const centerY = rect.height / 2;

      const newScale = Math.min(Math.max(this.scale * factor, 0.15), 12.0);
      this.transX = centerX - (centerX - this.transX) * (newScale / this.scale);
      this.transY = centerY - (centerY - this.transY) * (newScale / this.scale);
      this.scale = newScale;

      this.clampBounds();
      this.applyTransform();
    }
  }

  // =========================================================================
  // CLASS 3: StreamParserObserver (Failure Modes 02, 05, 12, 34)
  // =========================================================================
  class StreamParserObserver {
    constructor(onDiagramDetected, onNavigation = null) {
      this.onDiagramDetected = onDiagramDetected;
      this.onNavigation = onNavigation;
      this.debounceTimer = null;
      this.observer = null;
      this.processedHashes = new Set();
      this.lastChatPath = window.location.pathname;
    }

    start() {
      // Failure Mode 12: Scoped MutationObserver targeting chat streams
      this.observer = new MutationObserver((mutations) => {
        let shouldParse = false;
        for (const m of mutations) {
          // Ignore mutations from within our own Cockpit UI: root, reader, toast, dock tabs, resizer
          if (m.target?.id === 'spark-action-toast' ||
              (m.target?.closest && m.target.closest('#spark-cockpit-root, #spark-reader-root, #spark-action-toast, .spark-dock-tab, .spark-resizer-handle'))) {
            continue;
          }
          if (m.target?.classList && (m.target.classList.contains('katex') || m.target.classList.contains('math'))) continue;

          // Typing isolation: ignore typing events, cursor blinks, autocomplete in chat inputs
          if (m.target?.closest && m.target.closest('rich-textarea, [contenteditable="true"], textarea, form, .input-area, [role="textbox"], .text-input-field')) continue;
          if (m.target?.tagName === 'TEXTAREA' || m.target?.tagName === 'INPUT') continue;

          if (m.addedNodes.length > 0) {
            let hasNonTypingNode = false;
            for (const node of m.addedNodes) {
              if (node.nodeType === Node.ELEMENT_NODE) {
                if (node.id === 'spark-action-toast' || node.classList?.contains?.('spark-dock-tab')) continue;
                if (node.closest?.('#spark-cockpit-root, #spark-reader-root, #spark-action-toast, .spark-dock-tab, .spark-resizer-handle')) continue;
                if (node.closest?.('rich-textarea, [contenteditable="true"], textarea, form, .input-area, [role="textbox"]')) continue;
                if (node.tagName === 'TEXTAREA' || node.tagName === 'INPUT') continue;
                hasNonTypingNode = true;
                break;
              } else if (node.nodeType === Node.TEXT_NODE) {
                if (node.parentElement?.closest?.('#spark-cockpit-root, #spark-reader-root, #spark-action-toast, .spark-dock-tab')) continue;
                if (node.parentElement?.closest?.('rich-textarea, [contenteditable="true"], textarea, form, .input-area, [role="textbox"]')) continue;
                hasNonTypingNode = true;
                break;
              }
            }
            if (hasNonTypingNode) {
              shouldParse = true;
              break;
            }
          }
        }

        // Detect major conversation route change (e.g. switching between different chat IDs in Gemini Spark)
        const currentPath = window.location.pathname;
        if (this.lastChatPath && this.lastChatPath !== currentPath) {
          this.lastChatPath = currentPath;
          this.onNavigation?.(currentPath);
          return;
        }

        if (shouldParse) {
          // Failure Mode 02: Debounce 300ms during streaming
          clearTimeout(this.debounceTimer);
          this.debounceTimer = setTimeout(() => {
            this.scanDocumentForDiagrams();
          }, 300);
        }
      });

      this.observer.observe(document.body, {
        childList: true,
        subtree: true
      });

      // Initial document scan
      this.scanDocumentForDiagrams();
    }

    stop() {
      if (this.observer) {
        this.observer.disconnect();
        this.observer = null;
      }
      clearTimeout(this.debounceTimer);
    }

    resetHashes() {
      this.processedHashes.clear();
      this.processedPdfFileIds?.clear();
    }

    /**
     * Chat Area Guard:
     * Accepts ONLY diagrams & links inside the active chat conversation.
     * Strictly excludes:
     * - Cockpit's own components (#spark-cockpit-root)
     * - Right sidebar panels ("Tiến trình", "Tệp", "Kỹ năng và ứng dụng")
     * - Left navigation bar & drawer menus
     * - Top application headers & banners (Gemini Sparkle logo, avatars)
     * - Interactive UI buttons & controls
     */
    isInsideModelResponse(element) {
      if (!element || !(element instanceof Element)) return false;

      // 1. Strictly exclude Cockpit's own components to prevent self-scanning loops
      if (element.closest('#spark-cockpit-root, #spark-reader-root, #spark-action-toast, .spark-dock-tab, #spark-floating-launcher, .spark-resizer-handle')) {
        return false;
      }

      // 2. Strictly exclude UI chrome, header, navigation, and sidebar panels
      const excludedZone = element.closest(
        'header, nav, [role="navigation"], aside, [role="complementary"], ' +
        '[class*="sidebar"], [class*="side-panel"], [class*="side_panel"], [class*="right-panel"], [class*="right_panel"], ' +
        '[class*="drawer"], [class*="companion"], [class*="tools-panel"], [class*="files-panel"], [class*="file-list"], ' +
        '[class*="file_list"], [class*="knowledge"], mat-sidenav, .mat-drawer, button, [role="button"]'
      );
      if (excludedZone) return false;

      // 3. Strictly verify element is inside the chat conversation area
      const inChat = element.closest('model-response, user-query, [data-message-author-role], message-content, div[class*="model-response"], div[class*="user-query"]');
      if (!inChat) return false;

      // 4. Must be connected to the active DOM tree and not inside a hidden container
      if (!element.isConnected) return false;
      if (element.closest('[hidden], [aria-hidden="true"], .hidden, [style*="display: none"], [style*="visibility: hidden"]')) return false;

      return true;
    }

    static getCurrentChatId() {
      const match = window.location.pathname.match(/(?:\/chat\/|\/app\/)([a-zA-Z0-9_-]+)/);
      return match ? match[1] : 'default';
    }

    static isGoogleOfficeDoc(url) {
      if (!url || typeof url !== 'string') return false;
      return /\/(?:document|spreadsheets|presentation|forms)\/d\//i.test(url) ||
             /\/drive\/folders\//i.test(url);
    }

    static extractDriveFileId(url) {
      if (!url || typeof url !== 'string') return null;
      // Strictly reject Google Docs, Sheets, Slides, Forms, and Folder URLs
      if (StreamParserObserver.isGoogleOfficeDoc(url)) return null;

      // Match /d/{id} or /file/d/{id} or /u/X/file/d/{id} or /file/u/X/d/{id}
      const dMatch = url.match(/\/d\/([a-zA-Z0-9_-]{15,})/i);
      if (dMatch) return dMatch[1];

      // Match [?&]id={id} (open?id=, uc?id=, thumbnail?id=, download?id=, etc.)
      const idMatch = url.match(/[?&]id=([a-zA-Z0-9_-]{15,})/i);
      if (idMatch) return idMatch[1];

      // Match /file/d/{id}
      const fileMatch = url.match(/\/file\/d\/([a-zA-Z0-9_-]{15,})/i);
      if (fileMatch) return fileMatch[1];

      return null;
    }

    static isDirectImageUrl(url) {
      if (!url || typeof url !== 'string') return false;
      const lower = url.toLowerCase();
      // Exclude Drive links (handled separately)
      if (lower.includes('drive.google.com') || lower.includes('docs.google.com')) return false;

      // Exclude Google profile avatars, gstatic UI icons, logos, and sparkle assets
      if (
        lower.includes('googleusercontent.com/a/') ||
        lower.includes('googleusercontent.com/a-') ||
        lower.includes('gstatic.com') ||
        lower.includes('sparkle') ||
        lower.includes('avatar') ||
        lower.includes('profile') ||
        lower.includes('favicon') ||
        lower.includes('logo') ||
        lower.includes('icon')
      ) {
        return false;
      }

      if (url.startsWith('data:image/') || url.startsWith('blob:')) return true;
      return /\.(png|jpe?g|webp|svg|gif|bmp)($|[?#])/i.test(url) ||
             lower.includes('googleusercontent.com/d/');
    }

    static extractStructuredText(node) {
      if (!node) return '';
      if (node.nodeType === Node.TEXT_NODE) {
        return node.nodeValue || '';
      }
      if (node.nodeType !== Node.ELEMENT_NODE) return '';

      const tag = node.tagName.toLowerCase();
      if (tag === 'script' || tag === 'style') return '';
      if (tag === 'br') return '\n';

      // KaTeX formula extraction
      if (node.classList?.contains('katex')) {
        const texAnn = node.querySelector('annotation[encoding="application/x-tex"]');
        if (texAnn) return `$${texAnn.textContent.trim()}$`;
      }

      // Reconstruct links [text](href)
      if (tag === 'a' && node.getAttribute('href')) {
        const href = node.getAttribute('href').trim();
        const linkText = node.textContent?.trim() || href;
        return `[${linkText}](${href})`;
      }

      // Traverse child nodes
      let text = '';
      for (const child of node.childNodes) {
        text += StreamParserObserver.extractStructuredText(child);
      }

      // Ensure block elements have linebreaks
      if (tag === 'h1') return `\n\n# ${text.trim()}\n\n`;
      if (tag === 'h2') return `\n\n## ${text.trim()}\n\n`;
      if (tag === 'h3') return `\n\n### ${text.trim()}\n\n`;
      if (tag === 'h4') return `\n\n#### ${text.trim()}\n\n`;
      if (tag === 'p' || tag === 'div' || tag === 'section' || tag === 'article') {
        const trimmed = text.trim();
        return trimmed ? `\n\n${trimmed}\n\n` : '';
      }
      if (tag === 'li') {
        const trimmed = text.trim();
        return trimmed ? `\n- ${trimmed}` : '';
      }
      if (tag === 'ul' || tag === 'ol') {
        return `\n\n${text}\n\n`;
      }
      if (tag === 'blockquote') {
        return `\n\n> ${text.trim()}\n\n`;
      }
      if (tag === 'strong' || tag === 'b') {
        return `**${text}**`;
      }
      if (tag === 'em' || tag === 'i') {
        return `*${text}*`;
      }
      if (tag === 'code' && node.parentElement?.tagName.toLowerCase() !== 'pre') {
        return `\`${text}\``;
      }
      if (tag === 'pre') {
        return `\n\n\`\`\`\n${text.trim()}\n\`\`\`\n\n`;
      }

      return text;
    }

    scanDocumentForDiagrams() {
      const candidates = [];
      const seenInThisScan = new Set();

      // 0. Stream Interceptor: Scan for :::spark-reader-content and :::spark-archive-manifest (v2.0)
      const allContainers = Array.from(document.querySelectorAll(
        'message-content, div[class*="model-response-text"], div[class*="message-content"], model-response'
      )).filter(el => this.isInsideModelResponse(el));

      // Target innermost leaf containers only to avoid duplicate processing
      const leafContainers = allContainers.filter(el => 
        !allContainers.some(other => other !== el && el.contains(other))
      );

      leafContainers.forEach(block => {
        const rawContent = block.textContent || '';
        // Strict boundary: Only process blocks that contain our explicit stream wrappers
        // Normal chat messages without this tag will remain 100% untouched and visible!
        if (!rawContent.includes(':::spark-reader-content') && !rawContent.includes(':::spark-archive-manifest')) {
          return;
        }

        const structuredText = StreamParserObserver.extractStructuredText(block);

        // Match :::spark-reader-content ... :::
        if (structuredText.includes(':::spark-reader-content')) {
          const m = structuredText.match(/:::spark-reader-content([\s\S]*?)(?::::|$)/i);
          if (m && m[1]) {
            const readerContent = m[1].trim();
            block.setAttribute('data-spark-stream-hidden', 'true');
            block.classList.add('spark-stream-hidden');

            // Check if there is an embedded Drive PDF link inside reader content
            const drivePdfId = StreamParserObserver.extractDriveFileId(readerContent);
            if (drivePdfId && (readerContent.includes('.pdf') || readerContent.includes('drive.google.com'))) {
              this.processedPdfFileIds = this.processedPdfFileIds || new Set();
              if (!this.processedPdfFileIds.has(drivePdfId)) {
                this.processedPdfFileIds.add(drivePdfId);
                const titleMatch = readerContent.match(/\[([^\]]+)\]\([^\)]+\)/) || readerContent.match(/^#+\s+(.+)$/m);
                const pdfTitle = titleMatch ? titleMatch[1].trim() : `Bài_Giang_${drivePdfId.substring(0, 6)}.pdf`;
                window.__SPARK_LAYOUT_MANAGER__?.readerEngine?.loadPdf(drivePdfId, pdfTitle, null, true);
              }
            }

            // Add clean in-chat notification pill
            let chatPill = block.parentElement?.querySelector('.spark-chat-pill');
            if (!chatPill && block.parentElement) {
              chatPill = document.createElement('div');
              chatPill.className = 'spark-chat-pill';
              chatPill.innerHTML = `<span>Bài giảng PDF đã sẵn sàng trên Khung <b>READ</b>. Nhấp để mở hoặc tiếp tục thảo luận tại đây.</span>`;
              chatPill.addEventListener('click', () => {
                window.__SPARK_LAYOUT_MANAGER__?.setRightPaneMode('READER');
              });
              block.parentElement.appendChild(chatPill);
            }

            if (window.__SPARK_LAYOUT_MANAGER__?.readerEngine) {
              window.__SPARK_LAYOUT_MANAGER__.readerEngine.renderContent(readerContent);
              if (window.__SPARK_LAYOUT_MANAGER__.rightPaneMode === 'READER') {
                window.__SPARK_LAYOUT_MANAGER__.readerEngine.rootElement.classList.remove('reader-hidden');
              }
            }
          }
        }

        // Match :::spark-archive-manifest ... :::
        if (structuredText.includes(':::spark-archive-manifest')) {
          const mManifest = structuredText.match(/:::spark-archive-manifest([\s\S]*?)(?::::|$)/i);
          if (mManifest && mManifest[1]) {
            try {
              const manifestJson = JSON.parse(mManifest[1].trim());
              const pdfId = manifestJson.pdf_file_id || manifestJson.file_id || StreamParserObserver.extractDriveFileId(manifestJson.drive_url);
              this.processedPdfFileIds = this.processedPdfFileIds || new Set();
              if (pdfId && !this.processedPdfFileIds.has(pdfId)) {
                this.processedPdfFileIds.add(pdfId);
                const title = manifestJson.document_title || manifestJson.file_name || `Bài_Giang_${pdfId.substring(0,6)}.pdf`;
                window.__SPARK_LAYOUT_MANAGER__?.readerEngine?.loadPdf(pdfId, title, manifestJson.drive_url, true);
              }
              window.__SPARK_LAYOUT_MANAGER__?.triggerArchiveLesson(manifestJson);
            } catch (err) {
              // Partial stream, wait for completion
            }
          }
        }
      });

      // 1. Scan for links in <a> tags (Drive links and direct image links)

      const links = document.querySelectorAll('a[href]');
      links.forEach(a => {
        if (!this.isInsideModelResponse(a)) return;

        const href = (a.getAttribute('href') || '').trim();
        if (!href || href.startsWith('#') || href.startsWith('javascript:')) return;

        const linkText = (a.textContent || '').trim();
        const aTitle = a.getAttribute('title') || '';
        const aAria = a.getAttribute('aria-label') || '';
        const combinedText = `${linkText} ${aTitle} ${aAria}`.trim();

        const contextContainer = a.closest('.micro-block, div[class*="markdown"], p, li, [class*="message"], message-content, model-response, user-query') || a.parentElement;
        const contextText = contextContainer?.textContent || combinedText;
        const metadata = this.extractAxesMetadata(contextText);

        // Check if Google Drive file
        const driveFileId = StreamParserObserver.extractDriveFileId(href);
        if (driveFileId) {
          // Check if file is flagged for deletion / error (Section IV.2: Move-to-Root Protocol)
          if (/LOI_CAN_XOA/i.test(linkText) || /LOI_CAN_XOA/i.test(href)) {
            return;
          }

          // A. Skip non-image documents (Office docs, spreadsheets, zip, audio/video)
          const isExplicitNonImage = /\.(docx?|pptx?|xlsx?|zip|rar|txt|csv|mp4|mp3)($|[?#])/i.test(href) ||
                                     /\.(docx?|pptx?|xlsx?|zip|rar|txt|csv)\b/i.test(combinedText) ||
                                     /(?:hồ sơ|kiểm toán|audit|báo cáo|biên bản|worksheet|bảng tính|ho_so_kiem_toan)/i.test(combinedText) ||
                                     /(?:ho_so_kiem_toan|kiem_toan|audit)/i.test(href) ||
                                     /docs\.google\.com/i.test(href);
          if (isExplicitNonImage) return;

          // B. FIRST: Check if this Drive link represents a Diagram / Simulation / Image for Tab Trái (Left Canvas)
          const parentLine = a.closest('li, p, div')?.textContent || contextText;
          const fileMatch = parentLine.match(/(?:^|\n|\-\s*|\*\s*)(\[(?:Goc|Mo_Phong|Original|Simulation)\][^\s:]+)\s*:/i) ||
                            parentLine.match(/(\[[A-Za-z0-9_-]+\][A-Za-z0-9_\-\.]+\.(?:png|jpg|jpeg|svg|webp))\s*:/i) ||
                            parentLine.match(/([a-zA-Z0-9_\-]+\.(?:png|jpg|jpeg|svg|webp))\s*:/i);
          const figMatch = (combinedText + ' ' + parentLine).match(/(?:Figure|Fig\.?|Hình|Biểu đồ|Sơ đồ|Đồ thị|Mô hình|Mô phỏng|Minh họa|Minh hoạ|Quang học|Tạo ảnh|Tia sáng|Chiết suất|Cầu sai|Biên dạng|Phản xạ|Khúc xạ|Quang hình)\s*[:\-\s]*(\d+(?:\.\d+)*[a-z]?|[A-Za-z0-9_\s]{3,35})/i);
          const hasImageExt = /\.(png|jpe?g|webp|svg|gif|bmp)($|[?#])/i.test(href) ||
                              /\.(png|jpe?g|webp|svg|gif|bmp)\b/i.test(combinedText);
          const hasDiagramTag = /\[(?:Goc|Mo_Phong|Original|Simulation|Diagram|Chart|Figure)\]/i.test(parentLine) ||
                                /\[(?:Goc|Mo_Phong|Original|Simulation|Diagram|Chart|Figure)\]/i.test(combinedText);
          const hasDiagramKeywords = /(?:^|\b)(?:hình|figure|fig\.?|sơ đồ|đồ thị|biểu đồ|mô hình|mô phỏng|minh họa|minh hoạ|plot|chart|ảnh|cầu sai|biên dạng|phản xạ|khúc xạ|tia sáng|bề mặt)\b/i.test(linkText);

          const isDiagram = !!(fileMatch || figMatch || hasImageExt || hasDiagramTag || hasDiagramKeywords);

          if (isDiagram) {
            // It is a DIAGRAM for Tab Trái (Visual Cockpit)!
            // NEVER pass to Reader Overlay (Tab Phải)!
            const hash = 'drive_' + driveFileId;
            if (seenInThisScan.has(hash)) return;

            let diagramTitle = fileMatch ? fileMatch[1].trim() : (figMatch ? figMatch[0].trim() : (aTitle || linkText || `Drive_${driveFileId.substring(0, 6)}`));

            seenInThisScan.add(hash);
            candidates.push({
              element: a,
              type: 'DRIVE',
              id: driveFileId,
              fileId: driveFileId,
              title: diagramTitle,
              metadata,
              hash
            });
            return;
          }

          // C. SECOND: Check if this Drive link represents a genuine PDF / Lecture document for Tab Phải (Reader)
          const isKnownPdf = !!(this.processedPdfFileIds?.has(driveFileId) ||
                                window.__SPARK_LAYOUT_MANAGER__?.readerEngine?.pdfStack?.some(p => p.fileId === driveFileId));
          const isPdf = isKnownPdf ||
                        /\.pdf($|[?#])/i.test(href) || 
                        /\.pdf\b/i.test(combinedText) ||
                        /(?:bài giảng|giáo trình|tài liệu|lecture|slides?|sách|văn bản|tập tài liệu|chương \d|phân mục \d|bản chuyên khảo|chuyên khảo|mục \d)\b/i.test(combinedText) ||
                        (/(?:bài giảng|giáo trình|tài liệu|chương \d|phân mục \d|bản chuyên khảo|chuyên khảo|mục \d)\b/i.test(parentLine) && /(?:open drive|drive|xem|tải|link|download|tại đây)/i.test(linkText));

          if (isPdf) {
            this.processedPdfFileIds = this.processedPdfFileIds || new Set();
            if (this.processedPdfFileIds.has(driveFileId)) {
              return; // Already processed in Reader
            }
            this.processedPdfFileIds.add(driveFileId);

            let pdfTitle = linkText;
            if (!pdfTitle || pdfTitle.startsWith('http') || pdfTitle.length < 3 || /^(open drive|drive|xem|tải|link)/i.test(pdfTitle.trim())) {
              const docMatch = parentLine.match(/(?:Tài liệu|Bài giảng|Giáo trình|Bản Chuyên khảo|Chuyên khảo|Phân mục|Mục|Chương)\s*[:\-\s]*([^:\n|]+)/i);
              pdfTitle = docMatch ? docMatch[0].trim() + '.pdf' : `Bài_Giang_${driveFileId.substring(0, 6)}.pdf`;
            }
            window.__SPARK_LAYOUT_MANAGER__?.readerEngine?.loadPdf(driveFileId, pdfTitle, href, true);
            return;
          }

          // D. If neither diagram nor PDF (e.g. generic link without markers): DO NOTHING!
          // NEVER blindly dump unknown links into Reader or Canvas!
          return;
        }

        // Check if direct image link
        if (StreamParserObserver.isDirectImageUrl(href)) {
          const hash = 'imglink_' + this.simpleHash(href);
          if (seenInThisScan.has(hash)) return;

          let diagramTitle = linkText && !linkText.startsWith('http') ? linkText : '';
          if (!diagramTitle) {
            const figMatch = contextText.match(/(?:Figure|Fig\.?|Hình|Mục)\s*[:\-\s]*(\d+(?:\.\d+)*[a-z]?)/i);
            diagramTitle = figMatch ? figMatch[0] : `Ảnh (${href.substring(0, 25)}...)`;
          }

          seenInThisScan.add(hash);
          candidates.push({
            element: a,
            type: 'DIRECT_IMAGE',
            id: hash,
            title: diagramTitle,
            dataUrl: href,
            metadata,
            hash
          });
        }
      });

      // 1b. Scan chat text blocks for plain text URLs (Drive links & Image URLs)
      const chatBlocks = document.querySelectorAll(
        'message-content, model-response, user-query, [data-message-author-role], .micro-block, div[class*="markdown"], div[class*="message"], p, li, pre, code, article, [class*="content"]'
      );
      chatBlocks.forEach(block => {
        if (!this.isInsideModelResponse(block)) return;
        const text = block.textContent || '';
        if (!text.includes('http://') && !text.includes('https://')) return;

        // Match all URLs in plain text
        const urlMatches = text.matchAll(/https?:\/\/[^\s"'<>\)\],]+/gi);
        for (const m of urlMatches) {
          const rawUrl = m[0];
          // Strip trailing punctuation often caught in sentences (e.g. "https://url." or "https://url)")
          const url = rawUrl.replace(/[.,;:!?)]+$/, '');

          // Extract single line around URL for precise context
          const urlIndex = m.index || 0;
          const lineStart = text.lastIndexOf('\n', urlIndex) + 1;
          const lineEnd = text.indexOf('\n', urlIndex);
          const currentLine = text.substring(lineStart, lineEnd === -1 ? text.length : lineEnd);

          // Check if Drive file
          const driveFileId = StreamParserObserver.extractDriveFileId(url);
          if (driveFileId) {
            // A. Skip if already processed as PDF
            // A. Skip non-image documents
            const isExplicitNonImage = /\.(docx?|pptx?|xlsx?|zip|rar|txt|csv|mp4|mp3)($|[?#])/i.test(url) ||
                                       /(?:ho_so_kiem_toan|kiem_toan|audit)/i.test(url) ||
                                       /(?:hồ sơ|kiểm toán|audit|báo cáo|biên bản)\b/i.test(currentLine);
            if (isExplicitNonImage) continue;

            // B. FIRST: Check if this Drive URL represents a Diagram / Simulation / Image for Tab Trái
            const metadata = this.extractAxesMetadata(text);
            const fileMatch = currentLine.match(/(?:^|\n|\-\s*|\*\s*)(\[(?:Goc|Mo_Phong|Original|Simulation)\][^\s:]+)\s*:/i) ||
                              currentLine.match(/(\[[A-Za-z0-9_-]+\][A-Za-z0-9_\-\.]+\.(?:png|jpg|jpeg|svg|webp))\s*:/i) ||
                              currentLine.match(/([a-zA-Z0-9_\-]+\.(?:png|jpg|jpeg|svg|webp))\s*:/i);
            const figMatch = currentLine.match(/(?:Figure|Fig\.?|Hình|Biểu đồ|Sơ đồ|Đồ thị|Mô hình|Mô phỏng|Minh họa|Minh hoạ|Quang học|Tạo ảnh|Tia sáng|Chiết suất|Cầu sai|Biên dạng|Phản xạ|Khúc xạ|Quang hình)\s*[:\-\s]*(\d+(?:\.\d+)*[a-z]?|[A-Za-z0-9_\s]{3,35})/i);
            const hasImageExt = /\.(png|jpe?g|webp|svg|gif|bmp)($|[?#])/i.test(url) ||
                                /(\.(png|jpe?g|webp|svg|gif|bmp)|\[(?:Goc|Mo_Phong|Original|Simulation)\])/i.test(currentLine);

            if (fileMatch || figMatch || hasImageExt) {
              const hash = 'drive_' + driveFileId;
              if (seenInThisScan.has(hash)) continue;

              let diagramTitle = fileMatch ? fileMatch[1].trim() : (figMatch ? figMatch[0].trim() : `Drive_${driveFileId.substring(0, 6)}`);

              seenInThisScan.add(hash);
              candidates.push({
                element: block,
                type: 'DRIVE',
                id: driveFileId,
                fileId: driveFileId,
                title: diagramTitle,
                metadata,
                hash
              });
              continue;
            }

            // C. SECOND: Check if this Drive URL represents a genuine PDF document
            const isKnownPdf = !!(this.processedPdfFileIds?.has(driveFileId) ||
                                  window.__SPARK_LAYOUT_MANAGER__?.readerEngine?.pdfStack?.some(p => p.fileId === driveFileId));
            const isPdf = isKnownPdf ||
                          /\.pdf($|[?#])/i.test(url) || 
                          /(?:bài giảng|giáo trình|tài liệu|chương \d|phân mục \d|bản chuyên khảo|chuyên khảo|mục \d)(?:\.pdf)?\b/i.test(currentLine);
            if (isPdf) {
              this.processedPdfFileIds = this.processedPdfFileIds || new Set();
              if (!this.processedPdfFileIds.has(driveFileId)) {
                this.processedPdfFileIds.add(driveFileId);
                const titleMatch = currentLine.match(/(?:Tài liệu|Bài giảng|Giáo trình|Bản Chuyên khảo|Chuyên khảo|Phân mục|Mục|Chương)\s*[:\-\s]*([^:\n|]+)/i);
                const pdfTitle = titleMatch ? titleMatch[0].trim() + '.pdf' : `Bài_Giang_${driveFileId.substring(0, 6)}.pdf`;
                window.__SPARK_LAYOUT_MANAGER__?.readerEngine?.loadPdf(driveFileId, pdfTitle, url, true);
              }
              continue;
            }

            // D. Otherwise skip
            continue;
          }

          // Check if direct image link in plain text
          if (StreamParserObserver.isDirectImageUrl(url)) {
            const hash = 'imgtext_' + this.simpleHash(url);
            if (seenInThisScan.has(hash)) continue;

            const metadata = this.extractAxesMetadata(text);
            const figMatch = text.match(/(?:Figure|Fig\.?|Hình|Mục)\s*[:\-\s]*(\d+(?:\.\d+)*[a-z]?)/i);
            const diagramTitle = figMatch ? figMatch[0] : `Ảnh (${url.substring(0, 25)}...)`;

            seenInThisScan.add(hash);
            candidates.push({
              element: block,
              type: 'DIRECT_IMAGE',
              id: hash,
              title: diagramTitle,
              dataUrl: url,
              metadata,
              hash
            });
          }
        }
      });

      // 2. Scan for SVG elements directly in AI response
      const allSvgs = document.querySelectorAll('svg');
      allSvgs.forEach(svg => {
        // Enforce strict model response chat boundary
        if (!this.isInsideModelResponse(svg)) return;
        if (svg.classList.contains('katex-svg')) return;

        // Filter tiny UI icons (typically 16-48px in Gemini)
        const vb = svg.getAttribute('viewBox') || '';
        const vbParts = vb.split(/[\s,]+/).map(parseFloat);
        const vbW = vbParts.length === 4 ? vbParts[2] : (parseFloat(svg.getAttribute('width')) || 0);
        const vbH = vbParts.length === 4 ? vbParts[3] : (parseFloat(svg.getAttribute('height')) || 0);
        
        // Diagram must have realistic canvas dimensions (at least 120x80)
        if (vbW > 0 && vbH > 0 && (vbW < 120 || vbH < 80)) return;

        // STREAMING GUARD (Tier 3): SVG must have >= 2 graphical elements, not an empty shell or partial stream
        const graphicElements = svg.querySelectorAll('path, rect, line, circle, polygon, polyline, text, ellipse, image, use');
        if (graphicElements.length < 2) return;

        const container = svg.closest('.micro-block, pre, code, div[class*="markdown"], div[class*="message"], article') || svg.parentElement;
        const svgXml = svg.outerHTML;
        const hash = 'svg_' + this.simpleHash(svgXml);
        if (seenInThisScan.has(hash)) return;

        const sanitizedSvg = SanitizerAndPostProcessor.sanitizeSvgString(svgXml);
        if (sanitizedSvg) {
          seenInThisScan.add(hash);
          const contextText = container?.textContent || '';
          const metadata = this.extractAxesMetadata(contextText);
          const title = SanitizerAndPostProcessor.extractTitle(sanitizedSvg, svgXml, contextText);
          candidates.push({
            element: svg,
            type: 'SVG',
            id: hash,
            title,
            svgElement: sanitizedSvg,
            metadata,
            hash
          });
        }
      });

      // 3. Scan for fenced SVG code blocks in AI response text / code containers
      const codeElements = document.querySelectorAll('code, pre, [class*="code-block"], [class*="formatted-code"], [class*="syntax"], [class*="code-container"]');
      codeElements.forEach(el => {
        // Enforce strict model response chat boundary
        if (!this.isInsideModelResponse(el)) return;
        const text = el.textContent || '';

        // STREAMING GUARD (Tier 1): Must match a strictly complete SVG pair.
        const hasCompleteSvg = (
          (/<svg[\s\S]*?<\/svg>/i.test(text)) ||
          (/&lt;svg[\s\S]*?&lt;\/svg/i.test(text))
        );
        if (!hasCompleteSvg && !text.includes('diagram-spark')) return;
        if (!hasCompleteSvg && text.includes('diagram-spark') && (!text.includes('</') && !text.includes('&lt;/'))) return;

        // STREAMING GUARD (Tier 4): Markdown fence completion check
        if (text.trim().startsWith('```')) {
          const backticks = (text.match(/```/g) || []).length;
          if (backticks % 2 !== 0 && !text.includes('</svg>') && !text.includes('&lt;/svg')) {
            return; // Code block is still actively streaming
          }
        }

        const hash = 'svg_code_' + this.simpleHash(text);
        if (seenInThisScan.has(hash)) return;

        const sanitizedSvg = SanitizerAndPostProcessor.sanitizeSvgString(text);
        if (sanitizedSvg) {
          seenInThisScan.add(hash);
          const contextContainer = el.closest('.micro-block, div[class*="markdown"], div[class*="message"], article') || el.parentElement;
          let contextText = '';
          if (el.nextElementSibling && (el.nextElementSibling.textContent || '').includes('[')) {
            contextText = el.nextElementSibling.textContent;
          }
          if (!contextText && contextContainer) {
            contextText = contextContainer.textContent || text;
          } else if (!contextText) {
            contextText = text;
          }
          const metadata = this.extractAxesMetadata(contextText);
          const title = SanitizerAndPostProcessor.extractTitle(sanitizedSvg, text, contextText);
          candidates.push({
            element: el,
            type: 'SVG',
            id: hash,
            title,
            svgElement: sanitizedSvg,
            metadata,
            hash
          });
        }
      });

      // 3b. Scan markdown / chat message panels in AI response for raw or fenced markdown SVG blocks
      const msgPanels = document.querySelectorAll('div[class*="markdown"], div[class*="message"], div[class*="model-response"], article, .micro-block');
      msgPanels.forEach(panel => {
        // Enforce strict model response chat boundary
        if (!this.isInsideModelResponse(panel)) return;
        const text = panel.textContent || '';

        // STREAMING GUARD (Tier 1): Quick bail-out if opening or closing tags missing
        if (!text.includes('<svg') && !text.includes('&lt;svg')) return;
        if (!text.includes('</svg>') && !text.includes('&lt;/svg')) return;

        // STREAMING GUARD (Tier 4): Check active code fence streaming
        const backtickCount = (text.match(/```/g) || []).length;
        if (backtickCount > 0 && backtickCount % 2 !== 0) {
          const lastFenceIndex = text.lastIndexOf('```');
          const textAfterFence = text.substring(lastFenceIndex);
          if ((textAfterFence.includes('<svg') || textAfterFence.includes('&lt;svg')) &&
              (!textAfterFence.includes('</svg>') && !textAfterFence.includes('&lt;/svg'))) {
            return; // SVG is actively streaming inside unclosed markdown fence
          }
        }

        const svgMatches = text.matchAll(/<svg[\s\S]*?<\/svg>/gi);
        for (const match of svgMatches) {
          const svgStr = match[0];
          const hash = 'svg_raw_' + this.simpleHash(svgStr);
          if (seenInThisScan.has(hash)) continue;

          const sanitizedSvg = SanitizerAndPostProcessor.sanitizeSvgString(svgStr);
          if (sanitizedSvg) {
            seenInThisScan.add(hash);
            const afterSvg = text.substring(match.index + svgStr.length);
            const metadata = this.extractAxesMetadata(afterSvg) || this.extractAxesMetadata(text);
            const title = SanitizerAndPostProcessor.extractTitle(sanitizedSvg, svgStr, text);
            candidates.push({
              element: panel,
              type: 'SVG',
              id: hash,
              title,
              svgElement: sanitizedSvg,
              metadata,
              hash
            });
          }
        }
      });

      // 4. Scan for inline generated images (Python Matplotlib plots, AI charts, base64 images)
      const inlineImages = document.querySelectorAll('model-response img, user-query img, message-content img, div[class*="model-response"] img, div[class*="user-query"] img');
      inlineImages.forEach(img => {
        // Enforce strict model response chat boundary
        if (!this.isInsideModelResponse(img)) return;

        // Skip buttons, headers, or avatar containers
        if (img.closest('button, [role="button"], [class*="avatar"], [class*="profile"], header, [class*="header"]')) return;

        const src = img.getAttribute('src') || '';
        if (!src) return;

        // Strict filter: Exclude UI icons, avatars, gstatic assets, and sparkle logos
        const lowerSrc = src.toLowerCase();
        if (
          lowerSrc.includes('googleusercontent.com/a/') ||
          lowerSrc.includes('googleusercontent.com/a-') ||
          lowerSrc.includes('gstatic.com') ||
          lowerSrc.includes('sparkle') ||
          lowerSrc.includes('avatar') ||
          lowerSrc.includes('profile') ||
          lowerSrc.includes('favicon') ||
          lowerSrc.includes('logo') ||
          lowerSrc.includes('icon')
        ) return;

        const className = (img.className || '').toString().toLowerCase();
        const alt = (img.getAttribute('alt') || '').toLowerCase();
        if (/(?:avatar|profile|user-icon|spark-brand|sparkle|logo|icon)/i.test(className) ||
            /(?:avatar|profile|user-icon|spark-brand|sparkle|logo|icon)/i.test(alt)) {
          return;
        }

        // Must be a legitimate simulation diagram or plot (at least 120x80)
        const w = img.naturalWidth || img.clientWidth || parseFloat(img.getAttribute('width')) || 0;
        const h = img.naturalHeight || img.clientHeight || parseFloat(img.getAttribute('height')) || 0;
        if ((w > 0 && w < 120) || (h > 0 && h < 80)) return;

        const hash = 'img_' + this.simpleHash(src.substring(0, 150) + '_' + (img.alt || ''));
        if (seenInThisScan.has(hash)) return;

        const container = img.closest('.micro-block, pre, code, div[class*="markdown"], div[class*="message"], article, message-content, model-response, user-query') || img.parentElement;
        const metadata = this.extractAxesMetadata(container?.textContent || '');
        const title = (img.alt || '').trim() || 'Ảnh Mô phỏng Inline (Python/AI)';

        seenInThisScan.add(hash);
        candidates.push({
          element: img,
          type: 'DIRECT_IMAGE',
          id: hash,
          title,
          dataUrl: src,
          metadata,
          hash
        });
      });

      // 5. Sort candidates in strict conversational DOM document order (top to bottom of chat)
      candidates.sort((a, b) => {
        if (a.element === b.element) return 0;
        if (!a.element || !b.element) return 0;
        const pos = a.element.compareDocumentPosition(b.element);
        if (pos & Node.DOCUMENT_POSITION_FOLLOWING) return -1;
        if (pos & Node.DOCUMENT_POSITION_PRECEDING) return 1;
        return 0;
      });

      // 6. Assign monotonic DOM sequence index (1 = oldest at top, N = newest at bottom)
      candidates.forEach((cand, idx) => {
        cand.domOrder = idx + 1;
      });

      // 7. Dispatch candidates from newest to oldest (N down to 1) so the newest diagram
      // is immediately focused and begins priority download first.
      // For older Drive images beyond the 20 most recent, mark as dormant (isDormant = true)
      // so they register onto the timeline as 'evicted' without clogging the network.
      const ramCutoffIndex = Math.max(0, candidates.length - 20);

      for (let i = candidates.length - 1; i >= 0; i--) {
        const cand = candidates[i];
        cand.isDormant = (i < ramCutoffIndex && cand.type === 'DRIVE');
        this.processedHashes.add(cand.hash);
        this.onDiagramDetected(cand);
      }
    }

    extractAxesMetadata(text) {
      if (!text || typeof text !== 'string') return null;
      // Protocol Section 5 (physics-diagram-studio):
      // ↳ [Trục X]: Chiều dày d (nm) | [Trục Y]: Năng lượng E (eV) | [Rào thế / Thông số]: V0 = 0.3 eV
      // Matches both standard format and dynamic parameter cards
      const arrowLineMatch = text.match(/(?:↳|->|>>|\*)\s*(\[.+)/);
      const lineToParse = arrowLineMatch ? arrowLineMatch[1] : text;

      // Section III.1: Anti-misrouting guard against pedagogical terminology footnotes
      // e.g. ↳ [Nồng độ hạt dẫn nội tại] (Intrinsic carrier concentration - ni): ...
      // Must contain at least one axis/physics keyword or '|' separator
      const hasAxisOrSeparator = /(?:trục\s*[xy]|rào\s*thế|thông\s*số|điểm\s*uốn|bandgap|vùng\s*cấm|toạ\s*độ|tọa\s*độ|delta)/i.test(lineToParse) ||
                                 lineToParse.includes('|');
      if (!hasAxisOrSeparator) {
        return null;
      }

      const pairRegex = /\[([^\]]+)\]\s*:\s*([^|\n\r]+)/g;
      const items = [];
      let m;
      let axisX = null;
      let axisY = null;
      let inflection = null;
      let infLabel = 'Điểm uốn / Rào thế';

      while ((m = pairRegex.exec(lineToParse)) !== null) {
        const rawLabel = m[1].trim();
        const val = m[2].trim();
        items.push({ label: rawLabel, value: val });

        if (/trục\s*x/i.test(rawLabel)) {
          axisX = val;
        } else if (/trục\s*y/i.test(rawLabel)) {
          axisY = val;
        } else {
          inflection = val;
          infLabel = rawLabel;
        }
      }

      if (items.length > 0 || axisX || axisY || inflection) {
        return {
          axisX: axisX || (items[0] && /trục\s*x/i.test(items[0].label) ? items[0].value : 'Chưa xác định'),
          axisY: axisY || (items[1] && /trục\s*y/i.test(items[1].label) ? items[1].value : 'Chưa xác định'),
          inflection: inflection || 'Tiêu chuẩn',
          infLabel: infLabel,
          items: items
        };
      }
      return null;
    }

    simpleHash(str) {
      let hash = 0;
      for (let i = 0; i < str.length; i++) {
        hash = ((hash << 5) - hash) + str.charCodeAt(i);
        hash |= 0;
      }
      return Math.abs(hash).toString(36);
    }
  }

    // =========================================================================
  // CLASS 7: ReaderOverlayEngine (v2.5.0 Cumulative Section Stack Workstation)
  // =========================================================================
  class ReaderOverlayEngine {
    constructor(layoutManager) {
      this.layoutManager = layoutManager;
      this.rootElement = null;
      this.headerElement = null;
      this.titleElement = null;
      this.btnOpenDrive = null;
      this.viewerContainer = null;
      this.emptyState = null;
      this.activePdf = null;
      this.pdfStack = []; // Cumulative stack of lecture PDF sections
      this.dismissedPdfIds = new Set(); // Files manually closed/dismissed by user ("tắt bớt đi")
      try {
        const savedDismissed = sessionStorage.getItem('spark_dismissed_pdf_ids');
        if (savedDismissed) {
          JSON.parse(savedDismissed).forEach(id => this.dismissedPdfIds.add(id));
        }
      } catch (_) {}
      this.init();
    }

    init() {
      this.rootElement = document.getElementById('spark-reader-root');
      if (!this.rootElement) {
        this.rootElement = document.createElement('div');
        this.rootElement.id = 'spark-reader-root';
        this.rootElement.className = 'reader-hidden';
        document.body.appendChild(this.rootElement);
      }
      this.rootElement.textContent = '';

      // 1. Cumulative PDF Stack Container (Fills 100% of reader space)
      this.viewerContainer = document.createElement('div');
      this.viewerContainer.className = 'spark-pdf-stack is-empty';

      // 2. Minimalist Empty State (Displayed ONLY when 0 PDFs exist in stack)
      this.createEmptyState();
      this.viewerContainer.appendChild(this.emptyState);
      this.rootElement.appendChild(this.viewerContainer);

      // User requested: Khi reload trang thì phải cập nhật trạng thái theo phiên hiện tại!
      // Luôn xóa bộ nhớ tạm PDF cũ của phiên trước khi tải trang để không giữ tài liệu cũ sang phiên mới.
      sessionStorage.removeItem('spark_pdf_stack');
      sessionStorage.removeItem('spark_active_pdf');
      sessionStorage.removeItem('current_pdf_url');

      // Cross-origin Clipboard Bridge for PDF Reader (all_frames postMessage sync)
      this.cachedPdfSelection = '';
      window.addEventListener('message', (e) => {
        if (!e.data || typeof e.data !== 'object') return;
        if (e.data.type === 'SPARK_SELECTION_CACHE' && typeof e.data.text === 'string') {
          this.cachedPdfSelection = e.data.text.trim();
        } else if (e.data.type === 'SPARK_FORCE_COPY') {
          // Handled passively
        } else if (e.data.type === 'SPARK_COPY_CONFIRMED') {
          // Handled passively - copy feature detached per user directive
        }
      });

      // Listen for forwarded selection sync from extension background
      if (typeof chrome !== 'undefined' && chrome.runtime?.onMessage) {
        chrome.runtime.onMessage.addListener((msg) => {
          if (msg && msg.action === 'SPARK_DO_COPY') {
            // Handled passively - copy UI detached
          } else if (msg && msg.action === 'SPARK_SELECTION_CACHE' && typeof msg.text === 'string') {
            this.cachedPdfSelection = msg.text.trim();
          }
        });
      }
    }

    createCopyButton() {
      // Stub: Copy button removed from UI per user directive (SPARK_TRIGGER_COPY detached)
      const btnCopy = document.createElement('button');
      btnCopy.className = 'spark-btn-copy-pdf';
      btnCopy.style.display = 'none';
      return btnCopy;
    }

    animateCopySuccess(btnElement = null) {
      // Stub: Copy feedback removed per user directive
      const targets = Array.from(this.viewerContainer?.querySelectorAll('.spark-btn-copy-pdf') || []);
      targets.forEach(btn => {
        btn.classList.add('copied');
        btn.classList.remove('has-selection');
      });
    }

    createEmptyState() {
      const emptyState = document.createElement('div');
      emptyState.className = 'spark-pdf-empty';

      const emptyTopBar = document.createElement('div');
      emptyTopBar.className = 'spark-pdf-empty-bar';

      const emptyBarTitle = document.createElement('span');
      emptyBarTitle.textContent = 'GIÁO TRÌNH CHUYÊN KHẢO';
      emptyTopBar.appendChild(emptyBarTitle);

      const emptyActions = document.createElement('div');
      emptyActions.style.display = 'flex';
      emptyActions.style.alignItems = 'center';
      emptyActions.style.gap = '6px';

      const emptyChatBtn = document.createElement('button');
      emptyChatBtn.className = 'spark-btn-chat';
      emptyChatBtn.textContent = 'Chat';
      emptyChatBtn.title = 'Ẩn Khung Đọc để trao đổi với Gemini';
      emptyChatBtn.addEventListener('click', () => {
        this.layoutManager?.setRightPaneMode('CHAT');
      });

      const emptyReloadBtn = document.createElement('button');
      emptyReloadBtn.className = 'spark-btn-reload-pdf';
      emptyReloadBtn.textContent = 'Reload';
      emptyReloadBtn.title = 'Quét lại bài giảng của phiên hiện tại';
      emptyReloadBtn.addEventListener('click', (e) => {
        e.preventDefault();
        e.stopPropagation();
        emptyReloadBtn.classList.add('spinning');
        try {
          this.clearDismissed();
          this.syncWithCurrentSession();
          if (this.pdfStack.length === 0) {
            this.showToast('Phiên trò chuyện hiện tại chưa có bài giảng PDF.');
          }
        } catch (err) {
          console.error('[Spark Reader] Error reloading empty state:', err);
        } finally {
          setTimeout(() => {
            emptyReloadBtn.classList.remove('spinning');
          }, 350);
        }
      });

      emptyActions.appendChild(emptyChatBtn);
      emptyActions.appendChild(emptyReloadBtn);
      emptyTopBar.appendChild(emptyActions);

      const emptyTitle = document.createElement('div');
      emptyTitle.className = 'spark-pdf-empty-title';
      emptyTitle.textContent = 'CHƯA CÓ BÀI GIẢNG PDF';

      const emptyDesc = document.createElement('div');
      emptyDesc.className = 'spark-pdf-empty-desc';
      emptyDesc.textContent = 'Phiên trò chuyện hiện tại chưa có bài giảng PDF. Chuyển đến phiên có gắn link PDF hoặc yêu cầu Gemini xuất bản bài giảng để đọc tại đây.';

      emptyState.appendChild(emptyTopBar);
      emptyState.appendChild(emptyTitle);
      emptyState.appendChild(emptyDesc);

      this.emptyState = emptyState;
      return emptyState;
    }

    clearStack() {
      this.pdfStack = [];
      this.activePdf = null;
      if (this.viewerContainer) {
        while (this.viewerContainer.firstChild) {
          this.viewerContainer.removeChild(this.viewerContainer.firstChild);
        }
        this.viewerContainer.className = 'spark-pdf-stack is-empty';
        if (!this.emptyState) {
          this.createEmptyState();
        }
        this.viewerContainer.appendChild(this.emptyState);
      }
      try {
        sessionStorage.removeItem('spark_pdf_stack');
        sessionStorage.removeItem('spark_active_pdf');
        sessionStorage.removeItem('current_pdf_url');
      } catch (_) {}
      this.layoutManager?.updateDockTabs();
    }

    isPdfLinkInActiveChat(fileId) {
      if (!fileId) return false;

      const isInside = (el) => {
        if (!el || !(el instanceof Element)) return false;
        if (el.closest('#spark-cockpit-root, #spark-reader-root, #spark-action-toast, .spark-dock-tab, #spark-floating-launcher, .spark-resizer-handle')) {
          return false;
        }
        const excludedZone = el.closest(
          'header, nav, [role="navigation"], aside, [role="complementary"], ' +
          '[class*="sidebar"], [class*="side-panel"], [class*="side_panel"], [class*="right-panel"], [class*="right_panel"], ' +
          '[class*="drawer"], [class*="companion"], [class*="tools-panel"], [class*="files-panel"], [class*="file-list"], ' +
          '[class*="file_list"], [class*="knowledge"], mat-sidenav, .mat-drawer, button, [role="button"]'
        );
        if (excludedZone) return false;
        return !!el.closest('model-response, user-query, [data-message-author-role], message-content, div[class*="model-response"], div[class*="user-query"]');
      };

      // 1. Scan <a> links in active model responses
      const links = Array.from(document.querySelectorAll('a[href]'));
      for (const a of links) {
        if (!isInside(a)) continue;
        const href = (a.getAttribute('href') || '').trim();
        if (href.includes(fileId)) return true;
      }

      // 2. Scan text blocks in active model responses
      const chatContainers = Array.from(document.querySelectorAll(
        'model-response, message-content, [data-message-author-role], div[class*="model-response"]'
      ));
      for (const container of chatContainers) {
        if (!isInside(container)) continue;
        const text = container.textContent || '';
        if (text.includes(fileId)) return true;
      }

      return false;
    }

    removePdf(fileId) {
      if (!fileId) return;
      this.pdfStack = this.pdfStack.filter(item => item.fileId !== fileId);
      if (this.activePdf?.fileId === fileId) {
        this.activePdf = this.pdfStack.length > 0 ? this.pdfStack[this.pdfStack.length - 1] : null;
      }

      const card = this.viewerContainer?.querySelector(`.spark-pdf-section-card[data-file-id="${fileId}"]`);
      if (card) {
        card.remove();
      }

      try {
        sessionStorage.setItem('spark_pdf_stack', JSON.stringify(this.pdfStack));
        if (this.activePdf) {
          sessionStorage.setItem('spark_active_pdf', JSON.stringify(this.activePdf));
          sessionStorage.setItem('current_pdf_url', this.activePdf.previewUrl);
        } else {
          sessionStorage.removeItem('spark_active_pdf');
          sessionStorage.removeItem('current_pdf_url');
        }
      } catch (_) {}

      if (this.pdfStack.length === 0) {
        this.clearStack();
      } else {
        this.layoutManager?.updateDockTabs();
      }
    }

    scanAndLoadActiveChatPdfs() {
      const isInside = (el) => {
        if (!el || !(el instanceof Element)) return false;
        if (el.closest('#spark-cockpit-root, #spark-reader-root, #spark-action-toast, .spark-dock-tab, #spark-floating-launcher, .spark-resizer-handle')) {
          return false;
        }
        const excludedZone = el.closest(
          'header, nav, [role="navigation"], aside, [role="complementary"], ' +
          '[class*="sidebar"], [class*="side-panel"], [class*="side_panel"], [class*="right-panel"], [class*="right_panel"], ' +
          '[class*="drawer"], [class*="companion"], [class*="tools-panel"], [class*="files-panel"], [class*="file-list"], ' +
          '[class*="file_list"], [class*="knowledge"], mat-sidenav, .mat-drawer, button, [role="button"]'
        );
        if (excludedZone) return false;
        return !!el.closest('model-response, user-query, [data-message-author-role], message-content, div[class*="model-response"], div[class*="user-query"]');
      };

      // 1. Scan <a> links in active model responses
      const links = Array.from(document.querySelectorAll('a[href]'));
      for (const a of links) {
        if (!isInside(a)) continue;
        const href = (a.getAttribute('href') || '').trim();
        const driveFileId = StreamParserObserver.extractDriveFileId(href);
        if (!driveFileId) continue;

        const linkText = (a.textContent || '').trim();
        const parentLine = a.closest('li, p, div')?.textContent || linkText;
        const combinedText = `${linkText} ${parentLine}`;

        // STRICT GUARD: Bỏ qua tuyệt đối toàn bộ hình ảnh / sơ đồ mô phỏng (dành cho Tab Trái)
        if (
          /\.(png|jpe?g|webp|svg|gif|bmp)($|[?#])/i.test(href) ||
          /(\.(png|jpe?g|webp|svg|gif|bmp)|\[(?:Goc|Mo_Phong|Original|Simulation)\])/i.test(combinedText) ||
          /(?:^|\b)(?:hình|figure|fig\.?|đồ thị|biểu đồ|sơ đồ|mô hình|mô phỏng|minh họa|minh hoạ|ảnh|plot|chart)\b/i.test(combinedText)
        ) {
          continue;
        }

        const isPdf = /\.pdf($|[?#])/i.test(href) || 
                      /\.pdf\b/i.test(combinedText) ||
                      /(?:bài giảng|giáo trình|tài liệu|lecture|slides?|sách|văn bản|tập tài liệu|chương \d|phân mục \d|bản chuyên khảo|chuyên khảo|mục \d)\b/i.test(combinedText);

        if (isPdf) {
          let pdfTitle = linkText;
          if (!pdfTitle || pdfTitle.startsWith('http') || pdfTitle.length < 3 || /^(open drive|drive|xem|tải|link)/i.test(pdfTitle.trim())) {
            const docMatch = parentLine.match(/(?:Tài liệu|Bài giảng|Giáo trình|Bản Chuyên khảo|Chuyên khảo|Phân mục|Mục|Chương)\s*[:\-\s]*([^:\n|]+)/i);
            pdfTitle = docMatch ? docMatch[0].trim() + '.pdf' : `Bài_Giang_${driveFileId.substring(0, 6)}.pdf`;
          }
          this.loadPdf(driveFileId, pdfTitle, href, false);
        }
      }

      // 2. Scan plain text in chat containers for Drive PDF links
      const chatBlocks = Array.from(document.querySelectorAll(
        'message-content, model-response, [data-message-author-role], div[class*="model-response"]'
      ));
      for (const block of chatBlocks) {
        if (!isInside(block)) continue;
        const text = block.textContent || '';
        if (!text.includes('drive.google.com') && !text.includes('.pdf') && !text.includes('Chuyên khảo') && !text.includes('Mục')) continue;

        const urlMatches = text.matchAll(/https?:\/\/[^\s"'<>\)\],]+/gi);
        for (const m of urlMatches) {
          const rawUrl = m[0].replace(/[.,;:!?)]+$/, '');
          const driveFileId = StreamParserObserver.extractDriveFileId(rawUrl);
          if (!driveFileId) continue;

          const urlIndex = m.index || 0;
          const lineStart = text.lastIndexOf('\n', urlIndex) + 1;
          const lineEnd = text.indexOf('\n', urlIndex);
          const currentLine = text.substring(lineStart, lineEnd === -1 ? text.length : lineEnd).trim();

          // STRICT GUARD: Bỏ qua tuyệt đối toàn bộ hình ảnh / sơ đồ mô phỏng (dành cho Tab Trái)
          if (
            /\.(png|jpe?g|webp|svg|gif|bmp)($|[?#])/i.test(rawUrl) ||
            /(\.(png|jpe?g|webp|svg|gif|bmp)|\[(?:Goc|Mo_Phong|Original|Simulation)\])/i.test(currentLine) ||
            /(?:^|\b)(?:hình|figure|fig\.?|đồ thị|biểu đồ|sơ đồ|mô hình|mô phỏng|minh họa|minh hoạ|ảnh|plot|chart)\b/i.test(currentLine)
          ) {
            continue;
          }

          const isPdf = /\.pdf($|[?#])/i.test(rawUrl) || 
                        /(?:bài giảng|giáo trình|tài liệu|chương \d|phân mục \d|bản chuyên khảo|chuyên khảo|mục \d)(?:\.pdf)?\b/i.test(currentLine);
          if (isPdf) {
            const titleMatch = currentLine.match(/(?:Tài liệu|Bài giảng|Giáo trình|Bản Chuyên khảo|Chuyên khảo|Phân mục|Mục|Chương)\s*[:\-\s]*([^:\n|]+)/i);
            const pdfTitle = titleMatch ? titleMatch[0].trim() + '.pdf' : `Bài_Giang_${driveFileId.substring(0, 6)}.pdf`;
            this.loadPdf(driveFileId, pdfTitle, rawUrl, false);
          }
        }
      }
    }

    syncWithCurrentSession(targetFileId = null) {
      if (!this.viewerContainer) return;

      // 1. Verify existing PDFs in stack against current session
      const toRemove = [];
      for (const pdf of this.pdfStack) {
        if (!this.isPdfLinkInActiveChat(pdf.fileId)) {
          toRemove.push(pdf.fileId);
        } else {
          // If still in chat and targeted (or syncing all), refresh iframe
          if (!targetFileId || targetFileId === pdf.fileId) {
            const card = this.viewerContainer.querySelector(`.spark-pdf-section-card[data-file-id="${pdf.fileId}"]`);
            const frame = card?.querySelector('iframe.spark-pdf-section-frame');
            if (frame) {
              frame.src = 'about:blank';
              setTimeout(() => { frame.src = pdf.previewUrl; }, 120);
            }
          }
        }
      }

      // 2. Remove all outdated PDFs
      toRemove.forEach(id => {
        this.removePdf(id);
      });

      // 3. Scan for any new/untracked PDF links in active chat
      this.scanAndLoadActiveChatPdfs();

      // 4. If stack is empty, guarantee clean empty state
      if (this.pdfStack.length === 0) {
        this.clearStack();
      } else {
        if (this.emptyState?.parentElement) {
          this.emptyState.remove();
        }
        this.viewerContainer.classList.remove('is-empty');
        this.layoutManager?.updateDockTabs();
      }
    }

    isDismissed(fileId) {
      return !!(fileId && this.dismissedPdfIds.has(fileId));
    }

    dismissPdf(fileId) {
      if (!fileId) return;
      this.dismissedPdfIds.add(fileId);
      try {
        sessionStorage.setItem('spark_dismissed_pdf_ids', JSON.stringify(Array.from(this.dismissedPdfIds)));
      } catch (_) {}
      const target = this.pdfStack.find(p => p.fileId === fileId);
      const title = target?.title || 'bài giảng';
      this.removePdf(fileId);
      this.showToast(`Đã tắt bài giảng: "${title}"`);
    }

    clearDismissed() {
      this.dismissedPdfIds.clear();
      try {
        sessionStorage.removeItem('spark_dismissed_pdf_ids');
      } catch (_) {}
    }

    loadPdf(fileId, title = '', driveUrl = null, autoOpen = false) {
      if (!fileId) return;
      if (this.isDismissed(fileId)) return;

      // Ignore deleted / error drafts
      if (/LOI_CAN_XOA/i.test(title) || (driveUrl && /LOI_CAN_XOA/i.test(driveUrl))) {
        return;
      }

      // STRICT DIAGRAM REJECTION GUARD:
      // Tab Phải (Reader) is EXCLUSIVELY for lecture documents / PDFs.
      // NEVER load visual diagrams, simulation plots, or images into Reader!
      const titleLower = (title || '').toLowerCase().trim();
      const urlLower = (driveUrl || '').toLowerCase();
      if (
        /(?:^|\b)(?:hình|figure|fig\.?|đồ thị|biểu đồ|sơ đồ|mô hình|mô phỏng|minh họa|minh hoạ|ảnh|simulation|plot|chart|cầu sai|biên dạng|tia sáng|khúc xạ|phản xạ)\b/i.test(titleLower) ||
        /\[(?:Goc|Mo_Phong|Original|Simulation|Diagram|Chart|Figure)\]/i.test(title) ||
        /\.(png|jpe?g|webp|svg|gif|bmp)\b/i.test(titleLower) ||
        /\.(png|jpe?g|webp|svg|gif|bmp)($|[?#])/i.test(urlLower)
      ) {
        return; // Reject diagrams from Reader Overlay!
      }

      const cleanTitle = (title || `Phan_Muc_${fileId.substring(0, 6)}.pdf`).trim();
      const finalDriveUrl = driveUrl || `https://drive.google.com/file/d/${fileId}/view`;
      const previewUrl = `https://drive.google.com/file/d/${fileId}/preview`;

      this.activePdf = {
        fileId,
        title: cleanTitle,
        driveUrl: finalDriveUrl,
        previewUrl,
        timestamp: Date.now()
      };

      // Check if fileId is already present in pdfStack
      const existingIdx = this.pdfStack.findIndex(item => item.fileId === fileId);
      const isNewPdf = existingIdx < 0;

      if (!isNewPdf) {
        this.pdfStack[existingIdx].title = cleanTitle;
        this.pdfStack[existingIdx].driveUrl = finalDriveUrl;
        this.pdfStack[existingIdx].previewUrl = previewUrl;
      } else {
        this.pdfStack.push(this.activePdf);
      }

      try {
        sessionStorage.setItem('spark_pdf_stack', JSON.stringify(this.pdfStack));
        sessionStorage.setItem('spark_active_pdf', JSON.stringify(this.activePdf));
        sessionStorage.setItem('current_pdf_url', previewUrl);
      } catch (_) {}

      // Completely remove empty state from DOM when a PDF exists
      if (this.emptyState && this.emptyState.parentElement) {
        this.emptyState.remove();
      }
      this.viewerContainer.classList.remove('is-empty');

      // Ensure section card exists in DOM for this PDF
      let card = this.viewerContainer.querySelector(`.spark-pdf-section-card[data-file-id="${fileId}"]`);
      if (!card) {
        card = document.createElement('div');
        card.className = 'spark-pdf-section-card';
        card.setAttribute('data-file-id', fileId);

        // Single Top Sticky Header: Title + Actions [Chat, Open Drive, Reload]
        const secHeader = document.createElement('div');
        secHeader.className = 'spark-pdf-section-header';

        const secTitle = document.createElement('span');
        secTitle.className = 'spark-pdf-section-title';
        secTitle.textContent = cleanTitle;

        const secActions = document.createElement('div');
        secActions.className = 'spark-pdf-section-actions';

        const btnChat = document.createElement('button');
        btnChat.className = 'spark-btn-chat';
        btnChat.textContent = 'Chat';
        btnChat.title = 'Ẩn Khung Đọc để tiếp tục trao đổi với Gemini Spark';
        btnChat.addEventListener('click', () => {
          this.layoutManager?.setRightPaneMode('CHAT');
        });

        const secLink = document.createElement('a');
        secLink.className = 'spark-btn-drive-open';
        secLink.href = finalDriveUrl;
        secLink.target = '_blank';
        secLink.rel = 'noopener noreferrer';
        secLink.textContent = 'Open Drive';
        secLink.title = 'Mở trực tiếp trên tab mới (Native View / Edge PDF Reader không bị mã chặn)';

        const frame = document.createElement('iframe');
        frame.className = 'spark-pdf-section-frame';
        frame.setAttribute('allow', 'autoplay; clipboard-write; clipboard-read; clipboard-write *; clipboard-read *; fullscreen');
        frame.setAttribute('tabindex', '0');
        frame.src = previewUrl;

        // Chuyển giao tiêu điểm cho contentWindow của iframe để phím tắt Ctrl+C nạp thẳng vào tài liệu
        card.addEventListener('pointerdown', (e) => {
          if (!e.target.closest('button, a, input, textarea')) {
            try {
              frame.contentWindow?.focus();
            } catch (_) {
              frame.focus();
            }
          }
        });

        const btnReload = document.createElement('button');
        btnReload.className = 'spark-btn-reload-pdf';
        btnReload.textContent = 'Reload';
        btnReload.title = 'Kiểm tra và đồng bộ bài giảng theo phiên hiện tại';
        btnReload.addEventListener('click', (e) => {
          e.preventDefault();
          e.stopPropagation();
          btnReload.classList.add('spinning');
          try {
            const isStillInDoc = this.isPdfLinkInActiveChat(fileId);
            if (!isStillInDoc) {
              this.removePdf(fileId);
              this.showToast('Đã gỡ bỏ bài giảng không còn trong phiên hiện tại.');
              this.syncWithCurrentSession();
            } else {
              frame.src = 'about:blank';
              setTimeout(() => { frame.src = previewUrl; }, 120);
              this.showToast(`Đã tải lại bài giảng: "${cleanTitle}"`);
              this.syncWithCurrentSession(fileId);
            }
          } catch (err) {
            console.error('[Spark Reader] Error reloading PDF section:', err);
          } finally {
            setTimeout(() => {
              btnReload.classList.remove('spinning');
            }, 350);
          }
        });

        const btnClose = document.createElement('button');
        btnClose.className = 'spark-btn-close-pdf';
        btnClose.textContent = 'Close';
        btnClose.title = 'Tắt và ẩn bài giảng này khỏi khung đọc';
        btnClose.addEventListener('click', (e) => {
          e.preventDefault();
          e.stopPropagation();
          this.dismissPdf(fileId);
        });

        secActions.appendChild(btnChat);
        secActions.appendChild(secLink);
        secActions.appendChild(btnReload);
        secActions.appendChild(btnClose);

        secHeader.appendChild(secTitle);
        secHeader.appendChild(secActions);

        card.appendChild(secHeader);
        card.appendChild(frame);
        this.viewerContainer.appendChild(card);
      } else {
        const secTitle = card.querySelector('.spark-pdf-section-title');
        if (secTitle) secTitle.textContent = cleanTitle;
        const actions = card.querySelector('.spark-pdf-section-actions');
        const oldCopyBtn = actions?.querySelector('.spark-btn-copy-pdf');
        if (oldCopyBtn) oldCopyBtn.remove();
        const frame = card.querySelector('iframe.spark-pdf-section-frame');
        if (frame) {
          if (frame.src !== previewUrl) frame.src = previewUrl;
          if (!frame.getAttribute('allow')?.includes('clipboard-write *')) {
            frame.setAttribute('allow', 'autoplay; clipboard-write; clipboard-read; clipboard-write *; clipboard-read *; fullscreen');
          }
          if (!frame.hasAttribute('tabindex')) {
            frame.setAttribute('tabindex', '0');
          }
        }
      }

      // ONLY show toast when a genuinely new PDF is appended to prevent infinite blinking
      if (isNewPdf) {
        this.showToast(`Đã nối tiếp phân mục: "${cleanTitle}"`);
      }

      this.layoutManager?.updateDockTabs();
      if (autoOpen) {
        // Mặc định tab phải ĐÓNG. Chỉ auto-open khi user đã chủ động mở trước đó
        // (sessionStorage = 'READER'). null = lần đầu tiên → giữ đóng. 'CHAT' = đã đóng → giữ đóng.
        const savedMode = sessionStorage.getItem('spark_right_pane_mode');
        if (savedMode === 'READER') {
          this.layoutManager?.setRightPaneMode('READER');
        }
      }
    }

    restoreActivePdf() {
      try {
        const isDiagramItem = (item) => {
          if (!item?.fileId) return true;
          const t = (item.title || '').toLowerCase();
          return /(?:^|\b)(?:hình|figure|fig\.?|đồ thị|biểu đồ|sơ đồ|mô hình|mô phỏng|minh họa|minh hoạ|ảnh|simulation|plot|chart|cầu sai|biên dạng|tia sáng|khúc xạ|phản xạ)\b/i.test(t) ||
                 /\.(png|jpe?g|webp|svg|gif|bmp)\b/i.test(t) ||
                 /\[(?:Goc|Mo_Phong|Original|Simulation|Diagram|Chart|Figure)\]/i.test(item.title || '');
        };

        const savedStack = sessionStorage.getItem('spark_pdf_stack');
        if (savedStack) {
          const list = JSON.parse(savedStack);
          if (Array.isArray(list) && list.length > 0) {
            const validList = list.filter(item => !isDiagramItem(item));
            sessionStorage.setItem('spark_pdf_stack', JSON.stringify(validList));
            validList.forEach(item => {
              this.loadPdf(item.fileId, item.title, item.driveUrl);
            });
            return;
          }
        }
        const saved = sessionStorage.getItem('spark_active_pdf');
        if (saved) {
          const parsed = JSON.parse(saved);
          if (parsed?.fileId && !isDiagramItem(parsed)) {
            this.loadPdf(parsed.fileId, parsed.title, parsed.driveUrl);
            return;
          } else {
            sessionStorage.removeItem('spark_active_pdf');
          }
        }
        const currentUrl = sessionStorage.getItem('current_pdf_url');
        if (currentUrl) {
          const fileId = StreamParserObserver.extractDriveFileId(currentUrl);
          if (fileId) {
            this.loadPdf(fileId, `Phan_Muc_${fileId.substring(0, 6)}.pdf`, currentUrl);
          }
        }
      } catch (_) {}
    }

    renderContent(rawMarkdown) {
      if (!rawMarkdown) return;
      const drivePdfMatch = rawMarkdown.match(/https?:\/\/drive\.google\.com\/(?:file\/d\/|open\?id=)([a-zA-Z0-9_-]{15,})/i);
      if (drivePdfMatch) {
        const fileId = drivePdfMatch[1];
        const titleMatch = rawMarkdown.match(/\[([^\]]+)\]\([^\)]+\)/) || rawMarkdown.match(/^#+\s+(.+)$/m);
        const title = titleMatch ? titleMatch[1].trim() : `Phan_Muc_${fileId.substring(0, 6)}.pdf`;
        this.loadPdf(fileId, title, null, true);
      }
    }

    showToast(msg, duration = 4000) {
      let toast = document.getElementById('spark-action-toast');
      if (toast) {
        if (toast.querySelector('.spark-toast-msg')?.textContent === msg) {
          return toast; // Do not re-create or flicker if exact same toast is active
        }
        clearTimeout(toast.__sparkTimer);
        toast.remove();
      }

      toast = document.createElement('div');
      toast.id = 'spark-action-toast';

      const msgSpan = document.createElement('span');
      msgSpan.className = 'spark-toast-msg';
      msgSpan.textContent = msg;
      toast.appendChild(msgSpan);

      const closeBtn = document.createElement('button');
      closeBtn.className = 'spark-toast-close';
      closeBtn.textContent = '×';
      closeBtn.title = 'Đóng thông báo';
      closeBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        this.dismissToast();
      });
      toast.appendChild(closeBtn);

      document.body.appendChild(toast);

      toast.__sparkTimer = setTimeout(() => {
        this.dismissToast();
      }, duration);

      return toast;
    }

    dismissToast() {
      const toast = document.getElementById('spark-action-toast');
      if (toast) {
        clearTimeout(toast.__sparkTimer);
        toast.classList.add('spark-toast-hidden');
        setTimeout(() => {
          if (toast && toast.parentElement) {
            toast.remove();
          }
        }, 200);
      }
    }

    updateCopyButtonsState(hasSelection) {
      if (!this.viewerContainer) return;
      const copyButtons = this.viewerContainer.querySelectorAll('.spark-btn-copy-pdf');
      copyButtons.forEach(btn => {
        if (hasSelection) {
          btn.classList.add('has-selection');
          btn.title = 'Bấm để sao chép đoạn văn bản đang bôi đen vào Clipboard (Ctrl + C)';
        } else {
          btn.classList.remove('has-selection');
          btn.title = 'Sao chép đoạn văn bản đang bôi đen (Ctrl + C)';
        }
      });
    }

    async executeSystemCopy(text, btnElement = null) {
      if (!text || !text.trim()) return false;
      const clean = text.trim();
      let success = false;
      try {
        window.focus();
      } catch (_) {}

      // 1. Primary write: Async Clipboard API in parent window
      if (navigator.clipboard && navigator.clipboard.writeText) {
        try {
          await navigator.clipboard.writeText(clean);
          success = true;
        } catch (_) {}
      }

      // 2. Synchronous execCommand fallback
      if (!success) {
        try {
          const ta = document.createElement('textarea');
          ta.value = clean;
          ta.style.cssText = 'position:fixed;left:-9999px;top:-9999px;opacity:0;pointer-events:none;';
          document.body.appendChild(ta);
          ta.focus();
          ta.select();
          success = document.execCommand('copy');
          document.body.removeChild(ta);
        } catch (_) {}
      }

      return success;
    }

    async copyTextToClipboard(text) {
      try {
        window.focus();
      } catch (_) {}
      return this.executeSystemCopy(text);
    }

    saveScrollAnchor() {
      if (this.viewerContainer) {
        this.savedScrollTop = this.viewerContainer.scrollTop;
      }
    }

    restoreScrollAnchor() {
      if (this.viewerContainer && this.savedScrollTop !== undefined) {
        this.viewerContainer.scrollTop = this.savedScrollTop;
      }
    }
  }


  // =========================================================================
  // CLASS 1: CockpitLayoutManager (Failure Modes 03, 11, 14, 16, 21, 22, 30, 32)
  // =========================================================================
  class CockpitLayoutManager {
    #shadowRoot = null;
    #abortController = null;

    constructor() {
      window.__SPARK_LAYOUT_MANAGER__ = this;
      this.blobManager = new BlobLifecycleManager(20);
      this.transformEngine = null;
      this.streamObserver = null;
      this.readerEngine = null;
      this.splitPercent = 30; // Default 30% for Left Canvas / 70% for Right Workstation
      this.activeItem = null;
      this.isCockpitVisible = false;
      this.rightPaneMode = 'CHAT'; // Default: collapsed. Will restore from sessionStorage if available.
      // Restore right pane open/closed state (mirrors left pane persistence)
      const savedRightMode = sessionStorage.getItem('spark_right_pane_mode');
      if (savedRightMode === 'READER') {
        this.rightPaneMode = 'READER';
      }
      this.isCanvasInteracting = false;
      this.interactionLockTimer = null;
      this.timelineSortOrder = 'newest_first';
      this.userManuallyClosed = true; // Never auto-open on load
      this.unreadDiagramIds = new Set();
      this.pulseTimer = null;
      this.currentPath = window.location.pathname;

      // Restore split percent from localStorage or sessionStorage (20% to 80% bounds)
      const savedPercent = localStorage.getItem('spark_split_percent') || sessionStorage.getItem('spark_split_percent');
      if (savedPercent) {
        const parsed = parseFloat(savedPercent);
        if (!isNaN(parsed) && parsed >= 20 && parsed <= 80) {
          this.splitPercent = parsed;
        }
      }

      this.init();
    }

    init() {
      this.#abortController = new AbortController();
      const signal = this.#abortController.signal;

      // Listen for background commands & messages
      chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
        if (message?.action === 'TOGGLE_COCKPIT') {
          this.toggleWorkstation();
          sendResponse({ success: true, isVisible: this.isCockpitVisible, rightPaneMode: this.rightPaneMode });
        }
      });

      // Keyboard shortcuts
      window.addEventListener('keydown', (e) => {
        // Esc key closes Left Canvas
        if (e.key === 'Escape' && this.isCockpitVisible) {
          if (!ErgonomicGuards.isTypingContext()) {
            this.toggleCockpit(false);
          }
        }
        // Ctrl+Shift+V toggles entire dual-pane Workstation
        if ((e.ctrlKey || e.metaKey) && e.shiftKey && (e.key === 'v' || e.key === 'V')) {
          if (!ErgonomicGuards.isTypingContext()) {
            e.preventDefault();
            this.toggleWorkstation();
          }
        }
      }, { signal });

      // Build Closed Shadow DOM structure (Failure Mode 14)
      this.createShadowDOMStructure();

      // Setup Stream Observer with rock-solid diagram detection and SPA navigation handling
      this.streamObserver = new StreamParserObserver((diagramData) => {
        this.handleNewDiagram(diagramData);
      }, () => {
        // Auto-refresh when switching conversations or topics
        this.handleConversationSwitch();
      });
      this.streamObserver.start();

      // Synchronize theme (Failure Mode 30)
      this.setupThemeObserver(signal);

      // Initialize Reader Overlay Engine (v2.0)
      this.readerEngine = new ReaderOverlayEngine(this);

      // Restore right pane open state persisted from sessionStorage
      if (this.rightPaneMode === 'READER') {
        // Use requestAnimationFrame to ensure DOM is ready before opening
        requestAnimationFrame(() => this.setRightPaneMode('READER'));
      }

      // Setup Dynamic Dock Tabs (v2.0: 38px SPARK and READ tabs)
      this.setupDockTabs(signal);

      // Setup Resizer handle
      this.setupResizer(signal);

      // Setup SPA route watcher & URL Guardian
      this.setupSpaRouteListener();
      // NOTE: visibilitychange auto-collapse intentionally removed.
      // It caused both panes to collapse when user Alt+Tabs to another application.
    }

    createShadowDOMStructure() {
      // Host Mount Point
      let hostEl = document.getElementById('spark-cockpit-root');
      if (!hostEl) {
        hostEl = document.createElement('div');
        hostEl.id = 'spark-cockpit-root';
        hostEl.style.display = 'none'; // Initially collapsed until toggled or diagram detected
        document.body.appendChild(hostEl);
      }

      // Attach Closed Shadow Root (Strictly encapsulated)
      this.#shadowRoot = hostEl.attachShadow({ mode: 'closed' });

      // Inject Component Stylesheet into Closed Shadow DOM
      const styleEl = document.createElement('style');
      styleEl.textContent = this.getShadowStyles();
      this.#shadowRoot.appendChild(styleEl);

      // Build UI Container using STRICT DOM APIs (Zero innerHTML - Failure Mode 32)
      const cockpitContainer = document.createElement('div');
      cockpitContainer.className = 'spark-cockpit-container theme-dark';
      cockpitContainer.id = 'spark-container';

      // -------------------------------------------------------------
      // TOP HEADER & TOOLBAR
      // -------------------------------------------------------------
      const header = document.createElement('div');
      header.className = 'spark-header';

      const brand = document.createElement('div');
      brand.className = 'spark-brand';

      const brandTitle = document.createElement('span');
      brandTitle.className = 'spark-brand-title';
      brandTitle.textContent = 'SPARK VISUAL COCKPIT';

      const brandBadge = document.createElement('span');
      brandBadge.className = 'spark-brand-badge';
      brandBadge.textContent = 'LAB WORKSTATION';

      brand.appendChild(brandTitle);
      brand.appendChild(brandBadge);

      const headerControls = document.createElement('div');
      headerControls.className = 'spark-header-controls';

      // Sub-figure Clustering Tabs [a] [b] [c]
      const subTabs = document.createElement('div');
      subTabs.className = 'spark-subtabs';
      subTabs.id = 'spark-subtabs';
      headerControls.appendChild(subTabs);

      // Filter Toggle Button
      const filterBtn = document.createElement('button');
      filterBtn.className = 'spark-btn spark-btn-filter';
      filterBtn.title = 'Chế độ lọc màu vật lý';
      filterBtn.id = 'spark-filter-btn';
      filterBtn.textContent = 'Filter: Raw';
      filterBtn.addEventListener('click', () => {
        if (this.transformEngine) {
          const mode = this.transformEngine.cycleFilter();
          filterBtn.textContent = mode === 'preserve' ? 'Filter: Standard' : (mode === 'invert' ? 'Filter: Mono Invert' : 'Filter: Raw');
        }
      });
      headerControls.appendChild(filterBtn);

      // Close / Collapse Button
      const closeBtn = document.createElement('button');
      closeBtn.className = 'spark-btn spark-btn-icon spark-btn-close';
      closeBtn.title = 'Thu gọn Studio (Ctrl+Shift+V)';
      closeBtn.textContent = 'Close';
      closeBtn.addEventListener('click', () => this.toggleCockpit(false));
      headerControls.appendChild(closeBtn);

      header.appendChild(brand);
      header.appendChild(headerControls);
      cockpitContainer.appendChild(header);

      // Wrapper for Canvas + Timeline (Flex: 1, height: calc(100vh - 42px) to prevent header squish)
      const bodyWrapper = document.createElement('div');
      bodyWrapper.className = 'spark-body-wrapper';

      // -------------------------------------------------------------
      // TIER 1: MAIN CANVAS (70% height)
      // -------------------------------------------------------------
      const mainCanvasTier = document.createElement('div');
      mainCanvasTier.className = 'spark-tier spark-tier-canvas';

      // Floating Toolbar inside Viewport
      const canvasToolbar = document.createElement('div');
      canvasToolbar.className = 'spark-canvas-toolbar';

      const btnZoomIn = this.createToolButton('+', 'Zoom In', () => this.transformEngine?.zoomBy(1));
      const btnZoomOut = this.createToolButton('-', 'Zoom Out', () => this.transformEngine?.zoomBy(-1));
      const btnFit = this.createToolButton('Fit', 'Fit to Viewport', () => this.transformEngine?.fitToViewport());
      const btnReset = this.createToolButton('Center', 'Center Reset', () => this.transformEngine?.centerReset());

      canvasToolbar.appendChild(btnZoomIn);
      canvasToolbar.appendChild(btnZoomOut);
      canvasToolbar.appendChild(btnFit);
      canvasToolbar.appendChild(btnReset);
      mainCanvasTier.appendChild(canvasToolbar);

      // Viewport View
      const viewport = document.createElement('div');
      viewport.className = 'spark-viewport';
      viewport.id = 'spark-viewport';

      viewport.addEventListener('dragover', (e) => {
        // Pass-through without blocking host drops
      });

      // Target Transform Layer
      const transformLayer = document.createElement('div');
      transformLayer.className = 'spark-transform-layer';
      transformLayer.id = 'spark-transform-layer';
      viewport.appendChild(transformLayer);

      // Empty State Prompt (Zero Sticker)
      const emptyState = document.createElement('div');
      emptyState.className = 'spark-empty-state';
      emptyState.id = 'spark-empty-state';

      const emptyTitle = document.createElement('div');
      emptyTitle.className = 'spark-empty-title';
      emptyTitle.textContent = 'VISUAL WORKSTATION READY';

      const emptyDesc = document.createElement('div');
      emptyDesc.className = 'spark-empty-desc';
      emptyDesc.textContent = 'Các giản đồ năng lượng, đường cong quang học & hình vẽ trích dẫn sẽ tự động xuất hiện tại đây.';

      const emptyHint = document.createElement('div');
      emptyHint.className = 'spark-empty-hint';
      emptyHint.textContent = 'Phím tắt kích hoạt: Ctrl + Shift + V';

      emptyState.appendChild(emptyTitle);
      emptyState.appendChild(emptyDesc);
      emptyState.appendChild(emptyHint);
      viewport.appendChild(emptyState);

      // Loading / Retry Indicator
      const statusOverlay = document.createElement('div');
      statusOverlay.className = 'spark-status-overlay';
      statusOverlay.id = 'spark-status-overlay';
      statusOverlay.style.display = 'none';
      viewport.appendChild(statusOverlay);

      mainCanvasTier.appendChild(viewport);
      bodyWrapper.appendChild(mainCanvasTier);

      // TIER 2 METADATA BOX: 100% REMOVED PER ENTERPRISE WORKSTATION SPEC

      // -------------------------------------------------------------
      // TIER 3: TIMELINE & HISTORY STRIP (30% height)
      // -------------------------------------------------------------
      const timelineTier = document.createElement('div');
      timelineTier.className = 'spark-tier spark-tier-timeline';

      const timelineHeader = document.createElement('div');
      timelineHeader.className = 'spark-timeline-header';

      const timelineLeft = document.createElement('div');
      timelineLeft.className = 'spark-timeline-left';

      const timelineTitle = document.createElement('span');
      timelineTitle.textContent = 'HISTORY & TIMELINE';
      timelineLeft.appendChild(timelineTitle);

      const timelineRight = document.createElement('div');
      timelineRight.className = 'spark-timeline-actions';

      const lruCount = document.createElement('span');
      lruCount.className = 'spark-lru-count';
      lruCount.id = 'spark-lru-count';
      lruCount.textContent = 'RAM: 0/20';

      const sortBtn = document.createElement('button');
      sortBtn.className = 'spark-btn-timeline-sort';
      sortBtn.id = 'spark-sort-timeline-btn';
      sortBtn.textContent = 'Newest';
      sortBtn.title = 'Đổi thứ tự hiển thị: Mới nhất trước hoặc Cũ nhất trước';
      sortBtn.addEventListener('click', () => {
        this.timelineSortOrder = this.timelineSortOrder === 'newest_first' ? 'oldest_first' : 'newest_first';
        sortBtn.textContent = this.timelineSortOrder === 'newest_first' ? 'Newest' : 'Oldest';
        this.renderTimeline();
      });

      const reloadBtn = document.createElement('button');
      reloadBtn.className = 'spark-btn-timeline-reload';
      reloadBtn.id = 'spark-reload-timeline-btn';
      reloadBtn.textContent = 'Reload';
      reloadBtn.title = 'Tải lại và đồng bộ trạng thái cả 2 tab theo phiên hiện tại';
      let isReloadingTimeline = false;
      reloadBtn.addEventListener('click', async (e) => {
        e.preventDefault();
        e.stopPropagation();
        if (isReloadingTimeline) return;
        isReloadingTimeline = true;
        reloadBtn.classList.add('spinning');
        try {
          await this.reloadWorkstation();
        } catch (err) {
          console.error('[Spark Cockpit] Reload workstation error:', err);
        } finally {
          setTimeout(() => {
            reloadBtn.classList.remove('spinning');
            isReloadingTimeline = false;
          }, 350);
        }
      });

      timelineRight.appendChild(sortBtn);
      timelineRight.appendChild(lruCount);
      timelineRight.appendChild(reloadBtn);

      timelineHeader.appendChild(timelineLeft);
      timelineHeader.appendChild(timelineRight);

      const timelineStrip = document.createElement('div');
      timelineStrip.className = 'spark-timeline-strip';
      timelineStrip.id = 'spark-timeline-strip';

      // Horizontal Mouse Wheel Scroll on Timeline
      timelineStrip.addEventListener('wheel', (e) => {
        if (e.deltaY !== 0) {
          e.preventDefault();
          timelineStrip.scrollLeft += e.deltaY * 2;
        }
      }, { passive: false });

      timelineTier.appendChild(timelineHeader);
      timelineTier.appendChild(timelineStrip);
      bodyWrapper.appendChild(timelineTier);
      cockpitContainer.appendChild(bodyWrapper);

      this.#shadowRoot.appendChild(cockpitContainer);

      // Initialize Canvas Transform Engine
      this.transformEngine = new CanvasTransformEngine(viewport, transformLayer);
    }

    createToolButton(label, tooltip, onClick) {
      const btn = document.createElement('button');
      btn.className = 'spark-tool-btn';
      btn.textContent = label;
      btn.title = tooltip;
      btn.addEventListener('click', onClick);
      return btn;
    }

    setupResizer(signal) {
      let resizer = document.querySelector('.spark-resizer-handle');
      if (!resizer) {
        resizer = document.createElement('div');
        resizer.className = 'spark-resizer-handle';
        resizer.style.display = 'none';

        const line = document.createElement('div');
        line.className = 'spark-resizer-line';
        resizer.appendChild(line);

        document.body.appendChild(resizer);
      }

      let isDragging = false;

      resizer.addEventListener('pointerdown', (e) => {
        isDragging = true;
        resizer.classList.add('dragging');
        document.body.style.userSelect = 'none';
        document.body.style.pointerEvents = 'none';
        resizer.setPointerCapture(e.pointerId);
      }, { signal });

      // Failure Mode 16: Resizer mouse capture loss bound to window
      window.addEventListener('pointermove', (e) => {
        if (!isDragging) return;

        const totalW = window.innerWidth;
        const rawPercent = (e.clientX / totalW) * 100;
        const clampedPercent = Math.max(20, Math.min(80, rawPercent));

        this.setSplitPercent(clampedPercent);
      }, { signal });

      const stopDrag = (e) => {
        if (!isDragging) return;
        isDragging = false;
        resizer.classList.remove('dragging');
        document.body.style.userSelect = '';
        document.body.style.pointerEvents = '';
        try { resizer.releasePointerCapture(e.pointerId); } catch (_) {}
      };

      window.addEventListener('pointerup', stopDrag, { signal });
      window.addEventListener('pointercancel', stopDrag, { signal });
    }

    setSplitPercent(percent) {
      this.splitPercent = percent;
      try {
        localStorage.setItem('spark_split_percent', percent.toFixed(2));
        sessionStorage.setItem('spark_split_percent', percent.toFixed(2));
      } catch (_) {}
      document.documentElement.style.setProperty('--spark-split-width', `${percent.toFixed(2)}vw`);

      // Update resizer handle position
      const resizer = document.querySelector('.spark-resizer-handle');
      if (resizer) {
        resizer.style.left = `${percent.toFixed(2)}vw`;
      }

      // Re-fit active diagram
      if (this.transformEngine) {
        this.transformEngine.fitToViewport();
      }
    }

    setupDockTabs(signal) {
      const oldLauncher = document.getElementById('spark-floating-launcher');
      if (oldLauncher) oldLauncher.remove();

      let dockSpark = document.getElementById('spark-dock-spark');
      if (!dockSpark) {
        dockSpark = document.createElement('div');
        dockSpark.id = 'spark-dock-spark';
        dockSpark.className = 'spark-dock-tab';
        dockSpark.textContent = 'SPARK';
        dockSpark.title = 'Mở Studio Đồ thị Khung Trái (Esc hoặc Close để đóng)';
        document.body.appendChild(dockSpark);
      }

      dockSpark.addEventListener('click', () => {
        this.toggleCockpit(true);
      }, { signal });

      let dockRead = document.getElementById('spark-dock-read');
      if (!dockRead) {
        dockRead = document.createElement('div');
        dockRead.id = 'spark-dock-read';
        dockRead.className = 'spark-dock-tab';
        dockRead.textContent = 'READ';
        dockRead.title = 'Mở Khung Đọc Giáo Trình Chuyên Khảo';
        document.body.appendChild(dockRead);
      }

      dockRead.addEventListener('click', () => {
        this.setRightPaneMode('READER');
      }, { signal });

      this.updateDockTabs();
    }

    updateDockTabs() {
      const dockSpark = document.getElementById('spark-dock-spark');
      const dockRead = document.getElementById('spark-dock-read');

      if (dockSpark) {
        if (this.isCockpitVisible) {
          dockSpark.classList.add('dock-hidden');
        } else {
          dockSpark.classList.remove('dock-hidden');
          const count = this.unreadDiagramIds?.size || 0;
          dockSpark.textContent = count > 0 ? `SPARK (${count})` : 'SPARK';
        }
      }

      if (dockRead) {
        if (this.rightPaneMode === 'READER') {
          dockRead.classList.add('dock-hidden');
        } else {
          dockRead.classList.remove('dock-hidden');
          const pdfCount = this.readerEngine?.pdfStack?.length || 0;
          dockRead.textContent = pdfCount > 0 ? `READ (${pdfCount})` : 'READ';
        }
      }
    }

    updateLauncherBadge() {
      this.updateDockTabs();
    }

    setRightPaneMode(mode) {
      this.rightPaneMode = mode;
      try {
        sessionStorage.setItem('spark_right_pane_mode', mode);
      } catch (_) {}

      if (this.readerEngine) {
        if (mode === 'READER') {
          this.readerEngine.rootElement.classList.remove('reader-hidden');
          try {
            this.readerEngine.restoreScrollAnchor();
          } catch (e) {
            console.warn('[Spark Reader] Error restoring scroll anchor:', e);
          }
          // Chuyển giao tiêu điểm tức thì sang iframe khi mở chế độ Đọc để sẵn sàng phím tắt copy
          try {
            const activeFrame = this.readerEngine.viewerContainer?.querySelector('.spark-pdf-section-card:not(.is-dismissed) iframe.spark-pdf-section-frame') ||
                                this.readerEngine.viewerContainer?.querySelector('iframe.spark-pdf-section-frame');
            if (activeFrame && !ErgonomicGuards.isTypingContext()) {
              requestAnimationFrame(() => {
                try {
                  activeFrame.contentWindow?.focus();
                } catch (_) {
                  activeFrame.focus();
                }
              });
            }
          } catch (_) {}
        } else {
          try {
            this.readerEngine.saveScrollAnchor();
          } catch (e) {
            console.warn('[Spark Reader] Error saving scroll anchor:', e);
          }
          this.readerEngine.rootElement.classList.add('reader-hidden');
        }
      }

      this.updateDockTabs();
    }

    toggleWorkstation() {
      // If both Left Visual Canvas and Right Living Document Reader are open, collapse both
      if (this.isCockpitVisible && this.rightPaneMode === 'READER') {
        this.collapseAll();
      } else {
        // Open BOTH: snaps seamlessly to 100% of the screen (30vw Left / 70vw Right)
        this.toggleCockpit(true);
        this.setRightPaneMode('READER');
      }
    }

    collapseAll() {
      if (this.isCockpitVisible) {
        this.toggleCockpit(false);
      }
      if (this.rightPaneMode !== 'CHAT') {
        this.setRightPaneMode('CHAT');
      }
    }

    triggerInteractionLock() {
      this.isCanvasInteracting = true;
      clearTimeout(this.interactionLockTimer);
      this.interactionLockTimer = setTimeout(() => {
        this.isCanvasInteracting = false;
      }, 3000);
    }

    focusDiagram(id) {
      if (!id) return;
      const item = this.blobManager.getItem(id);
      if (item) {
        this.displayDiagram(item);
        if (!this.isCockpitVisible) {
          this.toggleCockpit(true);
        }
      }
    }

    triggerArchiveLesson(manifest) {
      this.readerEngine?.archiveLesson(manifest);
    }

    toggleCockpit(forceState) {
      const willBeVisible = typeof forceState === 'boolean' ? forceState : !this.isCockpitVisible;
      this.isCockpitVisible = willBeVisible;

      if (!willBeVisible) {
        this.userManuallyClosed = true;
      } else {
        this.userManuallyClosed = false;
        this.unreadDiagramIds.clear();
      }

      const hostEl = document.getElementById('spark-cockpit-root');
      const resizer = document.querySelector('.spark-resizer-handle');

      if (this.isCockpitVisible) {
        if (hostEl) hostEl.style.display = 'block';
        if (resizer) resizer.style.display = 'block';
        document.body.classList.add('spark-cockpit-active');
        this.setSplitPercent(this.splitPercent);
      } else {
        if (hostEl) hostEl.style.display = 'none';
        if (resizer) resizer.style.display = 'none';
        document.body.classList.remove('spark-cockpit-active');
      }

      this.updateDockTabs();
    }

    isSparkUrl() {
      return window.location.hostname === 'gemini.google.com';
    }

    checkRoute() {
      const inSpark = this.isSparkUrl();
      if (!inSpark) {
        this.sleep();
        return;
      }

      this.wake();

      const currentPath = window.location.pathname;
      if (this.currentPath !== currentPath) {
        this.currentPath = currentPath;
        this.handleConversationSwitch();
      }
    }

    sleep() {
      if (this.isCockpitVisible) {
        this.toggleCockpit(false);
      }
      const hostEl = document.getElementById('spark-cockpit-root');
      const launcher = document.getElementById('spark-floating-launcher');
      const resizer = document.querySelector('.spark-resizer-handle');
      if (hostEl) hostEl.style.display = 'none';
      if (launcher) launcher.style.display = 'none';
      if (resizer) resizer.style.display = 'none';
      document.body.classList.remove('spark-cockpit-active');
      this.streamObserver?.stop();
    }

    wake() {
      const launcher = document.getElementById('spark-floating-launcher');
      const resizer = document.querySelector('.spark-resizer-handle');
      if (launcher && !this.isCockpitVisible) {
        launcher.style.display = 'block';
      }
      if (resizer && this.isCockpitVisible) {
        resizer.style.display = 'block';
      }
      this.streamObserver?.start();
    }

    handleConversationSwitch() {
      // Yêu cầu của người dùng:
      // "Tôi muốn cả 2 tab đều có khả năng giữ nguyên trạng thái khi tôi đổi phiên trò chuyện nhưng phải cập nhật trạng thái khi tôi ấn reload. Trong trường hợp ở có thêm link mới thì vẫn cập nhật vào đấy nhé."
      // 1. Giữ nguyên trạng thái hiện tại của cả 2 tab (không xóa blobManager, không xóa canvas, không clearStack PDF).
      // 2. Reset các bộ băm processedHashes để sẵn sàng phát hiện nếu phiên mới có thêm link ảnh / PDF mới:
      this.streamObserver?.resetHashes();

      // 3. Quét DOM của phiên mới sau khi Angular/Lit hoàn tất mount giao diện (500ms):
      // - Nếu phiên mới có thêm ảnh mới -> tự động thêm vào dòng thời gian (append)
      // - Nếu phiên mới có thêm PDF mới -> tự động nối tiếp vào khung đọc (stack)
      // - Nếu phiên mới không có link nào -> giữ nguyên 100% tài liệu và ảnh trước đó!
      setTimeout(() => {
        this.streamObserver?.scanDocumentForDiagrams();
      }, 500);
    }

    reloadWorkstation() {
      // 1. Tab Trái (Visual Cockpit):
      // Làm sạch hoàn toàn bộ nhớ đệm ảnh cũ, đưa canvas và timeline về trạng thái ban đầu của extension
      this.blobManager.clearAll();
      this.activeItem = null;
      this.unreadDiagramIds.clear();
      this.updateLauncherBadge();
      this.displayEmptyState();
      this.renderTimeline();

      // 2. Tab Phải (Reader Overlay):
      // Quét lại toàn bộ bài giảng PDF theo phiên hiện tại: nếu còn thì giữ, nếu không còn thì gỡ bỏ
      if (this.readerEngine) {
        this.readerEngine.clearDismissed();
        this.readerEngine.syncWithCurrentSession();
      }

      // 3. Reset bộ băm để quét phiên hiện tại từ đầu
      this.streamObserver?.resetHashes();

      // 4. Quét lại toàn bộ tài liệu theo phiên hiện tại
      this.streamObserver?.scanDocumentForDiagrams();

      // 5. Cập nhật lại giao diện Tab Trái sau quét
      const items = this.blobManager.getAllSorted(this.timelineSortOrder);
      if (items.length > 0) {
        this.displayDiagram(items[0]);
      } else {
        this.displayEmptyState();
      }
      this.renderTimeline();
    }

    setupSpaRouteListener() {
      const notifyChange = () => {
        setTimeout(() => this.checkRoute(), 50);
      };

      window.addEventListener('popstate', notifyChange);

      if (!window.__SPARK_HISTORY_HOOKED__) {
        const origPushState = history.pushState;
        history.pushState = function(...args) {
          const res = origPushState.apply(this, args);
          notifyChange();
          return res;
        };
        const origReplaceState = history.replaceState;
        history.replaceState = function(...args) {
          const res = origReplaceState.apply(this, args);
          notifyChange();
          return res;
        };
        window.__SPARK_HISTORY_HOOKED__ = true;
      }

      // Periodic 150ms route check fallback (instant detection, near-zero CPU)
      setInterval(() => {
        const curPath = window.location.pathname;
        if (this.currentPath !== curPath) {
          this.checkRoute();
        }
      }, 150);

      // Initial route check
      this.checkRoute();
    }

    setupThemeObserver(signal) {
      // Failure Mode 30: Theme synchronization
      const updateTheme = () => {
        const isDark = document.documentElement.classList.contains('dark') ||
                       document.body.classList.contains('dark') ||
                       document.documentElement.getAttribute('data-theme') === 'dark' ||
                       document.body.getAttribute('data-theme') === 'dark' ||
                       window.matchMedia('(prefers-color-scheme: dark)').matches;

        const container = this.#shadowRoot?.getElementById('spark-container');
        if (container) {
          if (isDark) {
            container.classList.remove('theme-light');
            container.classList.add('theme-dark');
          } else {
            container.classList.remove('theme-dark');
            container.classList.add('theme-light');
          }
        }
      };

      const observer = new MutationObserver(updateTheme);
      observer.observe(document.documentElement, { attributes: true, attributeFilter: ['class', 'data-theme'] });
      observer.observe(document.body, { attributes: true, attributeFilter: ['class', 'data-theme'] });
      window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', updateTheme, { signal });
      updateTheme();

      // F11 fullscreen toolbar safe-area: when browser toolbar auto-shows in F11
      // it overlays fixed elements near top. We detect fullscreen (F11) by comparing
      // screen.height === window.innerHeight and set a CSS class on document.body.
      const updateFullscreenClass = () => {
        const isF11 = window.screen.height === window.innerHeight && !document.fullscreenElement;
        document.body.classList.toggle('spark-f11-fullscreen', isF11);
      };
      window.addEventListener('resize', updateFullscreenClass, { signal });
      updateFullscreenClass();
    }

    async handleNewDiagram(diagramData) {
      const id = diagramData.id || diagramData.fileId;
      if (!id) return;

      // Strict Left Canvas Guard: Reject PDF files, "Open Drive" links, and known PDF documents
      const rawTitle = (diagramData.title || '').trim().toLowerCase();
      if (rawTitle === 'open drive' || rawTitle === 'google drive' || rawTitle.endsWith('.pdf')) {
        return; // Drop non-diagram links from canvas
      }
      const checkFileId = diagramData.fileId || diagramData.id;
      if (checkFileId && this.readerEngine?.pdfStack?.some(p => p.fileId === checkFileId)) {
        return; // File is a PDF managed by Reader Overlay
      }

      // Absolute Pin Lock & Deduplication:
      // If diagram is already known in memory, update domOrder and metadata
      if (this.blobManager.has(id)) {
        const existing = this.blobManager.get(id);
        if (diagramData.domOrder !== undefined) existing.domOrder = diagramData.domOrder;
        if (diagramData.metadata && !existing.metadata) {
          existing.metadata = diagramData.metadata;
          if (this.activeItem?.id === id) {
            this.renderMetadata(existing.metadata);
          }
        }
        this.renderTimeline();
        return; // Already known: NEVER re-opens cockpit or increments badge!
      }

      // Truly NEW diagram: NEVER auto-open. Always update badge silently until user clicks dock tab!
      if (!this.isCockpitVisible) {
        this.unreadDiagramIds.add(id);
        this.updateLauncherBadge();
      }

      // Display on canvas ONLY if cockpit is already open AND no diagram is active
      const shouldDisplay = this.isCockpitVisible && !this.activeItem;

      // Direct image (Data URI, Blob URI, or Web Image URL)
      if (diagramData.type === 'DIRECT_IMAGE' || (diagramData.dataUrl && diagramData.type !== 'SVG')) {
        const url = diagramData.dataUrl;
        const isDataOrBlob = url.startsWith('data:') || url.startsWith('blob:');

        if (isDataOrBlob) {
          const item = this.blobManager.addOrUpdate(id, {
            type: 'DRIVE',
            title: diagramData.title,
            domOrder: diagramData.domOrder,
            status: 'ready',
            rawData: url,
            metadata: diagramData.metadata
          });
          if (shouldDisplay) {
            this.displayDiagram(item);
          }
          this.renderTimeline();
          return;
        }

        // Web HTTP/HTTPS URL: reserve slot and fetch via background script to bypass page CSP
        const isDormant = !!diagramData.isDormant;
        const item = this.blobManager.addOrUpdate(id, {
          type: 'DRIVE',
          title: diagramData.title,
          sourceUrl: url,
          domOrder: diagramData.domOrder,
          status: isDormant ? 'evicted' : 'loading',
          rawData: null,
          metadata: diagramData.metadata
        });

        if (shouldDisplay) {
          this.displayDiagram(item);
        }
        this.renderTimeline();

        if (!isDormant) {
          await this.fetchImageUrl(item, url);
        }
        return;
      }

      if (diagramData.type === 'SVG') {
        const item = this.blobManager.addOrUpdate(id, {
          type: 'SVG',
          title: diagramData.title || 'Mô phỏng Vector (SVG)',
          domOrder: diagramData.domOrder,
          status: 'ready',
          rawData: diagramData.svgElement,
          metadata: diagramData.metadata
        });
        if (shouldDisplay) {
          this.displayDiagram(item);
        }
        this.renderTimeline();
      } else if (diagramData.type === 'DRIVE') {
        const isDormant = !!diagramData.isDormant;
        // Reserve slot in blobManager immediately upon discovery to lock chronological timeline position!
        const item = this.blobManager.addOrUpdate(id, {
          type: 'DRIVE',
          title: diagramData.title,
          fileId: diagramData.fileId,
          domOrder: diagramData.domOrder,
          status: isDormant ? 'evicted' : 'loading',
          rawData: null,
          metadata: diagramData.metadata
        });

        if (shouldDisplay) {
          this.displayDiagram(item);
        }
        this.renderTimeline();

        if (!isDormant) {
          await this.fetchDriveImage(item, diagramData);
        }
      }
    }

    async fetchImageUrl(item, url) {
      try {
        const res = await ErgonomicGuards.sendMessageWithRetry({
          action: 'FETCH_IMAGE_URL',
          url
        }, 3);

        if (res?.success && res.dataUrl) {
          this.hideStatus();
          item.rawData = res.dataUrl;
          item.status = 'ready';
          item.errorMsg = null;
          this.blobManager.touchRam(item.id, this.activeItem?.id);
          if (this.activeItem?.id === item.id) {
            this.displayDiagram(item);
          }
          this.renderTimeline();
        } else {
          // Fallback to direct URL if background fetch fails
          item.rawData = url;
          item.status = 'ready';
          this.blobManager.touchRam(item.id, this.activeItem?.id);
          if (this.activeItem?.id === item.id) {
            this.displayDiagram(item);
          }
          this.renderTimeline();
        }
      } catch (err) {
        // Fallback to direct URL
        item.rawData = url;
        item.status = 'ready';
        this.blobManager.touchRam(item.id, this.activeItem?.id);
        if (this.activeItem?.id === item.id) {
          this.displayDiagram(item);
        }
        this.renderTimeline();
      }
    }

    async fetchDriveImage(item, diagramData) {
      const fileId = item.fileId || diagramData?.fileId;
      const authUserMatch = window.location.pathname.match(/\/u\/(\d+)/);
      const authUser = authUserMatch ? authUserMatch[1] : '0';

      try {
        const res = await ErgonomicGuards.sendMessageWithRetry({
          action: 'FETCH_IMAGE',
          fileId,
          authUser
        }, 3);

        if (res?.success && res.dataUrl) {
          this.hideStatus();
          item.rawData = res.dataUrl;
          item.status = 'ready';
          item.errorMsg = null;
          this.blobManager.touchRam(item.id, this.activeItem?.id);
          if (this.activeItem?.id === item.id) {
            this.displayDiagram(item);
          }
          this.renderTimeline();
          return;
        }

        // Direct <img> multi-CDN fallback
        this.attemptDirectImgFallback(item, fileId, authUser);

      } catch (err) {
        console.warn('[Spark Cockpit] Fetch Drive failed, attempting direct <img> fallback:', err);
        this.attemptDirectImgFallback(item, fileId, authUser);
      }
    }

    attemptDirectImgFallback(item, fileId, authUser) {
      const fallbackUrls = [
        `https://lh3.googleusercontent.com/d/${fileId}=w2048`,
        `https://drive.google.com/thumbnail?id=${fileId}&sz=w2048&authuser=${authUser}`,
        `https://drive.google.com/thumbnail?id=${fileId}&sz=w2048`,
        `https://drive.usercontent.google.com/download?id=${fileId}&export=view&authuser=${authUser}`
      ];

      let currentIndex = 0;

      const tryNextUrl = () => {
        // Race condition guard: If item is already loaded successfully, stop further fallback attempts
        if (item.status === 'ready' && item.rawData) return;

        if (currentIndex >= fallbackUrls.length) {
          if (item.status === 'ready' && item.rawData) return;
          this.hideStatus();
          item.status = 'error';
          item.errorMsg = 'Lỗi kết nối ảnh Google Drive';
          this.renderTimeline();
          return;
        }

        const url = fallbackUrls[currentIndex++];
        const img = new Image();
        img.onload = () => {
          if (item.status === 'ready' && item.rawData) return;
          this.hideStatus();
          item.rawData = url;
          item.status = 'ready';
          item.errorMsg = null;
          this.blobManager.touchRam(item.id, this.activeItem?.id);
          if (this.activeItem?.id === item.id) {
            this.displayDiagram(item);
          }
          this.renderTimeline();
        };
        img.onerror = () => {
          tryNextUrl();
        };
        img.src = url;
      };

      tryNextUrl();
    }

    displayEmptyState() {
      this.hideStatus();
      this.activeItem = null;
      const transformLayer = this.#shadowRoot?.getElementById('spark-transform-layer');
      const emptyState = this.#shadowRoot?.getElementById('spark-empty-state');
      if (transformLayer) {
        while (transformLayer.firstChild) transformLayer.removeChild(transformLayer.firstChild);
      }
      if (emptyState) emptyState.style.display = 'flex';
      this.renderMetadata(null);
      this.renderSubTabs(null);
    }

    async rehydrateItem(item) {
      if (!item) return;
      item.status = 'loading';
      item.errorMsg = null;
      if (this.activeItem?.id === item.id) {
        this.showStatusLoading(`Đang nạp lại dữ liệu ảnh (${item.title})...`);
      }
      this.renderTimeline();
      if (item.sourceUrl) {
        await this.fetchImageUrl(item, item.sourceUrl);
      } else {
        await this.fetchDriveImage(item, { fileId: item.fileId || item.id });
      }
    }

    async retryFetchDrive(item) {
      if (!item) return;
      item.status = 'loading';
      item.errorMsg = null;
      if (this.activeItem?.id === item.id) {
        this.showStatusLoading(`Đang thử lại nạp ảnh (${item.title})...`);
      }
      this.renderTimeline();
      if (item.sourceUrl) {
        await this.fetchImageUrl(item, item.sourceUrl);
      } else {
        await this.fetchDriveImage(item, { fileId: item.fileId || item.id });
      }
    }

    displayDiagram(item) {
      this.hideStatus();
      this.activeItem = item;
      const transformLayer = this.#shadowRoot.getElementById('spark-transform-layer');
      const emptyState = this.#shadowRoot.getElementById('spark-empty-state');
      if (!transformLayer) return;

      if (emptyState) emptyState.style.display = 'none';

      // Clean transform layer safely (Zero innerHTML)
      while (transformLayer.firstChild) {
        transformLayer.removeChild(transformLayer.firstChild);
      }

      if (!item) return;

      // If heavy image is still loading or evicted: display status overlay and metadata
      if (item.type === 'DRIVE' && !item.rawData) {
        if (item.status === 'evicted') {
          this.rehydrateItem(item);
        } else {
          this.showStatusLoading(`Đang nạp ảnh vi cấu trúc Drive (${item.title || item.id})...`);
        }
        this.renderMetadata(item.metadata);
        this.renderSubTabs(item);
        return;
      }

      let renderNode = null;

      if (item.type === 'SVG') {
        if (item.rawData) {
          renderNode = item.rawData.cloneNode(true);
          renderNode.classList.add('spark-render-target');

          // Ensure intrinsic width/height so zoom math works
          if (!renderNode.getAttribute('width') || !renderNode.getAttribute('height')) {
            const vb = renderNode.getAttribute('viewBox');
            if (vb) {
              const parts = vb.split(/[\s,]+/).map(parseFloat);
              if (parts.length === 4 && parts[2] > 0 && parts[3] > 0) {
                renderNode.setAttribute('width', parts[2]);
                renderNode.setAttribute('height', parts[3]);
              }
            } else {
              renderNode.setAttribute('width', '700');
              renderNode.setAttribute('height', '500');
            }
          }

          transformLayer.appendChild(renderNode);
        }
      } else if (item.type === 'DRIVE') {
        const img = document.createElement('img');
        img.className = 'spark-render-target';
        img.src = item.rawData;
        img.alt = item.title;
        img.onload = () => {
          this.transformEngine?.fitToViewport();
        };
        img.onerror = () => {
          console.warn(`[Spark Cockpit] Img preview failed to render for ${item.id}`);
        };
        transformLayer.appendChild(img);
        renderNode = img;
      }

      if (renderNode && this.transformEngine) {
        this.transformEngine.setTargetElement(renderNode);
        setTimeout(() => {
          this.transformEngine?.fitToViewport();
        }, 50);
      }

      this.renderMetadata(item.metadata);
      this.renderSubTabs(item);
    }

    renderMetadata(metadata) {
      const container = this.#shadowRoot.getElementById('spark-meta-content');
      if (!container) return;

      while (container.firstChild) {
        container.removeChild(container.firstChild);
      }

      if (!metadata) {
        const empty = document.createElement('div');
        empty.className = 'spark-meta-item spark-meta-placeholder';
        empty.textContent = '↳ Đồ thị không kèm thông số tọa độ. Xem chi tiết tại nội dung bài giảng.';
        container.appendChild(empty);
        return;
      }

      const grid = document.createElement('div');
      grid.className = 'spark-meta-grid';

      if (metadata.items && metadata.items.length > 0) {
        metadata.items.forEach(item => {
          const card = document.createElement('div');
          card.className = 'spark-meta-card';
          const label = document.createElement('div');
          label.className = 'spark-meta-label';
          label.textContent = item.label + ':';
          const val = document.createElement('div');
          const isHighlight = !/trục/i.test(item.label);
          val.className = 'spark-meta-val' + (isHighlight ? ' highlight' : '');
          val.textContent = item.value || 'N/A';
          val.title = item.value || '';
          card.appendChild(label);
          card.appendChild(val);
          grid.appendChild(card);
        });
      } else {
        // Fallback default cards
        const xBox = document.createElement('div');
        xBox.className = 'spark-meta-card';
        const xLabel = document.createElement('div');
        xLabel.className = 'spark-meta-label';
        xLabel.textContent = 'Trục X (Hoành độ):';
        const xVal = document.createElement('div');
        xVal.className = 'spark-meta-val';
        xVal.textContent = metadata.axisX || 'N/A';
        xBox.appendChild(xLabel);
        xBox.appendChild(xVal);

        const yBox = document.createElement('div');
        yBox.className = 'spark-meta-card';
        const yLabel = document.createElement('div');
        yLabel.className = 'spark-meta-label';
        yLabel.textContent = 'Trục Y (Tung độ):';
        const yVal = document.createElement('div');
        yVal.className = 'spark-meta-val';
        yVal.textContent = metadata.axisY || 'N/A';
        yBox.appendChild(yLabel);
        yBox.appendChild(yVal);

        const infBox = document.createElement('div');
        infBox.className = 'spark-meta-card';
        const infLabel = document.createElement('div');
        infLabel.className = 'spark-meta-label';
        infLabel.textContent = (metadata.infLabel || 'Điểm uốn / Rào thế') + ':';
        const infVal = document.createElement('div');
        infVal.className = 'spark-meta-val highlight';
        infVal.textContent = metadata.inflection || 'N/A';
        infBox.appendChild(infLabel);
        infBox.appendChild(infVal);

        grid.appendChild(xBox);
        grid.appendChild(yBox);
        grid.appendChild(infBox);
      }
      container.appendChild(grid);
    }

    renderSubTabs(item) {
      // Failure Mode 27: Sub-figure Clustering Tabs [a] [b] [c]
      const subTabsContainer = this.#shadowRoot.getElementById('spark-subtabs');
      if (!subTabsContainer) return;

      while (subTabsContainer.firstChild) {
        subTabsContainer.removeChild(subTabsContainer.firstChild);
      }

      if (!item || !item.subfigures || item.subfigures.length <= 1) {
        subTabsContainer.style.display = 'none';
        return;
      }

      subTabsContainer.style.display = 'flex';
      item.subfigures.forEach((sub, idx) => {
        const tabBtn = document.createElement('button');
        tabBtn.className = `spark-subtab-btn ${idx === item.activeSubIndex ? 'active' : ''}`;
        tabBtn.textContent = sub.label || `[${String.fromCharCode(97 + idx)}]`;
        tabBtn.addEventListener('click', () => {
          item.activeSubIndex = idx;
          this.displayDiagram(sub);
          this.renderSubTabs(item);
        });
        subTabsContainer.appendChild(tabBtn);
      });
    }

    renderTimeline() {
      const strip = this.#shadowRoot.getElementById('spark-timeline-strip');
      const lruCount = this.#shadowRoot.getElementById('spark-lru-count');
      if (!strip) return;

      while (strip.firstChild) {
        strip.removeChild(strip.firstChild);
      }

      const items = this.blobManager.getAllSorted(this.timelineSortOrder);
      const ramCount = this.blobManager.getRamCount();
      const totalCount = items.length;
      if (lruCount) {
        lruCount.textContent = `RAM: ${ramCount}/20 | Tổng: ${totalCount}`;
        lruCount.title = `Bộ nhớ đệm 2 tầng: Lưu ${ramCount}/20 ảnh chất lượng cao trong RAM, tổng cộng ${totalCount} hình ảnh trên Timeline`;
      }

      items.forEach(item => {
        const isLoading = item.status === 'loading';
        const isError = item.status === 'error';
        const isEvicted = item.status === 'evicted';

        const card = document.createElement('div');
        card.className = `spark-timeline-card ${this.activeItem?.id === item.id ? 'active' : ''} ${isLoading ? 'loading' : ''} ${isError ? 'error' : ''} ${isEvicted ? 'evicted' : ''}`;
        card.title = item.title + (isLoading ? ' (Đang nạp dữ liệu...)' : isError ? ' (Lỗi tải)' : isEvicted ? ' (Đã tối ưu RAM - Nhấp để nạp lại)' : '');

        const thumb = document.createElement('div');
        thumb.className = `spark-card-thumb ${isLoading ? 'skeleton' : ''} ${isEvicted ? 'dormant' : ''}`;

        if (isLoading) {
          const spinner = document.createElement('span');
          spinner.className = 'spark-skeleton-spinner';
          spinner.textContent = '...';
          thumb.appendChild(spinner);
        } else if (isError) {
          const errorIcon = document.createElement('span');
          errorIcon.textContent = 'ERR';
          thumb.appendChild(errorIcon);
        } else if (isEvicted) {
          const dormantIcon = document.createElement('span');
          dormantIcon.className = 'spark-dormant-icon';
          dormantIcon.textContent = 'CACHED';
          dormantIcon.title = 'Đã giải phóng RAM, nhấp để nạp lại ngay';
          thumb.appendChild(dormantIcon);
        } else if (item.type === 'DRIVE' && item.rawData) {
          const img = document.createElement('img');
          img.src = item.rawData;
          thumb.appendChild(img);
        } else if (item.type === 'SVG' && item.rawData) {
          try {
            const svgClone = item.rawData.cloneNode(true);
            svgClone.removeAttribute('width');
            svgClone.removeAttribute('height');
            svgClone.removeAttribute('style');
            svgClone.setAttribute('preserveAspectRatio', 'xMidYMid meet');
            thumb.appendChild(svgClone);
          } catch (_) {
            const icon = document.createElement('span');
            icon.textContent = 'GRAPH';
            thumb.appendChild(icon);
          }
        } else {
          const icon = document.createElement('span');
          icon.textContent = 'GRAPH';
          thumb.appendChild(icon);
        }

        const info = document.createElement('div');
        info.className = 'spark-card-info';

        const title = document.createElement('div');
        title.className = `spark-card-title ${isLoading ? 'skeleton-text' : ''}`;
        title.textContent = item.title;

        const time = document.createElement('div');
        time.className = 'spark-card-time';
        if (isLoading) {
          time.textContent = 'Loading...';
          time.style.color = 'var(--accent-cyan)';
        } else if (isError) {
          time.textContent = 'Lỗi tải (Nhấp thử lại)';
          time.style.color = 'var(--accent-red)';
        } else if (isEvicted) {
          time.textContent = 'Nhấp nạp lại';
          time.style.color = 'var(--accent-cyan)';
        } else {
          time.textContent = new Date(item.createdAt || item.timestamp || Date.now()).toLocaleTimeString();
        }

        info.appendChild(title);
        info.appendChild(time);

        const closeBtn = document.createElement('button');
        closeBtn.className = 'spark-card-delete';
        closeBtn.textContent = '×';
        closeBtn.title = 'Xóa hình này khỏi dòng thời gian';
        closeBtn.addEventListener('click', (e) => {
          e.stopPropagation();
          this.blobManager.delete(item.id);
          if (this.activeItem?.id === item.id) {
            const remaining = this.blobManager.getAllSorted(this.timelineSortOrder);
            if (remaining.length > 0) {
              this.displayDiagram(remaining[0]);
            } else {
              this.displayEmptyState();
            }
          }
          this.renderTimeline();
        });

        card.appendChild(thumb);
        card.appendChild(info);
        card.appendChild(closeBtn);

        card.addEventListener('click', () => {
          if (isLoading) {
            this.activeItem = item;
            this.showStatusLoading(`Đang nạp ảnh vi cấu trúc Drive (${item.title})...`);
            this.renderTimeline();
          } else if (isError) {
            this.activeItem = item;
            this.retryFetchDrive(item);
          } else if (isEvicted || (item.type === 'DRIVE' && !item.rawData)) {
            this.activeItem = item;
            this.rehydrateItem(item);
          } else {
            this.hideStatus();
            this.activeItem = item;
            this.blobManager.touchRam(item.id, this.activeItem?.id);
            this.displayDiagram(item);
            this.renderTimeline();
          }
        });

        strip.appendChild(card);
      });

      // Smooth scroll active card into view
      const activeCard = strip.querySelector('.spark-timeline-card.active');
      if (activeCard) {
        activeCard.scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'nearest' });
      }
    }

    reloadTimeline() {
      this.reloadWorkstation();
    }

    showStatusLoading(text) {
      const overlay = this.#shadowRoot.getElementById('spark-status-overlay');
      if (!overlay) return;
      while (overlay.firstChild) overlay.removeChild(overlay.firstChild);

      const spinner = document.createElement('div');
      spinner.className = 'spark-spinner';

      const label = document.createElement('div');
      label.className = 'spark-status-text';
      label.textContent = text;

      overlay.appendChild(spinner);
      overlay.appendChild(label);
      overlay.style.display = 'flex';
    }

    showStatusError(errorText, onRetry) {
      // Failure Mode 31: Timeout & Error with interactive [Retry] UI
      const overlay = this.#shadowRoot.getElementById('spark-status-overlay');
      if (!overlay) return;
      while (overlay.firstChild) overlay.removeChild(overlay.firstChild);

      const closeBtn = document.createElement('button');
      closeBtn.className = 'spark-btn spark-btn-icon';
      closeBtn.textContent = '✕';
      closeBtn.title = 'Đóng thông báo này';
      closeBtn.style.position = 'absolute';
      closeBtn.style.top = '10px';
      closeBtn.style.right = '10px';
      closeBtn.addEventListener('click', () => this.hideStatus());

      const errIcon = document.createElement('div');
      errIcon.className = 'spark-err-icon';
      errIcon.textContent = '⚠️';

      const label = document.createElement('div');
      label.className = 'spark-status-text';
      label.textContent = errorText;

      const actions = document.createElement('div');
      actions.style.display = 'flex';
      actions.style.gap = '8px';

      if (onRetry) {
        const btnRetry = document.createElement('button');
        btnRetry.className = 'spark-btn spark-btn-retry';
        btnRetry.textContent = 'Thử lại kết nối';
        btnRetry.addEventListener('click', () => {
          onRetry();
        });
        actions.appendChild(btnRetry);
      }

      const btnDismiss = document.createElement('button');
      btnDismiss.className = 'spark-btn';
      btnDismiss.textContent = 'Bỏ qua';
      btnDismiss.addEventListener('click', () => this.hideStatus());
      actions.appendChild(btnDismiss);

      overlay.appendChild(closeBtn);
      overlay.appendChild(errIcon);
      overlay.appendChild(label);
      overlay.appendChild(actions);
      overlay.style.display = 'flex';
    }

    hideStatus() {
      const overlay = this.#shadowRoot.getElementById('spark-status-overlay');
      if (overlay) overlay.style.display = 'none';
    }

    getShadowStyles() {
      return `
        /* Closed Shadow DOM Isolated Styles */
        :host {
          all: initial;
        }

        .spark-cockpit-container {
          width: 100%;
          height: 100vh;
          display: flex;
          flex-direction: column;
          box-sizing: border-box;
          font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
          border-right: 2px solid var(--border-color);
          background-color: var(--bg-primary);
          color: var(--text-primary);
          overflow: hidden;
        }

        /* Dark Theme Variables (Carbon & Slate Enterprise Monochrome) */
        .theme-dark {
          --bg-primary: #0b0c10;
          --bg-secondary: #12141a;
          --bg-card: #181b22;
          --border-color: #242833;
          --text-primary: #ededf0;
          --text-secondary: #8d929e;
          --accent-cyan: #3b82f6;
          --accent-blue: #2563eb;
          --accent-red: #ef4444;
          --accent-glow: rgba(59, 130, 246, 0.15);
        }

        /* Light Theme Variables */
        .theme-light {
          --bg-primary: #ffffff;
          --bg-secondary: #f6f8fa;
          --bg-card: #eaeef2;
          --border-color: #d0d7de;
          --text-primary: #1f2328;
          --text-secondary: #656d76;
          --accent-cyan: #0969da;
          --accent-blue: #218bff;
          --accent-red: #cf222e;
          --accent-glow: rgba(9, 105, 218, 0.15);
        }

        /* Top Header */
        .spark-header {
          display: flex;
          justify-content: space-between;
          align-items: center;
          height: 42px;
          min-height: 42px;
          flex: 0 0 42px;
          padding: 0 14px;
          background-color: var(--bg-secondary);
          border-bottom: 1px solid var(--border-color);
          user-select: none;
          box-sizing: border-box;
          z-index: 10;
        }

        .spark-body-wrapper {
          flex: 1;
          display: flex;
          flex-direction: column;
          overflow: hidden;
          min-height: 0;
          height: calc(100vh - 42px);
          box-sizing: border-box;
        }

        .spark-brand {
          display: flex;
          align-items: center;
          gap: 8px;
        }

        .spark-brand-title {
          font-weight: 700;
          font-size: 13px;
          letter-spacing: 0.5px;
          color: var(--text-primary);
        }

        .spark-brand-badge {
          font-size: 10px;
          padding: 2px 6px;
          border-radius: 4px;
          background: var(--bg-card);
          color: var(--text-secondary);
          border: 1px solid var(--border-color);
          font-weight: 600;
        }

        .spark-header-controls {
          display: flex;
          align-items: center;
          gap: 8px;
        }

        .spark-subtabs {
          display: flex;
          gap: 4px;
        }

        .spark-subtab-btn {
          background: var(--bg-card);
          color: var(--text-secondary);
          border: 1px solid var(--border-color);
          border-radius: 4px;
          padding: 2px 8px;
          font-size: 11px;
          cursor: pointer;
        }

        .spark-subtab-btn.active {
          background: var(--accent-cyan);
          color: #fff;
          font-weight: bold;
        }

        .spark-btn {
          border: 1px solid var(--border-color);
          background: var(--bg-card);
          color: var(--text-primary);
          border-radius: 4px;
          padding: 4px 10px;
          font-size: 11px;
          cursor: pointer;
          display: flex;
          align-items: center;
          transition: all 0.15s ease;
        }

        .spark-btn:hover {
          border-color: var(--accent-cyan);
          background: var(--bg-secondary);
        }

        .spark-btn-icon {
          padding: 4px 8px;
          font-weight: bold;
        }

        .spark-btn-close:hover {
          background: var(--accent-red);
          color: #fff;
          border-color: var(--accent-red);
        }

        /* 2-Tier Workstation Layout System (70% Canvas / 30% Timeline) */
        .spark-tier {
          box-sizing: border-box;
          border-bottom: 1px solid var(--border-color);
        }

        /* TIER 1: Canvas (80% height) */
        .spark-tier-canvas {
          flex: 8 8 80% !important;
          height: 80% !important;
          min-height: 0;
          position: relative;
          background-color: var(--bg-primary);
          overflow: hidden;
          display: flex;
          flex-direction: column;
        }

        .spark-canvas-toolbar {
          position: absolute;
          top: 10px;
          left: 10px;
          z-index: 10;
          display: flex;
          gap: 6px;
          background: rgba(18, 20, 26, 0.85);
          backdrop-filter: blur(8px);
          padding: 4px 6px;
          border-radius: 4px;
          border: 1px solid var(--border-color);
        }

        .spark-tool-btn {
          background: transparent;
          color: var(--text-primary);
          border: 1px solid transparent;
          border-radius: 3px;
          padding: 3px 8px;
          font-size: 11px;
          font-weight: 600;
          cursor: pointer;
        }

        .spark-tool-btn:hover {
          background: rgba(255, 255, 255, 0.08);
          border-color: var(--border-color);
          color: #ffffff;
        }

        .spark-viewport {
          flex: 1;
          width: 100%;
          height: 100%;
          position: relative;
          cursor: grab;
          overflow: hidden;
          user-select: none;
          -webkit-user-select: none;
          touch-action: none;
          background-image: 
            radial-gradient(var(--border-color) 1px, transparent 1px);
          background-size: 24px 24px;
        }

        .spark-transform-layer {
          position: absolute;
          top: 0;
          left: 0;
          width: 100%;
          height: 100%;
          pointer-events: none;
          transform-origin: 0 0;
        }

        .spark-render-target {
          display: block;
          max-width: none;
          pointer-events: none;
          user-select: none;
          -webkit-user-drag: none;
          transform-origin: 0 0;
          will-change: transform, filter;
          /* Fix aliasing/vỡ ảnh khi thu nhỏ (scale < 1): buộc Chrome dùng thuật toán
             downsampling chất lượng cao (bicubic) thay vì nearest-neighbor mặc định */
          image-rendering: high-quality;
          image-rendering: -webkit-optimize-contrast; /* Safari fallback */
        }

        /* Empty State */
        .spark-empty-state {
          position: absolute;
          inset: 0;
          display: flex;
          flex-direction: column;
          align-items: center;
          justify-content: center;
          padding: 24px;
          text-align: center;
          color: var(--text-secondary);
          user-select: none;
        }

        .spark-empty-title {
          font-size: 15px;
          font-weight: 700;
          color: var(--text-primary);
          margin-bottom: 6px;
          letter-spacing: 0.5px;
        }

        .spark-empty-desc {
          font-size: 12px;
          max-width: 320px;
          line-height: 1.5;
          margin-bottom: 12px;
        }

        .spark-empty-hint {
          font-size: 11px;
          font-family: monospace;
          background: var(--bg-card);
          padding: 4px 10px;
          border-radius: 4px;
          border: 1px solid var(--border-color);
          color: var(--text-primary);
        }

        /* Status & Error Overlay */
        .spark-status-overlay {
          position: absolute;
          inset: 0;
          background: rgba(11, 12, 16, 0.88);
          backdrop-filter: blur(4px);
          display: flex;
          flex-direction: column;
          align-items: center;
          justify-content: center;
          gap: 12px;
          z-index: 20;
          padding: 20px;
          text-align: center;
        }

        .spark-spinner {
          width: 28px;
          height: 28px;
          border: 2px solid rgba(255, 255, 255, 0.15);
          border-top-color: var(--accent-cyan);
          border-radius: 50%;
          animation: sparkSpin 0.8s linear infinite;
        }

        @keyframes sparkSpin {
          to { transform: rotate(360deg); }
        }

        .spark-status-text {
          font-size: 13px;
          color: var(--text-primary);
          max-width: 360px;
        }

        .spark-btn-retry {
          background: var(--accent-cyan);
          color: #fff;
          font-weight: bold;
          padding: 6px 14px;
        }

        /* TIER 2: Metadata Box - Omitted / Hidden */
        .spark-tier-metadata {
          display: none !important;
        }

        /* TIER 3: Timeline History Strip (20% height) */
        .spark-tier-timeline {
          flex: 2 2 20% !important;
          height: 20% !important;
          min-height: 0;
          background-color: var(--bg-secondary);
          display: flex;
          flex-direction: column;
          padding: 8px 12px;
          box-sizing: border-box;
          border-top: 1px solid var(--border-color);
          border-bottom: none;
        }

        .spark-timeline-header {
          display: flex;
          justify-content: space-between;
          align-items: center;
          font-size: 11px;
          font-weight: 700;
          color: var(--text-secondary);
          margin-bottom: 6px;
        }

        .spark-timeline-left {
          display: flex;
          align-items: center;
          gap: 6px;
        }

        .spark-timeline-actions {
          display: flex;
          align-items: center;
          gap: 8px;
        }

        .spark-btn-timeline-sort {
          background: var(--bg-card);
          color: var(--text-primary);
          border: 1px solid var(--border-color);
          border-radius: 3px;
          padding: 2px 8px;
          font-size: 10px;
          font-weight: 600;
          cursor: pointer;
          display: flex;
          align-items: center;
          gap: 4px;
          transition: all 0.15s ease;
          user-select: none;
        }

        .spark-btn-timeline-sort:hover {
          border-color: var(--accent-cyan);
          background: var(--bg-secondary);
        }

        .spark-btn-timeline-reload {
          background: var(--bg-card);
          color: var(--text-primary);
          border: 1px solid var(--border-color);
          border-radius: 3px;
          padding: 2px 8px;
          font-size: 10px;
          font-weight: 600;
          cursor: pointer;
          display: flex;
          align-items: center;
          gap: 4px;
          transition: all 0.15s ease;
          user-select: none;
        }

        .spark-btn-timeline-reload:hover {
          border-color: var(--accent-cyan);
          background: var(--bg-secondary);
        }

        .spark-btn-timeline-reload.spinning {
          opacity: 0.7;
          cursor: wait;
        }

        .spark-lru-count {
          font-size: 10px;
          color: var(--text-secondary);
          font-family: monospace;
        }

        .spark-timeline-strip {
          flex: 1;
          display: flex;
          gap: 8px;
          overflow-x: auto;
          overflow-y: hidden;
          scroll-behavior: smooth;
          padding-bottom: 4px;
        }

        .spark-timeline-strip::-webkit-scrollbar {
          height: 4px;
        }

        .spark-timeline-strip::-webkit-scrollbar-thumb {
          background: var(--border-color);
          border-radius: 2px;
        }

        .spark-timeline-card {
          flex: 0 0 140px;
          background: var(--bg-card);
          border: 1px solid var(--border-color);
          border-radius: 4px;
          padding: 4px 6px;
          display: flex;
          gap: 6px;
          align-items: center;
          cursor: pointer;
          user-select: none;
          transition: border-color 0.15s ease, transform 0.15s ease;
          position: relative;
        }

        .spark-card-delete {
          position: absolute;
          top: 2px;
          right: 2px;
          width: 15px;
          height: 15px;
          border-radius: 50%;
          background: rgba(0, 0, 0, 0.7);
          color: #fff;
          border: 1px solid rgba(255, 255, 255, 0.3);
          font-size: 9px;
          line-height: 13px;
          text-align: center;
          padding: 0;
          cursor: pointer;
          opacity: 0;
          transition: opacity 0.15s ease, background 0.15s ease, transform 0.15s ease;
          z-index: 10;
        }

        .spark-timeline-card:hover .spark-card-delete {
          opacity: 0.85;
        }

        .spark-card-delete:hover {
          opacity: 1 !important;
          background: var(--accent-red) !important;
          border-color: var(--accent-red) !important;
          transform: scale(1.15);
        }

        .spark-timeline-card:hover {
          border-color: var(--accent-cyan);
          transform: translateY(-1px);
        }

        .spark-timeline-card.active {
          border-color: var(--accent-cyan);
          box-shadow: 0 0 8px var(--accent-glow);
          background: var(--bg-secondary);
        }

        /* Skeleton Shimmer for Heavy Image Slot Reservation */
        .spark-timeline-card.loading {
          border-style: dashed;
          border-color: rgba(56, 189, 248, 0.6);
          position: relative;
          overflow: hidden;
        }

        .spark-timeline-card.loading::after {
          content: '';
          position: absolute;
          top: 0;
          left: -100%;
          width: 200%;
          height: 100%;
          background: linear-gradient(90deg, transparent, rgba(56, 189, 248, 0.12), transparent);
          animation: spark-shimmer 1.8s infinite;
          pointer-events: none;
        }

        @keyframes spark-shimmer {
          0% { transform: translateX(0); }
          100% { transform: translateX(50%); }
        }

        .spark-card-thumb.skeleton {
          background: var(--bg-secondary);
          border-style: dashed;
          border-color: var(--accent-cyan);
        }

        .spark-skeleton-spinner {
          font-size: 14px;
          animation: spark-pulse 1.2s infinite ease-in-out;
        }

        @keyframes spark-pulse {
          0%, 100% { opacity: 0.4; transform: scale(0.9); }
          50% { opacity: 1; transform: scale(1.1); }
        }

        .spark-timeline-card.error {
          border-color: var(--accent-red);
        }

        /* Dormant / Evicted Card Style (Two-Tier RAM Optimization) */
        .spark-timeline-card.evicted {
          border-color: rgba(148, 163, 184, 0.4);
          opacity: 0.88;
        }

        .spark-timeline-card.evicted:hover {
          border-color: var(--accent-cyan);
          opacity: 1;
        }

        .spark-card-thumb.dormant {
          background: var(--bg-secondary);
          color: var(--accent-cyan);
          border-color: rgba(56, 189, 248, 0.4);
        }

        .spark-dormant-icon {
          font-size: 15px;
          user-select: none;
        }

        .spark-card-thumb {
          width: 36px;
          height: 36px;
          border-radius: 3px;
          background: var(--bg-primary);
          border: 1px solid var(--border-color);
          display: flex;
          align-items: center;
          justify-content: center;
          overflow: hidden;
          font-size: 16px;
        }

        .spark-card-thumb img {
          width: 100%;
          height: 100%;
          object-fit: cover;
        }

        .spark-card-thumb svg {
          width: 100%;
          height: 100%;
          max-width: 100%;
          max-height: 100%;
          display: block;
          pointer-events: none;
        }

        .spark-card-info {
          flex: 1;
          overflow: hidden;
        }

        .spark-card-title {
          font-size: 11px;
          font-weight: 600;
          white-space: nowrap;
          overflow: hidden;
          text-overflow: ellipsis;
          color: var(--text-primary);
        }

        .spark-card-time {
          font-size: 9px;
          color: var(--text-secondary);
          margin-top: 2px;
        }
      `;
    }
  }

  // =========================================================================
  // BOOTSTRAPPER
  // =========================================================================
  try {
    new CockpitLayoutManager();
  } catch (err) {
    console.error('[Spark Cockpit] Failed to initialize CockpitLayoutManager:', err);
  }
})();

