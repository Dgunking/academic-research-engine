# -*- coding: utf-8 -*-
import glob
import re

for s in ['3_1', '3_2', '3_3', '3_4', '3_5']:
    path = f"scripts/generate_simulations_muc_{s}_nano.py"
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    print(f"=== {path} ===")
    for i, line in enumerate(lines):
        if "legend(" in line or "annotate(" in line or "set_ylim" in line or "set_xlim" in line:
            print(f"  Line {i+1}: {line.strip()}")
