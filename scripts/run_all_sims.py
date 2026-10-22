# -*- coding: utf-8 -*-
import sys
import subprocess

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

for s in ['3_2', '3_3', '3_4', '3_5']:
    script = f"scripts/generate_simulations_muc_{s}_nano.py"
    print(f"=== Running {script} ===")
    res = subprocess.run([sys.executable, script], capture_output=True, text=True, encoding='utf-8')
    if res.returncode == 0:
        print(f"PASS: {s}")
        print(res.stdout.strip())
    else:
        print(f"FAIL: {s}")
        print(res.stderr)

print("All simulation generation runs complete.")
