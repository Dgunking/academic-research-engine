# CHỈ THỊ KỸ THUẬT: ĐÓNG GÓI, VỆ SINH & XUẤT BẢN DỰ ÁN LÊN GITHUB
# (PROJECT PACKAGING, HYGIENE AUDIT & GITHUB RELEASE DIRECTIVE v2.0)

> **Cấp thẩm quyền & Phê duyệt:** Bùi Trung Dũng (Khoa Vật lý Kỹ thuật, ĐH Bách khoa Hà Nội - HUST).  
> **Dự án:** `Academic Research Engine` — Động cơ Tác nhân Tự trị Nghiên cứu & Xuất bản Chuyên khảo Vật lý Bán dẫn.  
> **Phân vai AI:** Kỹ sư Trưởng DevOps & Kiến trúc sư Phát hành Phần mềm (Lead DevOps & Release Engineer).  
> **Mục tiêu:** Vệ sinh toàn diện kho mã nguồn, rà soát bí mật (Secrets), đóng băng phụ thuộc (`requirements.txt`), hoàn thiện tài liệu (`README.md`, `LICENSE`, `.gitignore`), kiểm thử toàn vẹn (Test Suite) và tạo commit mốc chuẩn hóa để đẩy lên GitHub.  
> **Nguyên tắc cốt tử:** Không rò rỉ API Keys/Secrets — Loại bỏ 100% file rác/cache — Không đẩy tệp thừa quá 50 MB — Bảo toàn 100% tài liệu thiết kế gốc.

---

## I. 4 PHA ĐÓNG GÓI BẮT BUỘC THỰC THI TRÊN HOST OS

AI hãy kích hoạt terminal PowerShell trên Host OS và lần lượt thực thi 4 giai đoạn đóng gói:

### PHA 1: KIỂM TOÁN VỆ SINH, BẢO MẬT & CẬP NHẬT .GITIGNORE
1. **Quét cạn Secrets & Thông tin Nhạy cảm (Security & Privacy Audit):**
   - Quét toàn bộ repository để đảm bảo tuyệt đối KHÔNG chứa:
     * API Keys (Gemini API, OpenAI, Google Cloud tokens, GitHub Personal Access Tokens).
     * File cấu hình môi trường chứa secret: `.env`, `.env.local`, các tệp credentials JSON.
     * Token truy cập cá nhân hoặc cookies.
2. **Loại bỏ Tệp Rác, Cache & Build Artifacts:**
   - Dọn sạch toàn bộ thư mục `__pycache__/`, `*.pyc`, `*.pyo`, `.pytest_cache/`.
   - Dọn sạch các tệp test nháp tạm thời trong `output/test_*`, `output/tmp_*`, `scratch/`, `test_extract.py`.
   - Xóa bỏ các tệp rác hệ điều hành: `Thumbs.db`, `desktop.ini`, `.DS_Store`.
3. **Cập nhật File `.gitignore` Chuẩn Mực:**
   - Bổ sung và khóa chặt các mẫu đường dẫn sau vào `.gitignore`:
     ```gitignore
     # Byte-compiled / optimized / DLL files
     __pycache__/
     *.py[cod]
     *$py.class

     # Virtual environments
     .venv/
     venv/
     ENV/
     env/

     # Secrets & Local Environment
     .env
     .env.*
     *.key
     *.token
     credentials.json

     # Testing & Temporary Scratch
     .pytest_cache/
     .mypy_cache/
     .coverage
     htmlcov/
     scratch/
     temp_inspect/
     output/test_*
     output/tmp_*
     output/slide_previews/

     # Operating System & IDE
     .DS_Store
     Thumbs.db
     desktop.ini
     .vscode/
     .idea/
     *.bak
     *.tmp
     *.swp
     ```

### PHA 2: ĐÓNG BĂNG PHỤ THUỘC & HOÀN THIỆN BỘ HỒ SƠ DỰ ÁN
1. **Đóng băng Thư viện Phụ thuộc (`requirements.txt`):**
   - Rà soát và cập nhật tệp `requirements.txt` sạch sẽ, phân nhóm rõ ràng:
     * *Nhóm Core Framework & Schemas:* `pydantic>=2.7.0`, `pyyaml>=6.0`
     * *Nhóm Toán học & Giải tích:* `numpy>=1.26.0`, `scipy>=1.12.0`, `sympy>=1.13.0`
     * *Nhóm Đồ họa & Thị giác:* `matplotlib>=3.8.0`, `pillow>=10.2.0`
     * *Nhóm Chế bản PDF Chuyên khảo:* `reportlab>=4.1.0`, `pymupdf>=1.24.0`
