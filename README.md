# Academic Research Engine (v2.0)
### Động cơ Tác nhân Tự trị Nghiên cứu & Chế bản Chuyên khảo Vật lý Bán dẫn

[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/)
[![Pydantic v2](https://img.shields.io/badge/pydantic-v2.7+-green.svg)](https://docs.pydantic.dev/)
[![ReportLab](https://img.shields.io/badge/reportlab-v4.1+-orange.svg)](https://www.reportlab.com/)
[![SymPy CAS](https://img.shields.io/badge/sympy-CAS-brightgreen.svg)](https://www.sympy.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> **Cơ quan học thuật & Nghiên cứu:** Khoa Vật lý Kỹ thuật, Đại học Bách khoa Hà Nội (HUST).  
> **Chủ thể nghiên cứu:** Bùi Trung Dũng (K67 Kỹ thuật Vật lý — HUST).  
> **Phân vai tương tác:** AI Agent Chuyên gia Đầu ngành & Giảng viên Kỳ cựu kiêm Cộng sự Lab Nghiên cứu Ngang hàng.  
> **Nền tảng thực thi:** Google Antigravity Native Engine (Windows Host OS / PowerShell / Python 3.12 / SymPy CAS / ReportLab / Typst).

---

## 1. Giới Thiệu Tổng Quan (Overview)

**Academic Research Engine** là hệ thống AI Agent tự trị hợp nhất theo nguyên lý Feynman và tư duy nguyên lý đầu (First-Principles Thinking), chuyên trách tự động hóa toàn trình quy trình nghiên cứu, giải tích vi mô và chế bản chuyên khảo học thuật đỉnh cao trong lĩnh vực **Vật lý Bán dẫn, Laser Diode, Quang tử học & Mạch tích hợp quang học (PIC)**.

Hệ thống vận hành theo nguyên tắc **Zero-Omission** (quét cạn 100% tài liệu nguồn kép gồm Slide bài giảng HUST và Sách giáo trình chuyên khảo quốc tế), bảo toàn **Độ sâu Toàn văn Không Giới hạn (Unbounded Depth)** với định dạng xuất bản chuẩn mực quốc tế: `1 Mục X.Y = 1 File PDF Chuyên Khảo Tự Chứa`.

---

## 2. Kiến Trúc Cụm 4 Tác Nhân Tự Trị & Bộ Tổng Chỉ Huy

Toàn bộ hệ thống được phân tách trách nhiệm nghiêm ngặt thành Cụm 4 Tác nhân Tự trị (Multi-Agent Swarm) liên kết một chiều qua Hợp đồng Dữ liệu Pydantic v2 (Strict Immutable Data Contracts) và được điều phối bởi Bộ Tổng Chỉ Huy:

```
                            [Slide HUST + Giáo trình Quốc tế]
                                            │
                                            ▼
                          ┌───────────────────────────────────┐
                          │    1. curriculum-architect        │
                          │ (DAG Kahn, ATCC, MPT Spec)        │
                          └─────────────────┬─────────────────┘
                                            │ CurriculumBlueprint
                                            ▼
                          ┌───────────────────────────────────┐
                          │   2. physics-graphic-artist       │
                          │ (300K Sim, ZT-GVLE, Triple Buffer)│
                          └─────────────────┬─────────────────┘
                                            │ VisualAssetManifest
                                            ▼
                          ┌───────────────────────────────────┐
                          │     3. pedagogical-author         │
                          │ (UFME 5 Giai đoạn, MALAE 3 Cấp)   │
                          └─────────────────┬─────────────────┘
                                            │ DraftMonographPayload
                                            ▼
                          ┌───────────────────────────────────┐
                          │     4. quality-gatekeeper         │
                          │ (CAS SymPy, DejaVu PDF, 17 Điểm)  │
                          └─────────────────┬─────────────────┘
                                            │ Pass/Fail Audit
                                            ▼
    ┌────────────────────────────────────────────────────────────────────────┐
    │                       orchestration-kernel                             │
    │  - FSM 6 Trạng thái (INITIALIZING -> COMPLETE / HALTED)                │
    │  - Quy trình 2 Pha: /scan Sample Gate Mục X.1 -> Autonomous Rollout   │
    │  - Cơ chế Tự sửa lỗi Lai ghép (Hybrid Self-Healing 1-3 Local / 4-5 CS) │
    └────────────────────────────────────────────────────────────────────────┘
```

1. **`curriculum-architect` (Tác nhân 1 - Kiến trúc sư Học liệu):**
   - Khảo sát nguồn kép (Drive & NotebookLM), trích xuất DAG tri thức (Directed Acyclic Graph).
   - Triệt tiêu phụ thuộc vòng lặp kín bằng giải thuật Kahn (`GREEDYCYCLEBREAK`).
   - Khử ngữ cảnh đại từ chỉ định (`HPDE 2.0`) và chuẩn hóa danh pháp song ngữ ATCC.
   - Xuất bản hợp đồng dữ liệu `CurriculumBlueprint`.

2. **`physics-graphic-artist` (Tác nhân 2 - Nghệ nhân Đồ họa & Mô phỏng Giải tích):**
   - Mô phỏng giải tích bán dẫn 300 K (`SEMICONDUCTORS_300K`: GaAs, InP, GaN, Si, Ge, AlGaAs) và hằng số CODATA 2022.
   - Bóc tách ảnh gốc D-SAFE và khóa bố cục đồ họa ZT-GVLE theo chuẩn MATLAB R2014b+.
   - Kiểm soát hình học Triple Buffer Envelope ($\delta \ge 20.0\text{ pt}$ giữa Tiêu đề và Legend).
   - Ký số hàm băm mật mã SHA-256 sidecar manifest cho 100% hình ảnh.

3. **`pedagogical-author` (Tác nhân 3 - Tác giả Sư phạm Feynman):**
   - Chấp bút chuyên khảo toàn văn theo Khung Sư phạm Lũy tiến UFME 5 Giai đoạn.
   - Giải phẫu phương trình MALAE 3 cấp độ (Trực giác vi mô, Toán học hình thức, Kỹ thuật thực chiến).
   - Chuỗi nhân quả vi mô $\le 65$ từ/khối, dẫn xuất trung gian tường minh có nhãn `↳`.
   - Nén mật độ tri thức CoD (Chain-of-Density) $\ge 3$ vòng lặp.

4. **`quality-gatekeeper` (Tác nhân 4 - Trọng tài Kiểm định & Chế bản PDF):**
   - Trọng tài kiểm toán độc lập thực thi Trạm kiểm định nhị phân 17 điểm (Pass/Fail Gate).
   - Xác minh tính đúng đắn đại số hình thức bằng SymPy CAS engine (`simplify(A - B) == 0`).
   - Chế bản PDF xuất bản bằng ReportLab theo chuẩn Typography DejaVu Serif, đánh số trang hai lượt `Trang X / Y` và bookmarks đa tầng 3 cấp.
   - Cơ chế cách ly tệp tạm `%TEMP% Isolation` và thay thế nguyên tử `os.replace` chống xung đột ổ đĩa.

5. **`orchestration-kernel` (Bộ Tổng Chỉ Huy Điều Phối Trung Tâm):**
   - Vận hành Máy trạng thái hữu hạn FSM 6 trạng thái bảo đảm luồng dữ liệu 1 chiều không chat tự do.
   - Điều phối Quy trình 2 Pha: Pha 1 (Sample Gate Mục X.1 đối chuẩn) $\to$ Pha 2 (Autonomous Batch Rollout).
   - Vận hành cơ chế Tự phản tỉnh sửa lỗi Lai ghép (Hybrid Self-Healing): Vòng 1–3 sửa chữa cục bộ (Local Surgical Repair), Vòng 4–5 tái thiết lập sạch (Clean-Slate Recompilation).

---

## 3. Hệ Thống 13 Thuật Toán Cốt Lõi (Core Algorithms Lock)

Hệ thống được bảo vệ bởi Điều khoản Khóa cứng Bất biến Cấp độ 0 (Level-0 Security Protocol) đối với 13 thuật toán cốt lõi:

| STT | Mã hiệu Thuật toán | Tên gọi Thuật toán | Phạm vi & Trách nhiệm Chức năng |
| :---: | :--- | :--- | :--- |
| **01** | `HDIR/DICG` | Điều hướng Tri thức Nguồn Kép & Bắt tay Tiền kiểm | Xác thực tính toàn vẹn đồng bộ giữa Google Drive và NotebookLM |
| **02** | `HPDE 2.0` | Khử Phụ thuộc Ngữ cảnh & Độc lập Tự chứa MPT | Xóa bỏ đại từ chỉ định mơ hồ, đảm bảo mỗi phân mục tự giải thích độc lập |
| **03** | `UFME` | Khung Sư phạm Lũy tiến Hợp nhất 5 Giai đoạn | Cấu trúc chuyên khảo 5 khối: Bản đồ nghịch lý $\to$ Cột trụ $\to$ Dẫn xuất $\to$ Tiệm cận $\to$ CER |
| **04** | `PLBE` | Lập Lộ trình Bài giảng theo Đồ thị DAG & Giải thuật Kahn | Bẻ gãy chu trình phụ thuộc vòng, xếp hạng thứ tự học tập logic |
| **05** | `ZT-GVLE` | Khóa Bố cục Đồ họa Không Khoảng trống | Chuẩn hóa đồ thị MATLAB R2014b+, tỷ lệ 6.5:4.2, 300 DPI, bảo toàn Triple Buffer |
| **06** | `D-SAFE` | Khai thác Ảnh gốc Trực tiếp & Auto-Crop | Khử nền slide, bóc tách vùng biểu đồ gốc không nén suy hao |
| **07** | `MALAE` | Giải phẫu Phương trình 3 Cấp độ Tích hợp | Bóc tách công thức: Trực giác vi mô $\to$ Giải tích hình thức $\to$ Thực chiến Lab |
| **08** | `CPCS` | Chuỗi Biến đổi Nhân quả Vi mô & Chống Nén Tri thức | Giới hạn $\le 65$ từ/khối nhân quả, tường minh 100% bước biến đổi trung gian `↳` |
| **09** | `DOHG 2.0` | 5 Trạm Chốt chặn Kiểm duyệt & Chế bản PDF ReportLab | Trạm gác tiền xuất bản: Typography DejaVu, chống rò rỉ LaTeX thô, phân số gạch ngang |
| **10** | `ATCC` | Chuẩn hóa Danh pháp Song ngữ Song song | Tuân thủ Nghị định 30/2020/NĐ-CP, APA 7th, Luật Đo lường SI 04/2011/QH13 |
| **11** | `DBCV` | Đối sánh Đa tầng Bản thảo & Bảng Thẩm định 17 Điểm | Trọng tài kiểm toán nhị phân Pass/Fail 17 tiêu chí trước khi đóng gói xuất xưởng |
| **12** | `FASV` | Xác minh Đại số Hình thức Bằng SymPy CAS | Kiểm chứng tính tương đương giải tích và dấu đại số bằng động cơ đại số máy tính |
| **13** | `CSAC` | Kiểm toán Tính Toàn vẹn Mật mã Chuỗi Cung ứng Đồ họa | Xác thực chữ ký số SHA-256 sidecar manifest giữa đồ thị và chuyên khảo |

---

## 4. Cấu Trúc Thư Mục Dự Án (Repository Map)

```
academic-research-engine/
├── .agents/                                # Cấu hình Antigravity Native Engine
│   ├── agents/                             # Định nghĩa Subagents (agent.md)
│   ├── rules/                              # Quy tắc bất biến (AGENTS.md)
│   ├── schemas/                            # Pydantic v2 schemas nội bộ
│   ├── scripts/                            # Lifecycle hooks & security gates
│   └── skills/                             # Thư viện kỹ năng Antigravity
│
├── agents/                                 # Mã nguồn Cụm 4 Tác nhân Tự trị
│   ├── curriculum_architect/               # Agent 1: Phân rã DAG & Blueprint
│   ├── physics_graphic_artist/             # Agent 2: Mô phỏng 300 K & Đồ họa MATLAB
│   ├── pedagogical_author/                 # Agent 3: Chấp bút Feynman UFME & MALAE
│   ├── quality_gatekeeper/                 # Agent 4: CAS SymPy & DejaVu PDF Publisher
│   ├── orchestration_kernel/               # Central Kernel: FSM & Hybrid Self-Healing
│   ├── common/                             # CAS Engine, Materials DB, Linter, Terminology
│   └── schemas/                            # Hợp đồng Dữ liệu Pydantic xuất bản
│
├── data/                                   # Học liệu mốc, Outlines, Blueprints, Nomenclatures
├── output/                                 # Kho thành phẩm (Figures, Manifests, Payloads, PDF)
├── scripts/                                # Công cụ điều phối, sinh mô phỏng, batch runners
├── tests/                                  # Unit Test Suite chuẩn hóa (test_phase_0 -> 5)
├── .gitignore                              # Bộ lọc tệp rác & bảo mật secrets
├── LICENSE                                 # Giấy phép bản quyền mã nguồn mở MIT
├── README.md                               # Hồ sơ phát hành dự án
└── requirements.txt                        # Đóng băng thư viện phụ thuộc
```

---

## 5. Hướng Dẫn Cài Đặt & Khởi Chạy (Quickstart)

### 5.1. Yêu cầu Tiên quyết
- **Hệ điều hành:** Windows 10/11 (khuyến nghị PowerShell 7+) hoặc Linux/macOS.
- **Python:** Phiên bản `Python >= 3.12`.

### 5.2. Cài đặt Môi trường
```powershell
# Clone mã nguồn từ GitHub
git clone https://github.com/Dgunking/academic-research-engine.git
cd academic-research-engine

# Khởi tạo và kích hoạt môi trường ảo Python
python -m venv .venv
.venv\Scripts\activate

# Cài đặt toàn bộ thư viện phụ thuộc
pip install -r requirements.txt
```

### 5.3. Chạy Kiểm Thử Toàn Diện (Test Suite Gate)
Chạy toàn bộ 92 bài test đơn vị từ Pha 0 đến Pha 5 để xác nhận tính toàn vẹn 100%:

```powershell
# Chạy tự động phát hiện toàn bộ test suite
python -m unittest discover tests

# Hoặc chạy kiểm tra độc lập từng Pha:
python -m unittest tests/test_phase_0.py   # Schema Contracts & Common Utilities
python -m unittest tests/test_phase_1.py   # Curriculum & Structural Architect
python -m unittest tests/test_phase_2.py   # Physical Simulation & Graphic Artist
python -m unittest tests/test_phase_3.py   # Pedagogical Feynman Author
python -m unittest tests/test_phase_4.py   # Quality Gatekeeper & ReportLab Publisher
python -m unittest tests/test_phase_5.py   # Central Orchestration Kernel & E2E Pipeline
```

---

## 6. Bộ Bốn Lệnh Điều Phối Antigravity

Trong phiên làm việc với Google Antigravity, hệ thống tiếp nhận Bộ Bốn Lệnh Chuẩn Hóa:

- **/scan Chương [X] [Tên môn]:**
  * *Pha 1 (Sample Gate):* Phân tích dàn ý toàn chương, đồng bộ danh pháp song ngữ, biên dịch duy nhất `Mục X.1` hoàn chỉnh đạt chuẩn 17 điểm làm mẫu đối chuẩn và dừng lại trên Chat chờ Bùi Trung Dũng phê duyệt.
  * *Pha 2 (Autonomous Batch Rollout):* Sau khi phê duyệt, kích hoạt dây chuyền tác nhân cuốn chiếu (`1 Mục X.Y = 1 File PDF`), đẩy thẳng thành phẩm vào Google Drive.
- **/learn Mục [X.Y] Chương [X]:** Truy xuất tức thì trong ~2 giây, xuất Bộ ba Mỏ neo Điều hướng ra chat (không in bài giảng dài làm loãng ngữ cảnh).
- **/edit Mục [X.Y] Chương [X] [: Yêu cầu]:** Mặc định kích hoạt *Clean-Slate Recompilation* toàn phần (làm mới 100% nội dung, ảnh mô phỏng và PDF).
- **/bg [Tác vụ]:** Đẩy các tác vụ tính toán giải tích nặng hoặc xuất bản hàng loạt vào Subagent chạy ngầm.

---

## 7. Giấy Phép Bản Quyền (License)

Dự án được phân phối dưới giấy phép **MIT License**. Chi tiết xem tại [LICENSE](LICENSE).  
Bản quyền thuộc về **Bùi Trung Dũng (Khoa Vật lý Kỹ thuật, ĐH Bách khoa Hà Nội - HUST)**.
