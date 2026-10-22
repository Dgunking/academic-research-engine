# **Giải Pháp Khắc Phục Xung Đột Hiển Thị Điểm Ảnh Và Đè Chú Giải Khi Vẽ Nhiều Đồ Thị Python Bằng Google Antigravity**

Hiện tượng tác nhân AI (AI Agent) trong Google Antigravity vẽ chính xác tuyệt đối một đồ thị đơn lẻ nhưng lại tạo ra các chú giải (annotations, legends, text labels) đè lên nhau và cắt ngang đường biểu diễn khi xử lý hàng loạt đồ thị trong cùng một bài giảng là một vấn đề kinh điển tại giao điểm giữa **kiến trúc kết xuất đồ họa hai pha của Matplotlib** và **cơ chế phân bổ sự chú ý của mô hình ngôn ngữ lớn (LLM)**. Lời giải thích mà Antigravity đưa ra—rằng tính toán toán học của Python không sai nhưng xảy ra xung đột với thuật toán hiển thị điểm ảnh và lỗi thuộc về AI—phản ánh đúng bản chất kỹ thuật của hệ thống kết xuất đồ họa.  
Báo cáo này phân tích chi tiết cơ chế vật lý đứng sau lời giải thích của Antigravity, lý giải nguyên nhân sự cố chỉ bùng phát khi mở rộng quy mô từ một hình lên nhiều hình, đồng thời cung cấp bộ giải pháp toàn diện trên ba tầng: **thuật toán chống va chạm điểm ảnh trong mã nguồn Python**, **cấu hình kiến trúc điều phối đặc thù của Antigravity (Rules, Skills, Subagents)**, và **quy trình tự kiểm tra thị giác đa phương thức (Multimodal Visual Feedback)**.

## **1\. Giải Mã Kỹ Thuật: Tại Sao Tính Toán Python Đúng Nhưng Hiển Thị Điểm Ảnh Lại Xung Đột?**

Khi mô phỏng một bài toán khoa học hoặc kỹ thuật bằng Python (sử dụng NumPy, SciPy và Matplotlib), quá trình tạo ra một đồ thị hoàn chỉnh diễn ra trên hai hệ quy chiếu không gian hoàn toàn tách biệt: **Hệ tọa độ dữ liệu (Data Coordinates)** và **Hệ tọa độ hiển thị điểm ảnh (Display / Pixel Coordinates)**. Sự lệch pha giữa hai hệ tọa độ này chính là nguyên nhân cốt lõi khiến tác nhân AI mắc lỗi khi sinh mã nguồn tĩnh.

### **Sự đứt gãy giữa không gian toán học và không gian điểm ảnh**

Trong pha tính toán, các mảng dữ liệu (x, y), các điểm cực trị, giao điểm hoặc vị trí pha được Python tính toán trong không gian toán học thuần túy (Data Coordinates). Ở bước này, một điểm dữ liệu (x\_0, y\_0) có kích thước hình học bằng không. Khi tác nhân AI đặt một chú thích tại tọa độ đó bằng hàm ax.text() hoặc ax.annotate(), vị trí neo (xy) được xác định bằng đơn vị dữ liệu, nhưng bản thân chuỗi văn bản hiển thị lại chiếm một diện tích vật lý tính bằng **điểm ảnh (pixels)** hoặc **điểm in ấn (typographic points, với 1\\text{ pt} \= \\frac{1}{72}\\text{ inch})** trên bề mặt hiển thị.  
Điểm mấu chốt trong kiến trúc của Matplotlib là các đối tượng văn bản (Text và Annotation Artists) **không hề biết kích thước khung bao điểm ảnh (bounding box) của chính chúng tại thời điểm dòng lệnh Python được viết ra**. Phương thức Artist.get\_window\_extent() dùng để đo tọa độ khung bao bằng đơn vị pixel chỉ trả về kết quả chính xác sau khi bộ kết xuất đồ họa (Renderer, thường là Agg hoặc Cairo) đã thực sự vẽ (draw) phông chữ, cỡ chữ và mật độ điểm ảnh (DPI) lên bề mặt khung hình (Canvas) ít nhất một lần.

| Thuộc tính kỹ thuật | Hệ tọa độ dữ liệu (Data Coordinates) | Hệ tọa độ điểm ảnh (Display / Pixel Coordinates) | Hệ quả đối với AI Agent khi sinh mã tĩnh |
| :---- | :---- | :---- | :---- |
| **Đơn vị đo lường** | Giá trị biến số toán học (x, y) của bài toán | Điểm ảnh vật lý (\\text{px}) hoặc điểm in ấn (\\text{pt} \= \\frac{1}{72}\\text{ inch}) | AI chỉ nhìn thấy giá trị (x\[span\_21\](start\_span)\[span\_21\](end\_span), y) trong mã nguồn, hoàn toàn "mù" về diện tích chiếm chỗ \\text{px} |
| **Thời điểm xác định** | Tức thời ngay khi thực thi phép tính NumPy | Trì hoãn cho đến khi gọi lệnh fig.canvas.draw() hoặc savefig() | Các khoảng dịch chuyển cứng (xytext) do AI ước lượng bị sai lệch khi lên hình |
| **Sự phụ thuộc vào kích thước hình** | Độc lập với figsize, dpi và tỷ lệ khung hình | Thay đổi phi tuyến theo figsize, dpi, độ dài chuỗi ký tự và cỡ chữ | Khi thu nhỏ khung vẽ để ghép nhiều hình, hộp văn bản giữ nguyên cỡ chữ sẽ tràn và đè lên nhau |
| **Khả năng phát hiện lỗi qua Terminal** | Báo lỗi cú pháp hoặc ngoại lệ toán học (Traceback) | Không phát sinh bất kỳ lỗi hay cảnh báo nào khi các hộp pixel chồng lấn | AI nhận mã thoát exit code 0 và tin rằng đồ thị đã được vẽ hoàn hảo |

