# -*- coding: utf-8 -*-
"""
Test Suite: Kiểm toán Nhị phân Nghiệm thu Gemini Spark Agent
Tuân thủ: ENGINEERING_DISCIPLINE_WORKFLOW.md [Pha 3: Bước 3.5]
"""

import os
import sys

def test_all():
    base_dir = r""
    deploy_pkg = r"\GEMINI_SPARK_DEPLOYMENT_PACKAGE"
    
    # 1. Kiểm tra sự tồn tại của các tệp deliverables
    plan_path = os.path.join(base_dir, "PLAN_GEMINI_SPARK_AGENT.md")
    instr_path = os.path.join(base_dir, "FINAL_GEMINI_SPARK_SYSTEM_INSTRUCTIONS.txt")
    deploy_instr = os.path.join(deploy_pkg, "01_GEM_SYSTEM_INSTRUCTIONS", "GEMINI_SPARK_SYSTEM_INSTRUCTIONS.txt")
    kd1_path = os.path.join(deploy_pkg, "02_KNOWLEDGE_DOCUMENTS", "01_Co_So_Du_Lieu_Ban_Dan_Va_Hang_So_CODATA_300K.md")
    kd2_path = os.path.join(deploy_pkg, "02_KNOWLEDGE_DOCUMENTS", "02_Chuan_Danh_Phap_Thuat_Ngu_ATCC_Song_Ngu.md")
    
    assert os.path.exists(plan_path), "FAIL: PLAN_GEMINI_SPARK_AGENT.md not found"
    assert os.path.exists(instr_path), "FAIL: FINAL_GEMINI_SPARK_SYSTEM_INSTRUCTIONS.txt not found"
    assert os.path.exists(deploy_instr), "FAIL: Deploy Instructions not found"
    assert os.path.exists(kd1_path), "FAIL: Knowledge Doc 1 not found"
    assert os.path.exists(kd2_path), "FAIL: Knowledge Doc 2 not found"
    print("[PASS] Deliverables File Existence: 5/5 files verified.")
    
    # 2. Kiểm tra độ dài System Instructions (<= 12.000 ký tự)
    with open(instr_path, "r", encoding="utf-8") as f:
        content = f.read()
    char_count = len(content)
    assert char_count <= 12000, f"FAIL: Instructions exceed limit: {char_count} > 12000"
    print(f"[PASS] Character Limit: {char_count} <= 12000 characters.")
    
    # 3. Kiểm tra Headroom Context Hygiene (Zero zip packages in deployment folder)
    zip_folder = os.path.join(deploy_pkg, "03_SKILL_ZIP_PACKAGES")
    master_zip = os.path.join(deploy_pkg, "GEMINI_SPARK_MASTER_BUNDLE.zip")
    assert not os.path.exists(zip_folder), "FAIL: Redundant zip folder still exists"
    assert not os.path.exists(master_zip), "FAIL: Redundant master zip still exists"
    print("[PASS] Headroom Context Hygiene: 100% redundant zip files purged.")
    
    # 4. Kiểm tra chất lượng tệp Knowledge 1 (CODATA 2022 & 300 K parameters)
    with open(kd1_path, "r", encoding="utf-8") as f:
        kd1_text = f.read()
    assert r"\times" in kd1_text, "FAIL: Missing LaTeX \\times in KD1"
    assert "1{,}424" in kd1_text or "1,424" in kd1_text, "FAIL: Missing GaAs 300 K bandgap"
    assert "3{,}420" in kd1_text or "3,420" in kd1_text, "FAIL: Missing GaN bandgap"
    assert "VARSHNI" in kd1_text.upper(), "FAIL: Missing Varshni parameters"
    assert "ANDERSON" in kd1_text.upper(), "FAIL: Missing Anderson rule"
    print("[PASS] Knowledge Doc 1 (Semiconductor & CODATA): 100% verified.")
    
    # 5. Kiểm tra chất lượng tệp Knowledge 2 (Nomenclature Matrix & Decree 30)
    with open(kd2_path, "r", encoding="utf-8") as f:
        kd2_text = f.read()
    assert "tiếp giáp dị chất" in kd2_text and "heterojunction" in kd2_text, "FAIL: Missing heterojunction term"
    assert "dải dẫn" in kd2_text and "conduction band" in kd2_text, "FAIL: Missing conduction band term"
    assert "Nghị định 30/2020/NĐ-CP" in kd2_text, "FAIL: Missing Decree 30 reference"
    assert "APA 7" in kd2_text, "FAIL: Missing APA 7 reference"
    assert "Luật Đo lường 04" in kd2_text, "FAIL: Missing Law 04 reference"
    print("[PASS] Knowledge Doc 2 (Academic Bilingual Terminology Matrix): 100% verified.")
    
    # 6. Kiểm tra cấu trúc FSM, Zero-Text, Docx-First và Chốt Dừng An Toàn
    assert "/learn" in content, "FAIL: Missing /learn dispatcher"
    assert "Zero-Text" in content, "FAIL: Missing Zero-Text rule"
    assert "ZT-GVLE" in content, "FAIL: Missing ZT-GVLE sandbox specification"
    assert "Silent Drop" in content, "FAIL: Missing Silent Drop scaffolding"
    assert "Ho_So_Kiem_Toan_Chuong_" in content, "FAIL: Missing Word .docx audit file specification"
    assert "CHỐT DỪNG AN TOÀN" in content, "FAIL: Missing Safety Stop Gate when docx is missing"
    assert "Bản Chuyên khảo Mục" in content or "Bản chuyên khảo Mục" in content, "FAIL: Missing PDF anchor"
    assert "Danh mục hình ảnh" in content, "FAIL: Missing Image anchor"
    assert "[Goc]" in content and "[Mo_Phong]" in content, "FAIL: Missing dual-lane image spec"
    print("[PASS] System Instructions Content, Docx-First & Safety Stop Gate: 100% verified.")
    
    print("\n=======================================================")
    print("ALL 6 BINARY ASSERTION CHECKS PASSED (100% SUCCESS)")
    print("=======================================================")

if __name__ == "__main__":
    test_all()
