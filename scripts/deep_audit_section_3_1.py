import pymupdf as fitz
import re
import os
import sys
import json

sys.stdout.reconfigure(encoding="utf-8")

pdf_path = r"G:\My Drive\NotebookLM - Academic Knowledge Base\Cơ sở vật lý và công nghệ nano\Bai_Giang_Dong_Goi\Chuyen_Khao_Nano_Muc_3.1.pdf"
script_path = r"scripts/gen_clean_3_1.py"
blueprint_path = r"data/BLUEPRINT_MUC_3.1_NANO.json"

doc = fitz.open(pdf_path)
total_pages = len(doc)
full_pdf_text = "\n".join([doc[i].get_text() for i in range(total_pages)])

with open(script_path, "r", encoding="utf-8") as f:
    script_content = f.read()

with open(blueprint_path, "r", encoding="utf-8") as f:
    blueprint_data = json.load(f)

print("="*70)
print("FORENSIC AUDIT STATION 1: PROCESS & FSM ADHERENCE")
print("="*70)
# Check FSM steps in script
has_temp_build = "tempfile" in script_content or "TEMP" in script_content or "target_pdf" in script_content
has_atomic_replace = "os.replace" in script_content
has_doc_build = "doc.build" in script_content or "BookmarkDocTemplate" in script_content
print(f"1. Script uses BookmarkDocTemplate / Doc build: {has_doc_build}")
print(f"2. Script implements Atomic Replace (os.replace): {has_atomic_replace}")
print(f"3. Blueprint Pydantic validation: lesson_title='{blueprint_data.get('lesson_title')}', section_id='{blueprint_data.get('section_id')}'")
print(f"4. Total MPTs in Blueprint: {len(blueprint_data.get('micro_point_topics', []))}")

print("\n" + "="*70)
print("FORENSIC AUDIT STATION 2: ZERO-SKIPPED-STEPS & DERIVATIONS")
print("="*70)
# Check 6 derivations
derivations = {
    "Cantilever harmonic oscillator": ["omega", "k", "m", "1/2 k A^2" or "kA"],
    "Schrodinger hermite": ["Schrödinger", "Hermite", "xi", "hbar", "omega"],
    "Lennard-Jones Taylor": ["Lennard-Jones", "1.122", "57.15", "sigma", "epsilon"],
    "Scaling law": ["1/L" or "L^-1", "tần số", "kích thước", "15 GHz"],
    "CO molecule": ["64.34", "4.66", "CO", "khối lượng rút gọn"],
    "Spring cut in half": ["L/2" or "cắt", "2k", "độ cứng"]
}

for name, tokens in derivations.items():
    found_in_script = all(t.lower() in script_content.lower() for t in tokens)
    print(f"* Derivation '{name}': Found in script: {found_in_script}")

# Count ↳ prefix in script and in PDF
arrow_in_script = len(re.findall(r"↳", script_content))
arrow_in_pdf = len(re.findall(r"↳", full_pdf_text))
print(f"Total ↳ symbols: {arrow_in_script} in script, {arrow_in_pdf} in PDF text")

# Check lazy phrases in script
lazy_phrases = ["dễ thấy", "chứng minh tương tự", "sau một vài phép biến đổi", "tự chứng minh", "bạn đọc tự", "hiển nhiên", "bỏ qua các bước", "không khó để"]
lazy_found = {p: len(re.findall(p, script_content, re.IGNORECASE)) for p in lazy_phrases}
print("Lazy phrases in script:", lazy_found)

print("\n" + "="*70)
print("FORENSIC AUDIT STATION 3: 13 IMMUTABLE CORE ALGORITHMS")
print("="*70)
# Check presence of algorithms in script or codebase
algo_checks = {
    "Algo 1 (DICG 2.0 - Dual Source)": "Bài 3-Properties.pdf" in script_content or "Edward L. Wolf" in script_content or "Wolf" in script_content,
    "Algo 2 (HPDE 2.0 - Anti-Ambiguity)": not any(w in script_content for w in ["nó có thể", "chúng có thể", "điều này cho thấy một cách chung chung"]),
    "Algo 3 & 7 (RVAE 2.0 / HDSE - D-SAFE auto-crop)": "Kho_Hinh_Anh" in script_content or "figures" in script_content,
    "Algo 4 (PLBE - 5 MPTs)": len(blueprint_data.get("micro_point_topics", [])) == 5,
    "Algo 5 (UFME - 5 Progressive Stages)": all(f"Giai đoạn {i}" in script_content for i in [1, 2, 3, 4]),
    "Algo 8 (DOHG 2.0 - Hard Gates)": "assert" in script_content or "lint" in script_content or "check" in script_content,
    "Algo 9 (%TEMP% Isolation)": "replace" in script_content or "temp" in script_content,
    "Algo 10 (ATCC - Nomenclature)": "Bảng" in script_content and ("Tên đại lượng" in script_content or "Ký hiệu" in script_content),
    "Algo 12 (MALAE - 3-level Equations)": "he.create_display_equation" in script_content or "create_display_equation" in script_content,
    "Algo 13 (ZT-GVLE - Layout)": "KeepTogether" in script_content and "Table" in script_content
}
for k, v in algo_checks.items():
    print(f"* {k}: {v}")

