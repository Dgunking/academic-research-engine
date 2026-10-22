# -*- coding: utf-8 -*-
import os, glob
from PIL import Image
import numpy as np

img_dir = r"G:\My Drive\NotebookLM - Academic Knowledge Base\Cơ sở vật lý và công nghệ nano\Kho_Hinh_Anh"
sim_files = sorted(glob.glob(os.path.join(img_dir, "*Mo_Phong*.png")))
print(f"Total simulation images found: {len(sim_files)}")
for f in sim_files:
    im = Image.open(f)
    print(f"  {os.path.basename(f)}: size={im.size}, mode={im.mode}")