Khi Antigravity giải thích rằng *"lỗi do xung đột với thuật toán hiển thị điểm ảnh và hoàn toàn do AI"*, tác nhân này đang mô tả hiện tượng **sinh mã mù kết xuất (blind static code generation)**: AI đã tính đúng tọa độ điểm đặc biệt (x, y) và cộng thêm một khoảng dịch chuyển ước lượng, nhưng không lường trước được rằng khi bộ kết xuất chuyển đổi chuỗi ký tự tiếng Việt dài thành hộp pixel thực tế, hộp pixel đó lại mở rộng sang ngang và đè trực tiếp lên hộp pixel của chú thích bên cạnh hoặc cắt ngang đường cong đồ thị. Kết quả thực nghiệm trên Matplotlib 3.9.1 ở độ phân giải 150\\text{ DPI} cho thấy hai chú thích đặt tại hai điểm dữ liệu lân cận (1.57, 1.0) và (1.60, 1.05) với cùng độ lệch tĩnh xytext=(0, 20\) sẽ tạo ra hai khung bao điểm ảnh có kích thước lần lượt là 207.1 \\times 32.8\\text{ px} (tại tọa độ gốc x\_0 \= 178.8\\text{ px}, y\_0 \= 699.8\\text{ px}) và 258.1 \\times 35.1\\text{ px} (tại tọa độ gốc x\_0 \= 156.3\\text{ px}, y\_0 \= 714.7\\text{ px}), dẫn đến sự chồng lấn diện tích trực tiếp trên khung hình (overlaps() \== True). Chỉ khi áp dụng phép dịch chuyển trong không gian điểm ảnh hoặc thuật toán quét bán kính tự động để đưa các nhãn về các vector độ lệch tối ưu như (12, 21)\\text{ pt}, (65, 45)\\text{ pt} và (40, 69)\\text{ pt}, hiện tượng giao cắt khung bao mới được triệt tiêu hoàn toàn (overlaps() \== False).

## **2\. Tại Sao Vẽ Một Hình Thì Chuẩn Nhưng Vẽ Nhiều Hình Lại Đổ Vỡ Hàng Loạt?**

Sự khác biệt chất lượng đột ngột giữa tác vụ "vẽ 1 hình và biên tập 1 bài giảng" so với tác vụ "vẽ nhiều hình trong cùng quy trình" bắt nguồn từ sự cộng hưởng của ba cơ chế kỹ thuật: **co nén diện tích điểm ảnh vật lý**, **rò rỉ máy trạng thái của Matplotlib**, và **suy giảm sự chú ý trong cửa sổ ngữ cảnh của tác nhân AI**.

### **Hiệu ứng co nén diện tích điểm ảnh khi ghép nhiều đồ thị (Subplot Compression)**

Khi vẽ một đồ thị độc lập trên một khung hình tiêu chuẩn (ví dụ figsize=(8, 5\) ở độ phân giải 150\\text{ DPI}), tổng diện tích khung vẽ đạt 1200 \\times 750\\text{ pixels}. Một chú thích có cỡ chữ 9\\text{–}10\\text{ pt} chỉ cao khoảng 32\\text{–}35\\text{ pixels} và rộng khoảng 200\\text{–}258\\text{ pixels}, chiếm một tỷ lệ diện tích rất nhỏ so với khoảng trắng mênh mông của đồ thị. Do đó, dù AI gán tọa độ lệch một cách ước chừng, xác suất va chạm vẫn rất thấp.  
Ngược lại, khi yêu cầu AI vẽ nhiều hình dưới dạng lưới đồ thị con (plt.subplots(2, 2\) hoặc plt.subplots(3, 2)) để đưa vào bài giảng, diện tích điểm ảnh dành cho mỗi trục tọa độ (Axes) bị chia nhỏ xuống còn \\frac{1}{4} hoặc \\frac{1}{6}, trong khi cỡ chữ tính theo đơn vị in ấn (fontsize=10 hoặc 12\) và độ dài chuỗi chú giải tiếng Việt **không hề tự động thu nhỏ theo**. Hệ quả là tỷ lệ diện tích chiếm chỗ của văn bản so với diện tích trục tọa độ tăng vọt gấp nhiều lần, khiến các khung bao văn bản lập tức tràn qua nhau và đè kín các đường biểu diễn.

### **Rò rỉ trạng thái trong kiến trúc máy trạng thái (Pyplot State-Machine Leakage)**

Khi vẽ nhiều hình rời rạc thông qua vòng lặp hoặc chuỗi hàm nối tiếp trong cùng một tệp kịch bản Python, các mô hình ngôn ngữ lớn thường có thói quen sử dụng giao diện mệnh lệnh matplotlib.pyplot (plt.plot(), plt.annotate(), plt.legend()) thay vì giao diện hướng đối tượng tường minh. Giao diện pyplot hoạt động như một máy trạng thái toàn cục ngầm định (implicit state machine) luôn bám theo khung hình hiện hành. Nếu AI quên khởi tạo đối tượng fig, ax \= plt.subplots() riêng biệt hoặc quên đóng khung hình bằng lệnh plt.close(fig) sau mỗi lần xuất ảnh, các đường đồ thị và hộp chú giải của hình thứ (k+1) sẽ bị vẽ chồng trực tiếp lên bộ nhớ đệm của hình thứ k, hoặc lệnh plt.gca() sẽ trỏ nhầm vào trục tọa độ con cuối cùng trong lưới, gây ra cảnh tượng hỗn loạn nơi hàng chục chú giải chất đống lên cùng một vị trí.

### **Sự pha loãng cửa sổ ngữ cảnh (Context Window Dilution) trong phiên làm việc dài**

