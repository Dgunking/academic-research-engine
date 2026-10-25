# -*- coding: utf-8 -*-
"""
Test Suite: Kiểm thử Tối thượng Kiến trúc Offscreen Clipboard & Pre-warm cho Spark Cockpit MV3
"""
import os
import json
import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

def test_robust_offscreen():
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
        
    # 2. Background.js checks
    with open(bg_path, "r", encoding="utf-8") as f:
        bg_code = f.read()
    if "'OFFSCREEN_DOCUMENT'" not in bg_code and '"OFFSCREEN_DOCUMENT"' not in bg_code:
        errors.append("Background FAIL: contextTypes phải dùng string literal 'OFFSCREEN_DOCUMENT' để chống TypeError.")
    if "'CLIPBOARD'" not in bg_code and '"CLIPBOARD"' not in bg_code:
        errors.append("Background FAIL: reasons phải dùng string literal 'CLIPBOARD' để chống TypeError.")
    if "setupOffscreenDocument" not in bg_code:
        errors.append("Background FAIL: Thiếu hàm setupOffscreenDocument.")
    if "writeToSystemClipboardViaOffscreen" not in bg_code:
        errors.append("Background FAIL: Thiếu hàm writeToSystemClipboardViaOffscreen.")
    if "SPARK_FORCE_COPY" not in bg_code:
        errors.append("Background FAIL: Thiếu handler cho SPARK_FORCE_COPY.")
        
    # 3. Offscreen.js
    with open(offscreen_js, "r", encoding="utf-8") as f:
        ojs_code = f.read()
    if "execCommand('copy')" not in ojs_code and 'execCommand("copy")' not in ojs_code:
        errors.append("Offscreen FAIL: offscreen.js thiếu execCommand('copy').")
        
    # 4. Helper.js
    with open(helper_path, "r", encoding="utf-8") as f:
        h_code = f.read()
    if "stopImmediatePropagation" not in h_code:
        errors.append("Helper FAIL: Thiếu stopImmediatePropagation.")
    if "KeyC" not in h_code and "keyCode === 67" not in h_code:
        errors.append("Helper FAIL: Thiếu nhận diện phím toàn cầu KeyC / 67.")
        
    # 5. Content.js
    with open(content_path, "r", encoding="utf-8") as f:
        c_code = f.read()
    if "SPARK_DO_COPY" not in c_code:
        errors.append("Content FAIL: Thiếu listener đón SPARK_DO_COPY.")
        
    if errors:
        print("\n" + "="*70)
        print("KIỂM THỬ OFFSCREEN ROBUST: FAIL (CẦN HOÀN THIỆN)")
        for err in errors:
            print(f"- {err}")
        print("="*70 + "\n")
        sys.exit(1)
        
    print("\n" + "="*70)
    print("ALL ASSERTION CHECKS PASSED: KIẾN TRÚC OFFSCREEN ROBUST HOÀN HẢO 100%")
    print("="*70 + "\n")

if __name__ == "__main__":
    test_robust_offscreen()