2. **Cập nhật `README.md` Chuyên Nghiệp Chuẩn Quốc Tế:**
   - Hoàn thiện `README.md` với bố cục đầy đủ:
     * **Tiêu đề & Huy hiệu (Badges):** Python 3.12, Pydantic v2, ReportLab, License.
     * **Giới thiệu Tổng quan:** Động cơ AI biên soạn chuyên khảo tự trị theo nguyên lý Feynman, phục vụ nghiên cứu & đào tạo tại Khoa Vật lý Kỹ thuật — ĐHBK Hà Nội.
     * **Kiến trúc Cụm 4 Tác nhân Tự trị:** `curriculum-architect`, `physics-graphic-artist`, `pedagogical-author`, `quality-gatekeeper` + `orchestration-kernel`.
     * **13 Thuật toán Cốt lõi & Quy trình Dây chuyền 2 Pha:** Tóm tắt lưu đồ FSM `/scan` $\to$ Sample Gate Mục X.1 $\to$ `/edit` $\to$ Autonomous Batch Rollout.
     * **Hướng dẫn Cài đặt & Khởi chạy (Quickstart):**
       ```powershell
       # Cài đặt môi trường
       git clone https://github.com/<username>/academic-research-engine.git
       cd academic-research-engine
       python -m venv .venv
       .venv\Scripts\activate
       pip install -r requirements.txt

       # Chạy kiểm thử toàn diện
       python -m unittest discover tests
       ```
3. **Bổ sung Tệp Giấy phép (`LICENSE`):**
   - Khởi tạo tệp `LICENSE` theo chuẩn **MIT License** (hoặc Apache 2.0) với bản quyền thuộc về `Bui Trung Dung (HUST)`.

### PHA 3: KIỂM ĐỊNH TOÀN VẸN MÃ NGUỒN TRƯỚC PHÁT HÀNH (PRE-RELEASE TEST GATE)
- Chạy toàn bộ Unit Test Suite từ Pha 0 đến Pha 5 trên Host OS:
  ```powershell
  python -m unittest tests/test_phase_0.py
  python -m unittest tests/test_phase_1.py
  python -m unittest tests/test_phase_2.py
  python -m unittest tests/test_phase_3.py
  python -m unittest tests/test_phase_4.py
  python -m unittest tests/test_phase_5.py
  ```
- **Rào cản Pass 100%:** Bắt buộc toàn bộ các bài test đều đạt `OK` (0 Failures, 0 Errors). Tuyệt đối không đóng gói mã nguồn đang có bài test lỗi.

### PHA 4: ĐÓNG GÓI GIT COMMIT & CUNG CẤP LỆNH ĐẨY LÊN GITHUB
1. **Kiểm tra Kích thước Tệp (Git Large File Check):**
   - Quét cạn và cảnh báo nếu có bất kỳ tệp đơn lẻ nào vượt quá $50\text{ MB}$ (giới hạn cảnh báo của GitHub).
2. **Thực thi Git Staging & Tạo Commit Mốc:**
   - Thực thi chuỗi lệnh:
     ```powershell
     git status
     git add .
     git commit -m "feat(core): release v2.0 - autonomous multi-agent academic research engine"
     ```
3. **Hướng dẫn Đẩy Lên GitHub:**
   - Cung cấp sẵn mẫu câu lệnh cho Bùi Trung Dũng kết nối kho lưu trữ từ xa:
     ```powershell
     # Đổi tên nhánh chính thành main (nếu chưa có)
     git branch -M main

     # Thêm remote GitHub (Thay <username> và <repo_name>)
     git remote add origin https://github.com/<username>/<repo_name>.git

     # Đẩy toàn bộ mã nguồn lên GitHub
     git push -u origin main
     ```
4. **Phương án Đóng Gói Dự Phòng Ngoại Tuyến (Offline Bundle):**
   - Hướng dẫn lệnh tạo tệp Git Bundle dự phòng độc lập:
     ```powershell
     git bundle create academic_research_engine_v2.0.bundle --all
     ```

---

## II. ĐỊNH DẠNG BÁO CÁO ĐÓNG GÓI ĐẦU RA YÊU CẦU

Sau khi hoàn tất toàn bộ quy trình, AI hãy xuất trình:
1. **Bảng Thống Kê Vệ Sinh Dự Án:** Số lượng file cache đã dọn, các tệp nhạy cảm đã kiểm tra (Zero Secrets Leaked), tình trạng `.gitignore`.
2. **Log Kết Quả Thực Thi Test Suite Toàn Diện:** Tóm tắt kết quả chạy test từ Pha 0 đến Pha 5 (Tổng test cases, thời gian, trạng thái PASS 100%).
3. **Bản Tóm Tắt Commit Git:** Trích xuất kết quả lệnh `git log -1` và `git status` xác nhận working tree sạch sẽ.
4. **Khối Lệnh Cuối Cùng (Ready-to-Push):** Cung cấp chính xác 3 dòng lệnh PowerShell để Bùi Trung Dũng chỉ việc dán URL repo GitHub cá nhân vào và nhấn Enter để hoàn tất xuất bản.