Trong kiến trúc của Google Antigravity (sử dụng dòng mô hình Gemini 3 với cơ chế phân bổ token suy luận *Deep Think*), khi tác nhân chỉ phải giải quyết một bài giảng kèm một đồ thị duy nhất, toàn bộ ngân sách suy luận không gian được dồn vào việc căn chỉnh hình học cho đồ thị đó. Tuy nhiên, khi người dùng yêu cầu vừa biên tập nội dung chữ của bài giảng dài vừa sinh mã cho hàng loạt đồ thị trong cùng một luồng hội thoại đơn lẻ, hiện tượng **phình to ngữ cảnh (context window bloat)** sẽ xảy ra.  
Các nghiên cứu thực nghiệm về tác nhân trực quan hóa dữ liệu như MatPlotAgent, ChartMimic, Plot2Code và CoDA đã chứng minh rằng khi độ phức tạp của yêu cầu đa tác vụ tăng lên, LLM có xu hướng sao chép rập khuôn một mẫu câu lệnh đặt chú thích (boilerplate code) cho mọi đồ thị mà không tính toán lại hình thái học cục bộ của từng đường cong. Thực nghiệm trên tập chuẩn MatplotBench sử dụng nền tảng mô hình Gemini cho thấy các tác nhân đơn lẻ truyền thống như MatPlotAgent chỉ đạt tỷ lệ thành công chất lượng trực quan (VSR) từ 46,4\\% đến 58,8\\% và thường xuyên thất bại trước các yêu cầu đa diện phức tạp, trong khi kiến trúc cộng tác đa tác nhân có vòng lặp tự phản tỉnh thị giác (CoDA) nâng điểm tổng thể trong các kịch bản phần mềm thực tế lên 39,0\\%, tạo ra mức tăng tuyệt đối \+19,77 điểm phần trăm so với phương pháp cơ sở mạnh nhất (DA-Agent đạt 19,23\\%) và cải thiện hiệu năng tổng thể tới 41,5\\%. Hơn nữa, vì trình thông dịch Python chỉ kiểm tra lỗi cú pháp chứ không kiểm tra lỗi thẩm mỹ, một kịch bản vẽ đồ thị bị đè chữ hoàn toàn vẫn trả về trạng thái chạy thành công và nhận điểm thưởng quy tắc bằng 1.0, khiến tác nhân AI kết thúc nhiệm vụ sớm mà không tự sửa lỗi.

## **3\. Hệ Thống Giải Pháp Kỹ Thuật Trên Ba Tầng Kiến Trúc**

Để chấm dứt triệt để tình trạng đè chú giải mà không phải chỉnh sửa thủ công từng dòng mã cho mỗi bài giảng, quy trình làm việc cần được nâng cấp đồng bộ ở cả ba tầng: **Tầng mã nguồn Python/Matplotlib**, **Tầng cấu hình điều phối Antigravity (Rules, Skills, Subagents)**, và **Tầng kiểm định thị giác tự động (Multimodal Artifacts)**.

### **Tầng 1: Giải Pháp Trong Mã Nguồn Python (Từ Bố Cục Khung Hình Đến Thuật Toán Chống Đè Điểm Ảnh)**

Thay vì để AI tự ước lượng tọa độ văn bản bằng tay, mã nguồn Python cần áp dụng các cơ chế tự động tính toán khung bao điểm ảnh sau khi kết xuất.

#### **1\. Chuẩn hóa quy tắc khung hình, khoảng thở trục và cô lập bộ nhớ**

Mọi kịch bản vẽ nhiều đồ thị trong bài giảng cần thay thế lối viết mã mệnh lệnh truyền thống bằng quy trình quản lý khung hình hướng đối tượng chặt chẽ. Trước hết, thay vì sử dụng hàm plt.tight\_layout()—vốn chỉ thực hiện một phép căn chỉnh tĩnh duy nhất và thường xuyên bỏ sót các hộp chú giải hoặc làm cắt lẹm bảng chú giải nằm ngoài khung—mã nguồn phải khởi tạo khung hình với công cụ bố cục ràng buộc thông qua cú pháp fig, ax \= plt.subplots(layout="constrained") (hoặc layout="compressed" đối với lưới các đồ thị con có tỷ lệ khung hình cố định). Công cụ constrained\_layout tự động tính toán kích thước bao ngoài của nhãn trục, tiêu đề, thanh màu (colorbar) và bảng chú giải gắn với trục (ax.legend) trước khi phân bổ diện tích điểm ảnh cho từng đồ thị con.  
Bên cạnh việc kích hoạt bố cục ràng buộc, bảng chú giải (Legend) cần được tách khỏi vùng dữ liệu trung tâm mỗi khi đồ thị có từ hai đường cong trở lên. Việc đặt legend bên trong lòng khung vẽ gần như chắc chắn sẽ che khuất các điểm cực trị hoặc giao cắt với các mũi tên annotate; do đó, cần cố định bảng chú giải ở lề ngoài thông qua tổ hợp tham số ax.legend(loc="upper left", bbox\_to\_anchor=(1.02, 1.0)) kết hợp trực tiếp với layout="constrained" để Matplotlib tự động co giãn trục nhường chỗ cho bảng chú giải. Đồng thời, bởi vì Matplotlib mặc định chỉ chừa 5\\% khoảng trống quanh biên độ cực đại và cực tiểu của đường cong khiến các hộp văn bản đặt ở đỉnh sóng không có không gian hiển thị, mã nguồn cần gọi lệnh ax.margins(x=0.10, y=0.25) nhằm mở rộng 25\\% vùng đệm trắng phía trên và phía dưới trục tung. Cuối cùng, sau mỗi lệnh xuất tệp fig.savefig(), kịch bản bắt buộc phải gọi plt.close(fig) (hoặc plt.close('all') khi kết thúc vòng lặp) để hủy hoàn toàn đối tượng khung hình trong bộ nhớ, ngăn chặn triệt để hiện tượng máy trạng thái pyplot vẽ đè dữ liệu của hình trước lên hình sau.

#### **2\. Sử dụng thư viện chuyên dụng giải phóng va chạm (textalloc và adjustText)**

Khi cần đặt nhiều nhãn chú thích trực tiếp lên đồ thị, hai thư viện mã nguồn mở mạnh nhất hiện nay trong hệ sinh thái Python là adjustText và textalloc.

