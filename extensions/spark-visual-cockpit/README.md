# SPARK VISUAL COCKPIT v2.0 (CHROME EXTENSION MANIFEST V3)

> **Kiến trúc Buồng lái Học thuật Kỹ thuật Liền khối (Unified Decoupled Academic Workstation)**  
> Dành cho sinh viên, giảng viên và kỹ sư Vật lý Kỹ thuật, Cấu trúc Dị thể Bán dẫn (GaAs/AlGaAs), Laser Diode và Màng mỏng Quang học.

---

## 1. Tổng quan Kiến trúc v2.0

Spark Visual Cockpit v2.0 chuyển đổi giao diện học tập/chat trên Google Gemini thành **Trạm làm việc Kỹ thuật Hai Khung nhìn Liền khối**:
- **Cột Trái (Visual Studio Canvas [SPARK]):** Studio trực quan hóa vi cấu trúc, băng năng lượng heterostructure ($E_c, E_v, E_F$), mô phỏng màng mỏng quang phổ với khả năng zoom/pan mượt mà, bộ lọc màu Dark Mode bảo toàn màu sắc vật lý, trích xuất thông số trục tọa độ và dải lịch sử ảnh. Bật/tắt độc lập bằng phím `Esc` hoặc nút `[✕]`.
- **Cột Phải (Hybrid Right Pane [READ / CHAT]):**
  - **Lớp phủ [READ]:** Mặc định hiển thị bài giảng học thuật có cấu trúc (Living Document) bắt từ cặp thẻ `:::spark-reader-content`, ngăn chặn hoàn toàn hiện tượng mỏi cuộn và trôi bài trong chat.
  - **Khung Chat [CHAT]:** Khi cần hỏi sâu, bấm nút `[CHAT]` để lộ khung chat gốc của Gemini. Sau khi hiểu, bấm thẻ mép `[READ]` để quay lại đúng vị trí đang đọc dở (Zero-Tamper Resume).
- **Cụm Thẻ Mép Nổi Động 38px (Dynamic Dock Tabs):**
  - Đồng bộ kích thước $38\text{px}$ cho cả 2 thẻ `[SPARK]` và `[READ]`.
  - Khi đóng cả 2: Nằm kề nhau sát mép trái màn hình.
  - Khi mở Khung Trái: Thẻ `[READ]` tự động trượt ra bám dính vào mép ngoài của Khung Trái.

---

## 2. Cấu trúc Dự án

```text
spark-visual-cockpit-v2.0.0/
├── manifest.json         # Cấu hình Chrome Extension Manifest V3 (v2.0.0)
├── background.js        # Service Worker: Fetch Google Drive Blob, kiểm tra MIME/PDF, ủy quyền tab
├── content.js           # Engine chính: Closed Shadow DOM, ReaderOverlayEngine, StreamParserObserver, DockTabsManager
├── styles.css           # Bảng kiểu CSS: Thẻ dock 38px, Reader overlay, FOUC masking, @media print
├── CHROMEWEBSTORE.md    # Đặc tả phân phối Chrome Web Store
├── HUONG_DAN_CAI_DAT.txt# Hướng dẫn cài đặt và nâng cấp nhanh
├── README.md            # Tài liệu kỹ thuật tổng thể
├── demo/                # Trang web demo bài giảng kiểm thử ngoại tuyến
└── icons/               # Bộ icon chuẩn (16, 48, 128 px)
```

---

## 3. Các Giải pháp Kỹ thuật Đột phá v2.0

| Tính năng | Giải pháp Kỹ thuật |
| :--- | :--- |
| **Stream Interception & Masking** | Bắt cặp thẻ `:::spark-reader-content` trong luồng token, tiêm CSS `display: none !important` trên chat gốc để chống chớp nháy (FOUC), pipe trực tiếp vào Virtual DOM của Khung [READ]. |
| **Scroll-Sync & Interaction Lock (3s)** | Gắn `IntersectionObserver` tự động đồng bộ hình ảnh khi cuộn bài; tạm khóa 3 giây khi người dùng đang pan/zoom ở Khung Trái để tránh nhảy hình ngoài ý muốn. |
| **Unclosed Delimiter Fail-Safe** | Tự động đóng thẻ ảo nếu người dùng nhấn "Dừng sinh" (Stop generating) giữa chừng. |
| **Bảo toàn Tài liệu Gốc (Zero-Tamper)** | Chuyển đổi giữa `[CHAT]` và `[READ]` mà không làm thay đổi hay in lại bài giảng cũ, lưu tọa độ cuộn chuột qua `sessionStorage`. |
| **Xuất bản PDF & Lưu trữ Drive** | Bắt khối `:::spark-archive-manifest`, áp dụng CSS in ấn chống xé đôi công thức toán học (`break-inside: avoid !important`), điều hướng lưu vào thư mục con trên Google Drive. |

---

## 4. Hướng dẫn Cài đặt

1. Truy cập: `chrome://extensions/` trên Chrome/Edge/Brave.
2. Bật **"Developer mode"** ở góc trên bên phải.
3. Nhấp **"Load unpacked"** và chọn thư mục `spark-visual-cockpit-v2.0.0`.
4. Mở tab Gemini (`gemini.google.com`) để trải nghiệm buồng lái học thuật v2.0!
