---
name: academic-terminology-guardian
description: Chuẩn hóa danh pháp song ngữ (Anh - Việt), quy tắc viết hoa Nghị định 30, viết số APA 7 và đơn vị SI Luật Đo lường 04 trên Google Antigravity.
---
# Academic Terminology Guardian (Bilingual Lexicon Hub & ATCC Engine)

Kỹ năng chuyên trách quản lý, tra cứu và chuẩn hóa hệ thống danh pháp, thuật ngữ chuyên ngành song ngữ (Anh - Việt) và hệ quy chuẩn ngôn ngữ khoa học cho Lead Researcher tại ĐHBK Hà Nội theo Thuật toán 10 (`ATCC Engine`).

*Hợp đồng Đầu vào / Đầu ra:* Cung cấp thuật ngữ song ngữ từ sổ tay NotebookLM (`Academic Bilingual Terminology Matrix`) và giữ nguồn chân lý độc quyền về quy chuẩn ngôn ngữ cho `engineering-instructor`, `physics-diagram-studio`, `monograph-pdf-publisher` và `output-accuracy-verifier`.

---

## 1. Cơ Sở Dữ Liệu Sổ Tay NotebookLM & Điểm Chặn Tiền Biên Dịch (Pre-Compilation Gate)
- **Điểm chặn Tiền Biên dịch (Pre-Compilation Gate):** Bắt buộc kích hoạt ngay sau khi hoàn tất bóc tách cấu trúc `HPDE Engine` và trước khi thiết kế khung bài giảng `PLBE Engine` hoặc chấp bút toàn văn từng mục. Tuyệt đối cấm viết câu chữ chi tiết khi chưa hoàn tất bảng đối chiếu danh pháp của phân mục đó.
- **Sổ tay chuyên biệt:** `Academic Bilingual Terminology Matrix` (ID: `notebooks/76ca6cce-c7f1-48f0-8999-0615940c911e`).
- **Phân tách tệp nguồn theo chuyên ngành:**
  * `Vật lý Linh kiện Bán dẫn & Laser Diode`
  * `Quang học & Quang điện tử`
  * `Vật lý Chất rắn & Tinh thể học`
  * `Vật lý & Công nghệ Nano`
  * `Trường điện từ & Điện động lực học`
- **Cấu trúc bản ghi chuẩn hóa trong sổ tay:**
  `| Thuật ngữ tiếng Việt | English Term | Ký hiệu | Định nghĩa bản chất vi mô (1 câu chuẩn + 1–2 câu ẩn dụ thực tế) | Nguồn |`
- **Cập nhật theo lô (Batch Read-Modify-Write):** Trong quá trình chạy `/scan`, gom các thuật ngữ mới phát sinh để cập nhật một lần vào cuối phiên, tránh làm loãng ngữ cảnh.

---

## 2. Quy Chuẩn Hiển Thị Thuật Ngữ, Viết Hoa, Viết Số & Đơn Vị SI

### 2.1. Quy Chuẩn Thuật Ngữ 2 Trạng Thái
1. **Trạng thái 1 – Đã chuẩn hóa trong NotebookLM:**
   - *Trong văn bản PDF:* 100% toàn bộ các thuật ngữ chuyên ngành ở Trạng thái 1 luôn luôn có định dạng `thuật ngữ tiếng Việt chuẩn (english term)` xuyên suốt toàn bộ tài liệu (ví dụ: *dải dẫn (conduction band)*, *dòng ngưỡng (threshold current)*), tuyệt đối không lược bỏ phần tiếng Anh ở các lần xuất hiện sau.
   - *Trên Đồ thị MATLAB & Sơ đồ:* Viết ngắn gọn `Thuật ngữ tiếng Việt chuẩn + Ký hiệu + [Đơn vị SI]`, tuyệt đối không chèn cụm tiếng Anh dài dòng trên hình vẽ gây phình to kích thước hộp chữ làm vi phạm vùng đệm $\delta_{\text{geom}} \ge 8\%$.