| Tiêu chí kỹ thuật | Thư viện adjustText (Phlya/adjustText) | Thư viện textalloc (ckjellson/textalloc) | Hàm giải phóng thuần Matplotlib (Bbox Solver) |
| :---- | :---- | :---- | :---- |
| **Nguyên lý thuật toán** | Mô phỏng lực đẩy lặp (tương tự ggrepel trong R), đẩy các hộp văn bản ra xa nhau và xa điểm gốc qua nhiều vòng lặp | Phát sinh hàng loạt hộp ứng viên quanh điểm neo bằng phép quảng bá mảng NumPy (broadcasting), chọn hộp đầu tiên có diện tích giao cắt bằng 0 | Quét lưới tọa độ cực (radii \\times angles) theo đơn vị offset points, đo trực tiếp get\_window\_extent trên Renderer để tối thiểu hóa hàm phạt |
| **Khả năng tránh đè lên đường đồ thị (Lines)** | **Hạn chế**: Mặc định chỉ đẩy khỏi các điểm rời rạc (x, y); muốn tránh đường cong phải tự nội suy điểm ảo dọc theo đường | **Rất mạnh**: Hỗ trợ tham số gốc x\_lines và y\_lines, nhận trực tiếp mảng tọa độ của toàn bộ các đường cong để né tránh tuyệt đối | **Rất mạnh**: Chuyển đổi toàn bộ các đối tượng ax.get\_lines() sang tọa độ pixel qua ax.transData.transform() để tính điểm phạt va chạm |
| **Tính tất định và tốc độ** | Chậm khi số lượng nhãn lớn vì phải vẽ lại (draw) ở mỗi bước lặp; kết quả có yếu tố dịch chuyển ngẫu nhiên | Rất nhanh (xử lý \\sim 2000 điểm trong 2,9\\text{ giây}) và hiệu quả vượt trội cho đồ thị nhiều đường | Tức thời đối với đồ thị bài giảng (5\\text{–}30 chú thích/hình), hoàn toàn tất định và **không cần cài đặt thư viện ngoài** |

Nếu môi trường Python cho phép cài đặt gói mở rộng (pip install\[span\_100\](start\_span)\[span\_100\](end\_span) textalloc adjustText), thư viện **textalloc là lựa chọn tối ưu nhất cho đồ thị hàm số và mô phỏng vật lý/kỹ thuật** vì nó hỗ trợ truyền trực tiếp danh sách các đường cong vào tham số x\_lines và y\_lines để thuật toán tự động né tránh cả đường biểu diễn lẫn các nhãn khác:  
import numpy as np  
im\[span\_105\](start\_span)\[span\_105\](end\_span)\[span\_107\](start\_span)\[span\_107\](end\_span)port matplotlib.pyplot as plt  
import textalloc as ta

\# Khởi tạo khung hình chuẩn với constrained\_layout  
fig, ax \= plt.subplots(figsize=(8, 4.8), dpi=150, layout="constrained")

x \= np.linspace(0, 10, 500\)  
y1 \= np.sin(x)  
y2 \= np.cos(x)  
y3 \= np.sin(x) \+ np.cos(x)

ax.plot(x, y1, label="Dao động thành phần x1(t)", lw=1.8)  
ax.plot(x, y2, label="Dao động thành phần x2(t)", lw=1.8)  
ax.plot(x, y3, label="Dao động tổng hợp x(t)", lw=2.2)

\# Mở rộng khoảng thở trục Y thêm 25% và đặt Legend ra ngoài  
ax.margins(x=0.05, y=0.25)  
ax.legend(loc="upper left", bbox\_to\_anchor=(1.02, 1.0))

\# Các điểm đặc biệt cần chú giải trên đồ thị  
x\_targets \= np.array(\[np.pi / 4, np.pi / 4, np.pi / 2\])  
y\_targets \= np.array(\[np.sqrt(2), np.sqrt(2) / 2, 1.0\])  
labels \= \[  
    "Biên độ cực đại A\_max",  
    "Vị trí hai dao động cùng pha",  
    "Đỉnh pha thành phần x1(t)"  
\]

\# Truyền toàn bộ mảng tọa độ của 3 đường cong vào x\_lines và y\_lines  
\# để textalloc tự động tìm vùng trống không đè lên bất kỳ đường nào  
ta.allocate(  
    ax,  
    x\_targets,  
    y\_targets,  
    labels,  
    x\_lines=\[x, x, x\],  
    y\_lines=\[y1, y2, y3\],  
    textsize=9,  
    draw\_lines=True,  
    linecolor="\#555555",  
    linewidth=0.8,  
    avoid\_crossing\_label\_lines=True  
)

fig.savefig("mo\_phong\_dao\_dong.png", dpi=150)  
plt.close(fig)

#### **3\. Giải pháp thuần Matplotlib (Zero-Dependency Pixel-Space Solver) cho các hộp ax.annotate**

Trong nhiều bài giảng, người biên soạn muốn sử dụng hộp chú thích có khung viền bo tròn (bbox=dict(boxstyle="round", ...)) và mũi tên cong (arrowprops) của hàm ax.annotate gốc mà không muốn phụ thuộc vào thư viện bên thứ ba. Đoạn mã dưới đây cung cấp hàm resolve\_annotation\_overlaps(fig, ax, annotations) đã được kiểm chứng thực nghiệm: hàm này ép trình kết xuất vẽ nháp một lần (fig.canvas.draw()), lấy kích thước hộp pixel thực tế qua ann.get\_bbox\_patch().get\_window\_extent(renderer), ánh xạ toàn bộ các đường đồ thị sang tọa độ pixel bằng ax.transData.transform(), và tự động xoay góc mũi tên quanh điểm neo cho đến khi tìm được vị trí không đè lên bất kỳ nhãn hay đường cong nào:  
import matplotlib.pyplot as plt  
import matplotlib.transforms as mtransforms  
import numpy as np

