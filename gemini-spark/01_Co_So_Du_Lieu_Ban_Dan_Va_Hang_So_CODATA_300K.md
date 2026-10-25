# CƠ SỞ DỮ LIỆU VẬT LIỆU BÁN DẪN & HẰNG SỐ VẬT LÝ CODATA (300 K)

> **Mục đích:** Tài liệu tri thức nền tảng (Ground Truth Knowledge) cho Gemini Spark tra cứu đối soát, tính toán giải tích và giải phẫu mô hình vật lý cùng Lead Researcher ().  
> **Quy chuẩn:** CODATA 2022, thông số thực nghiệm chuẩn 300 K, chuẩn viết số APA 7 (dấu phẩy thập phân `,`), đơn vị SI Luật Đo lường 04.

---

## I. BẢNG HẰNG SỐ VẬT LÝ CĂN BẢN (CODATA 2022)

| Đại lượng vật lý | Ký hiệu | Giá trị giải tích chuẩn | Đơn vị SI | Vai trò vi mô |
| :--- | :---: | :---: | :--- | :--- |
| Điện tích nguyên tố | $q$ | $1{,}602176634 \times 10^{-19}$ | $\text{C}$ | Điện tích cơ bản của hạt mang điện (electron, lỗ trống) |
| Hằng số Planck rút gọn | $\hbar$ | $1{,}054571817 \times 10^{-34}$ | $\text{J}\cdot\text{s}$ | Lượng tử tác dụng, chuẩn hóa xung lượng $\mathbf{p} = \hbar \mathbf{k}$ |
| Hằng số Planck | $h$ | $6{,}62607015 \times 10^{-34}$ | $\text{J}\cdot\text{s}$ | Năng lượng photon $E = h\nu = \frac{hc}{\lambda}$ |
| Khối lượng nghỉ electron | $m_0$ | $9{,}1093837 \times 10^{-31}$ | $\text{kg}$ | Khối lượng electron tự do trong chân không |
| Hằng số Boltzmann | $k_B$ | $1{,}380649 \times 10^{-23}$ | $\text{J}/\text{K}$ | Thang đo nhiệt động học vi mô |
| Hằng số Boltzmann (năng lượng) | $k_B$ | $8{,}617333262 \times 10^{-5}$ | $\text{eV}/\text{K}$ | Phân bố Fermi-Dirac và thế nhiệt động |
| Độ điện thẩm chân không | $\varepsilon_0$ | $8{,}8541878128 \times 10^{-12}$ | $\text{F}/\text{m}$ | Hằng số điện trường tĩnh |
| Độ từ thẩm chân không | $\mu_0$ | $1{,}25663706212 \times 10^{-6}$ | $\text{H}/\text{m}$ | Hằng số từ trường tĩnh |
| Vận tốc ánh sáng chân không | $c$ | $2{,}99792458 \times 10^8$ | $\text{m}/\text{s}$ | Tốc độ lan truyền sóng điện từ trong chân không |
| Tích số $hc$ thực hành | $hc$ | $1{,}239841984$ | $\text{eV}\cdot\mu\text{m}$ | Chuyển đổi năng lượng sang bước sóng $\lambda(\mu\text{m}) = \frac{1{,}2398}{E(\text{eV})}$ |
| Năng lượng nhiệt ở 300 K | $k_B T$ | $0{,}02585$ | $\text{eV}$ ($25{,}85\text{ meV}$) | Năng lượng kích thích nhiệt ở nhiệt độ phòng |

---

## II. THÔNG SỐ VẬT LIỆU BÁN DẪN Ở NHIỆT ĐỘ PHÒNG (300 K)

| Bán dẫn | Loại vùng cấm | $E_g\text{ (eV)}$ | Bước sóng $\lambda_g\text{ (}\mu\text{m)}$ | Khối lượng hiệu dụng electron $m_e^*/m_0$ | Khối lượng lỗ trống nặng $m_{hh}^*/m_0$ | Độ điện thẩm $\varepsilon_r$ | Chiết suất $n_r$ | Độ linh động electron $\mu_n\text{ (cm}^2/\text{V}\cdot\text{s)}$ |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **GaAs** | Trực tiếp | $1{,}424$ | $0{,}871$ | $0{,}067$ | $0{,}450$ | $12{,}9$ | $3{,}65$ | $8500$ |
| **InP** | Trực tiếp | $1{,}344$ | $0{,}923$ | $0{,}077$ | $0{,}600$ | $12{,}5$ | $3{,}17$ | $5400$ |
| **GaN** (Wurtzite) | Trực tiếp | $3{,}420$ | $0{,}363$ | $0{,}200$ | $0{,}800$ | $8{,}9$ | $2{,}40$ | $1000$ |
| **InAs** | Trực tiếp | $0{,}354$ | $3{,}502$ | $0{,}023$ | $0{,}410$ | $15{,}1$ | $3{,}51$ | $33000$ |
| **InSb** | Trực tiếp | $0{,}180$ | $6{,}888$ | $0{,}014$ | $0{,}430$ | $16{,}8$ | $3{,}96$ | $78000$ |
| **AlAs** | Gián tiếp | $2{,}168$ | $0{,}572$ | $0{,}150$ | $0{,}500$ | $10{,}1$ | $3{,}00$ | $1000$ |
| **Si** | Gián tiếp | $1{,}120$ | $1{,}107$ | $1{,}080$ | $0{,}560$ | $11{,}7$ | $3{,}42$ | $1450$ |
| **Ge** | Gián tiếp | $0{,}660$ | $1{,}879$ | $0{,}550$ | $0{,}370$ | $16{,}0$ | $4{,}00$ | $3900$ |

