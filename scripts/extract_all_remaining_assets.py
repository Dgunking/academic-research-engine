# -*- coding: utf-8 -*-
import os
import sys
import io
import pymupdf
from PIL import Image

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

PDF_PATH = r"G:\My Drive\NotebookLM - Academic Knowledge Base\Cơ sở vật lý và công nghệ nano\Bài 3-Properties.pdf"
KHO_ANH = r"G:\My Drive\NotebookLM - Academic Knowledge Base\Cơ sở vật lý và công nghệ nano\Kho_Hinh_Anh"
os.makedirs(KHO_ANH, exist_ok=True)

doc = pymupdf.open(PDF_PATH)

def save_optimized(im, out_path, max_w=1400):
    w, h = im.size
    if w > max_w:
        target_h = int(h * max_w / w)
        im = im.resize((max_w, target_h), Image.Resampling.LANCZOS)
    if im.mode == 'RGBA':
        bg = Image.new('RGB', im.size, (255, 255, 255))
        bg.paste(im, mask=im.split()[3])
        im = bg
    elif im.mode != 'RGB':
        im = im.convert('RGB')
    im.save(out_path, 'PNG', optimize=True)
    size_kb = os.path.getsize(out_path) / 1024
    print(f"Saved: {os.path.basename(out_path)} ({im.size[0]}x{im.size[1]}, {size_kb:.1f} KB)")

def extract_image_by_xref(xref, out_filename):
    base_image = doc.extract_image(xref)
    im = Image.open(io.BytesIO(base_image['image']))
    out_path = os.path.join(KHO_ANH, out_filename)
    save_optimized(im, out_path)

def render_page_crop(page_idx, out_filename, dpi=200):
    page = doc[page_idx]
    pix = page.get_pixmap(dpi=dpi)
    im = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    out_path = os.path.join(KHO_ANH, out_filename)
    save_optimized(im, out_path)

print("--- Extracting Section 3.2 Assets ---")
render_page_crop(21, "[Goc]_Muc_3.2_Hinh_01_Trao_Doi_Nhiet_Va_Hang_So_Thoi_Gian_Tau.png")
render_page_crop(22, "[Goc]_Muc_3.2_Hinh_02_Dinh_Luat_Ti_Le_Nhiet_Va_Tan_Nhiet_Nano.png")
render_page_crop(23, "[Goc]_Muc_3.2_Hinh_03_Luc_Can_Nhot_Stokes_Va_Van_Toc_Roi.png")
render_page_crop(25, "[Goc]_Muc_3.2_Hinh_04_Sup_Do_Co_Hoc_Newton_O_Thang_Nano.png")
render_page_crop(26, "[Goc]_Muc_3.2_Hinh_05_Khuech_Tan_Nhiet_Brown_Va_He_Thuc_Einstein.png")
extract_image_by_xref(150, "[Goc]_Muc_3.2_Hinh_06_Hien_Tuong_Sieu_Tron_Graphite_Va_CNT.png")

print("\n--- Extracting Section 3.3 Assets ---")
extract_image_by_xref(153, "[Goc]_Muc_3.3_Hinh_01_Phan_Loai_Chieu_Khong_Gian_0D_1D_2D_3D.png")
extract_image_by_xref(156, "[Goc]_Muc_3.3_Hinh_02_Hinh_Thai_Hoc_Morphology_Vat_Lieu_ZnO.png")
extract_image_by_xref(160, "[Goc]_Muc_3.3_Hinh_03_So_Do_Mat_Do_Trang_Thai_Dien_Tu_DOS.png")
extract_image_by_xref(164, "[Goc]_Muc_3.3_Hinh_04_Bieu_Do_DOS_Theo_Chieu_Khong_Gian_3D_2D_1D_0D.png")
extract_image_by_xref(167, "[Goc]_Muc_3.3_Hinh_05_Vector_Chiral_Va_Cau_Truc_Ong_Than_CNT.png")
extract_image_by_xref(171, "[Goc]_Muc_3.3_Hinh_06_Tinh_Chat_Dien_Armchair_Zigzag_Chiral_CNT.png")

print("\n--- Extracting Section 3.4 Assets ---")
extract_image_by_xref(179, "[Goc]_Muc_3.4_Hinh_01_Pho_Tan_Xa_Raman_Giam_Giu_Phonon.png")
extract_image_by_xref(182, "[Goc]_Muc_3.4_Hinh_02_Dich_Dinh_Raman_Hat_Nano_CeO2.png")
extract_image_by_xref(186, "[Goc]_Muc_3.4_Hinh_03_Chuyen_Pha_Sat_Tu_Thuan_Tu_PbTiO3.png")

print("\n--- Extracting Section 3.5 Assets ---")
extract_image_by_xref(189, "[Goc]_Muc_3.5_Hinh_01_Phan_Chia_Dien_Tich_Be_Mat.png")
extract_image_by_xref(196, "[Goc]_Muc_3.5_Hinh_02_Bang_Tang_Dien_Tich_Lap_Phuong.png")
extract_image_by_xref(199, "[Goc]_Muc_3.5_Hinh_03_Ket_Tu_Giam_Nang_Luong_Be_Mat.png")
extract_image_by_xref(203, "[Goc]_Muc_3.5_Hinh_04_Co_Che_Xuc_Tac_Nano.png")
extract_image_by_xref(206, "[Goc]_Muc_3.5_Hinh_05_Co_Che_Cam_Bien_Lock_Key.png")
extract_image_by_xref(209, "[Goc]_Muc_3.5_Hinh_06_Giam_Giu_Mo_Vung_Cam_Kim_Loai.png")
extract_image_by_xref(212, "[Goc]_Muc_3.5_Hinh_07_Tuong_Tac_Quang_Tan_Xa_Hat_Keo.png")
extract_image_by_xref(215, "[Goc]_Muc_3.5_Hinh_08_Cong_Huong_Plasmon_LSPR.png")
extract_image_by_xref(218, "[Goc]_Muc_3.5_Hinh_09_Phat_Xa_Cham_Luong_Tu.png")

print("\nAll original assets for Sections 3.2, 3.3, 3.4, 3.5 extracted successfully!")
