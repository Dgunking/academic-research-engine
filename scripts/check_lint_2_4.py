import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

with open('output/build_monograph_muc_2_6_nano.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for idx, line in enumerate(lines, 1):
    s = line.strip()
    if s.startswith('#'):
        continue
    # check carets
    if '^' in s and 'r"' not in s and "r'" not in s:
        print(f"Line {idx} Caret: {s[:100]}")
    # check slash between alphanumeric or parens or greek
    if re.search(r'[0-9a-zA-Z\)\u0370-\u03ff\u2100-\u214f]\s*/\s*[0-9a-zA-Z\(\u0370-\u03ff\u2100-\u214f]', s):
        if 'os.path' not in s and 'sys.path' not in s and 'r"' not in s and "r'" not in s:
            print(f"Line {idx} Slash: {s[:100]}")

