# -*- coding: utf-8 -*-
"""
Test Suite: Kiểm thử Kiến trúc Offscreen Clipboard & Event Shield cho Spark Visual Cockpit MV3
"""
import os
import json
import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

def test_offscreen_architecture():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ext_dir = os.path.join(base_dir, "spark-visual-cockpit-v2.0.0")
    
    manifest_path = os.path.join(ext_dir, "manifest.json")
    offscreen_html = os.path.join(ext_dir, "offscreen.html")
    offscreen_js = os.path.join(ext_dir, "offscreen.js")
    bg_path = os.path.join(ext_dir, "background.js")
    helper_path = os.path.join(ext_dir, "drive-clipboard-helper.js")
    content_path = os.path.join(ext_dir, "content.js")
    
    errors = []
    
    # 1. Manifest
    with open(manifest_path, "r", encoding="utf-8") as f:
        manifest = json.load(f)
    perms = manifest.get("permissions", [])
    if "offscreen" not in perms:
        errors.append("Manifest FAIL: Thiếu 'offscreen' trong permissions.")
    if "clipboardWrite" not in perms:
        errors.append("Manifest FAIL: Thiếu 'clipboardWrite' trong permissions.")
        
    # 2. Offscreen files
    if not os.path.exists(offscreen_html):
        errors.append("Offscreen FAIL: Không tìm thấy offscreen.html.")
    if not os.path.exists(offscreen_js):
        errors.append("Offscreen FAIL: Không tìm thấy offscreen.js.")
    else:
        with open(offscreen_js, "r", encoding="utf-8") as f:
            ojs_code = f.read()
        if "document.execCommand('copy')" not in ojs_code and 'execCommand("copy")' not in ojs_code:
            errors.append("Offscreen FAIL: offscreen.js thiếu document.execCommand('copy').")
            
    # 3. Background.js
    with open(bg_path, "r", encoding="utf-8") as f:
        bg_code = f.read()
    if "chrome.offscreen.createDocument" not in bg_code:
        errors.append("Background FAIL: Thiếu khởi tạo chrome.offscreen.createDocument trong background.js.")
    if "SPARK_FORCE_COPY" not in bg_code:
        errors.append("Background FAIL: Thiếu xử lý tin nhắn SPARK_FORCE_COPY.")
        
    # 4. Helper script
    with open(helper_path, "r", encoding="utf-8") as f:
        helper_code = f.read()
    if "stopImmediatePropagation" not in helper_code:
        errors.append("Helper FAIL: Thiếu e.stopImmediatePropagation() để chặn Google Drive cướp phím Ctrl+C.")
    if "KeyC" not in helper_code and "keyCode === 67" not in helper_code:
        errors.append("Helper FAIL: Thiếu nhận diện phím toàn cầu (e.code === 'KeyC' / keyCode 67) chống xung đột bộ gõ tiếng Việt Unikey/EVKey.")
        
    # 5. Content.js
    with open(content_path, "r", encoding="utf-8") as f:
        content_code = f.read()
    if "SPARK_DO_COPY" not in content_code and "SPARK_FORCE_COPY" not in content_code:
        errors.append("Content FAIL: Thiếu listener xử lý copy.")
        
    if errors:
        print("\n" + "="*70)
        print("KIỂM THỬ OFFSCREEN CLIPBOARD: FAIL (CÁC MẮT XÍCH CẦN BỔ SUNG)")
        for err in errors:
            print(f"- {err}")
        print("="*70 + "\n")
        sys.exit(1)
        
    print("\n" + "="*70)
    print("ALL ASSERTION CHECKS PASSED: KIẾN TRÚC OFFSCREEN CLIPBOARD HOÀN HẢO 100%")
    print("="*70 + "\n")

if __name__ == "__main__":
    test_offscreen_architecture()
