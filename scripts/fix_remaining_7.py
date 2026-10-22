# -*- coding: utf-8 -*-
import sys
import os

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

with open(r'd:\antigravity\academic-research-engine\scripts\gen_clean_3_1.py', 'r', encoding='utf-8') as f:
    c = f.read()

rep_map_last = [
    ('Lấy đạo hàm bậc hai d^2U/dr^2 tại r = r_0 để tìm độ cứng đàn hồi tương đương:',
     'Lấy đạo hàm bậc hai của thế năng tại vị trí cân bằng để tìm độ cứng đàn hồi tương đương:'),
    ('Δ<i>f</i> / <i>f</i><sub>0</sub> ≈ − (2<i>k</i>)<sup>−1</sup> (<i>dF</i><sub>ts</sub>/<i>dz</i>).',
     'độ dịch tần tỉ đối tỉ lệ thuận với gradient lực theo phương thẳng đứng.'),
    ('Tần số góc dao động riêng <i>\u03c9</i><sub>0</sub> = (<i>k</i>/<i>m</i>)<sup>1/2</sup> do đó tỉ lệ nghịch bậc nhất với kích thước <i>L</i>:',
     'Tần số góc dao động riêng <i>\u03c9</i><sub>0</sub> do đó tỉ lệ nghịch bậc nhất với kích thước <i>L</i>:'),
    ('<i>\u03c9</i><sub>0</sub> = (<i>k</i>/<i>m</i>)<sup>1/2</sup>. Rút gọn biểu thức dưới căn bậc hai:',
     'công thức tần số góc riêng của dao động tử điều hòa. Rút gọn biểu thức dưới căn bậc hai:'),
    ('tính bằng λ = <i>c</i> / <i>f</i>. Số sóng tương ứng là ν = 1 / λ:',
     'xác định từ tốc độ ánh sáng <i>c</i> và tần số dao động <i>f</i>:'),
    ('<i>L\'</i> = <i>L</i>/2 trong khi giữ nguyên vật liệu và tiết diện',
     '<i>L\'</i> = 0.5 <i>L</i> trong khi giữ nguyên vật liệu và tiết diện'),
    ('hệ số giãn nở nhiệt tuyến tính α<sub><i>L</i></sub> = <i>L</i><sup>−1</sup> (<i>dL</i>/<i>dT</i>) ≈ 2.6 × 10<sup>−6</sup> K<sup>−1</sup>',
     'hệ số giãn nở nhiệt tuyến tính α<sub><i>L</i></sub> ≈ 2.6 × 10<sup>−6</sup> K<sup>−1</sup>'),
    ('α<sub><i>L</i></sub> = (1/<i>L</i>)(<i>dL</i>/<i>dT</i>)', 'α<sub><i>L</i></sub>'),
    ('α<sub><i>E</i></sub> = (1/<i>E</i>)(<i>dE</i>/<i>dT</i>)', 'α<sub><i>E</i></sub>')
]

for o, n in rep_map_last:
    if o in c:
        c = c.replace(o, n)
        print("Replaced:", o[:35])
    else:
        print("MISSING:", o[:35])

with open(r'd:\antigravity\academic-research-engine\scripts\gen_clean_3_1.py', 'w', encoding='utf-8') as f:
    f.write(c)

print("Applied last 7 fixes!")
