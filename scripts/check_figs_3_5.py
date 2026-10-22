# -*- coding: utf-8 -*-
with open("scripts/gen_clean_3_5.py", "r", encoding="utf-8") as f:
    lines = f.readlines()
for i, line in enumerate(lines[:100]):
    if "fig_" in line or "Mo_Phong" in line or "Goc" in line:
        print(f"{i+1}: {line.strip()}")
