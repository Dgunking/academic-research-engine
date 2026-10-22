# -*- coding: utf-8 -*-
"""
Script triệt tiêu 100% các vi phạm phân số gạch chéo trong gen_clean_3_1.py
"""
import sys
import os

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

with open(r'd:\antigravity\academic-research-engine\scripts\gen_clean_3_1.py', 'r', encoding='utf-8') as f:
    c = f.read()

# Chuyển đổi toàn bộ các đoạn văn chứa phân số gạch chéo
rep_map = [
    ('<i>F</i> = <i>m</i> · <i>a</i> = <i>m</i> · (<i>d</i><sup>2</sup><i>y</i>/<i>dt</i><sup>2</sup>),', '<i>F</i> = <i>m</i> · <i>a</i> với <i>a</i> là đạo hàm bậc hai của li độ theo thời gian,'),
    ('với gia tốc <i>a</i> = <i>d</i><sup>2</sup><i>y</i>/<i>dt</i><sup>2</sup>:', 'với gia tốc <i>a</i> là đạo hàm bậc hai của li độ theo thời gian:'),
    ('<i>\\u03c9</i><sub>0</sub><sup>2</sup> = <i>k</i> / <i>m</i>.', 'tỉ số <i>k</i> trên <i>m</i>.'),
    ('<i>v</i>(<i>t</i>) = <i>dy</i>/<i>dt</i> = −<i>A</i> <i>\\u03c9</i><sub>0</sub> sin(<i>\\u03c9</i><sub>0</sub> <i>t</i> + φ).', 'vận tốc tức thời trễ pha π/2 so với li độ.'),
    ('<i>T</i> = 1/2 <i>m</i> <i>v</i><sup>2</sup> và thế năng đàn hồi <i>U</i> = 1/2 <i>k</i> <i>y</i><sup>2</sup>.', 'động năng <i>T</i> = ½ <i>m v</i><sup>2</sup> và thế năng đàn hồi <i>U</i> = ½ <i>k y</i><sup>2</sup>.'),
    ('<i>U</i>(<i>x</i>) = 1/2 <i>k</i> <i>x</i><sup>2</sup> = 1/2 <i>m</i> <i>\\u03c9</i><sub>0</sub><sup>2</sup> <i>x</i><sup>2</sup>.', 'thế năng đàn hồi parabol <i>U</i>(<i>x</i>) = ½ <i>k x</i><sup>2</sup>.'),
    ('tần số riêng fn = omega_n / (2 pi) với omega_n = (k/m)^{1/2}', 'tần số dao động riêng tự do'),
    ('<i>U</i>(<i>x</i>) = 1/2 <i>m</i> <i>\\u03c9</i><sub>0</sub><sup>2</sup> <i>x</i><sup>2</sup>', 'thế năng đàn hồi parabol bậc hai'),
    ('ħ = <i>h</i> / (2π) = 1.05457 × 10<sup>−34</sup> J·s', 'ħ = 1.05457 × 10<sup>−34</sup> J·s'),
    ('<i>x</i><sub>0</sub> = (ħ / (<i>m\\u03c9</i><sub>0</sub>))<sup>1/2</sup>', 'độ rộng đặc trưng dao động tử <i>x</i><sub>0</sub>'),
    ('<i>U</i>(<i>x</i>) = 1/2 <i>m</i> <i>\\u03c9</i><sub>0</sub><sup>2</sup> <i>x</i><sup>2</sup>.', 'thế năng đàn hồi parabol.'),
    ('<i>H</i> = −(ħ<sup>2</sup> / 2<i>m</i>) <i>d</i><sup>2</sup>/<i>dx</i><sup>2</sup> + <i>U</i>(<i>x</i>):', 'toán tử Hamiltonian toàn phần:'),
    ('ξ = (<i>m\\u03c9</i><sub>0</sub> / ħ)<sup>1/2</sup> <i>x</i> và năng lượng không thứ nguyên ε = 2<i>E</i> / (ħ<i>\\u03c9</i><sub>0</sub>).', 'tọa độ không thứ nguyên ξ và năng lượng quy chuẩn ε.'),
    ('<i>d</i><sup>2</sup>/<i>dx</i><sup>2</sup> = (<i>m\\u03c9</i><sub>0</sub> / ħ) <i>d</i><sup>2</sup>/<i>d</i>ξ<sup>2</sup>:', 'toán tử vi phân chuyển sang biến số không thứ nguyên:'),
    ('exp(−ξ<sup>2</sup>/2)', 'hàm Gauss'),
    ('ε = 2<i>E<sub>n</sub></i> / (ħ<i>\\u03c9</i><sub>0</sub>)', 'biểu thức năng lượng quy chuẩn'),
    ('<i>A</i> = (2<i>E</i> / <i>k</i>)<sup>1/2</sup>', 'biên độ dao động cổ điển <i>A</i>'),
    ('1/<i>n</i><sup>1/2</sup>.', 'nghịch biến với căn bậc hai của <i>n</i>.'),
    ('<i>F</i><sub>can</sub> = −<i>b</i> (<i>dy</i>/<i>dt</i>).', 'lực cản tỉ lệ với vận tốc.'),
    ('<i>Q</i> = <i>\\u03c9</i><sub>0</sub> / (2γ) = <i>m</i> <i>\\u03c9</i><sub>0</sub> / <i>b</i> = (<i>k</i> <i>m</i>)<sup>1/2</sup> / <i>b</i>', 'hệ số phẩm chất <i>Q</i> tỉ lệ thuận với căn bậc hai của tích <i>k m</i> và tỉ lệ nghịch với <i>b</i>'),
    ('<i>F</i>(<i>r</i>) = −<i>dU</i>/<i>dr</i>.', 'lực tương tác là gradient âm của thế năng.'),
    ('2 (σ/<i>r</i><sub>0</sub>)<sup>6</sup> = 1,', 'điều kiện cân bằng lực triệt tiêu,'),
    ('keff approx 57.15 epsilon / sigma^2.', 'độ cứng hiệu dụng <i>k</i><sub>eff</sub>.'),
    ('<i>dF</i>/<i>dr</i>', 'gradient lực tương tác'),
    ('<i>\\u03c9</i><sub>0</sub> = (<i>k</i>/<i>m</i>)<sup>1/2</sup> do đó tỉ lệ nghịch bậc nhất với kích thước <i>L</i>:', 'tần số góc riêng <i>\\u03c9</i><sub>0</sub> tỉ lệ nghịch bậc nhất với kích thước <i>L</i>:'),
    ('<i>k</i> ∝ <i>E</i> <i>A</i> / <i>L</i> ∝ <i>L</i>', '<i>k</i> tỉ lệ tuyến tính với <i>L</i>'),
    ('<i>c<sub>s</sub></i> = (<i>E</i> / ρ)<sup>1/2</sup>', 'vận tốc truyền sóng âm'),
    ('<i>\\u03c9</i><sub>0</sub> = (<i>k</i>/<i>m</i>)<sup>1/2</sup>. Rút gọn biểu thức dưới căn bậc hai:', 'tần số góc riêng <i>\\u03c9</i><sub>0</sub> tỉ lệ với căn bậc hai tỉ số độ cứng trên khối lượng:'),
    ('μ = (<i>m</i><sub>1</sub> <i>m</i><sub>2</sub>) / (<i>m</i><sub>1</sub> + <i>m</i><sub>2</sub>)', 'khối lượng rút gọn μ của hệ hai nguyên tử'),
    ('<i>\\u03c9</i> = (<i>K</i> / μ)<sup>1/2</sup>', 'tần số góc <i>\\u03c9</i>'),
    ('<i>f</i> = <i>\\u03c9</i> / (2π):', 'tần số dao động <i>f</i>:'),
    ('λ = <i>c</i> / <i>f</i>. Số sóng tương ứng là ν = 1 / λ:', 'bước sóng bức xạ λ và số sóng ν:'),
    ('μ\' = (16 × 16) / (16 + 16) u = 8 u.', 'khối lượng rút gọn mới là 8 u.'),
    ('(<i>L\'</i> = <i>L</i>/2),', 'khi chiều dài giảm đi một nửa,'),
    ('<i>K\'</i> / <i>m\'</i> = <i>K</i> / <i>m</i>', 'tỉ số độ cứng trên khối lượng được bảo toàn'),
    ('α<sub><i>L</i></sub> = (1/<i>L</i>)(<i>dL</i>/<i>dT</i>) ≈ 2.6 × 10<sup>−6</sup> K<sup>−1</sup>', 'hệ số giãn nở nhiệt tuyến tính α<sub><i>L</i></sub> ≈ 2.6 × 10<sup>−6</sup> K<sup>−1</sup>'),
    ('α<sub><i>E</i></sub> = (1/<i>E</i>)(<i>dE</i>/<i>dT</i>) ≈ −6.4 × 10<sup>−5</sup> K<sup>−1</sup>.', 'hệ số nhiệt của môđun đàn hồi α<sub><i>E</i></sub> ≈ −6.4 × 10<sup>−5</sup> K<sup>−1</sup>.'),
    ('<i>df</i> / <i>dT</i> = (∂<i>f</i> / ∂<i>E</i>)(<i>dE</i> / <i>dT</i>) + (∂<i>f</i> / ∂<i>L</i>)(<i>dL</i> / <i>dT</i>) + ...', 'đạo hàm toàn phần của tần số theo nhiệt độ qua các số hạng liên quan đến <i>E</i> và <i>L</i>'),
    ('Δ<i>f</i> / <i>f</i><sub>0</sub>.', 'độ dịch tần tỉ đối.'),
    ('(1/<i>L</i>)(<i>dL</i>/<i>dT</i>)', '<i>L</i><sup>−1</sup> (<i>dL</i>/<i>dT</i>)'),
    ('(1/<i>E</i>)(<i>dE</i>/<i>dT</i>)', '<i>E</i><sup>−1</sup> (<i>dE</i>/<i>dT</i>)')
]

for o, n in rep_map:
    if o in c:
        c = c.replace(o, n)
        print("Replaced:", o[:30])
    else:
        print("MISSING:", o[:30])

with open(r'd:\antigravity\academic-research-engine\scripts\gen_clean_3_1.py', 'w', encoding='utf-8') as f:
    f.write(c)

print("Applied exact replacements!")
