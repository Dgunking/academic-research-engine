# ENGINEERING_DISCIPLINE_WORKFLOW.md — Quy Trình Kỷ Luật Kỹ Thuật Cho AI Coding Agent
> **Áp dụng cho:** Lead Researcher (Khoa Vật lý Kỹ thuật - HUST) & AI Agent.  
> **Cơ sở phương pháp luận:** Kế thừa tinh hoa từ `Superpowers` (TDD, Root-cause), `ECC` (Everything Code - Senior SWE Enforcement), `Ponytail` (Cực kỳ kiệm lời, zero văn mẫu), `Headroom` (Cách ly & kiểm soát ngữ cảnh) và `Quality Gatekeeper` 17 điểm.  
> **Mục đích:** File quy chuẩn này được dùng làm mỏ neo trỏ vào (`@ENGINEERING_DISCIPLINE_WORKFLOW.md`) trong mọi câu lệnh yêu cầu AI thực hiện **Vá lỗi**, **Chỉnh sửa / Tái cấu trúc**, hoặc **Nâng cấp tính năng** để triệt tiêu hoàn toàn thói quen code ẩu, sửa mò và phá vỡ kiến trúc hệ thống.

---

## 4 NGUYÊN TẮC BẤT BIẾN (CORE INVARIANTS)

1. **Cấm sửa mò khi chưa có bài test tái hiện (Zero-Shotgun-Debugging):** Tuyệt đối không chạm vào mã nguồn chính khi chưa cô lập được lỗi bằng một bài test độc lập có kết quả FAIL.
2. **Bảo toàn giao diện hợp đồng dữ liệu (Data Contract Invariant):** Khi tái cấu trúc, 100% chữ ký hàm (*signature*), kiểu dữ liệu (*type hints*), và lược đồ (*Pydantic schema*) đầu ra phải được giữ nguyên hoặc tương thích ngược 100%.
3. **Kiểm soát ngữ cảnh sạch sẽ (Headroom Context Hygiene):** Chỉ đọc đúng file cần sửa và các interface kết nối trực tiếp; cấm nạp tràn lan cả repository vào context gây loãng tư duy (*context rot*).
4. **Phản hồi gãy gọn, tập trung vào bản chất (Ponytail Mode):** Loại bỏ 100% lời chào hỏi, xin lỗi, tâng bốc hoặc giải thích sáo rỗng. Chỉ xuất: Phân tích nguyên tắc đầu $\to$ Diff code $\to$ Log kiểm thử $\to$ Trạng thái Pass/Fail.

---

## PHA 1: QUY TRÌNH VÁ LỖI (BUG FIXING PROTOCOL)
*(Kích hoạt bằng cú pháp: `@ENGINEERING_DISCIPLINE_WORKFLOW.md [PHA 1]`)*

```
[Báo lỗi / Hiện tượng] 
         │
         ▼
[Bước 1.1: Viết test tái hiện lỗi độc lập (FAIL)]
         │
         ▼
[Bước 1.2: Phân tích nguyên nhân gốc rễ (First-Principles)]
         │
         ▼
[Bước 1.3: Sửa mã nguồn tối thiểu (Atomic Fix)]
         │
         ▼
[Bước 1.4: Chạy test tái hiện (Bắt buộc PASS)]
         │
         ▼
[Bước 1.5: Hậu kiểm toàn bộ Test Suite (Zero-Regression Gate)]
```

### Chi tiết các bước thực hiện:
* **Bước 1.1 — Viết test tái hiện (Reproduction Script):**
  - Tạo một file kiểm thử tối giản trong thư mục tạm hoặc `tests/` (ví dụ: `scratch/test_reproduce_bug.py`).
  - Script này nạp dữ liệu đầu vào gây lỗi, gọi hàm mục tiêu và chạy thử.
  - **Điều kiện tiên quyết:** Script này **BẮT BUỘC PHẢI CHẠY VÀ BÁO LỖI (FAIL)** đúng với hiện tượng người học phản ánh. Cấm sửa code trước khi có test FAIL.
* **Bước 1.2 — Truy nguyên nguyên nhân gốc rễ (Root-Cause Analysis):**
  - Trả lời bằng nguyên lý đầu: Lỗi do sai lệch toán học/vật lý, do tràn số/sai kiểu dữ liệu, do điều kiện biên của thư viện (ReportLab, Matplotlib, SymPy), hay do cấu trúc thư mục?
  - Cấm giải thích triệu chứng; phải chỉ thẳng vào điểm nghẽn logic.
* **Bước 1.3 — Can thiệp mã nguồn tối thiểu (Atomic Fix):**
  - Chỉ sửa đúng vị trí gây ra lỗi gốc rễ, giữ nguyên kiến trúc xung quanh.
