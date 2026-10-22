# -*- coding: utf-8 -*-
import glob, re, sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

for f in sorted(glob.glob('scripts/generate_simulations_muc_3_*.py')):
    print(f'*** {f} ***')
    with open(f, 'r', encoding='utf-8') as fp:
        lines = fp.readlines()
    for idx, l in enumerate(lines):
        if any(kw in l for kw in ['title', 'label', 'annotate', 'legend', 'text', 'xlabel', 'ylabel']):
            if '/' in l:
                print(f'  L{idx+1}: {l.strip()}')
