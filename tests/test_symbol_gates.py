# -*- coding: utf-8 -*-
import pytest
import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
AGENTS_DIR = os.path.join(PROJECT_ROOT, ".agents")
for p in [AGENTS_DIR, PROJECT_ROOT]:
    if p not in sys.path:
        sys.path.insert(0, p)

from common.linter import ASTLinter
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet

sys.path.insert(0, os.path.abspath(".agents/skills/monograph-pdf-publisher/scripts"))
from hust_pdf_engine import assert_monograph_text_compliance


def test_ast_linter_catches_raw_chemicals():
    bad_text = "Hạt nano WO3 và phiến g-C3N4 phân tán đều trên Ag3VO4."
    good_text = "Hạt nano WO<sub>3</sub> và phiến g-C<sub>3</sub>N<sub>4</sub> phân tán đều trên Ag<sub>3</sub>VO<sub>4</sub>."
    
    assert len(ASTLinter.check_raw_chemicals(bad_text)) == 3
    assert len(ASTLinter.check_raw_chemicals(good_text)) == 0


def test_ast_linter_catches_raw_band_variables():
    bad_text = "Giá trị Eg = 2,42 eV, mức ECB = −1,13 V và EVB = +1,59 V."
    good_text = "Giá trị <i>E<sub>g</sub></i> = 2,42 eV, mức <i>E</i><sub>CB</sub> = −1,13 V và <i>E</i><sub>VB</sub> = +1,59 V."
    
    assert len(ASTLinter.check_raw_band_variables(bad_text)) == 3
    assert len(ASTLinter.check_raw_band_variables(good_text)) == 0


def test_ast_linter_catches_nested_tags():
    bad_text = "Độ âm điện X = [χ]<sup>(a+b)<sup>−1</sup></sup>."
    good_text = "Độ âm điện X = căn bậc (a + b) của tích [χ]."
    
    assert len(ASTLinter.check_nested_sup_sub(bad_text)) == 1
    assert len(ASTLinter.check_nested_sup_sub(good_text)) == 0


def test_ast_linter_catches_raw_arrow_entities():
    bad_text = "Chất phản ứng &rarr; Chất sản phẩm &larr; Cân bằng."
    good_text = "Chất phản ứng → Chất sản phẩm ← Cân bằng."
    
    assert len(ASTLinter.check_raw_html_entities(bad_text)) == 2
    assert len(ASTLinter.check_raw_html_entities(good_text)) == 0


def test_hust_pdf_engine_gate_assertions():
    styles = getSampleStyleSheet()
    
    # Raw chemical must raise AssertionError
    p_bad_chem = Paragraph("Mẫu WO3 monoclinic", styles["Normal"])
    with pytest.raises(AssertionError) as exc_chem:
        assert_monograph_text_compliance([p_bad_chem], require_5_blocks=False)
    assert "WO3" in str(exc_chem.value)
    
    # Raw Eg must raise AssertionError
    p_bad_band = Paragraph("Độ rộng vùng cấm Eg = 2,42 eV", styles["Normal"])
    with pytest.raises(AssertionError) as exc_band:
        assert_monograph_text_compliance([p_bad_band], require_5_blocks=False)
    assert "Eg" in str(exc_band.value)
    
    # Nested sup must raise AssertionError
    p_bad_nested = Paragraph("Hệ số [χ]<sup>(a+b)<sup>−1</sup></sup>", styles["Normal"])
    with pytest.raises(AssertionError) as exc_nested:
        assert_monograph_text_compliance([p_bad_nested], require_5_blocks=False)
    assert "nested sup/sub" in str(exc_nested.value)
    
    # Compliant paragraph must PASS
    p_good = Paragraph("Mẫu WO<sub>3</sub> có độ rộng vùng cấm <i>E<sub>g</sub></i> = 2,75 eV", styles["Normal"])
    report = assert_monograph_text_compliance([p_good], require_5_blocks=False)
    assert report["status"] == "PASS"
