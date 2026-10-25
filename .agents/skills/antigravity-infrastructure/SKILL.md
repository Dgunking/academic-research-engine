---
name: antigravity-infrastructure
description: Hướng dẫn cấu hình danh tính người dùng, quy chuẩn quản trị tài nguyên Google Drive, giao thức kiểm soát nguồn kép và điều phối song song H-LCC/Scan Engine trên Google Antigravity cho Lead Researcher.
---
# Antigravity Infrastructure - Host OS & Google Drive Integration

Tài liệu cấu hình gốc về danh tính người dùng, quy chuẩn quản trị tài nguyên lưu trữ và giao thức kiểm soát nguồn kép tích hợp giữa Google Antigravity (Local Host OS / PowerShell / Python 3.12 / Subagents) và Google Drive cục bộ (``) dành cho Lead Researcher tại ĐHBK Hà Nội.

*Điều kiện Nạp & Hợp đồng I/O (Trigger & I/O Contract):* Nạp khi thực thi `/learn`, `/scan`, `/edit`, `/bg` hoặc bất kỳ thao tác định vị, đối chiếu nguồn hoặc lưu trữ tệp nào trên workspace và Google Drive; cung cấp định danh gốc Lead Researcher (), cấu trúc cây thư mục tập trung trên ổ `G:\`, cơ chế kiểm soát khóa tệp nguyên tử và giao thức truy vấn Host-Native cho Antigravity Native Engine.

---

## 1. Thông Tin Danh Tính & Bối Cảnh Người Học
- **Họ và tên:** Lead Researcher (Hà Nội, Việt Nam).
- **Đơn vị:** Sinh viên năm 3 Khoa Vật lý Kỹ thuật, Đại học Bách khoa Hà Nội (HUST).
- **Lĩnh vực nghiên cứu mũi nhọn:** Kỹ thuật quân sự & quốc phòng; Vật lý Bán dẫn, Laser Diode, Quang điện tử, Mạch tích hợp quang tử (PIC), Màng mỏng quang học, Cảm biến quang, Công nghệ Nano.
- **Mối quan hệ làm việc:** AI đóng vai trò Chuyên gia Đầu ngành & Giảng viên Kỳ cựu (40 năm kinh nghiệm) kiêm Cộng sự Lab biên soạn; Lead Researcher là Sinh viên năm 3 & Học viên Nghiên cứu tiếp nhận.

---

## 2. Quy Chuẩn Hạ Tầng Google Drive & Workspace Local Trên Antigravity
- **Cấu trúc cây thư mục tập trung trên ổ `G:\`:**
  * Đường dẫn Mẹ học phần: `\<Tên_Học_Phần>\`
  * Thư mục con 1: `Bai_Giang_Dong_Goi/` (Lưu chuyên khảo PDF bài giảng hoàn chỉnh trên Google Drive; tuyệt đối KHÔNG nạp vào NotebookLM vì NotebookLM chỉ chứa dữ liệu gốc).
  * Thư mục con 2: `Kho_Hinh_Anh/` (Lưu ảnh giáo trình gốc `[Goc]_...png` và đồ thị mô phỏng `[Mo_Phong]_...png`).
  * Thư mục con 3 (tùy chọn): `Du_Lieu_Thuc_Nghiem_Lab/` (Số liệu đo đạc thực nghiệm, dữ liệu khớp hàm $I\text{–}V$, $L\text{–}I\text{–}V$).
  * Thư mục lưu trữ tệp cũ: `Kho_Hinh_Anh/Archive/` hoặc `Kho_Luu_Tru_File_Rac_Archive/`.
- **Nguyên tắc Thao tác Tệp Host-Native trên Antigravity:**
  * **Đọc Trực Tiếp (Host Direct Read):** Antigravity sử dụng trực tiếp các công cụ hệ thống (PowerShell, Python `os`, `pypdf`, `PIL`) đọc thẳng từ `\<Tên_Học_Phần>\` với độ trễ 0 ms, không qua trung gian API web.
  * **Lưu Trực Tiếp & Đồng Bộ Tức Thì (Direct-in-Place Sync):** Khi tạo ảnh (`[Mo_Phong]`) hoặc xuất bản PDF từ Python 3.12, tệp được ghi trực tiếp vào đúng thư mục `Kho_Hinh_Anh/` hoặc `Bai_Giang_Dong_Goi/` trên ổ `G:\`. Google Drive for Desktop trên Windows sẽ tự động đồng bộ lên Google Drive đám mây (tuyệt đối KHÔNG nạp/đồng bộ bài giảng đóng gói vào NotebookLM, vì NotebookLM là kho tri thức chuẩn chỉ lưu giữ tài liệu gốc).
- **Cơ chế dự phòng (Fallback):** Nếu chưa xác định được thư mục học phần cụ thể, tự động định tuyến vào `\Chung\`.

---

## 3. Giao Thức Quét Thư Mục & Phối Hợp Subagents
- **Tra cứu tệp Host-Native:** Tìm kiếm tệp theo đường dẫn tuyệt đối với mã hóa Unicode NFC chuẩn tiếng Việt.
- **Tận dụng Subagents:** Khi xử lý các tác vụ bóc tách OCR hàng loạt, mô phỏng quang học chuyên sâu hoặc khớp tham số thực nghiệm Lab, Antigravity kích hoạt các subagents chạy ngầm (Background Task) để không gây nghẽn luồng làm việc chính.
- **Cập nhật Hồ sơ Kiểm toán:** Duy trì tính nhất quán giữa các tài liệu `.gdoc`, `.json` trên Drive và tệp quy tắc [AGENTS.md](file:////.agents/rules/AGENTS.md) trong workspace.

---

## 4. Quy Chuẩn Quản Trị Tài Nguyên Google Drive Cấp Độ Phòng Thí Nghiệm
1. **Khoanh vùng Phạm vi Bất khả xâm phạm (Sandbox Whitelist):**
   - Mọi thao tác I/O chỉ được phép diễn ra bên trong:  
     `\<Tên_Học_Phần>\`
   - Bất kỳ thao tác đọc/ghi nào ngoài đường dẫn trên đều bị coi là vi phạm nghiêm trọng giới hạn an toàn workspace.
2. **Cách ly Tuyệt đối Tệp Tạm (%TEMP% Isolation Policy):**
   - 100% cache công thức toán (`hust_eq_cache`), đồ thị nháp, PDF biên dịch thử nghiệm, tệp batch scripts PHẢI được khởi tạo và thực thi trong `%TEMP%` (`tempfile.gettempdir()`).
   - Tuyệt đối cấm tạo tệp trung gian, `.tmp`, `.aux`, `.log` trên Google Drive `G:\`.
3. **Ghi Đè Nguyên Tử & Kiểm Soát Khóa Tệp (Atomic Replace & Anti-Duplicate):**
   - Trước khi ghi đè tệp tin đã tồn tại trên Drive, kiểm tra `os.access(target_path, os.W_OK)` để phát hiện file lock.
   - Biên dịch hoàn tất ra thư mục tạm `%TEMP%` trước khi thực hiện thay thế nguyên tử `os.replace` sang đích trên `G:\`. Triệt tiêu hoàn toàn hiện tượng sinh tệp trùng ` (1).pdf`, ` (2).pdf`, ` (1).png`.
4. **Quản Lý Phiên Bản & Lưu Trữ Sạch (Clean Archiving):**
   - Với chuyên khảo PDF: Giữ nguyên tên file cố định (`Mục_X.Y_...pdf`) để Google Drive tự động kích hoạt "Quản lý phiên bản" (Manage Versions).
   - Với ảnh mô phỏng cũ/lỗi thời cần bảo lưu: Di chuyển vào `Kho_Hinh_Anh/Archive/` hoặc `Kho_Luu_Tru_File_Rac_Archive/` với tiền tố `[OLD_YYYYMMDD_HHMMSS]_<tên_gốc>.png`.
5. **Giới Hạn Dung Lượng & Chuẩn Hóa Định Dạng Tệp (Size & DPI Caps):**
   - Hình ảnh mô phỏng & ảnh gốc (`.png`): Dung lượng $\le 300\text{ KB}$, độ phân giải $\ge 300\text{ DPI}$ (bắt buộc nén qua Pillow `optimize=True, compress_level=9`).
   - Chuyên khảo PDF (`.pdf`): Dung lượng $\le 5\text{ MB}$, định dạng vector chữ DejaVu sắc nét, tích hợp đầy đủ Bookmarks đa tầng và footer `Trang X / Y`.
6. **Bảo Vệ Liên Kết Ảo Google Docs/Sheets (Virtual Reparse Points):**
   - Nghiêm cấm ghi nhị phân thô vào các tệp shortcut ảo `.gdoc`, `.gsheet`, `.gslides`. Mọi tương tác tài liệu học thuật đều phải định dạng chuẩn `.pdf`, `.md`, hoặc thông qua CLI `nlm`.

---

## 5. Giao Thức Kiểm Tra Nguồn Kép & Kiểm Soát Cổng Đầu Vào (Pre-Scan Handshake)

Trước khi thực thi lệnh `/scan Chương [X] [Tên môn]`, Antigravity bắt buộc đối soát song song giữa Google Drive `G:\` và NotebookLM theo 3 kịch bản:
- **Kịch bản 1 (Có trên NotebookLM nhưng thiếu trên Google Drive):** Dừng quét ngay lập tức. Báo cáo cụ thể tên nguồn thiếu trên Drive `\<Tên_Học_Phần>\` và yêu cầu người học tải tệp gốc lên Drive. Cấm tự ý bịa đặt nội dung hoặc vẽ đồ thị phỏng đoán thay thế tài liệu gốc.
- **Kịch bản 2 (Có trên Google Drive nhưng thiếu trên NotebookLM):** Dừng quét ngay lập tức. Báo cáo cụ thể tên tệp trên Drive chưa được đồng bộ hoặc tải lên Notebook của học phần trên NotebookLM, yêu cầu người học đồng bộ trước khi quét.
- **Kịch bản 3 (Thiếu ở cả hai nơi):** Kích hoạt Chốt dừng an toàn (Hard Stop) ngay lập tức. Báo cáo điểm nghẽn thiếu cơ sở dữ liệu gốc, yêu cầu cung cấp tài liệu.

---

## 6. Thuật Toán Điều Phối Song Song Phân Cấp Lai Ghép Cho Tác Vụ Quy Mô Lớn (H-LCC/Scan Engine)

Quản trị toàn diện việc điều phối song song phân cấp cho lệnh `/scan Chương [X] [Tên môn]` theo kịch bản Python độc lập `scripts/parallel_scan_engine.py`, giải quyết triệt để 4 bệnh lý suy thoái (Sơ sài, Trôi ngữ cảnh, Suy thoái ràng buộc, Rơi rớt luận điểm vi mô):

### Kiến Trúc 5 Giai Đoạn Bất Biến (5-Phase Immutable Pipeline)
1. **Giai đoạn 0 — Tiền Kiểm Định & Prompt Caching:**
   - Kích hoạt Thuật toán 1 (`HDIR Engine` kết hợp `DICG 2.0`) thực thi Lớp 2 Pre-Scan Handshake (kiểm toán nhị phân đủ song song Slide & Sách trên Google Drive `G:\`, thiếu kích hoạt Hard Stop) và Lớp 3 Figure Inventory Scanner ($\mathbf{F}_{\text{blueprint}}$ kết nối Thuật toán 3 `RVAE Engine 2.0`).
   - Nạp tài liệu vào Gemini Prompt Caching giảm 95% chi phí input token ($\$0.025/\text{triệu token}$).
   - Khởi tạo tệp theo dõi tiến độ `PROGRESS_CHECKPOINT.json` trên Drive `G:\`.
2. **Giai đoạn 1 — Đề Cương Tuần Tự & Khóa Biên (Outline & Boundary Locking):**
   - Tiếp nhận `OUTLINE_CHUONG_X.json` từ Thuật toán 2 (`HPDE 2.0`), phân rã I-nodes và S-nodes theo SciSlide Dual-Plane (AIF + CPG DAG), gắn thẻ XML HoT (`<arg id="...">`, `<link id="...">`).
   - Tích hợp Master Nomenclature Matrix từ Thuật toán 10 (`ATCC`) vào Từ điển Toàn cục $G_{\text{attr}}$.
   - Sinh đệ quy tuần tự Đề cương LOGIC $O_i = f(T_{\text{chương}}, P_i, G_{\text{attr}}, O_1, \dots, O_{i-1})$.
   - Đóng gói bộ ba kiểm soát biên DOC: Ngữ cảnh Kế thừa $C_{\text{prev}}$, Ngữ cảnh Tương lai $C_{\text{next}}$ (kèm Ràng buộc Phủ định cấm $M_i$ lấn sân $M_{i+1}$) và Cặp Neo Chuyển tiếp $A_i = (A_i^{\text{in}}, A_i^{\text{out}})$.
   - Xuất bản hoàn chỉnh duy nhất `Mục X.1` làm mẫu đối chuẩn và KHÓA CỨNG Sample Gate Barrier (dừng trên Chat chờ người học duyệt, cấm tự ý chạy tiếp Pha 2).
3. **Giai đoạn 2 — Đóng Gói Hợp Đồng Máy FSM & Blueprint PLBE:**
   - Sau khi người học duyệt Pha 1, chuyển hóa từng mục $M_i$ ($i \ge 2$) thành Hợp đồng Prompt Tất định $\mathcal{C}_i = \langle \mathcal{O}_i, \Sigma_i, \mathcal{B}_i \rangle$: Quyền sở hữu độc quyền $\mathcal{O}_i$ phủ 100% mã thẻ HoT; Giao diện Pydantic $\Sigma_i$ khóa cứng câu neo biên và mảng MPT; Ràng buộc Ngân sách $\mathcal{B}_i$ gắn liền với `BLUEPRINT_MUC_X.Y.json` theo Thuật toán 4 (`PLBE`) lưu vào `%TEMP%`.
4. **Giai đoạn 3 — Phân Phối Đa Tác Nhân & Nén 3 Bước CoD:**
   - Điều phối song song qua Send API theo lô an toàn $K = 3\text{–}4$ workers tránh lỗi HTTP 429 rate limit. Mỗi Worker nhận lát cắt trạng thái cô lập trong `%TEMP%/worker_{section_id}/` (Thuật toán 9), kích hoạt trực tiếp Động cơ Thuật toán 12 (`MALAE Engine` Pha 2) để triển khai chu trình Nén 3 Bước Chain of Density (CoD) bám sát Khung Sư phạm 5 Giai đoạn của Thuật toán 5 (`UFME`):
     * Vòng 1: Dựng khung 5 giai đoạn và khóa neo biên;
     * Vòng 2: Giữ nguyên ngân sách độ dài, nén bỏ từ đệm sáo rỗng để nhường không gian nạp 100% mắt xích vi mô từ sách;
     * Vòng 3: Hoàn tất dẫn xuất trung gian $\ge 1$ bước có nhãn `↳` tường minh từ slide, nhúng ảnh gốc $\ge 300\text{ DPI}$ từ Thuật toán 3 (`RVAE`), nhúng đồ thị MATLAB R2014b+ từ Thuật toán 7 (`HDSE`), và dừng ở Vòng 3 (Sweet Spot) đạt mật độ thực thể $\ge 0.30$.
5. **Giai đoạn 4 — Cổng Kiểm Định Tất Định & Phản Xạ Cục Bộ:**
   - Chặn bắt bằng `academic_gate_hook.py`; kích hoạt Nhân kiểm định Thuật toán 8 (`Pass/Fail Gate` kết hợp `DOHG 2.0` gồm Trạm 1 AST Linter, Trạm 2 HDSE Collision $\delta_{\text{geom}} \ge 8\%$, Trạm 3 PyMuPDF Figure Coverage, Trạm 4 SymPy Formal CAS `simplify == 0`, Trạm 5 Atomic Sandbox) và kiểm đếm Thuật toán 6 (5 Mắt xích OCR). Nếu vi phạm $\implies$ Bơm lỗi ngôn ngữ vào riêng nhánh lỗi để tự sửa (Local Reflexion, tối đa 3 lần, quá 5 lần toàn trình kích hoạt Hard Stop).
6. **Giai đoạn 5 — Gom Cụm Trạng Thái, Khâu Nối Biên & Chế Bản PDF Nguyên Tử:**
   - Thu thập qua State Reducer; chạy Thuật toán Khâu nối Biên độ Cửa sổ Trượt Re3 (Sliding-Window Boundary Stitching 200 từ tại ranh giới $A_i^{\text{out}} \leftrightarrow A_{i+1}^{\text{in}}$) mài sắc câu chuyển ý và đối chiếu chéo $G_{\text{attr}}$.
   - Chế bản ReportLab PDF tại `%TEMP%` rồi thực hiện `os.replace` nguyên tử sang `Bai_Giang_Dong_Goi/` trên `G:\`; cập nhật `PROGRESS_CHECKPOINT.json`; thực thi Zero-Text Chat Rule (chỉ xuất Bộ ba Mỏ neo Điều hướng lên chat).

### Ràng Buộc Nhạc Trưởng Thuần Túy & Cô Lập Vùng Đệm (Pure Orchestrator & Namespace Gate)
1. **Ràng buộc Nhạc trưởng Thuần túy (Pure Orchestrator Hard Gate):**
   - Bắt buộc 100% mọi phân mục chuyên khảo (kể cả Mục X.1 Pha 1 và X.2 -> X.N Pha 2) đều phải được ủy quyền và biên dịch độc lập bên trong Subagent cô lập (`invoke_subagent`).
   - Phiên chat chính (Parent Orchestrator) TUYỆT ĐỐI KHÔNG được trực tiếp chạy đơn luồng để trích xuất ảnh, chạy script matplotlib hoặc biên dịch ReportLab, nhằm bảo tồn 100% độ sạch của cửa sổ ngữ cảnh (Zero Context Bloat).
2. **Cô lập Vùng đệm Đa tiến trình (Worker Namespace Cache Isolation):**
   - Mọi Worker khi thi công nội dung vi mô theo Thuật toán 12 (`MALAE`) đều vận hành trong `%TEMP%/worker_{section_id}/` và sở hữu thư mục cache công thức toán riêng biệt `%TEMP%/worker_{section_id}/hust_eq_cache/`.
   - Triệt tiêu 100% xung đột khóa tệp Windows `WinError 32` khi chạy song song.
