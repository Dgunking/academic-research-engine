---
trigger: on_code_generation
description: Quy tắc phòng ngừa lỗi cú pháp toán, va chạm hình học, trôi dạt bảng danh pháp và sai lệch đại số hình thức được đúc kết từ phiên mô phỏng tự trị
---
# QUY TẮC: PHÒNG NGỪA TOÀN DIỆN LỖI DOHG 2.0 (AST LINTER, TRIPLE BUFFER, FORMAL CAS & NOMENCLATURE INTEGRITY)

> **Căn cứ đúc kết:** Phiên mô phỏng vận hành tự trị dây chuyền /scan & /edit v2.0 và sự cố bảng danh pháp Chương 3 (Lead Researcher - HUST).  
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

4. **Rủi ro Trôi dạt Bảng Danh pháp (Nomenclature Dict-Unpack Drift):**
   - Lỗi xuất hiện khi thực hiện giải nén trực tiếp `name, sym, unit, meaning = row` trên phần tử `dict` (như `{'name': ..., 'symbol': ...}`), khiến Python giải nén keys thành chuỗi literal (`'name'`, `'symbol'`, `'unit'`, `'meaning'`) thay vì giá trị vật lý.
   - Hậu quả: Toàn bộ bảng danh pháp ISO 80000-2 bị điền thô các chuỗi placeholder tiếng Anh, làm mất toàn bộ thông tin vật lý.

5. **Rủi ro Cắt xén Bảng qua Trang Mới (Table Page-Split Defect):**
   - Lỗi xuất hiện khi khối phương trình cột trụ sử dụng cơ chế ngắt lỏng lẻo (`_PillarKeepTogether` tự ngắt khi `availHeight >= 210.0`) hoặc `splitByRow=1`, khiến bảng danh pháp bị ngắt đôi qua trang tiếp theo, lặp lại tiêu đề và cắt xén nội dung giữa hai trang liên tiếp.
   - Hậu quả: Phá vỡ tính liền mạch thị giác của khối tri thức hạt nhân MALAE Cấp 3.

6. **Rủi ro Rò rỉ Thẻ Tham số N/A (Simulation Parameter Card Leak):**
   - Lỗi xuất hiện khi tệp sidecar manifest `.manifest.json` thiếu các trường `material_system`, `sweep_parameters`, `lab_metrics` hoặc để mặc định `'N/A'`, khiến hàm nhúng ảnh in ra `↳ [Hệ vật liệu]: N/A | [Thông số quét]: N/A | [Hệ quả Lab]: N/A`.
   - Hậu quả: Gây rác thị giác, làm giảm tính chuyên nghiệp và vi phạm tính chính xác thực nghiệm.

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

4. **Chốt chặn Hình học Tiêu đề - Legend (Title-to-Legend Hard Clearance Gate):**
   - Trong cấu trúc 3 tầng tự chứa (`Title` in đậm → `External Top Banner Legend` → `Axes` dữ liệu):
     * Bắt buộc đặt `ax.legend(bbox_to_anchor=(0.5, 1.02), loc="lower center", ncol=2/3, edgecolor="#222222", fancybox=False, framealpha=0.95)`.
     * Bắt buộc gọi `fig.tight_layout()` trước, sau đó gọi `auto_space_title_legend(fig, ax, min_gap_pt=20.0)` từ `scripts.viz_legend_utils`.
     * Bắt buộc gọi `check_and_enforce_title_legend_clearance(fig, min_gap_pt=20.0, auto_correct=True)` và `assert_triple_buffer_geometry(fig)`.
     * Khoảng hở hình học giữa đáy tiêu đề (`title.y0`) và đỉnh viền Legend (`legend.y1`) BẮT BUỘC đạt $\delta_{\text{title-legend}} \ge 20.0\text{ pt}$ ($\approx 90\text{ px}$ ở $300\text{ DPI}$). Tuyệt đối cấm để tiêu đề chạm sát hoặc đè lên viền Legend.
     * CẤM TUYỆT ĐỐI tự ý viết hàm lưu ảnh riêng bằng `fig.savefig()` thô bỏ qua kiểm định Title-Legend; 100% đồ thị mô phỏng bắt buộc xuất qua `export_with_sidecar_manifest(fig, output_png_path, parameter_card=...)` hoặc có chốt kiểm tra nghiêm ngặt `check_and_enforce_title_legend_clearance`.

