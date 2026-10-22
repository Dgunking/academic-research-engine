# -*- coding: utf-8 -*-
import sys
import os

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

sys.path.insert(0, os.path.abspath("."))
from scripts.hdir_engine import DICG2Engine

dicg = DICG2Engine(course_dir=r"G:\My Drive\NotebookLM - Academic Knowledge Base\Cơ sở vật lý và công nghệ nano")
all_pass = True
for s in ['3.1', '3.2', '3.3', '3.4', '3.5']:
    res = dicg.layer4_blueprint_schema_gating(f"data/BLUEPRINT_MUC_{s}_NANO.json")
    print(f"Section {s}: pass={res.get('pass')}, pages={res.get('estimated_pages')}, mpts={res.get('mpt_count')}")
    if not res.get('pass'):
        all_pass = False

print(f"Overall Blueprint Validation: {'PASS 100%' if all_pass else 'FAIL'}")
