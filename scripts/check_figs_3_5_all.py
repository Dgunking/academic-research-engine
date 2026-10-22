# -*- coding: utf-8 -*-
with open("scripts/gen_clean_3_5.py", "r", encoding="utf-8") as f:
    for i, line in enumerate(f):
        if "add_figure" in line or "os.path.join(IMG_DIR" in line:
            print(f"{i+1}: {line.strip()}")