5. **Chốt chặn Bảng Danh pháp ISO 80000-2 & Bóc tách Dữ liệu Dict (Zero-Dict-Unpack-Drift Gate):**
   - Khi xây dựng bảng danh pháp cho phương trình cột trụ MALAE Cấp 3 từ `MicroPointTopic` hoặc `nomenclature_rows`:
     * Bắt buộc bóc tách an toàn hỗ trợ cả `dict` và `tuple/list`:
       ```python
       if isinstance(row, dict):
           name_val = row.get("name", "")
           sym_val = row.get("symbol", "")
           unit_val = row.get("unit", "")
           meaning_val = row.get("meaning", "")
       else:
           name_val, sym_val, unit_val, meaning_val = row
       ```
     * CẤM TUYỆT ĐỐI cú pháp unpack trực tiếp `name, sym, unit, meaning = row` khi `row` có thể là `dict`, vì Python sẽ gán tên keys thành chuỗi literal (`'name'`, `'symbol'`, `'unit'`, `'meaning'`) thay vì giá trị thực tế.
     * Cấm để xuất hiện các chuỗi placeholder thô `['name', 'symbol', 'unit', 'meaning']` trong bất kỳ ô dữ liệu nào của bảng danh pháp.

6. **Chốt chặn Toàn vẹn Khối Phương trình Cột trụ & Chống Cắt đôi Bảng (Atomic Table KeepTogether Gate):**
   - Bảng danh pháp và hộp phương trình cột trụ MALAE Cấp 3 BẮT BUỘC phải được đóng gói nguyên tử trong `KeepTogether([Spacer(1, 6), eq_box, Spacer(1, 6), nom_table, Spacer(1, 10)])` hoặc sử dụng hàm chuẩn hóa `build_pillar_equation_block()` từ `scripts/pillar_equation_utils.py`.
   - Bắt buộc thiết lập `nom_table = Table(..., repeatRows=0, splitByRow=0)` để triệt tiêu hoàn toàn hiện tượng lặp tiêu đề bảng hoặc bảng bị ngắt đôi giữa hai trang PDF liên tiếp.
   - Cấm sử dụng các cơ chế ngắt lỏng lẻo (`_PillarKeepTogether` tự ngắt khi `availHeight >= 210.0`) dẫn đến cắt xén bảng vật lý.

7. **Chốt chặn Thẻ Tham số Đồ thị Mô phỏng & Chống Rò rỉ N/A (Zero-NA-Badge Gate):**
   - 100% đồ thị mô phỏng xuất kèm tệp sidecar manifest `.manifest.json` bắt buộc phải có đầy đủ 3 trường hợp lệ trong `parameter_card`:
     * `material_system`: Hệ vật liệu cụ thể (không được để trống hoặc `'N/A'`).
     * `sweep_parameters`: Thông số quét giải tích cụ thể (không được để trống hoặc `'N/A'`).
     * `lab_metrics`: Hệ quả thực nghiệm / số liệu đo Lab cụ thể (không được để trống hoặc `'N/A'`).
   - CẤM TUYỆT ĐỐI xuất hiện chuỗi rò rỉ `↳ [Hệ vật liệu]: N/A` hoặc `[Thông số quét]: N/A` hoặc `[Hệ quả Lab]: N/A` trong chú giải đồ thị trên bản thảo chuyên khảo PDF.

8. **Chốt chặn Ký hiệu Hóa học & Vật lý Toàn văn (Zero-Plain-Symbol Gate):**
   - 100% công thức hóa học (`g-C3N4`, `Ag3VO4`, `WO3`, `TiO2`, `BiVO4`, `Fe2O3`, v.v.) trong mọi khối văn bản, tiêu đề H1/H2/H3, và các trường dữ liệu `cer_data` (CER Box) BẮT BUỘC phải dùng thẻ subscript `<sub>` (ví dụ: `g-C<sub>3</sub>N<sub>4</sub>`, `Ag<sub>3</sub>VO<sub>4</sub>`, `WO<sub>3</sub>`). CẤM TUYỆT ĐỐI chữ phẳng ASCII thô.
   - 100% ký hiệu đại lượng vật lý, dải năng lượng và thông số động học (`Eg`, `ECB`, `EVB`, `EF`, `Rct`, `kapp`, `h+`, `e-`, `k = ...`, `d = ...`, `Δ2θ`, `cotθ`) BẮT BUỘC phải in nghiêng qua thẻ `<i>...</i>` và bọc `<sub>`/`<sup>` (ví dụ: `<i>E<sub>g</sub></i>`, `<i>E</i><sub>CB</sub>`, `<i>E</i><sub>VB</sub>`, `<i>h</i><sup>+</sup>`, `<i>e</i><sup>−</sup>`, `<i>R</i><sub>ct</sub>`, `<i>k</i> = 0,0435 min<sup>−1</sup>`, `<i>d</i> = 0,384 nm`, `Δ2<i>θ</i>`).

