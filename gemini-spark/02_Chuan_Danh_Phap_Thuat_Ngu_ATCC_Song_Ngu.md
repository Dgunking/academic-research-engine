# CHUẨN DANH PHÁP THUẬT NGỮ SONG NGỮ ATCC (ANH - VIỆT)
## ACADEMIC BILINGUAL TERMINOLOGY MATRIX (NOTEBOOKLM SYNCHRONIZED)

> **Mục đích:** Khóa cứng chuẩn danh pháp học thuật cho Gemini Spark đối soát trước mọi lượt trao đổi học thuật cùng Lead Researcher ().  
> **Cơ sở pháp lý & Chuẩn mực:** Nghị định 30/2020/NĐ-CP về công tác văn thư, Định dạng số APA 7, Luật Đo lường 04/2011/QH13, Hệ chuẩn ISO 80000-2.  
> **Đồng bộ:** Khớp 100% với Sổ tay Thuật ngữ `Academic Bilingual Terminology Matrix` trên Google NotebookLM.

---

## I. NGUYÊN TẮC BẤT BIẾN VỀ DANH PHÁP VÀ ĐỊNH DẠNG VĂN BẢN

1. **Định dạng Song ngữ Bắt buộc:**  
   Mọi thuật ngữ chuyên ngành bắt buộc xuất hiện dưới dạng `thuật ngữ tiếng Việt chuẩn (english term)` ở lần đầu tiên đề cập và giữ nhất quán ngữ nghĩa xuyên suốt cuộc đối thoại.
2. **Quy tắc Viết hoa theo Nghị định 30/2020/NĐ-CP (Sentence Case):**  
   - Tuyệt đối **CẤM viết hoa danh từ chung giữa câu** (viết *"tiếp giáp dị chất"*, *"dải dẫn"*, *"dải hóa trị"*, *"mức Fermi"*; cấm viết hoa tùy tiện *"Tiếp Giáp Dị Chất"*, *"Dải Dẫn"*, *"Vùng Cấm"*).
   - Chỉ viết hoa chữ cái đầu câu hoặc danh từ riêng chỉ tên nhà khoa học (Fermi, Bragg, Fabry-Perot, Anderson, Varshni, Coulomb, Maxwell).
3. **Quy tắc Viết số & Khoảng số theo APA 7:**  
   - Dùng dấu phẩy `,` cho phần thập phân trong văn bản tiếng Việt: `1,424 eV`, `0,02585 eV`, `0,65`. (Trong khối mã Python sandbox chạy thực thi mới dùng dấu chấm `.`).
   - Dùng dấu gạch ngang en-dash `–` (không dùng gạch nối ngắn `-`) cho khoảng giá trị: `5–10 nm`, `300–400 K`.
4. **Quy tắc Đơn vị SI theo Luật Đo lường 04/2011/QH13:**  
   - Bắt buộc đặt **đúng 1 dấu cách** giữa giá trị số và đơn vị SI: `300 K` (cấm `300K`), `10 nm` (cấm `10nm`), `1,55 μm` (cấm `1.55um`), `50 mA` (cấm `50mA`).
   - Riêng dấu phần trăm `%` và độ góc `°` được viết liền: `100%`, `45°`.
5. **Danh từ Mượn Nguyên ngữ (Loan Nouns Whitelist):**  
   - Các thuật ngữ quốc tế mượn nguyên ngữ được giữ nguyên dạng gốc, **cấm in nghiêng và cấm dịch gượng gạo**:  
     `laser`, `diode`, `electron`, `photon`, `phonon`, `exciton`, `plasmon`, `polariton`, `plasma`, `vector`, `tensor`.
6. **Quy trình Xử lý Thuật ngữ Mới Phát sinh (Uncataloged Terms):**  
   - Khi gặp một khái niệm mới chưa có trong ma trận: Tuyệt đối **CẤM tự ý dịch bừa bãi**.
   - Bắt buộc giữ nguyên tiếng Anh gốc: `english term`.
   - Đề xuất phương án dịch từ nguyên lý đầu và thông báo cho Researcher:  
     `[Thuật ngữ mới: english term -> Đề xuất tiếng Việt: "thuật ngữ" (Cơ chế: ...) để thống nhất cập nhật vào NotebookLM]`.

