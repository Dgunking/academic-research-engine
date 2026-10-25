# -*- coding: utf-8 -*-
"""
Test Suite: Kiểm thử Nhận diện Vùng chọn Sâu (Deep Selection / Shadow DOM)
& Cơ chế Kích hoạt Sao chép Hai chiều (Bidirectional Copy Trigger)
"""
import os
import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

def test_deep_selection_and_copy_trigger():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ext_dir = os.path.join(base_dir, "spark-visual-cockpit-v2.0.0")
    
    content_path = os.path.join(ext_dir, "content.js")
    helper_path = os.path.join(ext_dir, "drive-clipboard-helper.js")
    
    errors = []
    
    # 1. Helper Script checks
    with open(helper_path, "r", encoding="utf-8") as f:
        helper_code = f.read()
        
    if "getDeepSelectedText" not in helper_code:
        errors.append("Helper FAIL: Thiếu hàm trích xuất vùng chọn sâu getDeepSelectedText() để xuyên qua Shadow DOM / Canvas / Viewer layer.")
    if "getComposedRanges" not in helper_code and "shadowRoot" not in helper_code:
        errors.append("Helper FAIL: getDeepSelectedText thiếu cơ chế duyệt shadowRoot / getComposedRanges.")
    if "SPARK_TRIGGER_COPY" not in helper_code:
        errors.append("Helper FAIL: Thiếu message listener đón lệnh SPARK_TRIGGER_COPY từ nút bấm ở cửa sổ cha.")
    if "SPARK_COPY_CONFIRMED" not in helper_code:
        errors.append("Helper FAIL: Thiếu thông điệp SPARK_COPY_CONFIRMED gửi lên cửa sổ cha khi lệnh copy thực thi thành công.")
        
    # Check that Ctrl+C doesn't abort prematurely if sel is empty and does NOT suppress native copy with e.preventDefault()
    kd_match = re.search(r"function handleKeyDown\s*\([^)]*\)\s*\{([^}]+(?:\{[^}]*\}[^}]*)*)\}", helper_code)
    if kd_match:
        kd_body = kd_match.group(1)
        if "if (!sel) return;" in kd_body or "if (!sel || !sel.trim()) return;" in kd_body:
            errors.append("Helper FAIL: handleKeyDown bị chặn sớm bởi 'if (!sel) return;'. Trong PDF viewer, sel có thể trả về rỗng trong JS DOM dù người dùng đã bôi đen màn hình, phải gọi document.execCommand('copy') vô điều kiện!")
        if re.search(r"^\s*e\.preventDefault\(\)\s*;", kd_body, re.MULTILINE):
            errors.append("Helper FAIL: handleKeyDown không được gọi e.preventDefault() vì làm triệt tiêu lệnh Copy mặc định của Chromium C++ trong PDFium.")
        if "execCommand('copy')" not in kd_body and 'execCommand("copy")' not in kd_body:
            errors.append("Helper FAIL: handleKeyDown thiếu document.execCommand('copy') trực tiếp.")
    else:
        errors.append("Helper FAIL: Không tìm thấy function handleKeyDown.")

    # 2. Content.js checks
    with open(content_path, "r", encoding="utf-8") as f:
        content_code = f.read()
        
    if "SPARK_TRIGGER_COPY" not in content_code:
        errors.append("Content.js FAIL: Nút Copy thiếu cơ chế postMessage SPARK_TRIGGER_COPY xuống iframe.")
    if "SPARK_COPY_CONFIRMED" not in content_code:
        errors.append("Content.js FAIL: Content.js thiếu listener đón SPARK_COPY_CONFIRMED để kích hoạt phản hồi xanh.")
        
    if errors:
        print("\n" + "="*70)
        print("KIỂM THỬ NHẬN DIỆN VÙNG CHỌN SÂU: FAIL")
        for err in errors:
            print(f"- {err}")
        print("="*70 + "\n")
        assert False, f"{len(errors)} lỗi kiểm định nhận diện vùng chọn sâu"
        
    print("\n" + "="*70)
    print("ALL ASSERTION CHECKS PASSED: NHẬN DIỆN VÙNG CHỌN SÂU & TRIGGER 2 CHIỀU HOÀN HẢO 100%")
    print("="*70 + "\n")

if __name__ == "__main__":
    test_deep_selection_and_copy_trigger()
