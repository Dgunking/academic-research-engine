# -*- coding: utf-8 -*-
"""
Common Linter Module (Static AST & Typography Linter)
Hạt nhân Kiểm định Tĩnh Trạm 1 (DOHG 2.0) và Luật 14, 15, 16.
Đóng gói phi trạng thái (Stateless/Reusable Utility).
"""

import re
from typing import List, Dict, Any, Optional
from schemas.payload import InternalASTLinterReport


# Danh sách lệnh LaTeX thô bị cấm trong text/table ReportLab (Paragraph)
BANNED_RAW_LATEX_COMMANDS = [
    r"\\frac\b", r"\\partial\b", r"\\tau\b", r"\\eta\b", r"\\mu\b", 
    r"\\sigma\b", r"\\Omega\b", r"\\omega\b", r"\\hbar\b", r"\\infty\b", 
    r"\\nabla\b", r"\\alpha\b", r"\\beta\b", r"\\gamma\b", r"\\Delta\b", 
    r"\\delta\b", r"\\lambda\b", r"\\epsilon\b", r"\\rho\b", r"\\times\b",
    r"\\cdot\b", r"\\approx\b", r"\\propto\b", r"\\leq\b", r"\\geq\b"
]

RAW_LATEX_PATTERN = re.compile("|".join(BANNED_RAW_LATEX_COMMANDS))

# Phân số gạch chéo bị cấm trong văn bản giải tích (Luật 14 - Zero-Slash-Fractions Gate)
SLASH_FRACTION_PATTERN = re.compile(
    r"(?:"
    r"[∂d]\s*[A-Za-z0-9_α-ωΑ-Ω]\s*/\s*[∂d]\s*[A-Za-z0-9_α-ωΑ-Ω]|"
    r"[=≈∝≤≥]\s*[^,;\n<>'\"]{1,30}/|"
    r"/\s*(?:r[²2]|r\^2|ε_?0|ε₀|k_?[Bb]|c[²2]|c\^2|4πε₀|4π|2[L]|n_r|ħω)"
    r")",
    re.IGNORECASE
)

# Biến số dạng lập trình ASCII gạch dưới thô bị cấm trong văn bản (cần <i>, <sub>)
RAW_ASCII_SUBSCRIPT_PATTERN = re.compile(
    r"\b(E_c\(z\)|N_th|I_th|V_j|BN\^2|t_d|v_g|g_th|alpha_i|alpha_m|k_B|n_i|N_c|N_v|E_g|E_F|E_v|E_c)\b"
)

# Ký hiệu chú giải ↳ dính liền dòng câu văn trước (Arrow Linebreak Gate)
ARROW_INLINE_PATTERN = re.compile(r"[^\n<>]\s*↳")

# Thực thể HTML đặt tên thô bị cấm (Zero-Raw-HTML-Entities Gate)
RAW_HTML_ENTITY_PATTERN = re.compile(
    r"&(?:beta|nu|tau|mu|Delta|delta|sigma|ndash|mdash|minus|times|middot|asymp|omega|Omega|alpha|gamma|rarr|larr);",
    re.IGNORECASE
)

# Cấm gộp giai đoạn sư phạm (Luật 16 - Anti-Merged-Stages Gate)
MERGED_STAGES_PATTERN = re.compile(
    r"Giai đoạn\s+\d+\s*(?:&|và|\+)\s*\d+",
    re.IGNORECASE
)

# Cấm cấu trúc 5 giai đoạn di sản (Zero-Legacy-Stages Gate)
LEGACY_STAGES_PATTERN = re.compile(
    r"\b(?:Giai\s+đoạn|GIAI\s+ĐOẠN)\s+[1-5]\b"
)

# Thẻ lồng nhau bất hợp lệ (Zero-Nested-Tags Gate)
NESTED_SUP_SUB_PATTERN = re.compile(
    r"<(sup|sub)[^>]*>(?:(?!</\1>).)*?<\1[^>]*>",
    re.IGNORECASE | re.DOTALL
)