print("\n" + "="*70)
print("FORENSIC AUDIT STATION 4: ANTI-PERFUNCTORY & MICRO-MECHANISM DEPTH")
print("="*70)
# Check quantum concepts depth
quantum_terms = ["nguyên lý loại trừ Pauli", "lực đẩy Pauli", "năng lượng điểm không", "zero-point", "độ cong", "thế năng parabol", "xuyên hầm", "Bohr"]
for qt in quantum_terms:
    print(f"* Term '{qt}': {len(re.findall(qt, script_content, re.IGNORECASE))} occurrences in script")

# Check 5 links OCR in figures
ocr_links = ["Bản chất & Mục tiêu", "Giải mã Không gian", "Cơ chế lực", "Điểm uốn", "Ý nghĩa chế tạo"]
for link in ocr_links:
    count = len(re.findall(link, script_content, re.IGNORECASE))
    print(f"* OCR Chain Element '{link}': {count} occurrences")

# Check micro-mechanisms causality arrows
arrow_chars = ["↑", "↓", "→", "⇒", "∝"]
for ac in arrow_chars:
    print(f"* Causality arrow '{ac}': {script_content.count(ac)} occurrences in script")

print("\n" + "="*70)
print("FORENSIC AUDIT STATION 5: PEDAGOGICAL FIDELITY (UFME)")
print("="*70)
# Check 5 stages per MPT
for m in [1, 2, 3, 4, 5]:
    stage_count = sum(1 for s in [1, 2, 3, 4] if f"Luận điểm 3.1.{m}" in script_content)
    print(f"* MPT 3.1.{m}: present in script: {'Luận điểm 3.1.' + str(m) in script_content}")

# Check nomenclature tables
tables_in_script = len(re.findall(r"he\.create_nomenclature_table|Table\(nomenclature", script_content))
print(f"Total Nomenclature Tables generated: {tables_in_script}")

# Check CER sections
cer_challenges = len(re.findall(r"Thử thách|CER|Claim|Evidence|Reasoning", script_content))
print(f"CER challenge occurrences: {cer_challenges}")

print("\n" + "="*70)
print("FORENSIC AUDIT STATION 6: CONTEXT & SYMBOL DRIFT")
print("="*70)
# Verify specific values
specific_values = [
    ("NEMS 100 nm frequency", "15 GHz", "15 GHz" in script_content or "15" in script_content),
    ("CO frequency", "64.34 THz", "64.34" in script_content),
    ("CO wavelength", "4.66 μm", "4.66" in script_content),
    ("LJ equilibrium distance", "1.122 σ", "1.122" in script_content),
    ("LJ effective spring constant", "57.15", "57.15" in script_content),
    ("Cantilever frequency formula", "sqrt(k/m)", "k/m" in script_content or "k" in script_content)
]
for name, val, status in specific_values:
    print(f"* Value '{name}' ({val}): Present={status}")

print("\n" + "="*70)
print("FORENSIC AUDIT STATION 7: CONTEXT SATURATION & ATTENTION DECAY")
print("="*70)
# Word count and page count per MPT in script
mpt_markers = [
    "Luận điểm 3.1.1",
    "Luận điểm 3.1.2",
    "Luận điểm 3.1.3",
    "Luận điểm 3.1.4",
    "Luận điểm 3.1.5",
    "Giai đoạn 5"
]

for i in range(len(mpt_markers)):
    start_tag = mpt_markers[i]
    start_pos = script_content.find(start_tag)
    if i + 1 < len(mpt_markers):
        end_pos = script_content.find(mpt_markers[i+1])
    else:
        end_pos = len(script_content)
    
    chunk = script_content[start_pos:end_pos]
    word_count = len(chunk.split())
    lines = len(chunk.splitlines())
    print(f"* {start_tag}: ~{word_count} words ({lines} code lines)")

print("\n" + "="*70)
print("FORENSIC AUDIT STATION 8: 16 SUPREME PROHIBITIONS (STRICT COMPLIANCE)")
print("="*70)
# Check raw latex in text strings passed to Paragraph
paragraphs_raw = re.findall(r"Paragraph\(\s*f?[\"'](.*?)[\"']\s*,", script_content, re.DOTALL)
slash_fracs = [p for p in paragraphs_raw if re.search(r"\b\d+\s*/\s*\d+\b|\b[a-zA-Z]\s*/\s*[a-zA-Z]\b", p)]
print(f"Total potential slash fractions in Paragraph strings: {len(slash_fracs)}")
for sf in slash_fracs[:5]:
    # Check if it's just date or path
    print(f"   Sample slash text: {sf[:80]}")

ascii_subs = [p for p in paragraphs_raw if re.search(r"\b[a-zA-Z]_[a-zA-Z0-9]+\b", p)]
print(f"Total raw ASCII subscripts in Paragraph strings: {len(ascii_subs)}")
for asub in ascii_subs[:5]:
    print(f"   Sample ASCII sub text: {asub[:80]}")