def resolve\_annotation\_overlaps(fig, ax, annotations, lines=None, pad\_px=6):  
    """  
    Hàm thuần Matplotlib giải quyết triệt để xung đột điểm ảnh:  
    Tự động dịch chuyển vị trí chú thích (xyann) trong không gian offset points  
    để không đè lên nhau, không đè lên đường đồ thị (lines) và không tràn khỏi trục.  
    """  
    if lines is None:  
        lines \= ax.get\_lines()

    \# Bước 1: Kích hoạt trình kết xuất để Matplotlib tính toán tọa độ pixel thực tế  
    fig.canvas.draw()  
    renderer \= fig.canvas.get\_renderer()  
    ax\_bbox \= ax.get\_window\_extent(renderer)

    \# Bước 2: Chuyển đổi tọa độ dữ liệu (Data Coords) của mọi đường cong sang Pixel Coords  
    line\_pixels \= \[\]  
    for line in lines:  
        xy\_data \= np.column\_stack(line.get\_data())  
        if len(xy\_data) \> 0:  
            xy\_px \= ax.transData.transform(xy\_data)  
            line\_pixels.append(xy\_px)  
    all\_line\_px \= np.vstack(line\_pixels) if line\_pixels else np.empty((0, 2))

    \# Bước 3: Khởi tạo lưới ứng viên tọa độ cực (bán kính x góc nghiêng) tính bằng offset points  
    radii \= \[25, 42, 60, 80\]  
    angles\_deg \= \[60, \-60, 120, \-120, 90, \-90, 35, \-35, 145, \-145, 15, \-15, 165, \-165\]  
    candidates \= \[  
        (int(r \* np.cos(np.deg2rad(a))), int(r \* np.sin(np.deg2rad(a))))  
        for r in radii for a in angles\_deg  
    \]

    placed\_bboxes \= \[\]

    for ann in annotations:  
        best\_offset \= ann.xyann  
        min\_penalty \= float("inf")

        for dx, dy in candidates:  
            ann.xyann \= (dx, dy)  
            fig.canvas.draw()  
            bbox\_patch \= ann.get\_bbox\_patch()  
            bbox \= bbox\_patch.get\_window\_extent(renderer) if bbox\_patch else ann.get\_window\_extent(renderer)

            \# Mở rộng khung bao thêm khoảng đệm (padding) tính bằng pixel  
            ebbox \= mtransforms.Bbox.from\_extents(  
                bbox.x0 \- pad\_px, bbox.y0 \- pad\_px, bbox.x1 \+ pad\_px, bbox.y1 \+ pad\_px  
            )

            penalty \= 0.0  
            \# Phạt nặng nếu hộp chú thích tràn ra ngoài khung trục Axes  
            if (ebbox.x0 \< ax\_bbox.x0 or ebbox.x1 \> ax\_bbox.x1 or  
                ebbox.y0 \< ax\_bbox.y0 or ebbox.y1 \> ax\_bbox.y1):  
                penalty \+= 5000.0

            \# Phạt tuyệt đối nếu giao cắt với bất kỳ hộp chú thích nào đã đặt trước đó  
            for prev\_bbox in placed\_bboxes:  
                if ebbox.overlaps(prev\_bbox):  
                    penalty \+= 10000.0

            \# Phạt nếu hộp chú thích đè lên các điểm ảnh thuộc đường đồ thị  
            if len(all\_line\_px) \> 0:  
                in\_box \= (  
                    (all\_line\_px\[:, 0\] \>= ebbox.x0) & (all\_line\_px\[:, 0\] \<= ebbox.x1) &  
                    (all\_line\_px\[:, 1\] \>= ebbox.y0) & (all\_line\_px\[:, 1\] \<= ebbox.y1)  
                )  
                penalty \+= np.sum(in\_box) \* 50.0

            \# Ưu tiên vị trí gần điểm neo nhất nếu không có va chạm  
            penalty \+= np.hypot(dx, dy) \* 0.1

            if penalty \< min\_penalty:  
                min\_penalty \= penalty  
                best\_offset \= (dx, dy)  
                if penalty \< 10.0:  \# Tìm thấy vị trí hoàn toàn sạch ở bán kính gần nhất  
                    break

        \# Cố định vị trí tối ưu và lưu khung bao vào danh sách vật cản  
        ann.xyann \= best\_offset  
        fig.canvas.draw()  
        final\_patch \= ann.get\_bbox\_patch()  
        final\_bbox \= final\_patch.get\_window\_extent(renderer) if final\_patch else ann.get\_window\_extent(renderer)  
        placed\_bboxes.append(  
            mtransforms.Bbox.from\_extents(  
                final\_bbox.x0 \- pad\_px, final\_bbox.y0 \- pad\_px,  
                final\_bbox.x1 \+ pad\_px, final\_bbox.y1 \+ pad\_px  
            )  
        )

### **Tầng 2: Giải Pháp Kiến Trúc Điều Phối Trong Google Antigravity (Rules, Skills, Subagents)**

Thay vì phải nhắc lại các quy tắc vẽ đồ thị trong từng câu lệnh trò chuyện (chat prompt), Google Antigravity cung cấp hệ thống **Kỹ thuật Khung điều phối (Harness Engineering)** gồm Rules (Luật bất biến), Skills (Kỹ năng quy trình) và Subagents (Tác nhân con cô lập ngữ cảnh). Việc thiết lập đúng ba cơ chế này sẽ giải quyết tận gốc sự cố suy giảm chất lượng khi biên soạn bài giảng có nhiều hình.

#### **1\. Thiết lập Luật bất biến (Rules) để cưỡng chế chuẩn vẽ đồ thị**

Trong Google Antigravity, Rules là các chỉ dẫn bền vững và ràng buộc kiến trúc được hệ thống tự động quét từ hệ thống tệp và tiêm thẳng vào ngữ cảnh của tác nhân mà không cần người dùng nhắc lại trong cửa sổ chat. Antigravity hỗ trợ hai cấp độ lưu trữ luật: cấp độ toàn cục trên máy trạm (\~/.gemini/AGENTS.md hoặc \~/.gemini/config/rules/\*.md) và cấp độ không gian làm việc của dự án (AGENTS.md hoặc .agents/rules/\*.md). Hệ thống áp dụng giới hạn dung lượng 24\\text{ KB} (24.000\\text{ bytes}) cho mỗi tệp luật đơn lẻ và phân bổ tổng ngân sách 20.000\\text{ tokens} cho toàn bộ các luật toàn cục và luật luôn bật (always\_on).  
Để quy tắc chỉ kích hoạt tự động mỗi khi tác nhân AI tạo hoặc chỉnh sửa tệp mã nguồn Python (giúp bảo toàn ngân sách 20.000\\text{ tokens} của hệ thống), người dùng cần tạo một tệp luật mô-đun tại đường dẫn .agents/rules/matplotlib-plotting.md (hoặc \~/.gemini/config/rules/matplotlib-plotting.md để áp dụng cho mọi bài giảng trên máy) với phần khai báo YAML frontmatter sử dụng chế độ trigger: glob. Lưu ý rằng Antigravity chỉ quét các tệp .md nằm trực tiếp trong thư mục .agents/rules/ (bỏ qua các thư mục con lồng bên trong trừ khi đăng ký tường minh trong .agents/rules.json) và sẽ âm thầm loại bỏ tệp luật nếu viết sai cú pháp trigger (ví dụ viết kiểu camelCase alwaysOn hoặc modelDecision thay vì always\_on, model\_decision, glob hoặc manual).  
Dưới đây là nội dung chuẩn cho tệp .agents/rules/matplotlib-plotting.md sử dụng bảng quy tắc định hướng trực tiếp cho tác nhân AI:

