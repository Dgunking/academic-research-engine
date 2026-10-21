"""
Academic Gate Hook for Antigravity Lifecycle Hooks (Workspace Root Wrapper)
Chặn bắt, kiểm toán an toàn và xác thực chuẩn mực trước/sau khi gọi công cụ (write_to_file, replace_file_content).
Tuân thủ nghiêm ngặt tài liệu thiết kế: AI Agent Giảng Dạy & Sáng Tạo Trên Antigravity.md.
"""
import sys
import os

# Delegate directly to .agents/scripts/academic_gate_hook.py
hook_impl = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".agents", "scripts", "academic_gate_hook.py")
if os.path.exists(hook_impl):
    with open(hook_impl, "r", encoding="utf-8") as f:
        code = f.read()
    exec(compile(code, hook_impl, "exec"))
else:
    # Fallback to local import if needed
    from academic_gate_hook import main
    main()
