import os
import sys
import pymupdf
from PIL import Image
import io

sys.stdout.reconfigure(encoding="utf-8")
pdf_path = r"G:\My Drive\NotebookLM - Academic Knowledge Base\Cơ sở vật lý và công nghệ nano\Bài 2-Quantum nature.pdf"
doc = pymupdf.open(pdf_path)

output_dir = r"G:\My Drive\NotebookLM - Academic Knowledge Base\Cơ sở vật lý và công nghệ nano\Kho_Hinh_Anh"
os.makedirs(output_dir, exist_ok=True)

# Function to save extracted image with high quality
def extract_and_save(xref, filename, min_dpi=300):
    base_img = doc.extract_image(xref)
    image_bytes = base_img["image"]
    image_ext = base_img["ext"]
    im = Image.open(io.BytesIO(image_bytes))
    
    # Check if RGB or RGBA
    if im.mode not in ("RGB", "RGBA"):
        im = im.convert("RGB")
        
    out_path = os.path.join(output_dir, filename)
    # Save with 300 DPI metadata
    im.save(out_path, format="PNG", dpi=(min_dpi, min_dpi))
    print(f"Saved {filename}: format={im.format}, size={im.size}, mode={im.mode} to {out_path}")

# Check slide 18 images
print("--- Page 18 images ---")
for idx, img in enumerate(doc[17].get_images(full=True)):
    xref = img[0]
    b = doc.extract_image(xref)
    print(f"P18 Img {idx}: xref={xref}, size={b['width']}x{b['height']}, ext={b['ext']}")

# Check slide 19 images
print("--- Page 19 images ---")
for idx, img in enumerate(doc[18].get_images(full=True)):
    xref = img[0]
    b = doc.extract_image(xref)
    print(f"P19 Img {idx}: xref={xref}, size={b['width']}x{b['height']}, ext={b['ext']}")

# Check slide 25 images
print("--- Page 25 images ---")
for idx, img in enumerate(doc[24].get_images(full=True)):
    xref = img[0]
    b = doc.extract_image(xref)
    print(f"P25 Img {idx}: xref={xref}, size={b['width']}x{b['height']}, ext={b['ext']}")
