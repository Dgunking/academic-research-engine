# Academic Research Engine — HUST Physics & Semiconductor Photonics Lab

> **Không gian làm việc:** `d:\antigravity\academic-research-engine`  
> **Chủ thể:** Bùi Trung Dũng (K67 Vật lý Kỹ thuật, ĐHBK Hà Nội)  
> **Đối tác:** AI Agent Chuyên gia Đầu ngành & Giảng viên Kỳ cựu (40 năm kinh nghiệm) kiêm Cộng sự Lab Nghiên cứu Ngang hàng  
> **Nền tảng thực thi:** Google Antigravity Native Engine (Windows Host OS / PowerShell / Python 3.12 / Typst / ReportLab / Subagents)

---

## 1. Cơ Chế Khởi Động Tự Động Toàn Cục (Universal Bootstrapping)

Mọi cuộc trò chuyện hoặc phiên làm việc khởi tạo trong thư mục này đều **tự động và tuyệt đối kích hoạt vai trò AI Agent Giảng dạy & Nghiên cứu Vật lý Bán dẫn / Quang điện tử** nhờ hai cơ chế nạp đồng thời của Google Antigravity:

1. **`GEMINI.md` (Thư mục gốc):** Bản quy chuẩn tối cao tự động nạp thẳng vào System Prompt của mọi phiên làm việc trong repository.
2. **`.agents/rules/AGENTS.md`:** Tệp quy tắc phân cấp (Hierarchical Workspace Rules) duy trì 5 Mệnh lệnh cốt lõi, 12 Luật cấm toàn cục và kiểm định nhị phân 15 điểm.

---

## 2. Bản Đồ Cấu Trúc Thư Mục (Workspace Architecture)

```
d:\antigravity\academic-research-engine\
├── GEMINI.md                               # [BẮT BUỘC] Tệp nạp System Prompt tự động cho mọi phiên chat
├── requirements.txt                        # Thư viện Python (numpy, scipy, matplotlib, pyyaml, reportlab...)
├── README.md                               # Bản đồ kiến trúc và cẩm nang vận hành
│
├── .agents\                                # Trung tâm điều phối Antigravity Native Engine
│   ├── hooks.json                          # Điểm chặn vòng đời Lifecycle Hooks (Pre/PostToolUse)
│   ├── skills.config.yaml                  # Cấu hình chuyên sâu dự án (HUST Optoelectronics Lab)
│   │
│   ├── rules\
│   │   └── AGENTS.md                       # Hồ sơ Ground Truth, 5 Mệnh lệnh & 12 Luật cấm (trigger: always_on)
│   │
│   ├── scripts\
│   │   └── academic_gate_hook.py           # Kịch bản kiểm duyệt I/O và bảo vệ Sandbox Google Drive
│   │
│   ├── agents\                             # Thư viện Subagents tĩnh (.agents/agents/<name>/agent.md)
│   │   ├── curriculum-fidelity-auditor\    # Tác nhân kiểm toán trung thực học liệu (chống suy diễn)
│   │   ├── physics-diagram-artist\         # Tác nhân đồ họa kỹ thuật MATLAB R2014b+ & Auto-crop
│   │   └── monograph-pdf-publisher\        # Tác nhân chế bản ReportLab / Typst PDF chuẩn 3 cấp
│   │
│   └── skills\                             # Kho kỹ năng chuyên môn tự động phát hiện (Progressive Disclosure)
│       ├── engineering-instructor\         # Sư phạm Feynman, 5 Khối toàn văn & Cấu hình sâu
│       │   ├── config.default.yaml         # Khung cấu hình sư phạm mặc định
│       │   └── scripts\resolve_config.py   # Thuật toán hợp nhất sâu (Deep-Merge)
│       ├── user-insights-profiler\         # Tổng chỉ huy nhận thức thời gian thực & điều phối 4 lệnh
│       ├── physics-diagram-studio\         # Đồ họa MATLAB R2014b+, Triple Buffer & Auto-crop
│       │   └── scripts\matlab_plot_engine.py
│       ├── semiconductor-photonics-lab\    # Cơ sở dữ liệu bán dẫn 300 K & Hằng số CODATA
│       │   └── scripts\
│       │       ├── materials_db.py
│       │       └── matlab_style.py
│       ├── monograph-pdf-publisher\        # Chế bản PDF ReportLab 2 lượt đánh số & bookmarks 3 cấp
│       │   └── scripts\hust_pdf_engine.py
│       ├── academic-terminology-guardian\  # Danh pháp song ngữ, Sentence case, SI, APA 7
│       ├── output-accuracy-verifier\       # Trạm kiểm định nhị phân 15 điểm (Pass/Fail Gate)
│       ├── antigravity-infrastructure\     # Cấu hình Host OS, Drive G:\ & Subagents
│       ├── nlm-skill\                      # Đồng bộ nguồn kép NotebookLM CLI (nlm < 500 lines)
│       └── match-my-writing-style\         # Văn phong đối ngoại (tắt 100% trong học thuật)
│
├── data\                                   # Kho tài nguyên dữ liệu đầu vào
│   ├── source_materials\                   # Slide bài giảng HUST, sách giáo trình quốc tế (PDF)
│   └── raw_lab_data\                       # Dữ liệu đo đạc thực nghiệm Lab (I-V, L-I-V, phổ PL/EL)
│
└── output\                                 # Kho thành phẩm đầu ra
    ├── figures\                            # Ảnh trích xuất [Goc] và đồ thị giải tích [Mo_Phong] (300 DPI)
    ├── pdf\                                # Tệp PDF chuyên khảo hoàn chỉnh (1 Mục X.Y = 1 File PDF)
    └── reports\                            # Báo cáo kiểm định 15 điểm, biên bản scan và audit log
```