---

## II. MA TRẬN ĐỐI CHIẾU THUẬT NGỮ CỐT LÕI (5 NGÀNH MŨI NHỌN)

### 1. Vật lý Bán dẫn & Dải Năng lượng (Semiconductor Physics & Band Structure)

| Thuật ngữ tiếng Việt chuẩn | English Term | Ký hiệu / Quy ước | Bản chất vi mô & Định nghĩa vật lý |
| :--- | :--- | :---: | :--- |
| dải dẫn / vùng dẫn | conduction band | $E_c$ | Dải năng lượng chứa electron tự do tham gia dẫn điện |
| dải hóa trị / vùng hóa trị | valence band | $E_v$ | Dải năng lượng điền đầy electron liên kết, sinh lỗ trống khi electron nhảy lên dải dẫn |
| vùng cấm | energy bandgap | $E_g$ | Khoảng cách năng lượng giữa đáy dải dẫn và đỉnh dải hóa trị: $E_g = E_c - E_v$ |
| vùng cấm trực tiếp | direct bandgap | Direct $E_g$ | Đáy dải dẫn và đỉnh dải hóa trị cùng vector sóng $\mathbf{k} = 0$ ($\Gamma$), tái hợp trực tiếp |
| vùng cấm gián tiếp | indirect bandgap | Indirect $E_g$ | Đáy dải dẫn lệch vector sóng so với đỉnh dải hóa trị, cần phonon hỗ trợ bảo toàn xung lượng |
| mức Fermi | Fermi level | $E_F$ | Mức năng lượng có xác suất chiếm chỗ của electron bằng $0{,}5$ ở cân bằng nhiệt |
| chuẩn mức Fermi | quasi-Fermi level | $E_{Fc}, E_{Fv}$ | Thế hóa học riêng biệt của electron và lỗ trống khi bị kích thích phi cân bằng |
| tiếp giáp dị chất | heterojunction | Heterojunction | Mặt tiếp xúc giữa hai vật liệu bán dẫn có vùng cấm hoặc ái lực electron khác nhau |
| bước nhảy dải dẫn | conduction band offset | $\Delta E_c$ | Độ gián đoạn năng lượng tại đáy dải dẫn ở mặt phân giới tiếp giáp dị chất |
| bước nhảy dải hóa trị | valence band offset | $\Delta E_v$ | Độ gián đoạn năng lượng tại đỉnh dải hóa trị ở mặt phân giới tiếp giáp dị chất |
| ái lực electron | electron affinity | $\chi$ | Năng lượng cần thiết để đưa electron từ đáy dải dẫn ra mức chân không $E_0$ |
| công thoát | work function | $\Phi$ | Khoảng cách năng lượng từ mức Fermi $E_F$ đến mức chân không $E_0$ |
| mật độ trạng thái | density of states | DOS, $g(E)$ | Số lượng trạng thái lượng tử khả dụng trên một đơn vị năng lượng và thể tích |
| khối lượng hiệu dụng | effective mass | $m_e^*, m_h^*$ | Nghịch đảo độ cong dải năng lượng: $m^* = \hbar^2 / (\frac{d^2E}{dk^2})$ |
| độ linh động hạt tải | carrier mobility | $\mu_n, \mu_p$ | Tỉ số giữa vận tốc trôi trung bình của hạt tải và cường độ điện trường tác dụng |
| phân bố Fermi-Dirac | Fermi-Dirac distribution | $f(E)$ | Xác suất một trạng thái năng lượng $E$ bị chiếm giữ bởi fermion ở nhiệt độ $T$ |

### 2. Linh kiện Quang điện tử & Laser Diode (Optoelectronics & Diode Lasers)

