# -*- coding: utf-8 -*-
import sys
import os

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

with open(r'd:\antigravity\academic-research-engine\scripts\gen_clean_3_1.py', 'r', encoding='utf-8') as f:
    c = f.read()

rep_map_final = [
    ('<i>p</i><sub>cl</sub>(<i>x</i>) = <i>B</i> / <i>v</i>(<i>x</i>) = [π (<i>A</i><sup>2</sup> − <i>x</i><sup>2</sup>)<sup>1/2</sup>]<sup>−1</sup>.',
     'xác suất tìm thấy hạt trong cơ học cổ điển tỉ lệ nghịch với vận tốc tức thời, có biểu thức phụ thuộc vào li độ và đạt cực đại ở hai biên đảo chiều.'),
    ('hội tụ chính xác về hàm phân bố xác suất cổ điển <i>p</i><sub>cl</sub>(<i>x</i>) = [π (<i>A</i><sup>2</sup> − <i>x</i><sup>2</sup>)<sup>1/2</sup>]<sup>−1</sup>,',
     'hội tụ chính xác về đường bao hàm phân bố xác suất của cơ học cổ điển <i>p</i><sub>cl</sub>(<i>x</i>),'),
    ('Lực cản môi trường F_can = -b v làm suy giảm',
     'Lực cản môi trường <i>F</i><sub>can</sub> = −<i>b</i> <i>v</i> làm suy giảm'),
    ('xác định vị trí cân bằng r_0 tại đáy giếng thế nơi lực tương tác F = -dU/dr = 0 (Slide 15 bài giảng HUST).',
     'xác định vị trí cân bằng <i>r</i><sub>0</sub> tại đáy giếng thế nơi lực tương tác triệt tiêu bằng không (Slide 15 bài giảng HUST).'),
    ('2<sup>1/6</sup> σ', '1.122 σ'),
    ('2<sup>1/6</sup> * sigma approx 1.12246 * sigma', '1.12246 σ'),
    ('<i>m</i> (<i>d</i><sup>2</sup><i>y</i>/<i>dt</i><sup>2</sup>) = −<i>k</i> <i>y</i> − <i>b</i> (<i>dy</i>/<i>dt</i>):',
     'định luật II Newton cho hệ dao động có lực cản:'),
    ('với tần số dao động suy giảm <i>\\u03c9</i><sub><i>d</i></sub> = (<i>\\u03c9</i><sub>0</sub><sup>2</sup> − γ<sup>2</sup>)<sup>1/2</sup>.',
     'với tần số dao động suy giảm <i>\\u03c9</i><sub><i>d</i></sub>.'),
    ('vị trí cân bằng bền r_0 = 2^{1/6} * sigma approx 1.12246 * sigma và U(r_0) = -epsilon. Lấy đạo hàm bậc hai d^2U/dr^2 tại r = r_0 để tìm độ cứng đàn hồi tương đương:',
     'vị trí cân bằng bền <i>r</i><sub>0</sub> ≈ 1.12246 σ và thế năng cực tiểu −ε. Lấy đạo hàm bậc hai của thế năng để tìm độ cứng đàn hồi tương đương:'),
    ('biến đổi độ cứng hiệu dụng của dầm: <i>k</i><sub>eff</sub> = <i>k</i> − (<i>dF</i><sub>ts</sub>/<i>dz</i>).',
     'biến đổi độ cứng hiệu dụng của dầm phụ thuộc gradient lực.'),
    ('Tần số góc dao động riêng <i>\\u03c9</i><sub>0</sub> = (<i>k</i>/<i>m</i>)<sup>1/2</sup> do đó tỉ lệ nghịch bậc nhất với kích thước <i>L</i>:',
     'Tần số góc dao động riêng <i>\\u03c9</i><sub>0</sub> tỉ lệ nghịch bậc nhất với kích thước <i>L</i>:'),
    ('hệ thức: <i>\\u03c9</i><sub>0</sub> = (<i>k</i>/<i>m</i>)<sup>1/2</sup>. Rút gọn biểu thức dưới căn bậc hai:',
     'công thức tần số góc riêng của dao động tử điều hòa:'),
    ('Bước 3: Bước sóng của photon kích thích có năng lượng tương ứng với lượng tử dao động được tính bằng λ = <i>c</i> / <i>f</i>. Số sóng tương ứng là ν = 1 / λ:',
     'Bước 3: Bước sóng bức xạ λ và số sóng ν tương ứng của photon kích thích:'),
    ('<i>F</i> = (<i>E</i> · <i>A</i> / <i>L</i>) · Δ<i>L</i>. Do đó, độ cứng đàn hồi của thanh hoặc lò xo là: <i>K</i> = <i>E</i> <i>A</i> / <i>L</i>.',
     'lực đàn hồi tỉ lệ với độ dời qua độ cứng đàn hồi <i>K</i> tỉ lệ nghịch với chiều dài <i>L</i>.'),
    ('hệ số giãn nở nhiệt tuyến tính α<sub><i>L</i></sub> = <i>L</i><sup>−1</sup> (<i>dL</i>/<i>dT</i>) ≈ 2.6 × 10<sup>−6</sup> K<sup>−1</sup>',
     'hệ số giãn nở nhiệt tuyến tính α<sub><i>L</i></sub> ≈ 2.6 × 10<sup>−6</sup> K<sup>−1</sup>'),
    ('hệ số nhiệt của môđun đàn hồi Young (Temperature Coefficient of Elastic Modulus — TCEM) α<sub><i>E</i></sub> = <i>E</i><sup>−1</sup> (<i>dE</i>/<i>dT</i>) ≈ −6.4 × 10<sup>−5</sup> K<sup>−1</sup>.',
     'hệ số nhiệt của môđun đàn hồi Young (TCEM) α<sub><i>E</i></sub> ≈ −6.4 × 10<sup>−5</sup> K<sup>−1</sup>.')
]

for o, n in rep_map_final:
    if o in c:
        c = c.replace(o, n)
        print("Replaced:", o[:35])
    else:
        print("MISSING:", o[:35])

with open(r'd:\antigravity\academic-research-engine\scripts\gen_clean_3_1.py', 'w', encoding='utf-8') as f:
    f.write(c)

print("Applied final replacements!")
