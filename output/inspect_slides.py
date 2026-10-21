import os
import sys
import pymupdf

sys.stdout.reconfigure(encoding="utf-8")
pdf_path = r"G:\My Drive\NotebookLM - Academic Knowledge Base\Cơ sở vật lý và công nghệ nano\Bài 2-Quantum nature.pdf"
doc = pymupdf.open(pdf_path)

print(f"Total pages: {len(doc)}")
for pno in range(12, 28):
    page = doc[pno]
    images = page.get_images(full=True)
    print(f"\n=== PAGE {pno+1} (images: {len(images)}) ===")
    text = page.get_text("text").strip()
    first_lines = text.split("\n")[:3]
    print(f"Title/First lines: {' | '.join(first_lines)}")
    for idx, img in enumerate(images):
        xref = img[0]
        base_img = doc.extract_image(xref)
        w, h, ext = base_img["width"], base_img["height"], base_img["ext"]
        print(f"  Img {idx}: xref={xref}, size={w}x{h}, ext={ext}")
