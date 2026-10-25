# Chrome Web Store Listing: Spark Visual Cockpit

**Last Updated:** 2026-10-03  
**Extension Version:** 1.0.0  
**Target Category:** Productivity / Academic & Education  

---

## 1. Store Listing Metadata

### Extension Name
Spark Visual Cockpit

### Short Description (max 132 characters)
Dual-pane academic visual workstation for physics engineering, semiconductor heterostructure band diagrams, and optical curves.

### Detailed Description
**Spark Visual Cockpit** transforms your browser into a specialized dual-pane engineering workstation designed for students, researchers, and engineers in Engineering Physics and Photonics.

When studying semiconductor heterostructures, laser diodes, and optical thin films, inspecting complex band diagrams and simulation curves alongside theoretical derivations is essential. Spark Visual Cockpit provides a synchronized side-by-side workspace:

- **Integrated Visual Studio (Left Pane):** Inspect high-resolution energy band diagrams ($E_c, E_v, E_F$) and dynamic vector curves right next to your study notes without switching tabs.
- **Precision Zoom & Pan:** Smoothly examine deep microscopic details with fluid zoom and pan controls.
- **Physics-Preserving Dark Mode:** Read comfortably at night with an intelligent contrast filter that turns bright backgrounds dark while keeping physical band colors (conduction red, valence blue) true to life.
- **Interactive Coordinate & Parameter Display:** Instantly view extracted physical units, axes ranges ($d$ in nm, $E$ in eV), and bandgap inflection points.
- **Diagram History Timeline:** Rapidly review previously cited figures and simulation snapshots during intensive study sessions.
- **Uncompromised Chat Workspace (Right Pane):** Retain 100% of your notes and conversation interface with smooth, responsive boundary adjustments.

Designed specifically for academic workflows, exam preparation, and engineering research.

---

## 2. Permissions Justification

| Permission | Scope / Domain | Justification for Review Team |
| :--- | :--- | :--- |
| `storage` | Browser local storage | Persists user interface preferences (such as preferred pane width) locally on your device between browser sessions. |
| `host_permissions` | `https://drive.google.com/*` | Enables fetching figure illustrations and band diagrams referenced in academic course materials directly to display them in the side-by-side study canvas. |
| `host_permissions` | `https://*.googleusercontent.com/*` | Loads optimized image thumbnails for high-resolution course scans so they render crisply without slowing down your system. |

---

## 3. Privacy & Data Handling Disclosures

- **Single Purpose:** Academic split-view diagram and band structure workstation.
- **Data Collection:** Zero personal data collected. No analytics trackers, no advertising IDs, no browsing history recorded or transmitted to third-party servers.
- **Local Storage:** Only layout percentages and ephemeral image caches are kept temporarily in memory or tab-isolated session storage.
- **Third-Party Transmission:** None. All requests are direct calls to user-accessible course files and rendered purely on the client side.

---

## 4. Version History

- **v1.0.0 (2026-10-03):** Initial production release.
  - Closed Shadow DOM dual-pane layout.
  - Hardware-accelerated canvas pan and zoom with boundary safety.
  - Physics color-preserving contrast filter.
  - Academic 3-tier layout: Visual Canvas, Axes Metadata Box, Timeline History Strip.
  - Dedicated shortcut `Ctrl+Shift+V` with full typing isolation.
