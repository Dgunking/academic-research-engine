# -*- coding: utf-8 -*-
"""
Test Suite: Kiểm định Kiến trúc 5 Tầng Cầu nối Clipboard Đa Miền (Cross-Origin Clipboard Bridge)
Cho Google Drive Preview trong Spark Visual Cockpit v2.5.0
"""
import os
import re
import json
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

def test_clipboard_bridge():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ext_dir = os.path.join(base_dir, "spark-visual-cockpit-v2.0.0")
    
    manifest_path = os.path.join(ext_dir, "manifest.json")
    helper_path = os.path.join(ext_dir, "drive-clipboard-helper.js")
    content_path = os.path.join(ext_dir, "content.js")
    bg_path = os.path.join(ext_dir, "background.js")
    
    errors = []
    
    # 1. Manifest Checks
    with open(manifest_path, "r", encoding="utf-8") as f:
        manifest = json.load(f)
        
    perms = manifest.get("permissions", [])
    if "clipboardWrite" not in perms:
        errors.append("Manifest FAIL: Thiếu quyền 'clipboardWrite' trong permissions.")
        
    # Check helper script entry in content_scripts
    cs = manifest.get("content_scripts", [])
    helper_cs = [c for c in cs if "drive-clipboard-helper.js" in c.get("js", [])]
    if not helper_cs:
        errors.append("Manifest FAIL: Không tìm thấy entry cho drive-clipboard-helper.js trong content_scripts.")
    else:
        entry = helper_cs[0]
        matches = entry.get("matches", [])
        has_docs = any("docs.google.com" in m or "*.google.com" in m for m in matches)
        has_drive = any("drive.google.com" in m or "*.google.com" in m for m in matches)
        has_usercontent = any("googleusercontent.com" in m for m in matches)
        
        if not (has_docs and has_drive):
            errors.append(f"Manifest FAIL: matches ({matches}) thiếu docs.google.com hoặc *.google.com để bắt leaf frame hiển thị PDF.")
        if not has_usercontent:
            errors.append(f"Manifest FAIL: matches ({matches}) thiếu *.googleusercontent.com.")
        if not entry.get("all_frames", False):
            errors.append("Manifest FAIL: all_frames phải là true cho drive-clipboard-helper.js.")
        if not entry.get("match_about_blank", False):
            errors.append("Manifest FAIL: match_about_blank phải là true.")
            
    # 2. Helper Script Checks
    with open(helper_path, "r", encoding="utf-8") as f:
        helper_code = f.read()
        
    if "SPARK_FORCE_COPY" not in helper_code and "SPARK_READER_COPY" not in helper_code:
        errors.append("Helper FAIL: Thiếu lệnh postMessage gửi SPARK_FORCE_COPY lên top window.")
    if "SPARK_SELECTION_CACHE" not in helper_code:
        errors.append("Helper FAIL: Thiếu đồng bộ cache vùng chọn SPARK_SELECTION_CACHE qua selectionchange/mouseup.")
    if "createElement" not in helper_code and "MutationObserver" not in helper_code:
        errors.append("Helper FAIL: Thiếu cơ chế tiêm ủy quyền Permissions Policy (allow='clipboard-write') cho iframe con lồng nhau.")
    if "ta.select()" in helper_code or "textarea" in helper_code:
        errors.append("Helper FAIL: Phát hiện textarea/ta.select() trong helper script. Việc này làm hủy hoại vùng chọn DOM (Selection Collapse) khiến Chromium không thể dispatch sự kiện copy khi ấn Ctrl+C!")
        
    # 3. Content.js Checks
    with open(content_path, "r", encoding="utf-8") as f:
        content_code = f.read()
        
    if "SPARK_FORCE_COPY" not in content_code and "SPARK_SELECTION_CACHE" not in content_code:
        errors.append("Content.js FAIL: ReaderOverlayEngine thiếu message listener đón SPARK_FORCE_COPY / SPARK_SELECTION_CACHE.")
    if "copyTextToClipboard" not in content_code and "writeToClipboard" not in content_code:
        errors.append("Content.js FAIL: Thiếu hàm ghi clipboard chuyên trách copyTextToClipboard.")
    if "window.focus()" not in content_code:
        errors.append("Content.js FAIL: copyTextToClipboard thiếu window.focus() để giải phóng Focus Trapping khi iframe đang chiếm tiêu điểm.")
        
    # 4. Background.js Checks
    with open(bg_path, "r", encoding="utf-8") as f:
        bg_code = f.read()
    if "SPARK_FORCE_COPY" not in bg_code:
        errors.append("Background.js FAIL: Thiếu bộ chuyển tiếp tin nhắn SPARK_FORCE_COPY về active tab.")

    if errors:
        print("\n" + "="*70)
        print("KIỂM THỬ CẦU NỐI CLIPBOARD: FAIL (CÁC MẮT XÍCH CẦN BỔ SUNG)")
        for err in errors:
            print(f"- {err}")
        print("="*70 + "\n")
        sys.exit(1)
        
    print("\n" + "="*70)
    print("ALL ASSERTION CHECKS PASSED: CẦU NỐI 5 TẦNG CLIPBOARD HOÀN CHỈNH 100%")
    print("="*70 + "\n")

if __name__ == "__main__":
    test_clipboard_bridge()
