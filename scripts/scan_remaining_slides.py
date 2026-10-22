# -*- coding: utf-8 -*-
import sys
import os
import pymupdf

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

pdf_path = r"G:\My Drive\NotebookLM - Academic Knowledge Base\Cơ sở vật lý và công nghệ nano\Bài 3-Properties.pdf"
doc = pymupdf.open(pdf_path)

print(f"Total pages: {len(doc)}")
for i in range(21, len(doc)):
    page = doc[i]
    imgs = page.get_images()
    txt = page.get_text().strip().split('\n')[0] if page.get_text().strip() else "NO_TEXT"
    print(f"Slide {i+1}: {len(imgs)} images, title='{txt[:50]}'")
    for idx, img in enumerate(imgs):
        xref = img[0]
        base = doc.extract_image(xref)
        print(f"   Img {idx}: xref={xref}, {base['width']}x{base['height']}, ext={base['ext']}, size={len(base['image'])} B")
