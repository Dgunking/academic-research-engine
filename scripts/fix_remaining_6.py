# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('output/build_monograph_muc_2_4_nano.py', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Block 19: Thay đoạn g1_p2
old_1 = '∇<sup>2</sup> = (r−12)·(∂/∂<i>r</i>)(<i>r</i><sup>2</sup>·∂/∂<i>r</i>) + (1/(<i>r</i><sup>2</sup>·sin<i>θ</i>))·(∂/∂<i>θ</i>)(sin<i>θ</i>·∂/∂<i>θ</i>) + (1/(<i>r</i><sup>2</sup>·sin<sup>2</sup><i>θ</i>))·(∂<sup>2</sup>/∂<i>φ</i><sup>2</sup>).'
if old_1 not in c:
    # Tìm đoạn g1_p2 bắt đầu
    import re
    c = re.sub(r'∇<sup>2</sup>\s*=\s*[^<]+<br/>', 'Toán tử vi phân Laplace ∇<sup>2</sup> trong tọa độ cầu được phân tách thành các thành phần hướng kính và thành phần góc cực cùng góc phương vị.<br/>', c)
    print("Replaced Laplace operator description")
else:
    c = c.replace(old_1, 'Toán tử vi phân Laplace ∇<sup>2</sup> trong tọa độ cầu được phân tách thành các thành phần hướng kính và thành phần góc cực cùng góc phương vị.')
    print("Replaced old_1")

# 2. Block 106: step2_1_text
import re
c = re.sub(r'<i>R</i><sub>10</sub>\(<i>r</i>\)\s*=\s*[^<]+(?=\. Xây dựng)', 'hàm sóng hướng kính 1s phụ thuộc bán kính Bohr và suy giảm hàm mũ theo khoảng cách <i>r</i>', c)

# 3. Block 112: cer_ev_2: (3/2)·a0
c = c.replace('(3/2)·<i>a</i><sub>0</sub>', '1.5·<i>a</i><sub>0</sub>')
c = c.replace('(3/2)·a0', '1.5·a0')

# 4. Block 192: g4_p2: m·e4 / (8ε02·h3·c)
c = re.sub(r'trong đó <i>R<sub>H</sub></i>\s*=\s*[^<]+(?=≈ 1\.097)', 'trong đó hằng số Rydberg <i>R<sub>H</sub></i> ', c)

# 5. Block 255: g5_p2: √(K/μ)
c = c.replace('√(<i>K</i>/<i>μ</i>)', 'căn bậc hai của tỉ số giữa độ cứng <i>K</i> và <i>μ</i>')
c = c.replace('√(K/μ)', 'căn bậc hai của tỉ số giữa độ cứng K và μ')

# 6. Block 291: step5_3_text: √(I0 / μ)
c = c.replace('√(<i>I</i><sub>0</sub> / <i>μ</i>)', 'căn bậc hai của tỉ số giữa <i>I</i><sub>0</sub> và <i>μ</i>')
c = c.replace('√(I0 / μ)', 'căn bậc hai của tỉ số giữa I0 và μ')

with open('output/build_monograph_muc_2_4_nano.py', 'w', encoding='utf-8') as f:
    f.write(c)
print('Fixed remaining 6 points successfully!')