# Công thức hóa học dạng ASCII thô thiếu thẻ <sub> (Zero-Plain-Chemicals Gate)
RAW_CHEMICAL_PATTERN = re.compile(
    r"\b(?:g-C3N4|Ag3VO4|WO3|TiO2|BiVO4|Fe2O3|CH3OH|C2H5OH|H2O2|CO2|H2O|NO2|SO2)\b"
)

# Đại lượng vật lý / dải năng lượng dạng ASCII thô thiếu thẻ HTML (Zero-Plain-Band-Variables Gate)
RAW_BAND_VARIABLE_PATTERN = re.compile(
    r"\b(?:ECB|EVB|Eg)\b"
)


class ASTLinter:
    """Bộ kiểm tra AST tĩnh và quy chuẩn Typography cho nội dung học thuật."""

    @staticmethod
    def check_raw_latex_leaks(text: str) -> List[str]:
        """Phát hiện rò rỉ mã lệnh LaTeX thô trong văn bản cần định dạng HTML."""
        findings = []
        for match in RAW_LATEX_PATTERN.finditer(text):
            start = max(0, match.start() - 20)
            end = min(len(text), match.end() + 20)
            snippet = text[start:end].replace("\n", " ").strip()
            findings.append(f"Mã LaTeX thô '{match.group(0)}' tại: '...{snippet}...'")
        return findings

    @staticmethod
    def check_slash_fractions(text: str) -> List[str]:
        """Phát hiện phân số gạch chéo / trong các biểu thức toán."""
        findings = []
        for match in SLASH_FRACTION_PATTERN.finditer(text):
            start = max(0, match.start() - 15)
            end = min(len(text), match.end() + 15)
            snippet = text[start:end].replace("\n", " ").strip()
            findings.append(f"Phân số gạch chéo '{match.group(0)}' tại: '...{snippet}...'")
        return findings

    @staticmethod
    def check_raw_ascii_subscripts(text: str) -> List[str]:
        """Phát hiện biến số lập trình gạch dưới ASCII thô chưa bọc thẻ Typography."""
        findings = []
        for match in RAW_ASCII_SUBSCRIPT_PATTERN.finditer(text):
            findings.append(f"Biến ASCII thô: '{match.group(0)}' (cần chuẩn hóa: <i>...</i><sub>...</sub>)")
        return findings

    @staticmethod
    def check_arrow_linebreaks(text: str) -> List[str]:
        """Kiểm tra ký hiệu '↳' phải nằm ở đầu dòng hoặc sau thẻ ngắt dòng."""
        findings = []
        for match in ARROW_INLINE_PATTERN.finditer(text):
            start = max(0, match.start() - 15)
            end = min(len(text), match.end() + 15)
            snippet = text[start:end].replace("\n", " ").strip()
            findings.append(f"Ký hiệu '↳' dính dòng câu trước: '...{snippet}...' (cần xuống dòng hoặc chèn <br/>)")
        return findings

    @staticmethod
    def check_raw_html_entities(text: str) -> List[str]:
        """Phát hiện thực thể HTML thô thay vì ký tự Unicode bản địa."""
        findings = []
        for match in RAW_HTML_ENTITY_PATTERN.finditer(text):
            findings.append(f"Thực thể HTML thô '{match.group(0)}' (bắt buộc dùng ký tự Unicode bản địa)")
        return findings

    @staticmethod
    def check_merged_stages(text: str) -> List[str]:
        """Phát hiện hành vi gộp các giai đoạn sư phạm (ví dụ: 'Giai đoạn 2 & 3')."""
        findings = []
        for match in MERGED_STAGES_PATTERN.finditer(text):
            findings.append(f"Gộp giai đoạn sư phạm '{match.group(0)}' (mỗi giai đoạn phải đứng độc lập)")
        return findings

    @staticmethod
    def check_legacy_stages(text: str) -> List[str]:
        """Phát hiện cấu trúc 5 giai đoạn cũ đã bị bãi bỏ."""
        findings = []
        for match in LEGACY_STAGES_PATTERN.finditer(text):
            findings.append(f"Cấu trúc di sản '{match.group(0)}' (bắt buộc dùng Dòng chảy Nhận thức Nguyên lý Đầu 3 Khối)")
        return findings

    @staticmethod
    def check_nested_sup_sub(text: str) -> List[str]:
        """Phát hiện thẻ lồng nhau (ReportLab không hỗ trợ nested sup/sub)."""
        findings = []
        for match in NESTED_SUP_SUB_PATTERN.finditer(text):
            findings.append(f"Thẻ lồng nhau '{match.group(0)}' (cần tách lớp hoặc chuyển sang diễn giải căn thức)")
        return findings

    @staticmethod
    def check_raw_chemicals(text: str) -> List[str]:
        """Phát hiện công thức hóa học chữ phẳng thiếu thẻ <sub>."""
        findings = []
        for match in RAW_CHEMICAL_PATTERN.finditer(text):
            findings.append(f"Công thức hóa học chữ phẳng: '{match.group(0)}' (cần định dạng <sub>...</sub>)")
        return findings

    @staticmethod
    def check_raw_band_variables(text: str) -> List[str]:
        """Phát hiện biến số dải năng lượng chữ phẳng chưa bọc HTML tags."""
        findings = []
        for match in RAW_BAND_VARIABLE_PATTERN.finditer(text):
            findings.append(f"Biến số dải năng lượng chữ phẳng: '{match.group(0)}' (cần <i>...</i><sub>...</sub>)")
        return findings

    @staticmethod
    def check_unwarranted_claims(data: Any) -> List[str]:
        """
        Kiểm tra Zero-Unwarranted Claims Gate:
        Nếu có engineering_claim (hoặc Claim) mà thiếu micro_dynamics_warrant (Warrant 1)
        hoặc thiếu math_blending_scaling (Warrant 2), đánh FAIL ngay lập tức.
        Chấp nhận dict, Pydantic model (MechanisticBlendingEquation, DraftPayload), hoặc dict lồng.
        """
        findings = []
        if isinstance(data, dict):
            claim = data.get("engineering_claim") or data.get("claim")
            warrant1 = data.get("micro_dynamics_warrant") or data.get("warrant_1")
            warrant2 = data.get("math_blending_scaling") or data.get("warrant_2")
            
            if claim:
                if not warrant1 or not str(warrant1).strip():
                    findings.append("Thiếu Giải mã Động lực học Vi mô (Warrant 1 - Nhịp 2): Không thể đưa ra khẳng định kỹ thuật (Claim) mà không giải thích cơ chế vi mô.")
                if not warrant2 or not str(warrant2).strip():
                    findings.append("Thiếu Ánh xạ Toán - Lý & Thử Tương quan Độ lớn (Warrant 2 - Nhịp 3): Không thể đưa ra khẳng định kỹ thuật (Claim) mà thiếu phép thử tương quan độ lớn (Order-of-Magnitude Scaling Step).")
            
            if "micro_point_topics" in data:
                for mpt in data.get("micro_point_topics", []):
                    if isinstance(mpt, dict):
                        mbe = mpt.get("mechanistic_blending_equation") or mpt.get("block_2")
                        if mbe and isinstance(mbe, dict):
                            findings.extend(ASTLinter.check_unwarranted_claims(mbe))
                    elif hasattr(mpt, "mechanistic_blending_equation"):
                        findings.extend(ASTLinter.check_unwarranted_claims(mpt.mechanistic_blending_equation))

            if "mpt_payloads" in data:
                for mpt in data.get("mpt_payloads", []):
                    if isinstance(mpt, dict):
                        mbe = mpt.get("mechanistic_blending_equation") or mpt.get("block_2")
                        if mbe and isinstance(mbe, dict):
                            findings.extend(ASTLinter.check_unwarranted_claims(mbe))
                    elif hasattr(mpt, "mechanistic_blending_equation"):
                        findings.extend(ASTLinter.check_unwarranted_claims(mpt.mechanistic_blending_equation))

        elif hasattr(data, "engineering_claim"):
            claim = getattr(data, "engineering_claim", None)
            warrant1 = getattr(data, "micro_dynamics_warrant", None)
            warrant2 = getattr(data, "math_blending_scaling", None)
            if claim:
                if not warrant1 or not str(warrant1).strip():
                    findings.append("Thiếu Giải mã Động lực học Vi mô (Warrant 1 - Nhịp 2): Không thể đưa ra khẳng định kỹ thuật (Claim) mà không giải thích cơ chế vi mô.")
                if not warrant2 or not str(warrant2).strip():
                    findings.append("Thiếu Ánh xạ Toán - Lý & Thử Tương quan Độ lớn (Warrant 2 - Nhịp 3): Không thể đưa ra khẳng định kỹ thuật (Claim) mà thiếu phép thử tương quan độ lớn (Order-of-Magnitude Scaling Step).")
        
        elif hasattr(data, "micro_point_topics"):
            for mpt in getattr(data, "micro_point_topics", []):
                mbe = getattr(mpt, "mechanistic_blending_equation", None) or getattr(mpt, "block_2", None)
                if mbe:
                    findings.extend(ASTLinter.check_unwarranted_claims(mbe))

        elif hasattr(data, "mpt_payloads"):
            for mpt in getattr(data, "mpt_payloads", []):
                mbe = getattr(mpt, "mechanistic_blending_equation", None) or getattr(mpt, "block_2", None)
                if mbe:
                    findings.extend(ASTLinter.check_unwarranted_claims(mbe))
                    
        return findings

    @classmethod
    def lint_text(cls, text: str) -> Dict[str, Any]:
        """Kiểm tra toàn diện một đoạn văn bản hoặc payload."""
        latex_leaks = cls.check_raw_latex_leaks(text)
        slash_fractions = cls.check_slash_fractions(text)
        ascii_subscripts = cls.check_raw_ascii_subscripts(text)
        arrow_errors = cls.check_arrow_linebreaks(text)
        html_entity_errors = cls.check_raw_html_entities(text)
        merged_stages_errors = cls.check_merged_stages(text)
        legacy_stages_errors = cls.check_legacy_stages(text)
        nested_tag_errors = cls.check_nested_sup_sub(text)
        chemical_errors = cls.check_raw_chemicals(text)
        band_var_errors = cls.check_raw_band_variables(text)

        all_errors = (
            latex_leaks + slash_fractions + ascii_subscripts + 
            arrow_errors + html_entity_errors + merged_stages_errors + legacy_stages_errors +
            nested_tag_errors + chemical_errors + band_var_errors
        )
        passed = len(all_errors) == 0

        return {
            "passed": passed,
            "raw_latex_leaks": latex_leaks,
            "slash_fractions": slash_fractions,
            "raw_ascii_subscripts": ascii_subscripts,
            "arrow_linebreaks": arrow_errors,
            "raw_html_entities": html_entity_errors,
            "merged_stages": merged_stages_errors,
            "legacy_stages": legacy_stages_errors,
            "nested_tags": nested_tag_errors,
            "raw_chemicals": chemical_errors,
            "raw_band_variables": band_var_errors,
            "unwarranted_claims": [],
            "total_errors": len(all_errors),
        }

    @classmethod
    def generate_pre_check_report(cls, text: str) -> InternalASTLinterReport:
        """Sinh đối tượng InternalASTLinterReport chuẩn hóa theo schema Pydantic."""
        report = cls.lint_text(text)
        return InternalASTLinterReport(
            passed=report["passed"],
            raw_latex_leaks_count=len(report["raw_latex_leaks"]),
            slash_fraction_count=len(report["slash_fractions"]),
            raw_subscript_count=len(report["raw_ascii_subscripts"]),
            unwarranted_claims_count=len(report.get("unwarranted_claims", [])),
        )
