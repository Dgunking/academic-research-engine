# -*- coding: utf-8 -*-
"""
Common Terminology Module (ATCC Engine & Academic Nomenclature Guardian)
Thuật toán 10: Đối chiếu & Khóa Danh pháp Học thuật.
Đóng gói phi trạng thái (Stateless/Reusable Utility).
Tuân thủ: Nghị định 30/2020/NĐ-CP, Viết số APA 7, Đơn vị SI Luật Đo lường 04/2011/QH13, ISO 80000.
"""

import re
from typing import Dict, List, Any, Optional, Tuple


# Danh từ khoa học mượn nguyên ngữ: Giữ nguyên dạng gốc, cấm in nghiêng
LOAN_NOUNS_WHITELIST = {
    "laser", "diode", "electron", "photon", "phonon", 
    "exciton", "plasma", "vector", "tensor", "polaron", "plasmon"
}

# Đơn vị SI chuẩn theo Luật Đo lường 04/2011/QH13 (yêu cầu có dấu cách ngăn với số: 300 K, 10 nm)
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
    "t", "mt", "g", "kg", "mol", "cd", "lm", "lx"
}

# Regex tìm kiếm số dính liền với đơn vị SI (ví dụ: 300K, 10nm, 50mA)
# Bỏ qua trường hợp % và độ ° (cho phép 100%, 45°)
SI_ATTACHED_REGEX = re.compile(
    r"\b(\d+(?:[.,]\d+)?)\s*([a-zA-ZμΩåÅ]+)\b"
)

# Từ điển danh pháp song ngữ chuẩn mực chuyên ngành Quang điện tử & Bán dẫn
ATCC_BILINGUAL_DICTIONARY = {
    "vùng cấm": {"term_en": "bandgap", "term_vi": "vùng cấm", "symbol": "<i>E<sub>g</sub></i>", "unit": "eV"},
    "mật độ hạt tải": {"term_en": "carrier density", "term_vi": "mật độ hạt tải", "symbol": "<i>N</i>", "unit": "cm⁻³"},
    "mật độ hạt tải ngưỡng": {"term_en": "threshold carrier density", "term_vi": "mật độ hạt tải ngưỡng", "symbol": "<i>N</i><sub>th</sub>", "unit": "cm⁻³"},
    "dòng ngưỡng": {"term_en": "threshold current", "term_vi": "dòng ngưỡng", "symbol": "<i>I</i><sub>th</sub>", "unit": "mA"},
    "hiệu suất lượng tử vi phân": {"term_en": "differential quantum efficiency", "term_vi": "hiệu suất lượng tử vi phân", "symbol": "<i>η</i><sub>d</sub>", "unit": "%"},
    "hệ số phẩm chất": {"term_en": "quality factor", "term_vi": "hệ số phẩm chất", "symbol": "<i>Q</i>", "unit": "không thứ nguyên"},
    "bước sóng": {"term_en": "wavelength", "term_vi": "bước sóng", "symbol": "<i>λ</i>", "unit": "nm"},
    "tần số góc": {"term_en": "angular frequency", "term_vi": "tần số góc", "symbol": "<i>ω</i>", "unit": "rad/s"},
    "hệ số giam giữ quang học": {"term_en": "optical confinement factor", "term_vi": "hệ số giam giữ quang học", "symbol": "<i>Γ</i>", "unit": "không thứ nguyên"},
    "thời gian sống hạt tải": {"term_en": "carrier lifetime", "term_vi": "thời gian sống hạt tải", "symbol": "<i>τ</i>", "unit": "ns"},
    "thời gian sống photon": {"term_en": "photon lifetime", "term_vi": "thời gian sống photon", "symbol": "<i>τ</i><sub>p</sub>", "unit": "ps"},
    "phát xạ tự phát": {"term_en": "spontaneous emission", "term_vi": "phát xạ tự phát", "symbol": "<i>R</i><sub>sp</sub>", "unit": "cm⁻³·s⁻¹"},
    "phát xạ kích thích": {"term_en": "stimulated emission", "term_vi": "phát xạ kích thích", "symbol": "<i>R</i><sub>st</sub>", "unit": "cm⁻³·s⁻¹"},
    "độ linh động": {"term_en": "mobility", "term_vi": "độ linh động", "symbol": "<i>μ</i>", "unit": "cm²/(V·s)"},
    "điện trở vi phân tiếp xúc": {"term_en": "contact resistance", "term_vi": "điện trở vi phân tiếp xúc", "symbol": "<i>R</i><sub>s</sub>", "unit": "Ω"},
    "mức fermi": {"term_en": "Fermi level", "term_vi": "mức Fermi", "symbol": "<i>E</i><sub>F</sub>", "unit": "eV"},
    "chuẩn mức fermi": {"term_en": "quasi-Fermi level", "term_vi": "chuẩn mức Fermi", "symbol": "<i>E</i><sub>Fn</sub>, <i>E</i><sub>Fp</sub>", "unit": "eV"},
}

