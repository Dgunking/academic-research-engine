# -*- coding: utf-8 -*-
import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

sample_chat = """\
📄 **Bản Chuyên khảo Mục 2.1:** https://drive.google.com/file/d/1Chuyen_Khao_Laser_Diode_Muc_2.1_PDF/view
🖼️ **Danh mục hình ảnh (Đầy đủ 100% toàn bộ 4 ảnh):**
  - [Mo_Phong]_Do_Loi_Quang_Va_Dong_Nguong.png: https://drive.google.com/file/d/1Img_01_Do_Loi/view
  - [Mo_Phong]_Gian_Do_Dai_Nang_Luong_Di_Chat_DH.png: https://drive.google.com/file/d/1Img_02_Gian_Do/view
  - [Goc]_Hinh_01_Cau_Truc_Di_Chat_Kep.png: https://drive.google.com/file/d/1Img_03_Hinh_01/view
  - [Goc]_Hinh_02_Gian_Do_Nang_Luong.png: https://drive.google.com/file/d/1Img_04_Hinh_02/view
"""

def is_image_or_diagram(url, line):
    if re.search(r"\.(png|jpe?g|webp|svg|gif|bmp)($|[?#])", url, re.I):
        return True
    if re.search(r"(\.(png|jpe?g|webp|svg|gif|bmp)|\[(?:Goc|Mo_Phong|Original|Simulation)\])", line, re.I):
        return True
    if re.search(r"(?:^|\b)(?:hình|figure|fig\.?|đồ thị|biểu đồ|sơ đồ|mô hình|mô phỏng|minh họa|minh hoạ|ảnh|plot|chart)\b", line, re.I):
        return True
    return False

def test_routing():
    url_matches = list(re.finditer(r"https?://[^\s\"'<>\)\],]+", sample_chat))
    
    left_tab_diagrams = []
    right_tab_pdfs = []
    
    for m in url_matches:
        raw_url = m.group(0).rstrip(".,;:!?)")
        url_index = m.start()
        line_start = sample_chat.rfind("\n", 0, url_index) + 1
        line_end = sample_chat.find("\n", url_index)
        current_line = sample_chat[line_start : len(sample_chat) if line_end == -1 else line_end].strip()
        
        file_id = raw_url.split("/d/")[1].split("/")[0]
        
        # 1. ReaderOverlayEngine check (Right Pane - PDF ONLY):
        # Must strictly reject any diagram or image link!
        if is_image_or_diagram(raw_url, current_line):
            # It's a diagram, send to Left Canvas!
            file_match = (
                re.search(r"(?:^|\n|\-\s*|\*\s*)(\[(?:Goc|Mo_Phong|Original|Simulation)\][^\s:]+)\s*:", current_line, re.I) or
                re.search(r"(\[[A-Za-z0-9_-]+\][A-Za-z0-9_\-\.]+\.(?:png|jpg|jpeg|svg|webp))\s*:", current_line, re.I) or
                re.search(r"([a-zA-Z0-9_\-]+\.(?:png|jpg|jpeg|svg|webp))\s*:", current_line, re.I)
            )
            title = file_match.group(1).strip() if file_match else f"Drive_{file_id[:6]}"
            left_tab_diagrams.append({"file_id": file_id, "title": title})
        else:
            # Check if valid PDF for Right Reader:
            is_pdf = bool(
                re.search(r"\.pdf($|[?#])", raw_url, re.I) or
                re.search(r"(?:bài giảng|giáo trình|tài liệu|chương \d|phân mục \d|bản chuyên khảo|chuyên khảo|mục \d)(?:\.pdf)?\b", current_line, re.I)
            )
            if is_pdf:
                doc_match = re.search(r"(?:Tài liệu|Bài giảng|Giáo trình|Bản Chuyên khảo|Chuyên khảo|Phân mục|Mục|Chương)\s*[:\-\s]*([^:\n|]+)", current_line, re.I)
                title = (doc_match.group(0).strip() + ".pdf") if doc_match else f"Bai_Giang_{file_id[:6]}.pdf"
                right_tab_pdfs.append({"file_id": file_id, "title": title})

    print(f"Tab Trái (Visual Canvas - Diagrams): {len(left_tab_diagrams)} items")
    for d in left_tab_diagrams:
        print(f"  - [CANVAS] {d['title']} -> {d['file_id']}")
        
    print(f"\nTab Phải (Reader Overlay - PDFs): {len(right_tab_pdfs)} items")
    for p in right_tab_pdfs:
        print(f"  - [READER] {p['title']} -> {p['file_id']}")

    assert len(right_tab_pdfs) == 1, f"FAIL: Tab Phải phải có ĐÚNG 1 PDF, thực tế: {len(right_tab_pdfs)}"
    assert len(left_tab_diagrams) == 4, f"FAIL: Tab Trái phải có ĐÚNG 4 hình ảnh, thực tế: {len(left_tab_diagrams)}"
    assert right_tab_pdfs[0]["file_id"] == "1Chuyen_Khao_Laser_Diode_Muc_2.1_PDF"
    print("\n[PASS] Hoàn hảo: Phân luồng Tab Trái (4 ảnh) & Tab Phải (1 PDF) chính xác 100%!")

if __name__ == "__main__":
    test_routing()