| Thuật ngữ tiếng Việt chuẩn | English Term | Ký hiệu / Quy ước | Bản chất vi mô & Định nghĩa vật lý |
| :--- | :--- | :---: | :--- |
| nghịch đảo độ tích lũy | population inversion | $N_2 > N_1$ | Trạng thái mật độ hạt tải ở dải dẫn vượt trội so với dải hóa trị ($E_{Fc} - E_{Fv} > h\nu$) |
| phát xạ tự phát | spontaneous emission | $R_{\text{sp}}$ | Electron tái hợp ngẫu nhiên không có pha kết hợp, phát ra photon ngẫu nhiên |
| phát xạ kích thích | stimulated emission | $R_{\text{st}}$ | Photon tới kích thích electron tái hợp, phát ra photon thứ hai đồng pha, cùng tần số |
| tái hợp không bức xạ | nonradiative recombination | $R_{\text{nr}}$ | Electron tái hợp với lỗ trống truyền năng lượng cho phonon (nhiệt) hoặc hạt tải khác |
| tái hợp Auger | Auger recombination | $C n^2 p$ | Tái hợp không bức xạ truyền năng lượng cho electron/lỗ trống thứ ba lên mức cao |
| dòng ngưỡng | threshold current | $I_{\text{th}}$ | Dòng điện bơm tối thiểu để độ lợi quang học bù trừ hoàn toàn tổng suy hao hốc cộng hưởng |
| hiệu suất lượng tử vi phân | differential quantum efficiency | $\eta_d$ | Tỉ lệ giữa số photon phát xạ tăng thêm và số hạt tải bơm vào khi dòng vượt ngưỡng |
| hiệu suất độ dốc | slope efficiency | $SE = dP/dI$ | Độ dốc đặc tuyến công suất quang theo dòng bơm trên ngưỡng $I > I_{\text{th}}$ |
| hệ số giam hãm trường quang | optical confinement factor | $\Gamma$ | Tỉ số năng lượng mode quang học chồng lấn với vùng hoạt tính (active region) |
| hốc cộng hưởng Fabry-Perot | Fabry-Perot cavity | FP cavity | Cấu trúc cộng hưởng quang hình thành từ hai gương phẳng phản xạ song song đối diện |
| gương phản xạ Bragg phân tán | distributed Bragg reflector | DBR | Cấu trúc đa lớp chiết suất xen kẽ $\lambda/4$ tạo độ phản xạ cao qua giao thoa tăng cường |
| laser phản hồi phân tán | distributed feedback laser | DFB laser | Laser có cách mạng Bragg tích hợp dọc toàn bộ vùng hoạt tính để đơn mode phổ |
| thời gian sống hạt tải | carrier lifetime | $\tau, \tau_c$ | Thời gian tồn tại trung bình của hạt tải dẫn trước khi bị tái hợp |
| thời gian sống photon | photon lifetime | $\tau_p$ | Thời gian trung bình photon lưu trú trong hốc cộng hưởng trước khi thoát ra hoặc bị hấp thụ |
| điện trở vi phân tiếp xúc | contact resistance | $R_s$ | Điện trở ký sinh tại lớp kim loại hóa bán dẫn gây sụt áp và phát nhiệt Joule |

### 3. Mạch Tích hợp Quang tử (PIC) & Ống Dẫn Sóng (Photonics & Waveguides)

| Thuật ngữ tiếng Việt chuẩn | English Term | Ký hiệu / Quy ước | Bản chất vi mô & Định nghĩa vật lý |
| :--- | :--- | :---: | :--- |
| ống dẫn sóng quang | optical waveguide | Waveguide | Cấu trúc điện môi dẫn truyền ánh sáng bằng hiện tượng phản xạ toàn phần nội |
| chiết suất hiệu dụng | effective refractive index | $n_{\text{eff}}$ | Tỉ số giữa hằng số truyền sóng $\beta$ trong ống dẫn sóng và số sóng chân không $k_0$ |
| hằng số truyền sóng | propagation constant | $\beta$ | Tốc độ biến thiên pha của sóng ánh sáng truyền dọc theo trục ống dẫn sóng |
| mode điện ngang | transverse electric mode | TE mode | Mode sóng ánh sáng không có thành phần điện trường dọc trục truyền ($E_z = 0$) |
| mode từ ngang | transverse magnetic mode | TM mode | Mode sóng ánh sáng không có thành phần từ trường dọc trục truyền ($H_z = 0$) |
| sóng tắt dần | evanescent wave | Evanescent wave | Sóng điện từ suy giảm hàm mũ theo phương vuông góc với mặt phân giới phản xạ toàn phần |
| bộ ghép định hướng | directional coupler | Coupler | Cấu trúc hai ống dẫn sóng đặt sát nhau để trao đổi năng lượng sóng qua trường tắt dần |
| giao thoa kế Mach-Zehnder | Mach-Zehnder interferometer | MZI | Cấu trúc tách chùm và tái kết hợp để điều chế biên độ quang thông qua điều biến pha |
| bộ ghép cách mạng | grating coupler | Grating coupler | Cấu trúc cách mạng khắc trên bề mặt để ghép ánh sáng từ sợi quang vào chip quang tử |