---

## 3. Bộ Bốn Lệnh Chuẩn Hóa Điều Phối

* **/scan Chương [X] [Tên môn]:**
  * *Pha 1 (Sample Gate):* Phân tích dàn ý toàn chương, đồng bộ danh pháp, biên dịch hoàn chỉnh duy nhất `Mục X.1` đạt chuẩn 15 điểm làm mẫu đối chuẩn và dừng lại trên Chat chờ Bùi Trung Dũng duyệt.
  * *Pha 2 (Autonomous Batch Rollout):* Sau khi duyệt, hệ thống kích hoạt Subagents độc lập cuốn chiếu (`1 Mục X.Y = 1 File PDF`), đẩy thẳng vào thư mục đóng gói, chỉ báo tiến độ ngắn trên Chat.
* **/learn Mục [X.Y] Chương [X]:**
  * Truy xuất tức thì trong ~2 giây.
  * Khung Chat chỉ xuất duy nhất Bộ ba Mỏ neo Điều hướng, không in bài giảng dài.
* **/edit Mục [X.Y] Chương [X] [: Yêu cầu]:**
  * Mặc định thực thi *Clean-Slate Recompilation* toàn phần (làm lại 100% toàn bộ nội dung từ đầu và tạo lại toàn bộ hình ảnh mới hoàn toàn, xóa cache tạm, biên dịch lại PDF mới 100%).
  * Ngoại lệ duy nhất: Trừ khi Bùi Trung Dũng viết rõ/chỉ định đích danh nội dung cần chỉnh sửa, hệ thống mới thực hiện chỉnh sửa cục bộ theo đúng yêu cầu cụ thể đó.
* **/bg [Tác vụ]:**
  * Kích hoạt chế độ tính toán/mô phỏng chạy ngầm bằng Subagent / Background Process và xuất báo cáo.

---

## 4. Chuẩn Mực Bản Thảo 5 Khối (`1 Mục X.Y = 1 File PDF`)

1. **Khối 1: Bản đồ không gian & Nghịch lý mở đầu** (Ảnh gốc/Mô phỏng + OCR Mắt xích 1–3 + Nghịch lý thang đo).
2. **Khối 2: Hạt nhân vật lý & Khóa biến số** (Luận điểm vi mô + Hệ thức Cột trụ `#0072BD` trên `#F0F7FF` + Nomenclature 4 cột ISO 80000-2 + Ẩn dụ 3 Nhịp hữu hình).
3. **Khối 3: Chuỗi nhân quả dẫn xuất** (Mũi tên `⇒`/`↳` + Vùng áp dụng + OCR Mắt xích 4–5 + Tường minh bước biến đổi trung gian từ slide).
4. **Khối 4: Khảo sát tiệm cận & Thực chiến linh kiện** ($\ge 2$ cực hạn suy biến + thông số điều khiển $I_{\text{th}}, \eta_d, \lambda, R_s$ + đồ thị MATLAB).
5. **Khối 5: Thử thách chẩn đoán CER** (Claim – Evidence – Reasoning cuối PDF, cấm giải hộ trong PDF).

---

## 5. Trạm Kiểm Định Chất Lượng Nhị Phân 15 Điểm (Pass/Fail Gate)

Mọi ấn phẩm xuất xưởng bắt buộc đạt 100% 15 tiêu chí (Độ sâu toàn văn, 5 Khối, Ẩn dụ 3 Nhịp, OCR zero-symbol-drift, 5 Mắt xích OCR, Dấu đại số, Vùng áp dụng & Khối 4, Causal Flowchain, Hệ thức Cột trụ & Nomenclature, Chế độ vận hành, Zero-Text Chat, Clean-Slate, Đồ họa MATLAB, Chế bản PDF, Ngôn ngữ khoa học). Vòng lặp tự sửa lỗi *Self-Healing* tối đa 5 lần trước khi kích hoạt chốt dừng an toàn.
