# Autonomous Academic Research Engine & Pedagogical AI Ecosystem

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)](https://github.com/)
[![Gemini Spark](https://img.shields.io/badge/Gemini%20Spark-Custom%20Gem%20v3.3-orange.svg)](https://gemini.google.com/)
[![Chrome Extension](https://img.shields.io/badge/Chrome%20Extension-Manifest%20V3-green.svg)](https://developer.chrome.com/docs/extensions/mv3/)
[![LaTeX Engine](https://img.shields.io/badge/Math-Mathtext%20%E2%89%A5%20300%20DPI-red.svg)](https://matplotlib.org/)
[![Integrity](https://img.shields.io/badge/Integrity-SHA--256%20Locked-purple.svg)](scripts/verify_core_integrity.py)

An autonomous multi-agent pedagogical engineering system designed for deep scientific learning, monograph synthesis, analytical visualization, and real-time lab mentoring in **Engineering Physics, Semiconductor Devices, Quantum Electronics, Diode Lasers, Photonic Integrated Circuits (PIC), Optical Thin Films, and Nanotechnology**.

---

## 🏛️ Ecosystem Architecture: The 4 Core Pillars

```
+---------------------------------------------------------------------------------------------------+
|                                 ACADEMIC RESEARCH ECOSYSTEM                                      |
+---------------------------------------------------------------------------------------------------+
|  [PILLAR 1: BACKEND AGENT ENGINE]               |  [PILLAR 2: GEMINI SPARK CUSTOM GEM]           |
|  - Google Antigravity Multi-Agent Runtime       |  - Master System Instructions (instructions.txt)|
|  - Deterministic FSM 2-Phase Workflow (/scan)   |  - CODATA 2022 & 300 K Semiconductor Database   |
|  - Algorithmic Rigor: MALAE, HPDE, RVAE, HDIR   |  - ATCC Bilingual Terminology Matrix (Decree 30)|
|  - Quality Gates: Gate 18 TVD & SymPy CAS       |  - Fast Dispatcher (/learn in <= 2s)            |
+-------------------------------------------------+-------------------------------------------------+
|  [PILLAR 3: SPARK VISUAL COCKPIT EXTENSION]     |  [PILLAR 4: OPTIMIZATION & WORKSPACE INTEGRATION|
|  - Chrome Extension Manifest V3                 |  - Autonomous Hardware Profiler & .env Tuner    |
|  - Split Workstation: [SPARK] & [READ/CHAT]     |  - Google Drive for Desktop Sync                |
|  - Living Document Reader & Visual Canvas       |  - NotebookLM CLI (`nlm`) & Source Ground Truth |
|  - Native Clipboard Bridge & Sidecar Sync       |  - Anti-Tampering SHA-256 Guard Verification    |
+---------------------------------------------------------------------------------------------------+
```

---

## 🚀 Quick Start Guide (5-Module Master Setup)

### Module 1: System Hardware Profiler & Autonomous Environment Calibration

The repository includes an autonomous system profiling engine that inspects your hardware (CPU cores, RAM capacity, NVIDIA CUDA VRAM) and software compilers (Python, Typst, LaTeX, ReportLab, DejaVu fonts). It automatically calibrates optimal thread concurrency and memory buffer values for your `.env` configuration.

1. **Clone the repository:**
   ```bash
   git clone https://github.com/${GITHUB_USERNAME}/academic-research-engine.git
   cd academic-research-engine
   ```

2. **Install Python scientific dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Execute Hardware Profiler:**
   ```bash
   python scripts/system_profiler.py
   ```
   *The profiler runs without external dependencies, inspects host resources, validates external tools, and generates an optimized `.env` file.*

---

### Module 2: Setup Gemini Spark (Custom Gem)

Gemini Spark operates as an AI Peer-Level Feynman Mentor and Autonomous Drive Scanner directly inside the Google Gemini web interface.

1. **Open Gemini Gems Manager:**
   - Navigate to [gemini.google.com](https://gemini.google.com).
   - In the left sidebar, click **Gem manager** (or **Quản lý Gem**) -> **New Gem** (Tạo Gem mới).
   - Set the Gem Name to: `Gemini Spark`.

2. **Inject Master System Instructions:**
   - Open [`gemini-spark/instructions.txt`](gemini-spark/instructions.txt).
   - Copy the entire contents and paste into the **Instructions** box of the Gem.

3. **Attach Core Ground Truth Knowledge:**
   - In the **Knowledge** section of the Gem, upload the two foundational references:
     * [`gemini-spark/01_Co_So_Du_Lieu_Ban_Dan_Va_Hang_So_CODATA_300K.md`](gemini-spark/01_Co_So_Du_Lieu_Ban_Dan_Va_Hang_So_CODATA_300K.md)
     * [`gemini-spark/02_Chuan_Danh_Phap_Thuat_Ngu_ATCC_Song_Ngu.md`](gemini-spark/02_Chuan_Danh_Phap_Thuat_Ngu_ATCC_Song_Ngu.md)

4. **Enable Google Workspace Drive Extension:**
   - In Gemini Settings or Extensions, ensure the **Google Workspace Extension** (`@Google Drive`) is toggled **ON**.
   - This authorizes Gemini Spark to inspect your Drive knowledge base, locate audit dossiers (`.docx`), and retrieve lecture assets during `/learn` queries.

5. **Save & Publish:**
   - Click **Save** to activate your personalized Gemini Spark Custom Gem.

---

### Module 3: Setup Spark Visual Cockpit (Chrome Extension)

The **Spark Visual Cockpit** extension (Manifest V3) transforms the Gemini web interface into a unified, two-column decoupled workstation featuring an independent Visual Canvas, living document overlay, and real-time clipboard bridge.

1. **Open Chrome Extension Management:**
   - In Google Chrome (or any Chromium browser), enter the URL:
     `chrome://extensions/`
   - In the top-right corner, toggle **Developer mode** to **ON**.

2. **Load Unpacked Extension:**
   - Click the **Load unpacked** (Tải tiện ích đã giải nén) button.
   - Select the repository directory:
     `extensions/spark-visual-cockpit/`

3. **Verify Activation:**
   - Open [gemini.google.com](https://gemini.google.com) and start a session with `Gemini Spark`.
   - The interface seamlessly transforms into a dual-column workstation:
     * **Left Column [SPARK]:** High-speed interactive chat and analytical Python execution.
     * **Right Column [READ/CHAT]:** Full-height monograph PDF reader, high-DPI image viewer, and living audit dossier.

---

### Module 4: Google Drive for Desktop Integration

The engine synchronizes monographs, analytical simulations, and audit dossiers directly with Google Drive.

1. **Install Google Drive for Desktop:**
   - Download and install [Google Drive for Desktop](https://www.google.com/drive/download/).
   - Mount your Drive as a virtual drive (e.g., `G:\` on Windows, or `~/GoogleDrive/` on Linux/macOS).

2. **Directory Structure:**
   Ensure the following folder hierarchy exists inside your mounted Drive:
   ```
   [NOTEBOOKLM_DRIVE_PATH]/<Course_Name>/
   ├── Bai_Giang_Dong_Goi/            # Compiled DejaVu PDF monographs (1 Section = 1 PDF)
   ├── Kho_Hinh_Anh/                  # High-DPI native & simulated figures (*.png, *.manifest.json)
   └── Ho_So_Kiem_Toan_Chuong_[X].docx # Living audit dossier for fast link dispatching
   ```

3. **Configure Path in `.env`:**
   Set the exact mount path in `.env`:
   ```bash
   NOTEBOOKLM_DRIVE_PATH=/path/to/GoogleDrive/NotebookLM - Academic Knowledge Base
   ```

---

### Module 5: NotebookLM Integration (`nlm` CLI)

Google NotebookLM acts as the upstream Ground Truth and primary academic source of truth for textbook slides and syllabus curricula.

1. **Install NotebookLM CLI:**
   ```bash
   pip install notebooklm-cli
   ```

2. **Authenticate:**
   ```bash
   nlm login
   ```

3. **Sync Course Notes & Query Ground Truth:**
   Use the built-in MCP skill in `.agents/skills/nlm-skill/` or terminal commands:
   ```bash
   nlm notebooks list
   nlm source add --notebook "Laser Diode & Photonics" path/to/syllabus_slide.pdf
   ```

---

## 🔒 Cryptographic Anti-Tampering Guard

The integrity of pedagogical algorithms, invariant rules, and data contracts is protected cryptographically via SHA-256 signatures:

```bash
# Verify integrity of all core components
python scripts/verify_core_integrity.py
```

*Output:*
```
[PASS] Core Integrity Verified: 100% of 40 core components match official cryptographic signature.
```

If any core file in `agents/`, `.agents/rules/`, `.agents/schemas/`, or `gemini-spark/` is tampered with or modified to bypass audit gates, the engine automatically terminates execution with exit code 1.

---

## 🧪 Automated Verification Test Suite

Run the full end-to-end verification test suite:

```bash
pytest tests/test_phase_0.py tests/test_phase_1.py tests/test_phase_2.py tests/test_phase_3.py tests/test_phase_4.py tests/test_phase_5.py
```

*Expected output: `92 passed in ~14s (100% PASS)`.*

---

## 📜 Standards & Scientific Directives

- **Feynman UFME Engine:** Derivations built strictly from first principles (energy conservation, Fermi-Dirac statistics, band symmetry).
- **MALAE Equation Dissection:** 3-level anatomical breakdown (Physical Intuition -> ISO 80000-2 Table -> Asymptotic Limits).
- **Zero-Slash-Fractions Directive:** Fractions in text and equations strictly formatted as $\frac{a}{b}$ via Mathtext $\ge 300\text{ DPI}$.
- **ATCC Bilingual Nomenclature:** Decree 30/2020/NĐ-CP sentence case, APA 7 decimal comma (`1,424 eV`), Law 04 SI spacing (`300 K`, `10 nm`).
- **ZT-GVLE Visualization:** MATLAB R2014b+ styling, external banner legend `(0.5, 1.02)`, and Triple Buffer clearance $\ge 20\text{ pt}$.

---

## 📄 License

Distributed under the MIT License for Academic and Scientific Research. See [`LICENSE`](LICENSE) for details.