### 4. Màng Mỏng Quang Học & Tán Sắc (Optical Thin Films & Dispersion)

| Thuật ngữ tiếng Việt chuẩn | English Term | Ký hiệu / Quy ước | Bản chất vi mô & Định nghĩa vật lý |
| :--- | :--- | :---: | :--- |
| màng chống phản xạ | antireflection coating | AR coating | Lớp màng mỏng chiết suất $n = \sqrt{n_1 n_2}$ dày $\lambda/4$ triệt tiêu phản xạ bằng giao thoa |
| màng phản xạ cao | high-reflection coating | HR coating | Cấu trúc xếp chồng các lớp $\lambda/4$ chiết suất cao/thấp xen kẽ để đạt độ phản xạ $\approx 100\%$ |
| ma trận truyền sóng | transfer matrix method | TMM | Phương pháp đại số ma trận $2 \times 2$ tính toán hệ số phản xạ và truyền qua của màng đa lớp |
| tán sắc vận tốc nhóm | group velocity dispersion | GVD | Sự phụ thuộc của vận tốc nhóm $v_g$ vào tần số quang làm dãn rộng xung ánh sáng |
| hệ số phẩm chất hốc | quality factor | $Q$ | Thước đo tỉ số giữa năng lượng dự trữ trong hốc cộng hưởng và năng lượng tiêu hao mỗi chu kỳ |

### 5. Cảm biến Quang & Công nghệ Nano (Optical Sensors & Nanotechnology)

| Thuật ngữ tiếng Việt chuẩn | English Term | Ký hiệu / Quy ước | Bản chất vi mô & Định nghĩa vật lý |
| :--- | :--- | :---: | :--- |
| giếng lượng tử | quantum well | QW | Cấu trúc bán dẫn mỏng hơn bước sóng de Broglie làm giam hãm chuyển động hạt tải 1 chiều |
| dây lượng tử | quantum wire | QWR | Cấu trúc nano giam hãm hạt tải theo 2 chiều không gian, hạt tải chỉ tự do 1 chiều |
| chấm lượng tử | quantum dot | QD | Cấu trúc nano giam hãm hạt tải theo cả 3 chiều không gian (nguyên tử nhân tạo) |
| cộng hưởng plasmon bề mặt | surface plasmon resonance | SPR | Hiện tượng dao động tập thể của electron tự do tại mặt phân giới kim loại/điện môi |
| quang huỳnh quang | photoluminescence | PL | Sự phát quang của vật liệu sau khi hấp thụ photon kích thích từ nguồn quang học |
| điện phát quang | electroluminescence | EL | Sự phát quang của vật liệu khi có dòng điện hoặc điện trường ngoài tác dụng |
| phổ trở kháng điện hóa | electrochemical impedance spectroscopy | EIS | Phép đo đáp ứng trở kháng của hệ điện hóa/cảm biến dưới kích thích điện áp xoay chiều |
| dị liên kết kép Z-scheme | double Z-scheme heterojunction | Double Z-scheme | Cấu trúc liên kết dị chất 3 thành phần tái tạo cơ chế quang hợp tự nhiên tăng truyền điện tích |
| thế đáy dải dẫn | conduction band potential | $E_{\text{CB}}$ | Thế năng lượng của đáy dải dẫn đo theo thang điện cực hydro chuẩn (NHE) |
| thế đỉnh dải hóa trị | valence band potential | $E_{\text{VB}}$ | Thế năng lượng của đỉnh dải hóa trị đo theo thang điện cực hydro chuẩn (NHE) |
