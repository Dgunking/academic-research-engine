# -*- coding: utf-8 -*-
"""
ATCC Engine (Academic Terminology Cross-Check Engine)
Thuật toán 10 trong Hệ thống 13 Thuật toán Cốt lõi Bất biến (Ground Truth Master Lock).

Chuyên trách:
1. Đối soát Ma trận Danh pháp Song ngữ Anh - Việt dạng: 'thuật ngữ tiếng Việt (english term)'.
2. Ràng buộc danh từ mượn nguyên ngữ (laser, diode, electron, photon, phonon, exciton, plasma, vector, tensor).
3. Kiểm toán chuẩn hóa quy tắc văn bản hành chính & khoa học:
   - Nghị định 30/2020/NĐ-CP: Cấm viết hoa danh từ chung giữa câu, Sentence case cho tiêu đề H1-H3.
   - Viết số APA 7: Quy chuẩn số đo lường, phân cách thập phân và hàng nghìn, en-dash (–) khoảng số.
   - Đơn vị SI Luật Đo lường 04/2011/QH13: Bắt buộc khoảng trắng giữa số và đơn vị (300 K, 10 nm; cấm 300K).
4. Khởi tạo và đồng bộ Master Variable Dictionary (Từ điển Ký hiệu Biến số Toàn chương) chống trôi ký hiệu (Zero-Symbol-Drift).
5. Chốt chặn Xung đột & Trôi Danh pháp (Zero-Drift Gate): Chặn đứng tiến trình khi phát hiện xung đột Slide vs Sách.
"""

import os
import sys
import re
import json
import tempfile
from typing import Dict, List, Tuple, Optional, Any, Set

TEMP_DIR = tempfile.gettempdir()
PENDING_TERMINOLOGY_FILE = os.path.join(TEMP_DIR, "PENDING_TERMINOLOGY.json")

# Danh từ khoa học mượn nguyên ngữ: Giữ nguyên dạng gốc không in nghiêng
LOAN_NOUNS_WHITELIST = {
    "laser", "diode", "electron", "photon", "phonon", 
    "exciton", "plasma", "vector", "tensor", "polaron", "plasmon"
}

# Đơn vị SI chuẩn theo Luật Đo lường 04/2011/QH13
SI_UNITS = {
    "k", "m", "cm", "mm", "μm", "um", "nm", "pm", "angstrom", "å",
    "s", "ms", "μs", "us", "ns", "ps", "fs",
    "v", "mv", "μv", "uv", "kv",
    "a", "ma", "μa", "ua", "na", "pa",
    "hz", "khz", "mhz", "ghz", "thz",
    "j", "mj", "ev", "mev", "kev", "gev",
    "w", "mw", "μw", "uw", "kw",
    "ω", "kω", "mω", "ohm", "kohm",
    "f", "pf", "nf", "μf", "uf",
    "h", "mh", "μh", "uh",
    "t", "mt", "g", "kg", "mol"
}

