---
name: nlm-skill
description: 'Expert guide for the Gemini Notebook (formerly Google NotebookLM) CLI (`nlm`) and MCP server - interfaces for Gemini Notebook. Use this skill when users want to interact with Gemini Notebook programmatically, including: creating/managing notebooks, checking plan usage and quota windows, adding sources (URLs, YouTube, text, Google Drive), generating content (podcasts, reports, interactive reports, quizzes, flashcards, mind maps, slides, infographics, videos, data tables), conducting research, chatting with sources, or automating Gemini Notebook workflows. Triggers on mentions of "nlm", "notebooklm", "Gemini Notebook", "plan usage", "quota", "podcast generation", "audio overview", "interactive report", "lesson report", "refactor document", "critique draft", or any Gemini Notebook-related automation task.'
version: "0.15.5"
---

# Gemini Notebook CLI & MCP Expert

Cẩm nang điều phối Gemini Notebook (trước đây là Google NotebookLM) thông qua hai giao diện: giao diện dòng lệnh `nlm` CLI và máy chủ giao thức MCP.

## 1. Phát Hiện Công Cụ & Lựa Chọn Bề Mặt (CRITICAL)

**Luôn kiểm tra công cụ sẵn có trước khi thực thi:**

1. **Kiểm tra công cụ MCP**: Tìm kiếm các tiền tố `mcp__gemini-notebook-mcp__*`, `mcp__notebooklm_mcp__*`, hoặc `mcp_gemini_notebook_mcp_*`.
2. **Theo chỉ định tường minh**: Nếu người dùng yêu cầu rõ CLI hoặc MCP, thực thi đúng bề mặt đó.
3. **Quy tắc phân định khi có cả hai:**
   - Dùng **MCP** cho các thao tác sổ ghi chép nội bộ và tải xuống trong thư mục download cấu hình.
   - Dùng **CLI** khi cần cờ `--profile` riêng biệt mà không muốn đổi tài khoản mặc định của MCP, hoặc khi ghi tệp ra ngoài thư mục download của MCP.
4. **Quy tắc chuyển hồ sơ tài khoản (Profile Switching):**
   - Kiểm tra tài khoản đang hoạt động trước các thao tác đột biến: `nlm login profile list`.
   - Xem tài khoản mặc định của MCP: `nlm config get auth.default_profile`.

```
has_mcp_tools = check_available_tools()
has_cli = check_bash_available()

if user_named_mcp_or_cli:
    use_that_surface()
elif needs_workspace_output_outside_mcp_root or needs_explicit_profile_without_switching_default:
    use_cli()
elif has_mcp_tools:
    use_mcp()
elif has_cli:
    use_cli()
```

---

## 2. Tra Cứu Nhanh (Quick Reference)

Chạy `nlm --ai` để lấy tài liệu tối ưu hóa cho AI của toàn bộ tính năng CLI.

```bash
nlm --help              # Liệt kê toàn bộ lệnh
nlm <command> --help    # Tra cứu cờ và đối số của lệnh cụ thể
nlm --ai                # Tài liệu toàn diện dành cho Agent (KHUYẾN NGHỊ)
nlm usage               # Kiểm tra hạn ngạch rolling và weekly reset
nlm usage --json        # Xuất dữ liệu hạn ngạch định dạng JSON
```

---

## 3. Quy Tắc Bất Biến Cốt Lõi (Critical Invariants)

1. **Xác thực khi cần thiết**: Chạy `nlm login` cho thiết lập ban đầu hoặc khi cookie hết hạn. Đừng nhầm lẫn lỗi mạng với hết hạn phiên (`auth_status="unverified"`).
2. **Tự động phục hồi xác thực**: CLI tích hợp cơ chế tự phục hồi 3 tầng (`CSRF refresh` -> `Token reload` -> `Headless Auth`) và tự thử lại 3 lần với lỗi máy chủ.
3. **⚠️ XÁC NHẬN TRƯỚC KHI XÓA**: Thao tác xóa là **không thể hoàn tác**. Mọi lệnh xóa bắt buộc phải hỏi người dùng xác nhận rõ ràng trước khi thêm cờ `--confirm` / `confirm=True`.
4. **Phê duyệt trước khi sinh nội dung (Studio Create)**: Mọi thao tác `studio_create` bắt buộc phải có sự chấp thuận từ người dùng (`--confirm`).
5. **Nghiên cứu cần đích đến**: Luôn truyền `--notebook-id <id>` cho sổ có sẵn hoặc `--title <title>` để tạo sổ mới.
6. **Thu thập ID trả về**: Các lệnh tạo/khởi chạy trả về ID UUID cần lưu để dùng cho các bước kế tiếp.
7. **Sử dụng bí danh (Aliases)**: Rút gọn UUID dài bằng `nlm alias set <name> <uuid>`.
8. **TUYỆT ĐỐI KHÔNG mở REPL**: Không chạy `nlm chat start` vì lệnh này mở REPL tương tác chặn luồng của Agent. Dùng `nlm notebook query` cho hỏi đáp một lượt.
9. **Kiểm tra hạn ngạch trước tác vụ nặng**: Chạy `nlm usage` (MCP: `usage_get`) trước các tác vụ suy luận sâu hoặc sinh video/bài giảng tương tác tốn token.

---

## 4. Cây Quyết Định Quy Trình (Workflow Decision Tree)