* **Bước 1.4 — Xác minh đảo chiều:**
  - Chạy lại script tái hiện ở Bước 1.1. Kết quả bắt buộc phải chuyển từ **FAIL $\to$ PASS 100%**.
* **Bước 1.5 — Hậu kiểm không hồi quy (Zero-Regression):**
  - Chạy lại toàn bộ test suite hiện có của module. Nếu việc sửa lỗi làm gãy tính năng khác, lập tức quay lại phân tích, cấm ép code chạy bằng cách vá chắp vá.

---

## PHA 2: QUY TRÌNH CHỈNH SỬA & TÁI CẤU TRÚC (REFACTORING PROTOCOL)
*(Kích hoạt bằng cú pháp: `@ENGINEERING_DISCIPLINE_WORKFLOW.md [PHA 2]`)*

```
[Mục tiêu tái cấu trúc / Tối ưu]
         │
         ▼
[Bước 2.1: Khóa chặt Hợp đồng Dữ liệu (Data Contract Invariant)]
         │
         ▼
[Bước 2.2: Cô lập phạm vi tác động (Headroom Context Isolation)]
         │
         ▼
[Bước 2.3: Tái cấu trúc logic nội bộ & Tối ưu giải thuật]
         │
         ▼
[Bước 2.4: Kiểm tra tính toàn vẹn (Static Check & Unit Tests)]
         │
         ▼
[Bước 2.5: Ghi đè nguyên tử an toàn (%TEMP% $\to$ Target)]
```

### Chi tiết các bước thực hiện:
* **Bước 2.1 — Khóa Hợp đồng Dữ liệu:**
  - Xác định và ghi rõ: Hàm/Lớp này nhận vào những tham số gì và trả về cấu trúc dữ liệu nào.
  - Dù tái cấu trúc 100% thuật toán bên trong, kiểu trả về phải khớp tuyệt đối để không làm sập các module khác đang phụ thuộc.
* **Bước 2.2 — Cô lập ngữ cảnh:**
  - Xác định chính xác danh sách tệp bị ảnh hưởng. Không sửa đổi bất kỳ tệp nào nằm ngoài phạm vi tái cấu trúc đã thỏa thuận.
* **Bước 2.3 — Tái cấu trúc sạch (Clean-Slate Refactoring):**
  - Loại bỏ mã dư thừa, tối ưu độ phức tạp thời gian/bộ nhớ, làm sạch tên biến theo chuẩn vật lý song ngữ hoặc snake_case chuẩn mực.
* **Bước 2.4 — Kiểm thử tĩnh và động:**
  - Chạy kiểm tra cú pháp, Type Checker, và toàn bộ unit tests của module.
  - Đảm bảo đầu ra dữ liệu trước và sau khi refactor có giá trị tương đương về mặt toán học và vật lý.
* **Bước 2.5 — Ghi đè nguyên tử (Atomic Replacement):**
  - Biên dịch và xác thực tệp đích trong thư mục tạm `%TEMP%`, sau khi đạt 100% Pass mới tiến hành thay thế vào file chính.

---

## PHA 3: QUY TRÌNH NÂNG CẤP & MỞ RỘNG DỰ ÁN (FEATURE EXPANSION PROTOCOL)
*(Kích hoạt bằng cú pháp: `@ENGINEERING_DISCIPLINE_WORKFLOW.md [PHA 3]`)*

```
[Yêu cầu tính năng / Module mới]
         │
         ▼
[Bước 3.1: Lập bản thiết kế kiến trúc (Spec / Architecture Plan First)]
         │
         ▼
[Bước 3.2: Đóng gói Module hóa độc lập (Skill / Subagent / Module)]
         │
         ▼
[Bước 3.3: Viết Test kiểm thử nghiệm thu (Acceptance Criteria Tests)]
         │
         ▼
[Bước 3.4: Triển khai mã nguồn thực thi]
         │
         ▼
[Bước 3.5: Kiểm toán chất lượng toàn diện (Quality Gatekeeper Gate)]
```

### Chi tiết các bước thực hiện:
* **Bước 3.1 — Thiết kế kiến trúc trước khi viết mã (Plan First):**
  - Xuất bảng đặc tả kỹ thuật tóm tắt:
    * *Đầu vào / Đầu ra (Inputs/Outputs)*.
    * *Thư viện phụ thuộc*.
    * *Phương trình vật lý / Thuật toán toán học cốt lõi*.
  - Chờ thống nhất phương án kiến trúc trước khi sinh code hàng loạt.
* **Bước 3.2 — Đóng gói Module hóa độc lập (Anti-Monolithic):**
  - Tính năng mới phải nằm trong module riêng (trong `scripts/`, `agents/`, hoặc `.agents/skills/`), cấm nhồi nhét hàng nghìn dòng vào một file đa năng duy nhất.
  - Thiết kế các hàm tự chứa (*self-contained*), giao tiếp với hệ thống chính qua giao diện chuẩn.