---

## III. MÔ HÌNH HỢP KIM BA NGUYÊN TỬ & BỐN NGUYÊN TỬ

### 1. Hợp kim $\text{Al}_x\text{Ga}_{1-x}\text{As}$ (300 K):
- Vùng cấm trực tiếp (điểm $\Gamma$, ứng với $x \le 0{,}45$):
  $$E_g^\Gamma(x) = 1{,}424 + 1{,}247x\text{ [eV]}$$
- Vùng cấm gián tiếp (điểm $X$, ứng với $x > 0{,}45$):
  $$E_g^X(x) = 1{,}900 + 0{,}125x + 0{,}143x^2\text{ [eV]}$$
- Bước nhảy dải năng lượng tiếp giáp dị chất $\text{GaAs} / \text{Al}_x\text{Ga}_{1-x}\text{As}$ ($x \le 0{,}45$):
  $$\Delta E_c \approx 0{,}65 \times \Delta E_g \quad \text{và} \quad \Delta E_v \approx 0{,}35 \times \Delta E_g$$
  với $\Delta E_g = 1{,}247x\text{ [eV]}$.

### 2. Hợp kim $\text{In}_{1-x}\text{Ga}_x\text{As}_y\text{P}_{1-y}$ phối mạng trên đế $\text{InP}$ (300 K):
- Điều kiện phối mạng: $x \approx \frac{0{,}47y}{1 + 0{,}03y} \approx 0{,}47y$.
- Năng lượng vùng cấm theo $y$ ($0 \le y \le 1$):
  $$E_g(y) = 1{,}344 - 0{,}778y + 0{,}149y^2\text{ [eV]}$$
- Bước sóng phát xạ tương ứng: $\lambda = 0{,}92\,\mu\text{m} \to 1{,}65\,\mu\text{m}$ (phủ cửa sổ viễn thông $1{,}31\,\mu\text{m}$ và $1{,}55\,\mu\text{m}$).

---

## IV. PHỤ THUỘC NHIỆT ĐỘ CỦA VÙNG CẤM (MÔ HÌNH VARSHNI)

$$E_g(T) = E_g(0) - \frac{\alpha T^2}{T + \beta}$$

| Vật liệu | $E_g(0)\text{ [eV]}$ | $\alpha\text{ [eV/K]}$ | $\beta\text{ [K]}$ | $E_g(300\text{ K})\text{ [eV]}$ |
| :--- | :---: | :---: | :---: | :---: |
| **GaAs** | $1{,}519$ | $5{,}405 \times 10^{-4}$ | $204$ | $1{,}424$ |
| **InP** | $1{,}424$ | $4{,}900 \times 10^{-4}$ | $327$ | $1{,}344$ |
| **GaN** | $3{,}507$ | $9{,}090 \times 10^{-4}$ | $830$ | $3{,}420$ |
| **Si** | $1{,}170$ | $4{,}730 \times 10^{-4}$ | $636$ | $1{,}120$ |
| **Ge** | $0{,}744$ | $4{,}774 \times 10^{-4}$ | $235$ | $0{,}660$ |

---

## V. NGUYÊN LÝ DẢI NĂNG LƯỢNG TIẾP GIÁP DỊ CHẤT (HETEROJUNCTIONS)

### 1. Quy tắc Anderson (Electron Affinity Rule):
- Độ gián đoạn dải dẫn:
  $$\Delta E_c = \Delta \chi = \chi_1 - \chi_2$$
- Độ gián đoạn dải hóa trị:
  $$\Delta E_v = \Delta E_g - \Delta E_c = (E_{g2} - E_{g1}) - (\chi_1 - \chi_2)$$

### 2. Phân loại cấu trúc tiếp giáp dị chất:
- **Loại I (Straddling gap):** Dải hẹp nằm lọt hoàn toàn trong dải rộng ($\Delta E_c > 0, \Delta E_v > 0$). Ví dụ: $\text{GaAs} / \text{AlGaAs}$, $\text{InGaAs} / \text{InP}$. Tác dụng: giam hãm đồng thời cả electron và lỗ trống trong cùng một lớp không gian $\to$ lý tưởng cho vùng hoạt tính laser diode và LED.
- **Loại II (Staggered gap):** Đáy dải dẫn và đỉnh dải hóa trị đều dịch cùng chiều ($\Delta E_c > 0, \Delta E_v < 0$). Ví dụ: $\text{GaAsSb} / \text{InP}$. Tác dụng: tách hạt tải, electron và lỗ trống nằm ở hai lớp khác nhau $\to$ ứng dụng pin quang điện và laser hồng ngoại tầng.
- **Loại III (Broken gap):** Đáy dải dẫn bán dẫn này nằm sâu dưới đỉnh dải hóa trị bán dẫn kia. Ví dụ: $\text{InAs} / \text{GaSb}$. Tác dụng: đường hầm trực tiếp liên dải $\to$ transistor chui hầm (TFET).
