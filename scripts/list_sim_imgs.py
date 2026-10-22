# -*- coding: utf-8 -*-
import sys
import os
import pymupdf

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

kho_anh = r"G:\My Drive\NotebookLM - Academic Knowledge Base\Cơ sở vật lý và công nghệ nano\Kho_Hinh_Anh"
sim_imgs = sorted([f for f in os.listdir(kho_anh) if ("Mo_Phong" in f) and f.endswith(".png") and "Muc_3." in f])

print(f"Total Chapter 3 simulation images in Kho_Hinh_Anh: {len(sim_imgs)}")
for f in sim_imgs:
    fp = os.path.join(kho_anh, f)
    print(f" - {f} ({round(os.path.getsize(fp)/1024, 1)} KB)")
