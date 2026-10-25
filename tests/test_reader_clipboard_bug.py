# -*- coding: utf-8 -*-
"""
Test Suite: Kiểm thử Tái hiện Lỗi Clipboard & Focus Trapping trong Spark Reader Overlay
Quy trình: ENGINEERING_DISCIPLINE_WORKFLOW.md [PHA 1: Bước 1.1]
Mục tiêu: Đảm bảo script báo FAIL trước khi thực hiện can thiệp mã nguồn (Atomic Fix).
"""

import os
import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

def test_reader_clipboard_and_focus():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    content_js_path = os.path.join(base_dir, "spark-visual-cockpit-v2.0.0", "content.js")
    styles_css_path = os.path.join(base_dir, "spark-visual-cockpit-v2.0.0", "styles.css")
    
    assert os.path.exists(content_js_path), f"FAIL: Không tìm thấy {content_js_path}"
    assert os.path.exists(styles_css_path), f"FAIL: Không tìm thấy {styles_css_path}"
    
    with open(content_js_path, "r", encoding="utf-8") as f:
        content_js = f.read()
        
    with open(styles_css_path, "r", encoding="utf-8") as f:
        styles_css = f.read()

    errors = []

    # 1. Kiểm tra Cross-Origin Permissions Policy trên thẻ iframe
    # Thẻ iframe trong ReaderOverlayEngine bắt buộc phải có chỉ thị 'clipboard-write' và 'clipboard-read'
    iframe_allow_matches = re.findall(r"frame\.setAttribute\(\s*['\"]allow['\"]\s*,\s*['\"]([^'\"]+)['\"]\s*\)", content_js)
    if not iframe_allow_matches:
        errors.append("Mắt xích 1 FAIL: Không tìm thấy thiết lập frame.setAttribute('allow', ...) trong content.js")
    else:
        allow_val = iframe_allow_matches[0]
        if "clipboard-write" not in allow_val or "clipboard-read" not in allow_val:
            errors.append(
                f"Mắt xích 1 FAIL: Iframe 'allow' attribute ('{allow_val}') thiếu chỉ thị Cross-Origin 'clipboard-write; clipboard-read'. "
                f"Chromium Permissions Policy sẽ chặn toàn bộ lệnh ghi chép Clipboard từ tài liệu nhúng drive.google.com."
            )
        else:
            print("[PASS] Mắt xích 1: Iframe Permissions Policy đã ủy quyền clipboard-write & clipboard-read hợp lệ.")

    # 2. Kiểm tra Focus Management & Keyboard Trapping Prevention
    # Thẻ iframe cần có tabindex='0' và cơ chế chuyển giao tiêu điểm (focus routing) khi tương tác với card/frame
    has_tabindex = "frame.setAttribute('tabindex', '0')" in content_js or 'frame.tabIndex = 0' in content_js
    has_focus_routing = (
        ("frame.focus()" in content_js or "card.addEventListener" in content_js) and
        ("pointerdown" in content_js or "focus" in content_js)
    )
    # Cụ thể: Reader card hoặc frame phải kích hoạt focus vào frame khi tương tác để tránh Focus Trapping ở parent window
    has_card_focus_listener = bool(re.search(r"card\.addEventListener\(\s*['\"](?:pointerdown|click)['\"].*?frame\.focus\(\)", content_js, re.DOTALL)) or \
                              bool(re.search(r"frame\.addEventListener\(\s*['\"](?:pointerenter|focus)['\"].*?frame\.focus\(\)", content_js, re.DOTALL))
    
    if not (has_tabindex and has_card_focus_listener):
        reasons = []
        if not has_tabindex:
            reasons.append("frame thiếu tabindex='0'")
        if not has_card_focus_listener:
            reasons.append("thiếu event listener ủy quyền focus vào iframe khi click/hover vào PDF section")
        errors.append(f"Mắt xích 2 FAIL: Focus Routing chưa hoàn thiện ({', '.join(reasons)}). Khi người dùng ấn Ctrl+C, tiêu điểm vẫn bị kẹt ở cửa sổ cha thay vì nạp vào iframe.")
    else:
        print("[PASS] Mắt xích 2: Tiêu điểm bàn phím được ủy quyền chính xác cho iframe qua tabindex và focus listener.")

    # 3. Kiểm tra Selection Invalidation do CSS header
    # Quy tắc .spark-pdf-section-header không được khóa cứng 'user-select: none !important;'
    header_css_match = re.search(r"\.spark-pdf-section-header\s*\{([^}]+)\}", styles_css)
    if header_css_match:
        header_body = header_css_match.group(1)
        if re.search(r"user-select:\s*none\s*!important", header_body):
            errors.append(
                "Mắt xích 3 FAIL: .spark-pdf-section-header chứa thuộc tính 'user-select: none !important;'. "
                "Điều này làm hủy bỏ vùng chọn (Window Selection Collapse) khi chuột quét chệch lên phía mép trên của tài liệu."
            )
        else:
            print("[PASS] Mắt xích 3: Header bài giảng không áp đặt user-select: none !important, bảo toàn vùng chọn.")
    else:
        errors.append("Mắt xích 3 FAIL: Không tìm thấy quy tắc CSS cho .spark-pdf-section-header trong styles.css")

    if errors:
        print("\n" + "="*70)
        print("KẾT QUẢ KIỂM THỬ TÁI HIỆN LỖI: FAIL (CHỨNG MINH 3 ĐIỂM NGHẼN)")
        for err in errors:
            print(f"- {err}")
        print("="*70 + "\n")
        sys.exit(1)
    
    print("\n" + "="*70)
    print("ALL ASSERTION CHECKS PASSED: HỆ THỐNG ĐÃ ĐƯỢC VÁ HOÀN TOÀN 100%")
    print("="*70 + "\n")

if __name__ == "__main__":
    test_reader_clipboard_and_focus()
