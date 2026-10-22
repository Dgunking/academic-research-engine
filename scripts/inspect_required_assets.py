# -*- coding: utf-8 -*-
import sys
import re

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

for s in ['3_2', '3_3', '3_4', '3_5']:
    path = f"scripts/gen_clean_{s}.py"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    figs = re.findall(r"\[(?:Goc|Mo_Phong)\][^\"\'\)]+\.png", content)
    figs = sorted(list(set(figs)))
    print(f"=== Section {s} references {len(figs)} figures ===")
    for fig in figs:
        print("  ", fig)
