import os
import sys
import pymupdf
from PIL import Image

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

# 1. Slide 22: Trao đổi nhiệt vi mô qua cầu dẫn nhiệt nano
p22 = doc[21]
pix22 = p22.get_pixmap(dpi=200)
im22 = Image.frombytes("RGB", [pix22.width, pix22.height], pix22.samples)
out1 = os.path.join(KHO_ANH, "[Goc]_Muc_3.2_Hinh_01_Trao_Doi_Nhiet_Va_Hang_So_Thoi_Gian_Tau.png")
save_optimized(im22, out1)

# 2. Slide 23: Định luật tỉ lệ nhiệt L^2 và tản nhiệt siêu tốc
p23 = doc[22]
pix23 = p23.get_pixmap(dpi=200)
im23 = Image.frombytes("RGB", [pix23.width, pix23.height], pix23.samples)
out2 = os.path.join(KHO_ANH, "[Goc]_Muc_3.2_Hinh_02_Dinh_Luat_Ti_Le_Nhiet_Va_Tan_Nhiet_Nano.png")
save_optimized(im23, out2)

# 3. Slide 24: Lực cản nhớt Stokes và tốc độ rơi giới hạn
p24 = doc[23]
pix24 = p24.get_pixmap(dpi=200)
im24 = Image.frombytes("RGB", [pix24.width, pix24.height], pix24.samples)
out3 = os.path.join(KHO_ANH, "[Goc]_Muc_3.2_Hinh_03_Luc_Can_Nhot_Stokes_Va_Van_Toc_Roi.png")
save_optimized(im24, out3)

# 4. Slide 25 & 26: Bài toán động học lắng và giới hạn cơ học Newton
p26 = doc[25]
pix26 = p26.get_pixmap(dpi=200)
im26 = Image.frombytes("RGB", [pix26.width, pix26.height], pix26.samples)
out4 = os.path.join(KHO_ANH, "[Goc]_Muc_3.2_Hinh_04_Sup_Do_Co_Hoc_Newton_O_Thang_Nano.png")
save_optimized(im26, out4)

# 5. Slide 27: Chuyển động khuếch tán Brown và hệ thức Einstein
p27 = doc[26]
pix27 = p27.get_pixmap(dpi=200)
im27 = Image.frombytes("RGB", [pix27.width, pix27.height], pix27.samples)
out5 = os.path.join(KHO_ANH, "[Goc]_Muc_3.2_Hinh_05_Khuech_Tan_Nhiet_Brown_Va_He_Thuc_Einstein.png")
save_optimized(im27, out5)

# 6. Slide 28: Hiện tượng ma sát siêu trơn ở Graphite và Carbon Nanotubes
p28 = doc[27]
il = p28.get_images()
if il:
    base_img = doc.extract_image(il[0][0])
    import io
    im_stream = io.BytesIO(base_img['image'])
    im_raw = Image.open(im_stream)
    out6 = os.path.join(KHO_ANH, "[Goc]_Muc_3.2_Hinh_06_Hien_Tuong_Sieu_Tron_Graphite_Va_CNT.png")
    save_optimized(im_raw, out6)
else:
    pix28 = p28.get_pixmap(dpi=200)
    im28 = Image.frombytes("RGB", [pix28.width, pix28.height], pix28.samples)
    out6 = os.path.join(KHO_ANH, "[Goc]_Muc_3.2_Hinh_06_Hien_Tuong_Sieu_Tron_Graphite_Va_CNT.png")
    save_optimized(im28, out6)

print("All original assets for Section 3.2 extracted successfully!")