## **trigger: glob description: "Quy chuẩn bắt buộc chống đè chú giải và xung đột điểm ảnh khi vẽ đồ thị Matplotlib bằng Python" globs: "\*.py, \*.ipynb"**

# **Quy Chuẩn Bắt Buộc Khi Vẽ Đồ Thị Mô Phỏng Bằng Matplotlib**

Mỗi khi khởi tạo hoặc chỉnh sửa mã nguồn vẽ đồ thị khoa học và bài giảng bằng Matplotlib, Agent phải thực thi nghiêm ngặt các ràng buộc kỹ thuật trong bảng dưới đây:

| Hạng mục kiểm soát | Quy tắc bắt buộc trong mã nguồn Python | Hành vi bị nghiêm cấm |
| :---- | :---- | :---- |
| **Quản lý khung hình** | Khởi tạo tường minh fig, ax \= plt.subplots(figsize=(...), dpi=150, layout="constrained") và gọi plt.close(fig) ngay sau fig.savefig(). | Dùng giao diện mệnh lệnh plt.plot(), plt.annotate() hoặc để rò rỉ trạng thái giữa các hình. |
| **Bảng chú giải & Khoảng thở** | Gọi ax.margins(x=0.10, y=0.25) và đặt bảng chú giải ra ngoài trục bằng ax.legend(loc="upper left", bbox\_to\_anchor=(1.02, 1.0)). | Đặt legend đè lên vùng dữ liệu trung tâm khi đồ thị có nhiều đường cong và chú thích. |
| **Hệ tọa độ chú thích** | Sử dụng textcoords="offset points" cho ax.annotate() hoặc dùng textalloc.allocate(..., x\_lines=..., y\_lines=...). | Gán cứng tọa độ văn bản trong Data Coordinates mà không kiểm tra kích thước hộp pixel. |
| **Giải phóng va chạm Bbox** | Gọi fig.canvas.draw(), lấy khung bao qua get\_window\_extent(renderer) và chạy hàm resolve\_annotation\_overlaps(fig, ax, annotations). | Lưu hình trực tiếp khi chưa kiểm tra .overlaps() giữa các hộp văn bản và ax.get\_lines(). |
| **Kiểm định thị giác** | Đọc lại tệp .png vừa kết xuất bằng công cụ đa phương thức để xác nhận không có chữ tiếng Việt nào đè nhau hoặc bị cắt lẹm ở rìa. | Báo cáo hoàn thành nhiệm vụ chỉ dựa vào mã thoát exit code 0 của trình thông dịch Python. |

#### **2\. Đóng gói Kỹ năng (Skills) và Phân tách ngữ cảnh bằng Tác nhân con (Subagents)**

Trong triết lý thiết kế của Antigravity, nếu Rules đóng vai trò là các rào cản bất biến thì **Skills là các gói kiến thức quy trình (procedural workflows)** được lưu trữ trong từng thư mục con riêng biệt tại .agents/skills/\<tên-kỹ-năng\>/SKILL.md. Thông qua cơ chế *khám phá lũy tiến (progressive discovery)*, Antigravity chỉ lập chỉ mục phần mô tả ngắn của Skill vào đầu phiên và chỉ nạp toàn bộ nội dung hướng dẫn chi tiết khi tác nhân thực sự bước vào giai đoạn vẽ đồ thị, giúp giữ cho cửa sổ ngữ cảnh luôn gọn nhẹ. Người dùng có thể lưu đoạn mã hàm resolve\_annotation\_overlaps ở Tầng 1 vào tệp .agents/skills/scientific-plotting/SKILL.md hoặc nhúng trực tiếp vào tệp luật thông qua cú pháp @\[label\](path) để Antigravity tự động ghép nối nội dung trước khi đánh giá câu lệnh.  
Quan trọng hơn, để triệt tiêu hoàn toàn hiện tượng **vẽ 1 hình thì chuẩn nhưng vẽ nhiều hình kèm biên tập bài giảng thì lỗi**, người dùng cần khai thác tính năng **Tác nhân con (Subagents)** của Antigravity:

| Cơ chế trong Antigravity | Vị trí cấu hình chuẩn | Cơ chế hoạt động với Cửa sổ Ngữ cảnh (Context Window) | Ứng dụng cụ thể cho bài toán biên soạn bài giảng & vẽ đồ thị |
| :---- | :---- | :---- | :---- |
| **Rules (Luật bất biến)** | AGENTS.md hoặc .agents/rules/\*.md | Luôn hoạt động (always\_on) hoặc tự động tiêm vào ngữ cảnh khi chạm tới tệp khớp mẫu glob (\*.py) | Cưỡng chế tự động các tiêu chuẩn layout="constrained", plt.clos\[span\_126\](start\_span)\[span\_126\](end\_span)e(fig) và thuật toán kiểm tra pixel get\_window\_extent |
| **Skills (Kỹ năng quy trình)** | .agents/skills/\<domain\>/SKILL.md | Khám phá lũy tiến (progressive discovery): chỉ nạp toàn văn khi nhiệm vụ yêu cầu, chống phình to ngữ cảnh | Chứa mẫu hàm chuẩn resolve\_annotation\_overlaps và quy trình phối màu/phông chữ sư phạm cho bài giảng |
| **Subagents (Tác nhân con)** | .agents/agents/\*.md hoặc lệnh /agents, /teamwork-preview | **Cô lập ngữ cảnh hoàn toàn (Workspace & Context Isolation)**: mỗi Subagent có một cửa sổ ngữ cảnh độc lập, không làm ô nhiễm luồng của Agent chính | Agent chính phụ trách biên tập nội dung bài giảng và ủy quyền (delegate) mỗi đồ thị cho một Subagent riêng biệt để đạt chất lượng tương đương khi vẽ 1 hình đơn lẻ |
| **Artifacts & Multimodal** | Tích hợp sẵn trong Antigravity IDE / SDK (from\_file("\*.png")) | Chuyển đổi kết quả thực thi thành đối tượng thị giác để kiểm tra độc lập với nhật ký dòng lệnh (raw logs) | Buộc Agent tự "nhìn" lại bức ảnh .png vừa kết xuất để phát hiện lỗi đè chữ trước khi bàn giao |

