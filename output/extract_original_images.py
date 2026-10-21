import os
import sys
import pymupdf
from PIL import Image, ImageChops
import io

sys.stdout.reconfigure(encoding="utf-8")

pdf_path = r"G:\My Drive\NotebookLM - Academic Knowledge Base\Cơ sở vật lý và công nghệ nano\Bài 2-Quantum nature.pdf"
doc = pymupdf.open(pdf_path)

output_dir = r"G:\My Drive\NotebookLM - Academic Knowledge Base\Cơ sở vật lý và công nghệ nano\Kho_Hinh_Anh"
os.makedirs(output_dir, exist_ok=True)

def autocrop(im, bg_color=None):
    if im.mode == "RGBA":
        # Check alpha channel
        bbox = im.getbbox()
        if bbox:
            im = im.crop(bbox)
        # Convert to RGB with white background
        bg = Image.new("RGB", im.size, (255, 255, 255))
        bg.paste(im, mask=im.split()[3])
        im = bg
    elif im.mode != "RGB":
        im = im.convert("RGB")
        
    # Auto-crop solid border
    bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        # add slight padding
        w, h = im.size
        pad = 2
        bbox = (max(0, bbox[0]-pad), max(0, bbox[1]-pad), min(w, bbox[2]+pad), min(h, bbox[3]+pad))
        im = im.crop(bbox)
    return im

def extract_xref(xref, target_name):
    b = doc.extract_image(xref)
    im = Image.open(io.BytesIO(b["image"]))
    im = autocrop(im)
    out_path = os.path.join(output_dir, target_name)
    im.save(out_path, format="PNG", dpi=(300, 300))
    print(f"Extracted {target_name}: size={im.size}, saved to {out_path}")

# MUC 2.2 IMAGES:
# Slide 14:
# [Goc]_Muc_2.2_Hinh_01_So_Do_Thi_Nghiem_Quang_Dien.png (xref 108)
extract_xref(108, "[Goc]_Muc_2.2_Hinh_01_So_Do_Thi_Nghiem_Quang_Dien.png")

# Slide 15:
# [Goc]_Muc_2.2_Hinh_02_Pho_Tan_Xa_Compton_Cac_Goc.png (xref 111)
extract_xref(111, "[Goc]_Muc_2.2_Hinh_02_Pho_Tan_Xa_Compton_Cac_Goc.png")
# [Goc]_Muc_2.2_Hinh_03_Bo_Tri_Thi_Nghiem_Compton.png (xref 113)
extract_xref(113, "[Goc]_Muc_2.2_Hinh_03_Bo_Tri_Thi_Nghiem_Compton.png")

# Slide 16:
# [Goc]_Muc_2.2_Hinh_04_Va_Cham_Dan_Hoi_Photon_Electron.png (xref 124)
extract_xref(124, "[Goc]_Muc_2.2_Hinh_04_Va_Cham_Dan_Hoi_Photon_Electron.png")

# Slide 18:
# [Goc]_Muc_2.2_Hinh_05_Nhieu_Xa_Tia_X_Mat_Phang_Bragg.png (xref 164)
extract_xref(164, "[Goc]_Muc_2.2_Hinh_05_Nhieu_Xa_Tia_X_Mat_Phang_Bragg.png")
# [Goc]_Muc_2.2_Hinh_06_Giao_Thoa_Song_Bragg_Tinh_The.png (xref 163)
extract_xref(163, "[Goc]_Muc_2.2_Hinh_06_Giao_Thoa_Song_Bragg_Tinh_The.png")

# Slide 19:
# [Goc]_Muc_2.2_Hinh_07_So_Do_Davisson_Germer.png (xref 169)
extract_xref(169, "[Goc]_Muc_2.2_Hinh_07_So_Do_Davisson_Germer.png")
# [Goc]_Muc_2.2_Hinh_08_Ket_Qua_Nhieu_Xa_Electron_Ni.png (xref 171)
extract_xref(171, "[Goc]_Muc_2.2_Hinh_08_Ket_Qua_Nhieu_Xa_Electron_Ni.png")

# MUC 2.3 IMAGES:
# Slide 22:
# [Goc]_Muc_2.3_Hinh_01_Giao_Thoa_Van_Sang_Toi_Photon.png (xref 234)
extract_xref(234, "[Goc]_Muc_2.3_Hinh_01_Giao_Thoa_Van_Sang_Toi_Photon.png")

# Slide 25:
# [Goc]_Muc_2.3_Hinh_02_Bo_Song_Wave_Packet.png (xref 249)
extract_xref(249, "[Goc]_Muc_2.3_Hinh_02_Bo_Song_Wave_Packet.png")
# [Goc]_Muc_2.3_Hinh_03_Su_Lan_Truyen_Nhom_Song.png (xref 248)
extract_xref(248, "[Goc]_Muc_2.3_Hinh_03_Su_Lan_Truyen_Nhom_Song.png")

print("All original images extracted successfully!")
