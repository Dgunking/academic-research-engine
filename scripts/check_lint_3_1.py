# -*- coding: utf-8 -*-
import sys
import os

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

sys.path.insert(0, r"d:\antigravity\academic-research-engine\.agents\skills\monograph-pdf-publisher\scripts")
sys.path.insert(0, r"d:\antigravity\academic-research-engine\scripts")
import hust_pdf_engine as he

import gen_clean_3_1

# Monkey-patch doc.build in gen_clean_3_1 to just run the linter and report
def mock_build(self, flowables, filename=None, canvasmaker=None):
    flowables_list = list(flowables)
    try:
        he.assert_monograph_text_compliance(flowables_list, require_5_blocks=True)
        print("LINTER PASS: 100% compliant with assert_monograph_text_compliance!")
    except AssertionError as e:
        print("LINTER ERRORS FOUND:")
        print(e)

he.BookmarkDocTemplate.build = mock_build

gen_clean_3_1.build_monograph_muc_3_1()