Cụ thể, người dùng có thể định nghĩa một tác nhân con chuyên trách đồ họa tại .agents/agents/plot-specialist.md (hoặc \~/.gemini/config/agents/plot-specialist.md với cấu hình YAML frontmatter đặt subagent: true và model: pro). Khi ra lệnh biên soạn một bài giảng gồm nhiều đồ thị mô phỏng, thay vì để một Agent duy nhất vừa viết văn bản vừa viết mã cho toàn bộ các hình trong một luồng duy nhất, Agent chính sẽ đóng vai trò điều phối viên (Orchestrator): nó phân rã bài toán và khởi chạy song song hoặc tuần tự các phiên plot-specialist độc lập cho từng hình (hoặc chạy dưới dạng tác vụ nền bất đồng bộ qua bảng điều khiển /agents và /tasks). Vì mỗi Subagent chỉ nhận đúng thông số của **một đồ thị duy nhất** trong một cửa sổ ngữ cảnh hoàn toàn mới và sạch sẽ, nó sẽ tái lập lại trạng thái tập trung tối đa giống hệt như khi người dùng chỉ yêu cầu vẽ 1 hình.

### **Tầng 3: Thiết Lập Vòng Lặp Tự Kiểm Tra Thị Giác Đa Phương Thức (Multimodal Visual Self-Correction)**

Lý do cuối cùng khiến lỗi đè chú giải lọt qua quy trình kiểm duyệt của AI là vì mặc định các tác nhân lập trình chỉ kiểm tra **tính hợp lệ của mã nguồn (Code Execution Verification)** thông qua đầu ra văn bản của trình thông dịch (stdout/stderr), chứ không kiểm tra **tính hợp lệ thị giác (Visual Verification)** trên tệp ảnh điểm.  
Nền tảng Google Antigravity (cả trên giao diện IDE độc lập, CLI lẫn bộ công cụ phát triển Python google-antigravity SDK) đều hỗ trợ gốc khả năng **tiếp nhận đa phương thức (Multimodal Ingestion)** và hệ thống **Hiện vật kiểm chứng (Artifacts)**. Khi một kịch bản Python chạy xong và sinh ra các tệp hinh\_1.png, hinh\_2.png, tác nhân Antigravity có khả năng nạp trực tiếp các tệp ảnh đó vào bộ xử lý thị giác của mô hình Gemini để tự đánh giá bố cục.  
Nếu người dùng tự xây dựng kịch bản tự động hóa bài giảng bằng **Google Antigravity Python SDK** (pip install google-antigravity), vòng lặp tự sửa lỗi thị giác kết hợp Subagents có thể được lập trình tường minh như sau:  
import asyncio  
from google.antigravity import Agent, LocalAgentConfig, types  
from google.antigravity.types import from\_file

async def generate\_and\_verify\_plot(plot\_spec: str, output\_png: str):  
    \# Cấu hình Agent với quyền sử dụng Subagents và quy chuẩn kiến trúc đồ họa  
    config \= LocalAgentConfig(  
        system\_instructions=(  
            "Chuyên gia mô phỏng đồ thị khoa học bằng Python Matplotlib. "  
            "Luôn sử dụng layout='constrained', plt.close(fig) và kiểm tra va chạm Bbox."  
        ),  
        capabilities=types.CapabilitiesConfig(enable\_subagents=True)  
    )

    async with Agent(config) as agent:  
        \# Bước 1: Yêu cầu Agent viết mã và kết xuất đồ thị ra tệp PNG  
        await agent.chat(  
            f"Hãy viết mã Python vẽ đồ thị theo đặc tả sau và lưu thành '{output\_png}':\\n{plot\_spec}"  
        )

        \# Bước 2: Nạp trực tiếp tệp ảnh PNG vừa kết xuất vào ngữ cảnh Đa phương thức (Multimodal Ingestion)  
        rendered\_image \= from\_file(output\_png)  
        critique\_response \= await agent.chat(\[  
            rendered\_image,  
            (  
                "Hãy kiểm tra kỹ bức ảnh điểm vừa kết xuất này. "  
                "Có bất kỳ chú giải (annotation/text/legend) nào đè lên nhau, đè lên đường đồ thị, "  
                "hoặc bị cắt lẹm ở viền khung hình không? "  
                "Nếu có dù chỉ một lỗi nhỏ, hãy sửa lại tọa độ offset points hoặc chạy thuật toán "  
                "resolve\_annotation\_overlaps và xuất lại tệp ảnh hoàn chỉnh."  
            )  
        \])  
        print(await critique\_response.text())

if \_\_name\_\_ \== "\_\_main\_\_":  
    asyncio.run(generate\_and\_verify\_plot(  
        plot\_spec="Vẽ đồ thị giao thoa hai sóng kết hợp cùng biên độ và chú thích 3 điểm cực đại, cực tiểu liên tiếp.",  
        output\_png="giao\_thoa\_song.png"  
    ))

Ngay cả khi sử dụng trực tiếp trên giao diện đồ họa **Antigravity IDE** hoặc **Antigravity CLI** mà không viết mã SDK, người dùng chỉ cần áp dụng quy trình vận hành chuẩn thông qua các lệnh gạch chéo (/plan, /agents, /boost, /teamwork-preview) và cấu hình tệp .agents/rules/matplotlib-plotting.md đã cung cấp ở trên.

## **4\. Tổng Hợp Lộ Trình Khắc Phục Thực Thi Ngay**

