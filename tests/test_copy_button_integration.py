# -*- coding: utf-8 -*-
"""
Test Suite: Kiểm thử Tích hợp Nút Bấm Copy Chuyên Dụng (Dedicated Copy Button)
& Phản hồi Thị giác Trạng thái Vùng chọn trong Spark Reader Overlay
"""
import os
import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

def test_copy_button_integration():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ext_dir = os.path.join(base_dir, "spark-visual-cockpit-v2.0.0")
    
    content_path = os.path.join(ext_dir, "content.js")
    styles_path = os.path.join(ext_dir, "styles.css")
    helper_path = os.path.join(ext_dir, "drive-clipboard-helper.js")
    bg_path = os.path.join(ext_dir, "background.js")
    
    errors = []
    
    # 1. Content.js checks
    with open(content_path, "r", encoding="utf-8") as f:
        content_code = f.read()
        
    if "spark-btn-copy-pdf" not in content_code:
        errors.append("Content.js FAIL: Thiếu class 'spark-btn-copy-pdf' cho nút Copy trên header card PDF.")
    if "executeSystemCopy" not in content_code:
        errors.append("Content.js FAIL: Thiếu hàm executeSystemCopy() thực thi sao chép hệ thống đa tầng.")
    if "updateCopyButtonsState" not in content_code:
        errors.append("Content.js FAIL: Thiếu hàm updateCopyButtonsState() để cập nhật trạng thái phát sáng khi có vùng chọn.")
    if "createCopyButton" not in content_code:
        errors.append("Content.js FAIL: Thiếu hàm createCopyButton() khởi tạo nút sao chép.")
    if "has-selection" not in content_code:
        errors.append("Content.js FAIL: Thiếu xử lý class 'has-selection' khi phát hiện vùng chọn tài liệu.")
    if "copied" not in content_code:
        errors.append("Content.js FAIL: Thiếu trạng thái 'copied' để phản hồi thị giác xanh sau khi sao chép thành công.")
        
    # 2. Styles.css checks
    with open(styles_path, "r", encoding="utf-8") as f:
        styles_code = f.read()
        
    if ".spark-btn-copy-pdf" not in styles_code:
        errors.append("Styles.css FAIL: Thiếu quy tắc CSS cho '.spark-btn-copy-pdf'.")
    if ".spark-btn-copy-pdf.has-selection" not in styles_code and ".has-selection" not in styles_code:
        errors.append("Styles.css FAIL: Thiếu styling trạng thái phát sáng '.has-selection'.")
    if ".spark-btn-copy-pdf.copied" not in styles_code and ".copied" not in styles_code:
        errors.append("Styles.css FAIL: Thiếu styling trạng thái thành công '.copied'.")
        
    # 3. Helper Script checks
    with open(helper_path, "r", encoding="utf-8") as f:
        helper_code = f.read()
    if "SPARK_SELECTION_CACHE" not in helper_code:
        errors.append("Helper FAIL: Thiếu sự kiện SPARK_SELECTION_CACHE.")
        
    if errors:
        print("\n" + "="*70)
        print("KIỂM THỬ NÚT BẤM COPY CHUYÊN DỤNG: FAIL")
        for err in errors:
            print(f"- {err}")
        print("="*70 + "\n")
        assert False, f"{len(errors)} lỗi kiểm định nút Copy"
        
    print("\n" + "="*70)
    print("ALL ASSERTION CHECKS PASSED: NÚT BẤM COPY CHUYÊN DỤNG ĐÃ ĐƯỢC TÍCH HỢP HOÀN CHỈNH 100%")
    print("="*70 + "\n")

if __name__ == "__main__":
    test_copy_button_integration()