```
Yêu cầu của người học...
│
├─► Khởi tạo lần đầu
│   └─► nlm login → nlm notebook create "Tiêu đề"
│
├─► Thêm nguồn tài liệu vào Sổ ghi chép
│   ├─► Từ URL/Webpage → nlm source add <nb-id> --url "https://..."
│   ├─► Từ YouTube → nlm source add <nb-id> --url "https://youtube.com/..."
│   ├─► Từ Văn bản dán trực tiếp → nlm source add <nb-id> --text "nội dung" --title "Tiêu đề"
│   ├─► Từ Google Drive → nlm source add <nb-id> --drive <doc-id> --type doc
│   └─► Khám phá nguồn nghiên cứu mới → nlm research start "truy vấn" --notebook-id <nb-id>
│
├─► Kiểm tra hạn ngạch & tính khả dụng
│   └─► nlm usage (MCP: usage_get)
│
├─► Sinh nội dung Studio từ tài liệu gốc (Xem references/studio-prompting-guide.md)
│   ├─► Podcast / Audio → nlm audio create <nb-id> --confirm
│   ├─► Báo cáo / Chuyên khảo → nlm report create <nb-id> --confirm
│   ├─► Câu hỏi trắc nghiệm & Thẻ ghi nhớ → nlm quiz/flashcards create <nb-id> --confirm
│   ├─► Sơ đồ tư duy / Trình chiếu / Infographic → nlm mindmap/slides/infographic create <nb-id> --confirm
│   ├─► Video bài giảng → nlm video create <nb-id> --confirm
│   └─► Bảng dữ liệu trích xuất → nlm data-table create <nb-id> "mô tả" --confirm
│
├─► Tra cứu tài liệu (Hỏi đáp nguồn)
│   └─► nlm notebook query <nb-id> "câu hỏi" (Dùng --conversation-id để tiếp nối)
│
├─► Kiểm tra tiến độ hoàn thành Studio
│   └─► nlm studio status <nb-id>
│
└─► Quản lý & Dọn dẹp
    ├─► Liệt kê sổ → nlm notebook list
    ├─► Liệt kê nguồn → nlm source list <nb-id>
    ├─► Xóa nguồn → nlm source delete <source-id> --confirm (Sau khi hỏi người dùng)
    └─► Xóa sổ → nlm notebook delete <nb-id> --confirm (Sau khi hỏi người dùng)
```

---

## 5. Bản Đồ Điều Hướng Tài Liệu Chi Tiết (References Navigation)

Để tuân thủ nguyên lý Tiết lộ Lũy tiến (Progressive Disclosure) và giữ cửa sổ ngữ cảnh luôn tối ưu, toàn bộ thông số kỹ thuật chi tiết được phân tách vào thư mục `references/`:

| Chuyên đề kỹ thuật | Tệp tài liệu tra cứu chuyên sâu | Nội dung & Khi nào cần kích hoạt |
| :--- | :--- | :--- |
| **Đặc tả Lệnh & Cờ Đầy Đủ** | [command_reference.md](references/command_reference.md) | Tra cứu toàn bộ cú pháp lệnh, cờ tham số, batch operations, pipelines, tags, và alias. |
| **Quy Trình Nghiên Cứu & Tinh Chỉnh** | [workflows.md](references/workflows.md) | 17 quy trình làm việc chuẩn hóa: refactor tài liệu, nghiên cứu học thuật có giới hạn, tạo bài giảng tương tác. |
| **Nghệ Thuật Nhắc Studio** | [studio-prompting-guide.md](references/studio-prompting-guide.md) | Hướng dẫn viết `--focus` prompt tối ưu cho từng thể loại: Audio, Report, Slides, Video, Infographic. |
| **Mẫu Lời Nhắc Thực Chiến** | [studio-prompt-examples.md](references/studio-prompt-examples.md) | Thư viện mẫu prompt sẵn sàng chạy cho các loại ấn phẩm Studio. |
| **Xử Lý Sự Cố & Lỗi Xác Thực** | [troubleshooting.md](references/troubleshooting.md) | Khắc phục lỗi đăng nhập, cookie hỏng, giới hạn tần suất (rate limits) và khôi phục kết nối. |
| **Máy Chủ MCP Từ Xa & Bảo Mật** | [remote-mcp.md](references/remote-mcp.md) | Cấu hình máy chủ `notebooklm-mcp`, thiết lập cache hội thoại và bảo mật token từ xa. |

---

## 6. Các Mẫu Lệnh Thường Dùng (High-Impact Patterns)

### Thêm nguồn Google Drive và Đồng bộ
```bash
# Thêm file từ Drive vào sổ ghi chép
nlm source add <nb-id> --drive <file-id> --type doc

# Đồng bộ lại khi file trên Drive có cập nhật mới
nlm source sync <nb-id> <source-id>
```

### Nghiên cứu và Nhập nguồn tự động
```bash
# Bắt đầu nghiên cứu
nlm research start "heterojunction laser diode rate equations" --notebook-id <nb-id>

# Kiểm tra trạng thái nghiên cứu
nlm research status <task-id>

# Nhập các nguồn tìm được
nlm research import <task-id>
```

### Sinh Báo cáo Chuyên đề & Kiểm tra Trạng thái
```bash
# Sinh báo cáo chuyên khảo có chỉ đạo trọng tâm
nlm report create <nb-id> --format "Briefing Doc" --focus "Trích xuất mô hình toán và điều kiện ngưỡng laser" --confirm

# Theo dõi tiến trình cho đến khi hoàn tất
nlm studio status <nb-id>

# Tải ấn phẩm về thư mục chỉ định
nlm studio download <nb-id> <artifact-id> --output-dir "D:/antigravity/academic-research-engine/output/reports"
```