Để giải quyết dứt điểm hiện tượng chồng lấn chú giải ngay từ bài giảng tiếp theo trên Google Antigravity, quy trình thực thi cần kết hợp đồng bộ việcneo giữ quy tắc bất biến tại tầng hệ thống tệp, chuẩn hóa thuật toán giải phóng khung bao điểm ảnh tại tầng Python, và phân tách luồng thực thi bằng tác nhân con. Bước khởi đầu quan trọng nhất là tạo tệp luật .agents/rules/matplotlib-plotting.md với cấu hình trigger: glob cho \*.py, \*.ipynb như mẫu ở Mục 3\. Thao tác thiết lập một lần này buộc mọi tác nhân của Antigravity luôn phải khởi tạo layout="constrained", mở rộng khoảng thở trục ax.margins(x=0.10, y=0.25), đưa legend ra ngoài khung vẽ và gọi plt.close(fig) sau từng hình mà không cần nhắc lại trong cửa sổ trò chuyện.  
Song song với tệp luật, môi trường Python của dự án cần được cài đặt gói textalloc (pip install textalloc) để tự động né cả điểm lẫn đường cong thông qua tham số x\_lines và y\_lines, hoặc tích hợp hàm thuần Matplotlib resolve\_annotation\_overlaps() vào thư mục kỹ năng .agents/skills/scientific-plotting/SKILL.md nhằm buộc AI giải bài toán va chạm trong không gian điểm ảnh (get\_window\_extent) sau khi gọi fig.canvas.draw(). Cuối cùng, khi biên soạn bài giảng có nhiều hình mô phỏng, người dùng cần yêu cầu Antigravity phân tách mỗi đồ thị thành một nhiệm vụ cho Subagent độc lập thông qua cơ chế /agents hoặc /teamwork-preview kèm cổng kiểm duyệt bắt buộc đọc lại tệp ảnh .png sau khi xuất. Sự kết hợp giữa cô lập ngữ cảnh của Subagents và vòng lặp tự phản tỉnh thị giác đa phương thức sẽ đảm bảo dù bài giảng có chứa hàng chục đồ thị phức tạp, mỗi đồ thị đều đạt độ chuẩn xác hình học ngang bằng với khi vẽ một hình duy nhất.

#### **Nguồn trích dẫn**

1\. MM-ReCoder: Advancing Chart-to-Code Generation with ... \- arXiv, https\://arxiv.org/html/2604.01600v1 2\. Frequently Asked Questions — Matplotlib 3.11.2 documentation, https\://matplotlib.org/stable/users/faq.html 3\. Annotations — Matplotlib 3.11.2 documentation, https\://matplotlib.org/stable/users/explain/text/annotations.html 4\. MatPlotAgent: Method and Evaluation for LLM-Based Agentic, https\://www\.alphaxiv.org/abs/2402.11453 5\. text size \- matplotlib-users \- Matplotlib, https\://discourse.matplotlib.org/t/text-size/4770 6\. Rules | Google Antigravity Docs, https\://antigravity.google/docs/rules/ 7\. Subagents \- Antigravity SDK, https\://antigravity.google/docs/sdk/subagents/ 8\. The AI-Native Developer Experience, Part 2: Harness Engineering, https\://medium.com/google-cloud/the-ai-native-developer-experience-part-2-harness-engineering-with-google-antigravity-7fb72dab243f 9\. Fastest implementation of a way to adjust pyplot overlapping, https\://stackoverflow.com/questions/51237359/fastest-implementation-of-a-way-to-adjust-pyplot-overlapping-annotation-text-pr 10\. Matplotlib tight\_layout(): Fix Clipped Labels and Spacing \- Python Pool, https\://www\.pythonpool.com/matplotlib-tightlayout/ 11\. Subagents, hooks, scheduled tasks, agent management, voice, and, https\://antigravity.google/blog/google-io-2026-feature-deep-dive/ 12\. Introducing custom agents | Google Antigravity Blog, https\://antigravity.google/blog/introducing-custom-agents/ 13\. Python Plotting With Matplotlib (Guide), https\://realpython.com/python-matplotlib-guide/ 14\. Matplotlib Tutorial \- Principles of creating any plot with the Matplotlib, https\://machinelearningplus.com/plots/matplotlib-plotting-tutorial/ 15\. Matplotlib savefig() over multiple graphs keeps saving the same graph, https\://stackoverflow.com/questions/46418007/matplotlib-savefig-over-multiple-graphs-keeps-saving-the-same-graph 16\. Advanced 2D plots with Matplotlib in Python (codes included), https\://www\.earthinversion.com/techniques/advanced-2D-plots-with-matplotlib/ 17\. Plots in a loop are overwritten \- python \- Stack Overflow, https\://stackoverflow.com/questions/69240811/plots-in-a-loop-are-overwritten 18\. GitHub \- google-antigravity/antigravity-sdk-python: A Python library, https\://github.com/google-antigravity/antigravity-sdk-python 19\. Hello World, Antigravity: Building Your First Gemini 3 Agent in Python, https\://medium.com/@jalpeshvasa/hello-world-antigravity-building-your-first-gemini-3-agent-in-python-6cc0863a3bb9 20\. BREAKING THE SFT PLATEAU: MULTIMODAL STRUC, https\://proceedings.iclr.cc/paper\_files/paper/2026/file/b95c7e24501f5d1dddbc5e8526cda7ae-Paper-Conference.pdf 21\. CoDA: Agentic Systems for Collaborative Data Visualization \- arXiv, https\://arxiv.org/html/2510.03194v1 22\. Constrained layout guide — Matplotlib 3.11.2 documentation, https\://matplotlib.org/stable/users/explain/axes/constrainedlayout\_guide.html 23\. Add legend to figure with \`tight\_layout=True\` \- Matplotlib, https\://discourse.matplotlib.org/t/add-legend-to-figure-with-tight-layout-true/23345 24\. python \- Annotate lines without overlapping \- Stack Overflow, https\://stackoverflow.com/questions/79652639/annotate-lines-without-overlapping 25\. Phlya/adjustText: A small library for automatical adjustment of text, https\://github.com/Phlya/adjustText 26\. Software Tools for Mixture Analysis \- DSpace, https\://dspace.ut.ee/bitstreams/d21535af-6368-4216-8cb4-271e7f905a25/download 27\. GitHub \- ckjellson/textalloc: Allocates text labels in matplotlib, https\://github.com/ckjellson/textalloc 28\. How to Add Antigravity Skills: Folder and Setup Guide \- Layer3Labs, https\://www\.layer3labs.io/guides/google-antigravity-skills 29\. Agent skills | Google Antigravity Docs, https\://antigravity.google/docs/skills/ 30\. Custom subagents | Google Antigravity Docs, https\://antigravity.google/docs/subagents/ 31\. Subagent Reasoning level \- Google AI Developers Forum, https\://discuss.ai.google.dev/t/subagent-reasoning-level/189378 32\. Google Antigravity | AI Coding Tools \- Real Python, https\://realpython.com/ref/ai-coding-tools/google-antigravity/ 33\. Antigravity SDK, https\://antigravity.google/product/antigravity-sdk 34\. Antigravity SDK overview | Google Antigravity Docs, https\://antigravity.google/docs/sdk/overview/