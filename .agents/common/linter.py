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
    r"&(?:beta|nu|tau|mu|Delta|delta|sigma|ndash|mdash|minus|times|middot|asymp|omega|Omega|alpha|gamma);",
    re.IGNORECASE
)

# Cấm gộp giai đoạn sư phạm (Luật 16 - Anti-Merged-Stages Gate)
MERGED_STAGES_PATTERN = re.compile(
    r"Giai đoạn\s+\d+\s*(?:&|và|\+)\s*\d+",
    re.IGNORECASE
)

# Cấm cấu trúc 5 khối cũ (Anti-Old-Blocks Gate)
OLD_BLOCKS_PATTERN = re.compile(
    r"\b(?:Khối\s+[1-5]:|KHỐI\s+[1-5]:)",
    re.IGNORECASE
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
    def check_old_blocks(text: str) -> List[str]:
        """Phát hiện dấu tích cấu trúc 5 khối cũ (ví dụ: 'Khối 1:')."""
        findings = []
        for match in OLD_BLOCKS_PATTERN.finditer(text):
            findings.append(f"Cấu trúc cũ '{match.group(0)}' (bắt buộc dùng Khung 5 Giai đoạn lũy tiến)")
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
        old_blocks_errors = cls.check_old_blocks(text)

        all_errors = (
            latex_leaks + slash_fractions + ascii_subscripts + 
            arrow_errors + html_entity_errors + merged_stages_errors + old_blocks_errors
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
            "old_blocks": old_blocks_errors,
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
        )