9. **Chốt chặn Triệt tiêu Thẻ Lồng nhau (Zero-Nested-Tags Gate):**
   - CẤM TUYỆT ĐỐI lồng thẻ `<sup>` trong `<sup>` (`<sup>...<sup>...</sup>...</sup>`) hoặc `<sub>` trong `<sub>` (`<sub>...<sub>...</sub>...</sub>`). Trình phân tích XML của ReportLab không hỗ trợ đệ quy số mũ lồng nhau và sẽ làm vỡ ma trận toạ độ ký tự.
   - Đối với các biểu thức số mũ chứa số mũ (như độ âm điện Mulliken $(a+b+c)^{-1}$), BẮT BUỘC chuyển đổi sang dạng căn thức toán học tường minh: `căn bậc (<i>a</i> + <i>b</i> + <i>c</i>) của tích [...]` hoặc số mũ đơn tầng.

10. **Chốt chặn Ký tự Unicode Bản địa Trong Chuỗi Phản ứng & Bất đẳng thức (Native Unicode Symbols Gate):**
    - CẤM TUYỆT ĐỐI sử dụng các chuỗi thực thể HTML thô (`&rarr;`, `&larr;`, `&gt;`, `&lt;`) trong văn bản hoặc chuỗi phương trình phản ứng hóa học ReportLab.
    - BẮT BUỘC sử dụng trực tiếp ký tự Unicode bản địa (`→`, `←`, `>`, `<`, `≥`, `≤`, `—`, `–`, `−`, `·`, `×`) trong tệp mã nguồn lưu dưới định dạng chuẩn UTF-8.

11. **Chốt chặn Phân cấp Thị giác Khối 2 (Block 2 Toulmin Beat 1 Visual Hierarchy Gate):**
    - Trong mỗi Luận điểm Vi mô (MPT), ngay sau tiêu đề H3 Khối 2: Truy vết Cơ chế Vi mô, Giải phẫu Toán – Lý MALAE 3 Cấp và Dẫn xuất, phần tử nội dung ĐẦU TIÊN bắt buộc phải là lệnh story.append(he.embed_figure_with_caption(...)) (cho phép tối đa 1 phần tử Spacer(1, ...) trước hình).
    - CẤM TUYỆT ĐỐI đặt văn bản giải thích, Bộ tứ câu hỏi kỹ sư trưởng, Chuỗi biến đổi nhân quả hoặc các phương trình cột trụ/dẫn xuất trung gian TRƯỚC hình ảnh. Sinh viên và kỹ sư phải quan sát dữ liệu thực chứng (Nhịp 1 Toulmin) trước khi tiếp nhận phân tích cơ chế và công thức.

12. **Chốt chặn Phân tách Panel Độc lập 1:1 (D-SAFE Sub-panel 1:1 Isolation Gate):**
    - Áp dụng nghiêm ngặt Tầng 5 Thuật toán 3 (RVAE Engine): Mọi hình ảnh composite có nhiều panel chữ cái (a), (b), (c), ... bắt buộc phải được cắt rời thành từng tệp ảnh đơn lẻ ([Goc]_Muc_X.Y_Hinh_Za_[Ten].png).
    - Mỗi MPT sở hữu duy nhất 1 tệp hình ảnh độc lập tương ứng với luận điểm phân tích. CẤM TUYỆT ĐỐI hiện tượng 'mồ côi panel' (panel xuất hiện trong ảnh tổng nhưng không có MPT phân tích) hoặc dồn toàn bộ ảnh composite vào một mục rồi để trắng hình các mục kế tiếp.

13. **Chốt chặn Kiểm toán AST Flowables Thực chất (Zero-Hardcode Audit Gate):**
    - 100% các giá trị trong từ điển checklist_status của audit_monograph_*.py bắt buộc phải là biểu thức logic kiểm tra thuộc tính thực của tài liệu (AST flowables, số trang PyMuPDF, mã băm SHA-256 tệp ảnh và sidecar, kết quả sympy.simplify == 0).
    - CẤM TUYỆT ĐỐI gán trực tiếp giá trị True cố định.