* **Bước 3.3 — Viết bài kiểm thử nghiệm thu trước:**
  - Xây dựng các ca kiểm thử chuẩn mực cho tính năng mới: trường hợp thông thường, trường hợp biên (*edge cases*), giá trị giới hạn tiệm cận.
* **Bước 3.4 — Viết mã triển khai:**
  - Triển khai code tuân thủ các quy tắc bất biến trong `AGENTS.md` (hằng số CODATA 2022, thông số bán dẫn 300 K, chuẩn đồ họa MATLAB R2014b+, layout ReportLab).
* **Bước 3.5 — Kiểm định nghiệm thu qua trạm chốt chặn:**
  - Cho chạy qua `tests/` và bộ kiểm định tương ứng (`quality-gatekeeper` hoặc các script assert chuyên sâu).

---

## BỘ MẪU CÂU LỆNH (PROMPT TEMPLATES) ĐỂ Lead Researcher TRỎ VÀO CHAT

Khi giao tác vụ cho AI, bạn chỉ cần copy mẫu lệnh tương ứng và điền nội dung:

### 1. Mẫu lệnh Vá lỗi (Bug Fix)
```markdown
Áp dụng @ENGINEERING_DISCIPLINE_WORKFLOW.md [PHA 1: VÁ LỖI] để xử lý lỗi sau:
- Hiện tượng lỗi: [Mô tả hiện tượng, dán mã lỗi hoặc log terminal]
- File / Module liên quan: [Tên file hoặc đường dẫn]
Yêu cầu bắt buộc:
1. Tạo script test độc lập chứng minh lỗi (kết quả FAIL) trước khi sửa code chính.
2. Phân tích nguyên nhân gốc rễ bằng nguyên lý đầu.
3. Sửa mã và chứng minh test đã PASS 100%. Bật chế độ Ponytail.
```

### 2. Mẫu lệnh Chỉnh sửa / Tái cấu trúc (Refactor)
```markdown
Áp dụng @ENGINEERING_DISCIPLINE_WORKFLOW.md [PHA 2: REFACTOR] cho:
- Module cần tái cấu trúc: [Đường dẫn file]
- Mục tiêu: [Ví dụ: Tối ưu hiệu năng, chuẩn hóa layout đồ thị, làm sạch mã nguồn]
Yêu cầu bắt buộc:
1. Giữ nguyên 100% Data Contract (chữ ký hàm và cấu trúc trả về).
2. Không gây tác dụng phụ (side-effects) lên các module phụ thuộc.
3. Chạy kiểm thử xác minh tính toàn vẹn trước khi ghi đè file.
```

### 3. Mẫu lệnh Nâng cấp tính năng mới (Feature Expansion)
```markdown
Áp dụng @ENGINEERING_DISCIPLINE_WORKFLOW.md [PHA 3: NÂNG CẤP] để xây dựng tính năng mới:
- Tính năng: [Tên tính năng, ví dụ: Tính phổ phản xạ màng mỏng đa lớp bằng ma trận truyền sóng]
- Phạm vi: [Đường dẫn module mới cần tạo]
Yêu cầu bắt buộc:
1. Lập bản thiết kế kiến trúc (Spec/Plan) trước khi viết mã.
2. Đóng gói module hóa độc lập, không nhồi nhét vào file cũ.
3. Thiết lập bộ test kiểm thử nghiệm thu và chạy nghiệm thu đạt PASS 100%.
```

---

## CHECKLIST KIỂM TOÁN NHỊ PHÂN CHO AI (TỰ ĐỐI SOÁT TRƯỚC KHI TRẢ LỜI)

Mọi phản hồi của AI liên quan đến sửa code hoặc nâng cấp dự án bắt buộc tự đối soát 5 tiêu chí:
- [ ] **Tiêu chí 1:** Đã có bài test độc lập chứng minh lỗi trước khi sửa hay chưa? (Đối với Vá lỗi)
- [ ] **Tiêu chí 2:** Các chữ ký hàm và kiểu dữ liệu có bị phá vỡ không? (Đối với Refactor)
- [ ] **Tiêu chí 3:** Tính năng mới có được module hóa sạch sẽ hay đang viết dồn vào file cũ? (Đối với Nâng cấp)
- [ ] **Tiêu chí 4:** Toàn bộ test suite liên quan đã được chạy trên host OS và đạt PASS 100% chưa?
- [ ] **Tiêu chí 5:** Văn phong có tuân thủ Ponytail (gãy gọn, đi thẳng vào kỹ thuật, zero sáo rỗng) không?