2. **Trạng thái 2 – Chưa có trong NotebookLM (Thuật ngữ mới phát sinh):**
   - Bắt buộc trải qua quy trình kiểm chuẩn học thuật tối cao: rà soát tối thiểu 10 nguồn tài liệu chuẩn (Sze, Coldren, Yariv, Saleh, Griffiths, giáo trình HUST, kỷ yếu IEEE, chuẩn ISO 80000, TCVN) và đối chiếu chéo ít nhất 3 lần (bản chất vi mô nguyên lý đầu, tính đồng bộ danh pháp hệ thống, chuẩn ngữ pháp tiếng Việt khoa học theo Nghị định 30).
   - Viết `english term [thuật ngữ mới đề xuất]` và tự động ghi nhận vào hàng đợi `%TEMP%/PENDING_TERMINOLOGY.json` để cập nhật theo lô (Batch Read-Modify-Write) vào sổ tay NotebookLM `Academic Bilingual Terminology Matrix` cuối phiên; cấm tự ý dịch tản mạn làm phân mảnh danh pháp.
3. **Danh từ mượn nguyên ngữ:** Giữ nguyên dạng gốc không in nghiêng cho các danh từ quốc tế phổ dụng (laser, diode, electron, photon, phonon, exciton, plasma, vector, tensor).

### 2.2. Quy Tắc Viết Hoa (Nghị định 30/2020/NĐ-CP)
- **Cấm viết hoa tùy tiện danh từ chung giữa câu:** Khi đưa thuật ngữ vào giữa câu, viết thường toàn bộ chữ cái đầu (chỉ viết hoa đầu câu, tên riêng nhà khoa học như Maxwell, Fermi, Planck, hoặc ký hiệu nguyên tố GaAs, InP). Viết đúng: *"mật độ dòng điện dịch"*, *"vùng cấm quang học"*.
- **Sentence case bắt buộc:** Áp dụng cho 100% tiêu đề chương, mục, tiểu mục (H1–H3), tên bảng biểu, tên hình vẽ và nhãn trục đồ thị (chỉ viết hoa chữ cái đầu tiên và tên riêng/ký hiệu).

### 2.3. Quy Tắc Viết Số (APA 7 & Tiếng Việt Khoa Học)
- **Chữ vs. Số:** Số đếm từ 0 đến 9 khi không kèm đơn vị đo lường thì viết bằng chữ (*ba hệ tọa độ*, *bốn phương trình*); từ 10 trở lên viết bằng chữ số Ả Rập.
- **Luôn viết bằng số Ả Rập:** Mọi số liệu đo lường kèm đơn vị (`3 kg`, `5 V/m`), tỷ lệ phần trăm (`5%`), số thứ tự (*Chương 1*, *Mục 1.1*, *Hình 1.1*, *Bảng 1.1*). Cấm đặt chữ số ở đầu câu.
- **Dấu thập phân & khoảng số:** Dùng **dấu phẩy (`,`)** làm dấu thập phân (`3,14`, `1,424 eV`), **dấu chấm (`.`)** phân cách hàng nghìn (`1.000.000`), dấu gạch ngang **en-dash (`–`)** cho khoảng số (`5–10 nm`, đặc tuyến $I\text{–}V$).

### 2.4. Đơn Vị Đo Lường SI (Luật Đo Lường 04/2011/QH13)
- Đặt **đúng 1 khoảng trắng** giữa số và đơn vị (`300 K`, `10 nm`, `1,55 μm`, `25 °C`), trừ ký hiệu phần trăm (`%`) và độ góc (`°`) viết liền không có khoảng trắng (`95%`, `45°`).

---

## 3. Chốt Chặn Xung Đột & Trôi Danh Pháp (Zero-Drift Gate)
Nếu phát hiện xung đột thuật ngữ giữa Slide HUST và Giáo trình Sách, hoặc có sự trôi lệch ký hiệu toán/lý: Chặn tiến trình biên dịch (Hard Block), xuất bảng đối chiếu 3 cột `[Thuật ngữ Slide | Thuật ngữ Sách | Đề xuất chuẩn hóa]` lên chat chờ người học duyệt trước khi cuốn chiếu.
