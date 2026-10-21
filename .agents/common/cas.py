# -*- coding: utf-8 -*-
"""
Common CAS Module (Formal Symbolic Algebra & SymPy Verification Engine)
Trạm 3 (DOHG 2.0): Kiểm chứng Đại số Hình thức SymPy CAS (simplify == 0).
Đóng gói phi trạng thái (Stateless/Reusable Utility).
Phục vụ: quality-gatekeeper, pedagogical-author.
"""

import re
from typing import List, Dict, Tuple, Any, Optional
import sympy as sp
from sympy.parsing.sympy_parser import (
    parse_expr,
    standard_transformations,
    implicit_multiplication_application,
    convert_xor
)

TRANSFORMATIONS = standard_transformations + (
    implicit_multiplication_application,
    convert_xor
)


class SymPyCASEngine:
    """Động cơ Kiểm chứng Đại số Hình thức SymPy."""

    @staticmethod
    def latex_to_sympy_str(latex_str: str) -> str:
        """
        Tiền xử lý chuỗi công thức LaTeX sang biểu thức toán học SymPy có thể phân tích được.
        Hỗ trợ: phân số \\frac{}{}, căn thức \\sqrt{}, hàm lượng giác/mũ/log, và lũy thừa.
        """
        s = latex_str.strip()
        
        # 1. Loại bỏ các lệnh căn chỉnh và khoảng trắng LaTeX
        s = re.sub(r"\\[;,!]|\\quad|\\qquad|\\left|\\right", "", s)
        s = re.sub(r"\\mathrm\{([^}]+)\}", r"\1", s)
        s = re.sub(r"\\text\{([^}]+)\}", r"\1", s)
        
        # 1b. Chuyển đổi các toán tử nhân LaTeX và Unicode sang dấu nhân SymPy *
        s = re.sub(r"\\cdot\b|\\times\b|\\ast\b|[·×]", " * ", s)
        
        # 2. Xử lý phân số đệ quy: \frac{a}{b} -> ((a)/(b))
        while r"\frac" in s:
            new_s = re.sub(r"\\frac\{([^{}]+)\}\{([^{}]+)\}", r"((\1)/(\2))", s)
            if new_s == s:
                break
            s = new_s
            
        # 3. Xử lý căn bậc hai: \sqrt{x} -> sqrt(x)
        s = re.sub(r"\\sqrt\{([^{}]+)\}", r"sqrt(\1)", s)
        
        # 4. Xử lý hàm log và exp
        s = re.sub(r"\\ln\b", "log", s)
        s = re.sub(r"\\exp\b", "exp", s)
        s = re.sub(r"\\sin\b", "sin", s)
        s = re.sub(r"\\cos\b", "cos", s)
        s = re.sub(r"\\tan\b", "tan", s)
        
        # 5. Xóa ký tự gạch chéo ngược còn sót của các ký hiệu Hy Lạp thông dụng
        greek_symbols = [
            "alpha", "beta", "gamma", "delta", "epsilon", "eta", "theta",
            "lambda", "mu", "nu", "rho", "sigma", "tau", "omega", "Gamma", "Delta", "Omega"
        ]
        for g in greek_symbols:
            s = re.sub(rf"\\{g}\b", g, s)
            
        # 6. Thay thế dấu mũ ^ thành ** nếu chưa chuyển
        s = s.replace("^", "**")
        
        # 7. Loại bỏ các dấu gạch chéo ngược còn lại
        s = s.replace("\\", "")
        
        return s.strip()

    @classmethod
    def verify_algebraic_identity(cls, expr_a_latex: str, expr_b_latex: str) -> Tuple[bool, str]:
        """
        Kiểm chứng tính tương đương đại số hình thức:
        simplify(expr_a - expr_b) == 0.
        """
        try:
            str_a = cls.latex_to_sympy_str(expr_a_latex)
            str_b = cls.latex_to_sympy_str(expr_b_latex)
            
            parsed_a = parse_expr(str_a, transformations=TRANSFORMATIONS)
            parsed_b = parse_expr(str_b, transformations=TRANSFORMATIONS)
            
            diff = parsed_a - parsed_b
            simplified_diff = sp.simplify(diff)
            
            if simplified_diff == 0:
                return True, "SymPy CAS PASS: Biểu thức tương đương đồng nhất (hiệu = 0)."
            else:
                return False, f"SymPy CAS MISMATCH: Hiệu giản ước khác 0 (phần dư = {simplified_diff})."
        except Exception as e:
            # Đối với biểu thức quá phức tạp hoặc chứa toán tử vi phân phi giải tích
            return False, f"SymPy CAS PARSE_ERROR: {str(e)}"

    @classmethod
    def verify_derivation_step(cls, lhs_latex: str, rhs_latex: str) -> Tuple[bool, str]:
        """
        Kiểm chứng một bước biến đổi phương trình liên tiếp (LHS -> RHS).
        """
        return cls.verify_algebraic_identity(lhs_latex, rhs_latex)

    @classmethod
    def verify_derivation_chain(cls, steps_latex: List[str]) -> Tuple[bool, List[Dict[str, Any]]]:
        """
        Kiểm chứng toàn bộ chuỗi biến đổi giải tích qua từng bước liên tiếp.
        """
        if len(steps_latex) < 2:
            return True, [{"step": 1, "passed": True, "note": "Chuỗi chỉ có 1 phương trình."}]

        chain_results = []
        all_passed = True

        for i in range(len(steps_latex) - 1):
            step_current = steps_latex[i]
            step_next = steps_latex[i + 1]
            passed, msg = cls.verify_derivation_step(step_current, step_next)
            if not passed:
                all_passed = False
            chain_results.append({
                "step_transition": f"Bước {i + 1} -> Bước {i + 2}",
                "passed": passed,
                "details": msg
            })

        return all_passed, chain_results

    @staticmethod
    def check_zero_omission_residual(
        source_entities: List[str], 
        generated_text: str
    ) -> Tuple[bool, List[str]]:
        """
        Kiểm toán Phần dư Rỗng (Zero-Omission Residual Audit):
        R_residual = S_orig \\ (Union P_i) == rỗng.
        Bảo đảm 100% tham số, giả thiết, điều kiện biên của Slide & Sách đã được bóc tách.
        """
        lower_text = generated_text.lower()
        missing_entities = []

        for entity in source_entities:
            clean_entity = entity.strip()
            if not clean_entity:
                continue
            if clean_entity.lower() not in lower_text:
                missing_entities.append(clean_entity)

        is_zero_omission = (len(missing_entities) == 0)
        return is_zero_omission, missing_entities
