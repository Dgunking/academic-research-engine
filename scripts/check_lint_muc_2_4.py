# -*- coding: utf-8 -*-
import re, sys

sys.stdout.reconfigure(encoding='utf-8')
with open('output/build_monograph_muc_2_4_nano.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

errors = 0
for idx, line in enumerate(lines, 1):
    s = line.strip()
    if s.startswith('#'):
        continue
    
    # 1. Kiểm tra raw HTML entities
    html_ent = re.findall(r'&[a-zA-Z]+;', s)
    bad_ents = [e for e in html_ent if e not in ('&amp;', '&lt;', '&gt;', '&quot;')]
    if bad_ents:
        print(f'Line {idx} Bad HTML Entity: {bad_ents} -> {s[:100]}')
        errors += 1
        
    # 2. Kiểm tra carets ngoài raw strings
    if '^' in s and 'r"' not in s and "r'" not in s:
        print(f'Line {idx} Caret: {s[:100]}')
        errors += 1
        
    # 3. Kiểm tra raw LaTeX $ trong make_paragraph
    if 'make_paragraph' in s and '$' in s:
        print(f'Line {idx} Raw LaTeX: {s[:100]}')
        errors += 1

print(f'Done linting. Total errors found: {errors}')
