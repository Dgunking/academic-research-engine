---
trigger: on_code_generation
description: Quy tắc phòng ngừa lỗi cú pháp toán, va chạm hình học và sai lệch đại số hình thức được đúc kết từ phiên mô phỏng tự trị
---
# QUY TẮC: PHÒNG NGỪA TOÀN DIỆN LỖI DOHG 2.0 (AST LINTER, TRIPLE BUFFER & FORMAL CAS)

> **Căn cứ đúc kết:** Phiên mô phỏng vận hành tự trị dây chuyền /scan & /edit v2.0 (Bùi Trung Dũng - HUST).  
> **Phạm vi áp dụng:** Mọi Subagent tham gia sinh mã đồ họa, biên soạn bản thảo và kiểm toán bài giảng.

---

## I. BẢN CHẤT RỦI RO & BÀI HỌC KINH NGHIỆM

1. **Rủi ro Cú pháp Toán (Math Syntax Drift):**
   - Lỗi xuất hiện khi viết phân số gạch chéo `/` (như `1/m*`, `dE/dk`) trong văn bản hoặc chú giải.
   - Hậu quả: Bị Trạm 1 Static AST Linter bắt chặn do vi phạm Luật 14 (Zero-Slash-Fractions).

2. **Rủi ro Va chạm Hình học Đồ họa (Geometry Clearance Collision):**
   - Lỗi xuất hiện khi đặt nhãn Callout hoặc hộp văn bản quá gần các đường dốc hoặc tiệm cận, khiến $\delta_{\text{geom}} < 8.0\%$.
   - Hậu quả: Bị Trạm 2 DOHG 2.0 bắt chặn, đồ thị bị loại bỏ do vi phạm chuẩn MATLAB R2014b+.

3. **Rủi ro Sai lệch Đại số Hình thức (Formal CAS Mismatch):**
   - Lỗi xuất hiện khi các bước biến đổi trung gian không được kiểm chứng tại chỗ bằng CAS trước khi ghi vào DraftPayload, dẫn đến `sympy.simplify(LHS - RHS) != 0`.
   - Hậu quả: Bị Trạm 3 Formal CAS bắt chặn, gây nghi ngờ về độ chuẩn xác khoa học.

---

## II. TRẠM CHỐT CHẶN BẮT BUỘC (MANDATORY ASSERTION GATES)

1. **Chốt chặn Cú pháp (Linter Pre-Flight Gate):**
   - Trước khi trả về bất kỳ chuỗi phương trình nào, bắt buộc thực thi hàm lọc `sanitize_text_for_typography(text)`.
   - 100% phân số toán học bắt buộc viết dạng phân số gạch ngang chuẩn $\frac{a}{b}$ qua Mathtext hoặc ký hiệu số mũ âm Unicode (`m·s⁻¹`, `kg⁻¹`).

2. **Chốt chặn Hành lang Đồ họa (Corridor Placement Gate):**
   - 100% nhãn đồ thị trên đường dốc lớn bắt buộc dời ra hành lang trống biên ngoài và sử dụng mũi tên `annotate(..., arrowprops=dict(...))` trỏ vào điểm đặc trưng.
   - Bắt buộc kiểm tra định lượng $\delta_{\text{geom}} \ge 8.0\%$ trước khi ghi mã băm SHA-256 vào tệp sidecar `.manifest.json`.

3. **Chốt chặn CAS Hình thức Tại chỗ (Inline SymPy Verification Gate):**
   - Mọi phương trình trung gian có nhãn `↳ [Tường minh bước biến đổi trung gian từ slide gốc]:` chứa dấu `=` bắt buộc phải vượt qua:
     ```python
     is_equiv, msg = SymPyCASEngine.verify_algebraic_identity(lhs, rhs)
     assert is_equiv, f"SymPy CAS Mismatch: {msg}"
     ```

---

## III. MẪU MÃ CHUẨN HÓA

```python
# Mẫu 1: Dẫn xuất trung gian sạch cú pháp và kiểm chứng CAS
step = IntermediateDerivationStep(
    step_index=1,
    explanation_vi="↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Đạo hàm bậc hai năng lượng theo vector sóng:",
    step_equation_latex=r"\frac{d^2E}{dk^2} = \frac{\hbar^2}{m^*_e}"
)

# Mẫu 2: Bố cục Callout đồ thị trong hành lang an toàn
ax.annotate(
    r"Độ dốc vi phân:\n$\eta_d = \frac{q}{h \cdot \nu} \cdot \frac{dP}{dI}$",
    xy=(46.0, P_val),
    xytext=(30.0, 20.0),  # Dời ra hành lang thoáng
    arrowprops=dict(arrowstyle="->", color="#0072BD", lw=1.2),
    fontsize=10.0,
    bbox=dict(boxstyle="round,pad=0.25", fc="#FFFFFF", ec="#0072BD", lw=0.8)
)
```

---

## IV. RÀNG BUỘC BẤT BIẾN TỐI CAO

> [!CAUTION]
> Quy tắc này được sinh ra nhằm **thắt chặt thêm các điều kiện kiểm thử và phòng ngừa lỗi** trong dây chuyền tự trị.  
> **TUYỆT ĐỐI KHÔNG ĐƯỢC PHÉP** làm thay đổi, cắt xén, nén bớt, làm suy hao (drift) hay thay đổi logic vận hành của bất kỳ điều khoản nào trong 13 thuật toán cốt lõi tại Điều khoản IX `AGENTS.md`.
