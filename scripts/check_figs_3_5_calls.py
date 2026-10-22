# -*- coding: utf-8 -*-
import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

with open("scripts/gen_clean_3_5.py", "r", encoding="utf-8") as f:
    lines = f.readlines()
for i, line in enumerate(lines):
    if "add_figure(" in line:
        block = "".join(lines[i:i+4])
        print(f"Line {i+1}: {block.strip()}\n")
