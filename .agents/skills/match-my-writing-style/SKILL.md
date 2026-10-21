---
name: match-my-writing-style
description: Học theo giọng văn của bạn qua các nội dung trong Workspace; chỉ kích hoạt khi soạn thảo văn bản giao tiếp đối ngoại (email, tin nhắn, thông báo), tuyệt đối không can thiệp vào trao đổi học thuật hay nghiên cứu kỹ thuật.
---
# Match My Writing Style

Kỹ năng giúp mô phỏng chính xác văn phong cá nhân của người dùng, được giới hạn phạm vi áp dụng nghiêm ngặt cho các văn bản giao tiếp đối ngoại.

*Điều kiện Nạp & Hợp đồng I/O (Trigger & I/O Contract):* Chỉ nạp khi người dùng yêu cầu soạn thảo văn bản giao tiếp hành chính đối ngoại (email, tin nhắn, thông báo gửi giảng viên/đối tác bên ngoài); tự động ngắt tuyệt đối 100% trong mọi tác vụ học thuật, nghiên cứu kỹ thuật (`/bg`, `/scan`, `/learn`, `/edit`) và mọi email báo cáo tiến độ nội bộ gửi Bùi Trung Dũng.

## Phạm Vi Áp Dụng (Scope of Activation)

- **Chỉ kích hoạt khi:** Người dùng yêu cầu soạn thảo văn bản giao tiếp, liên lạc ra bên ngoài như email, tin nhắn, bài đăng, thông báo hành chính hoặc thư từ gửi giảng viên/đối tác bên ngoài.
- **Tuyệt đối KHÔNG kích hoạt khi:**
  - Trao đổi học thuật, thảo luận lý thuyết vật lý, giải bài tập kỹ thuật.
  - Phân tích linh kiện, thiết kế mạch, mô phỏng quang học/bán dẫn, lập trình (Python, MATLAB).
  - Nghiên cứu tài liệu khoa học, giải thích giáo trình hoặc tài liệu từ NotebookLM.
  - **LOẠI TRỪ TUYỆT ĐỐI BÁO CÁO NỘI BỘ CHO NGƯỜI HỌC:** Mọi email báo cáo tiến độ, thông báo nghiệm thu bài giảng, biên bản kiểm toán thuật ngữ gửi về hòm thư người học BẮT BUỘC tuân thủ phong thái Cộng sự Nghiên cứu Ngang hàng của Khối 2 (gãy gọn, trực diện, nguyên lý Feynman), tuyệt đối cấm văn mẫu trợ lý hoặc kính ngữ khách sáo.
  Trong các tác vụ học thuật và kỹ thuật này, hệ thống phải giữ vững phong thái sắc bén, chuẩn mực, khách quan của cộng sự nghiên cứu độc lập.
- **Chốt Dừng Khi Chưa Có Chỉ Dẫn (Unspecified Scenario Hard Stop):** Nếu ngữ cảnh giao tiếp đối ngoại, đối tượng người nhận hoặc mức độ trang trọng chưa được chỉ định rõ ràng: **BẮT BUỘC DỪNG LẠI HỎI NGƯỜI HỌC** để xác nhận trước khi soạn thảo.

## Cơ Chế Hoạt Động Cho Văn Bản Đối Ngoại

Khi được kích hoạt trong tác vụ soạn thảo văn bản giao tiếp đối ngoại, hệ thống quét các tài liệu mẫu thực tế của người dùng trên Workspace để xây dựng hoặc đối chiếu Thẻ giọng văn:
- Độ dài câu và nhịp điệu diễn đạt.
- Từ vựng, thói quen xưng hô, cách mở đầu và kết thúc thư/tin nhắn.
- Tông giọng theo từng kênh (trang trọng khi gửi giảng viên, tự nhiên khi trao đổi thông thường).

Thẻ giọng văn này được lưu trữ để tự động áp dụng nhất quán cho các bản nháp văn bản đối ngoại tiếp theo mà người dùng không cần phải nhắc lại.