# Master Variable Dictionary - Từ điển ký hiệu chuẩn toàn chương
MASTER_PHYSICS_SYMBOLS = {
    "h": {"name": "Hằng số Planck", "unit": "J·s", "symbol_html": "<i>h</i>", "value": "6.62607015e-34"},
    "hbar": {"name": "Hằng số Planck rút gọn", "unit": "J·s", "symbol_html": "ℏ", "value": "1.054571817e-34"},
    "k_B": {"name": "Hằng số Boltzmann", "unit": "J/K", "symbol_html": "<i>k</i><sub>B</sub>", "value": "1.380649e-23"},
    "q": {"name": "Điện tích nguyên tố", "unit": "C", "symbol_html": "<i>q</i>", "value": "1.602176634e-19"},
    "m_0": {"name": "Khối lượng nghỉ electron", "unit": "kg", "symbol_html": "<i>m</i><sub>0</sub>", "value": "9.1093837e-31"},
    "c": {"name": "Vận tốc ánh sáng trong chân không", "unit": "m/s", "symbol_html": "<i>c</i>", "value": "299792458"},
    "eps_0": {"name": "Hằng số điện môi chân không", "unit": "F/m", "symbol_html": "<i>ε</i><sub>0</sub>", "value": "8.8541878128e-12"},
    "mu_0": {"name": "Độ từ thẩm chân không", "unit": "H/m", "symbol_html": "<i>μ</i><sub>0</sub>", "value": "1.25663706212e-6"},
    "I_th": {"name": "Dòng ngưỡng laser", "unit": "mA", "symbol_html": "<i>I</i><sub>th</sub>"},
    "N_th": {"name": "Mật độ hạt tải ngưỡng", "unit": "cm⁻³", "symbol_html": "<i>N</i><sub>th</sub>"},
    "R_s": {"name": "Điện trở vi phân tiếp xúc", "unit": "Ω", "symbol_html": "<i>R</i><sub>s</sub>"},
    "eta_d": {"name": "Hiệu suất lượng tử vi phân", "unit": "%", "symbol_html": "<i>η</i><sub>d</sub>"}
}


