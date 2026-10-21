# -*- coding: utf-8 -*-
import sys, os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, r'd:\antigravity\academic-research-engine\.agents\skills\monograph-pdf-publisher\scripts')
import hust_pdf_engine as he

captured_story = []
class CaptureDoc:
    def __init__(self, path):
        pass
    def build(self, story):
        global captured_story
        captured_story = story

# Đọc mã nguồn
with open('output/build_monograph_muc_2_4_nano.py', 'r', encoding='utf-8') as f:
    code = f.read()

ns = {}
exec(code, ns)
ns['he'].BookmarkDocTemplate = CaptureDoc
ns['build_pdf']()

print(f"Captured {len(captured_story)} flowables.")

try:
    he.assert_monograph_text_compliance(captured_story, require_5_blocks=True)
    print("PASS 100%! All assertions compliant!")
except AssertionError as err:
    print("FAILED ASSERTIONS:")
    print(err)