14. **Chốt chặn Khóa cứng Danh pháp Tiêu đề Chuẩn mực (Strict Canonical Headings Invariant Gate):**
    - BẮT BUỘC 100% chuyên khảo trong mọi chương và môn học phải tuân thủ chuẩn xác 100% hệ thống tiêu đề:
      * **Khối 1:** Khối 1: Định vị Mục đích luận Hệ thống và Mỏ neo Không gian 3D (hoặc Khối 1: Định vị Mục đích luận Hệ thống (SBF) & Mỏ neo Không gian 3D)
      * **Khối 2:** Khối 2: Truy vết Cơ chế Vi mô, Giải phẫu Toán – Lý MALAE 3 Cấp và Dẫn xuất
      * **Khối 3:** Khối 3: Kiểm toán Biên, Rủi ro Kỹ thuật và Thử thách Chẩn đoán R&D
      * **Tiêu đề Tổng kết:** Tổng kết Phân mục X.Y và Mỏ neo Điều hướng Chuyển tiếp
    - CẤM TUYỆT ĐỐI tái sinh các danh pháp tiêu đề di sản:
      * ❌ CẤM Khởi Nguyên & Nỗi Đau Công Nghệ
      * ❌ CẤM Mỏ Neo Thị Giác & Mô Hình Hóa
      * ❌ CẤM Góc Nhìn Đối Trọng & Thử Thách Chẩn Đoán CER
      * ❌ CẤM Góc Nhìn Đối Trọng & Open CER Box
      * ❌ CẤM Tổng kết Chuyên khảo & Cầu nối Dẫn nhập sang Mục...
    - CẤM TUYỆT ĐỐI các nhãn con di sản gây rác thị giác:
      * ❌ CẤM Nền tảng Vật lý Đại cương Quen thuộc
      * ❌ CẤM Ẩn dụ Cơ học Vĩ mô 3 Nhịp Đời thực
      * ❌ CẤM ↳ Dây cáp Chuyển giao Nhận thức
      * ❌ CẤM Bộ Tứ Câu Hỏi Toàn Cục Kỹ Sư Trưởng (Bắt buộc dùng Giải phẫu Động lực học & Tham số Vận hành (Bộ Tứ Câu Hỏi Kỹ Sư Trưởng))
      * ❌ CẤM Phân nhánh Đa hình Khối 2
      * ❌ CẤM Kịch bản Quét Tham số Kiểm chứng Tính Phụ thuộc Hàm

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

# Mẫu 3: Cấu trúc 3 tầng tự chứa Title → External Top Banner Legend → Axes (Khóa khoảng thở >= 20.0 pt)
ax.set_title(r"$\textbf{Tiêu đề đồ thị chuẩn}", pad=12)
ax.legend(bbox_to_anchor=(0.5, 1.02), loc="lower center", ncol=2, edgecolor="#222222", fancybox=False, framealpha=0.95, fontsize=9.0)
fig.tight_layout()
auto_space_title_legend(fig, ax, min_gap_pt=20.0)
check_and_enforce_title_legend_clearance(fig, min_gap_pt=20.0, auto_correct=True)
export_with_sidecar_manifest(fig, out_path, parameter_card=param_card)

# Mẫu 4: Xây dựng khối phương trình cột trụ nguyên tử và an toàn kiểu dữ liệu (Atomic Pillar Block)
from scripts.pillar_equation_utils import build_pillar_equation_block
pillar_flowable = build_pillar_equation_block(
    latex_eq=r"\eta_{\text{diff}} = \frac{q}{h \cdot \nu} \cdot \frac{dP}{dI}",
    nom_data=[
        {"name": "Hiệu suất lượng tử vi phân", "symbol": "<i>η</i><sub>diff</sub>", "unit": "–", "meaning": "Xác suất photon phát xạ kích thích trên mỗi electron tiêm"},
        {"name": "Hằng số Planck", "symbol": "<i>h</i>", "unit": "J·s", "meaning": "Lượng tử tác dụng cơ bản"},
        {"name": "Tần số quang học", "symbol": "<i>ν</i>", "unit": "Hz", "meaning": "Tần số ánh sáng phát xạ"},
        {"name": "Độ dốc công suất vi phân", "symbol": "<i>dP</i>/<i>dI</i>", "unit": "W·A⁻¹", "meaning": "Độ dốc đường đặc tuyến P-I trên ngưỡng"}
    ],
    styles=styles
)
```

---

## IV. RÀNG BUỘC BẤT BIẾN TỐI CAO

> [!CAUTION]
> Quy tắc này được sinh ra nhằm **thắt chặt thêm các điều kiện kiểm thử và phòng ngừa lỗi** trong dây chuyền tự trị.  
> **TUYỆT ĐỐI KHÔNG ĐƯỢC PHÉP** làm thay đổi, cắt xén, nén bớt, làm suy hao (drift) hay thay đổi logic vận hành của bất kỳ điều khoản nào trong 13 thuật toán cốt lõi tại Điều khoản IX `AGENTS.md`.