class TerminologyGuardian:
    """Bộ bảo vệ và chuẩn hóa Danh pháp Khoa học ATCC."""

    @staticmethod
    def lint_si_units(text: str) -> List[Dict[str, Any]]:
        """
        Bắt lỗi dính liền số và đơn vị SI theo Luật Đo lường 04/2011/QH13.
        Ví dụ: '300K' -> lỗi, bắt buộc là '300 K'; '10nm' -> '10 nm'.
        """
        violations = []
        for match in SI_ATTACHED_REGEX.finditer(text):
            num = match.group(1)
            unit = match.group(2)
            unit_lower = unit.lower()
            
            # Kiểm tra nếu unit là đơn vị SI được nhận diện
            if unit_lower in SI_UNITS:
                # Kiểm tra xem có khoảng trắng giữa số và đơn vị không
                full_match = match.group(0)
                if not re.search(r"\s+", full_match):
                    violations.append({
                        "error_type": "SI_UNIT_NO_SPACE",
                        "raw_token": full_match,
                        "suggested": f"{num} {unit}",
                        "position": match.span()
                    })
        return violations

    @staticmethod
    def lint_loan_nouns_italic(text: str) -> List[Dict[str, Any]]:
        """
        Phát hiện các danh từ khoa học mượn nguyên ngữ bị in nghiêng sai quy cách (ví dụ: <i>laser</i>).
        Quy tắc: Các từ trong LOAN_NOUNS_WHITELIST phải giữ nguyên font chữ thường, không in nghiêng.
        """
        violations = []
        for word in LOAN_NOUNS_WHITELIST:
            pattern = re.compile(rf"<i>\s*{word}\s*</i>", re.IGNORECASE)
            for match in pattern.finditer(text):
                violations.append({
                    "error_type": "LOAN_NOUN_WRONGLY_ITALICIZED",
                    "raw_token": match.group(0),
                    "suggested": word,
                    "position": match.span()
                })
        return violations

    @staticmethod
    def lint_apa7_number_intervals(text: str) -> List[Dict[str, Any]]:
        """
        Kiểm tra quy tắc viết khoảng số APA 7: bắt buộc dùng dấu gạch ngang en-dash (–), cấm gạch nối (-).
        Ví dụ: '10-20 nm' -> lỗi, phải là '10–20 nm'.
        """
        violations = []
        interval_pattern = re.compile(r"\b(\d+)\s*-\s*(\d+)\b")
        for match in interval_pattern.finditer(text):
            # Kiểm tra xem đây có phải là phép trừ không (nếu đứng sau dấu = thì có thể là phép tính)
            start_idx = max(0, match.start() - 5)
            context = text[start_idx:match.start()]
            if "=" not in context and "+" not in context:
                violations.append({
                    "error_type": "APA7_HYPHEN_IN_INTERVAL",
                    "raw_token": match.group(0),
                    "suggested": f"{match.group(1)}–{match.group(2)}",
                    "position": match.span()
                })
        return violations

    @staticmethod
    def lint_decree_30_heading(heading_text: str) -> List[str]:
        """
        Kiểm tra quy tắc viết hoa tiêu đề Nghị định 30/2020/NĐ-CP:
        Sentence case cho H1-H3: Chỉ viết hoa chữ cái đầu và danh từ riêng (HUST, Planck, Boltzmann...).
        Cấm viết hoa mọi danh từ chung kiểu Title Case tiếng Anh.
        """
        errors = []
        words = heading_text.split()
        if len(words) <= 1:
            return errors
        
        # Bỏ qua từ đầu tiên (được phép viết hoa)
        for w in words[1:]:
            clean_w = re.sub(r"[^\w]", "", w)
            if not clean_w:
                continue
            # Nếu viết hoa chữ cái đầu nhưng là danh từ chung tiếng Việt
            if clean_w[0].isupper() and not clean_w.isupper():
                lower_w = clean_w.lower()
                common_physics_words = {
                    "vật", "lý", "quang", "học", "bán", "dẫn", "cấu", "trúc", 
                    "linh", "kiện", "nguyên", "tắc", "hoạt", "động", "phương", "trình",
                    "đặc", "tuyến", "chương", "mục", "phần", "bài", "toán"
                }
                if lower_w in common_physics_words:
                    errors.append(f"Từ '{w}' trong tiêu đề viết hoa sai quy cách Nghị định 30 (chỉ viết hoa đầu câu: '{lower_w}')")
        return errors

    @classmethod
    def lookup_bilingual(cls, term: str) -> Optional[Dict[str, str]]:
        """Tra cứu danh pháp song ngữ chuẩn xác."""
        term_lower = term.strip().lower()
        return ATCC_BILINGUAL_DICTIONARY.get(term_lower)

    @classmethod
    def format_bilingual(cls, term_vi: str) -> str:
        """Định dạng chuẩn: 'thuật ngữ tiếng Việt (english term)'."""
        entry = cls.lookup_bilingual(term_vi)
        if entry:
            return f"{entry['term_vi']} ({entry['term_en']})"
        return term_vi