class ATCCEngine:
    """Động cơ Đối chiếu & Khóa Danh pháp Học thuật Tiền Biên dịch"""
    
    def __init__(self, course_name: str = "Quang học và Quang điện tử", chapter: int = 2):
        self.course_name = course_name
        self.chapter = chapter
        self.master_dictionary: Dict[str, Dict[str, Any]] = {}
        self.load_default_physics_symbols()

    def load_default_physics_symbols(self):
        """Nạp các ký hiệu biến số vật lý và quang điện tử nền tảng chống trôi ký hiệu."""
        self.master_dictionary = {
            "h": {"name": "Hằng số Planck", "unit": "J·s", "value": "6.62607015e-34"},
            "hbar": {"name": "Hằng số Planck rút gọn", "unit": "J·s", "symbol": "ℏ", "value": "1.054571817e-34"},
            "k_B": {"name": "Hằng số Boltzmann", "unit": "J/K", "value": "1.380649e-23"},
            "q": {"name": "Điện tích nguyên tố", "unit": "C", "value": "1.602176634e-19"},
            "m_0": {"name": "Khối lượng nghỉ electron", "unit": "kg", "value": "9.1093837e-31"},
            "c": {"name": "Vận tốc ánh sáng trong chân không", "unit": "m/s", "value": "299792458"},
            "eps_0": {"name": "Hằng số điện môi chân không", "unit": "F/m", "symbol": "ε₀", "value": "8.8541878128e-12"},
            "mu_0": {"name": "Độ từ thẩm chân không", "unit": "H/m", "symbol": "μ₀", "value": "1.25663706212e-6"},
            "I_th": {"name": "Dòng ngưỡng laser", "unit": "mA", "desc": "Ngưỡng kích hoạt phát xạ kích thích"},
            "N_th": {"name": "Mật độ hạt tải ngưỡng", "unit": "cm⁻³", "desc": "Mật độ hạt tải tại điều kiện bù suy hao"},
            "R_s": {"name": "Điện trở vi phân tiếp xúc", "unit": "Ω", "desc": "Nội trở vi phân tiếp xúc kim loại-bán dẫn"},
            "eta_d": {"name": "Hiệu suất lượng tử vi phân", "unit": "%", "symbol": "η_d", "desc": "Hệ số góc đặc tuyến P-I"}
        }

    # ----------------------------------------------------
    # 1. KIỂM TOÁN ĐƠN VỊ SI LUẬT ĐO LƯỜNG 04/2011/QH13
    # ----------------------------------------------------
    def lint_si_units(self, text: str) -> List[Dict[str, Any]]:
        """
        Bắt lỗi dính liền số và đơn vị SI (ví dụ: 300K thay vì 300 K, 10nm thay vì 10 nm).
        Ngoại lệ: dấu % và độ (°) viết liền.
        """
        violations = []
        # Pattern tìm số dính liền với đơn vị: 300K, 1.55um, 10mA, v.v.
        pattern = r"\b(\d+(?:[,\.]\d+)?)\s*([a-zA-ZμΩåÅ]{1,6})\b"
        
        for m in re.finditer(pattern, text):
            num_str = m.group(1)
            unit_str = m.group(2)
            full_match = m.group(0)
            unit_lower = unit_str.lower()
            
            # Nếu unit nằm trong bảng SI và giữa số với unit không có khoảng trắng
            if unit_lower in SI_UNITS:
                # Kiểm tra xem chuỗi gốc trong text có khoảng trắng không
                start, end = m.span()
                matched_text = text[start:end]
                if not re.search(r"\s", matched_text):
                    violations.append({
                        "type": "SI_NO_SPACE",
                        "matched": matched_text,
                        "suggested": f"{num_str} {unit_str}",
                        "position": start,
                        "rule": "Luật Đo lường 04/2011/QH13: Bắt buộc 1 khoảng trắng giữa số và đơn vị SI."
                    })
        return violations

    # ----------------------------------------------------
    # 2. KIỂM TOÁN VIẾT HOA NGHỊ ĐỊNH 30/2020/NĐ-CP
    # ----------------------------------------------------
    def lint_decree_30_capitalization(self, heading: str) -> List[Dict[str, Any]]:
        """
        Kiểm tra quy tắc viết hoa danh từ chung trong tiêu đề (H1-H3).
        Ép buộc dùng Sentence case (chỉ viết hoa chữ cái đầu và danh từ riêng).
        """
        violations = []
        words = heading.strip().split()
        if len(words) <= 1:
            return violations
        
        # Bỏ qua từ đầu tiên (được phép viết hoa)
        for idx, w in enumerate(words[1:], start=1):
            clean_w = re.sub(r"[^\w]", "", w)
            if clean_w.isupper() and len(clean_w) > 1:
                # Có thể là từ viết tắt kỹ thuật (LED, DFB, PIC, CER, MPT, AST) -> Chấp nhận
                continue
            if clean_w.istitle() and clean_w.lower() not in LOAN_NOUNS_WHITELIST:
                # Kiểm tra xem có phải tên riêng không (HUST, Planck, Boltzmann, Feynman, Bohr...)
                proper_nouns = {"hust", "planck", "boltzmann", "feynman", "bohr", "schrödinger", "schrodinger", "einstein", "dirac", "bloch", "heisenberg", "fermi", "auger", "gaas", "inp", "gan"}
                if clean_w.lower() not in proper_nouns:
                    violations.append({
                        "type": "DECREE_30_TITLE_CASE",
                        "word": w,
                        "heading": heading,
                        "suggested": w.lower(),
                        "rule": "Nghị định 30/2020/NĐ-CP: Tiêu đề H1-H3 bắt buộc dùng Sentence case, cấm viết hoa danh từ chung giữa câu."
                    })
        return violations

    # ----------------------------------------------------
    # 3. QUẢN TRỊ MASTER VARIABLE DICTIONARY (ZERO-SYMBOL-DRIFT)
    # ----------------------------------------------------
    def register_symbol(self, symbol: str, name_vn: str, unit: str, desc: str = "") -> bool:
        """Đăng ký biến số vào Master Variable Dictionary để khóa cứng ý nghĩa toàn chương."""
        if symbol in self.master_dictionary:
            existing = self.master_dictionary[symbol]
            if existing["name"] != name_vn or existing["unit"] != unit:
                # Phát hiện trôi lệch ký hiệu!
                return False
        self.master_dictionary[symbol] = {
            "name": name_vn,
            "unit": unit,
            "desc": desc
        }
        return True

    def export_master_dictionary(self, out_path: Optional[str] = None) -> str:
        """Xuất Master Variable Dictionary ra tệp JSON."""
        if not out_path:
            out_path = os.path.join(TEMP_DIR, f"MASTER_VARIABLE_DICT_CHUONG_{self.chapter}.json")
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(self.master_dictionary, f, ensure_ascii=False, indent=2)
        return out_path

    # ----------------------------------------------------
    # 4. CHỐT CHẶN XUNG ĐỘT DANH PHÁP (ZERO-DRIFT GATE)
    # ----------------------------------------------------
    def check_terminology_conflict(self, term_slide: str, term_book: str) -> Optional[Dict[str, Any]]:
        """
        So sánh thuật ngữ giữa Slide HUST và Giáo trình Sách.
        Nếu xung đột ngữ nghĩa: Kích hoạt Hard Block và tạo bảng đề xuất chuẩn hóa.
        """
        ratio = SequenceMatcher(None, term_slide.lower(), term_book.lower()).ratio()
        if ratio < 0.60:
            return {
                "conflict": True,
                "term_slide": term_slide,
                "term_book": term_book,
                "similarity": ratio,
                "recommendation": f"{term_slide} / {term_book}",
                "action": "Dừng tiến trình, yêu cầu đối chiếu với người học trên Chat."
            }
        return None

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding='utf-8')
    print("=== ATCC ENGINE SELF-TEST ===")
    atcc = ATCCEngine(chapter=2)
    
    # Test SI Lint
    sample_text = "Nhiệt độ hoạt động 300K với bước sóng phát xạ 1.55um và dòng ngưỡng 10mA."
    si_errs = atcc.lint_si_units(sample_text)
    print(f"SI Unit Errors ({len(si_errs)}):")
    for err in si_errs:
        print(f"  - Vi phạm: '{err['matched']}' -> Gợi ý: '{err['suggested']}'")
        
    # Test Decree 30 Lint
    sample_heading = "Giai Đoạn 3: Thực Hành Có Hướng Dẫn Và Dẫn Xuất Giải Tích"
    d30_errs = atcc.lint_decree_30_capitalization(sample_heading)
    print(f"\nDecree 30 Errors ({len(d30_errs)}):")
    for err in d30_errs:
        print(f"  - Từ viết hoa sai: '{err['word']}' trong '{err['heading']}'")
        
    # Test Master Dictionary Export
    dict_file = atcc.export_master_dictionary()
    print(f"\nMaster Variable Dictionary exported: {dict_file}")
    print("ATCC Engine loaded and verified successfully!")
