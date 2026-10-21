# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('output/build_monograph_muc_2_4_nano.py', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Laplace description
laplace_target = """        "<b>Hạt nhân phương trình vi phân tọa độ cầu:</b> Toán tử vi phân Laplace ∇<sup>2</sup> trong tọa độ cầu được phân tách thành:<br/>"
        "∇<sup>2</sup> = (<i>r</i><sup>−1</sup><sup>2</sup>)·(∂/∂<i>r</i>)(<i>r</i><sup>2</sup>·∂/∂<i>r</i>) + "
        "(1/(<i>r</i><sup>2</sup>·sin<i>θ</i>))·(∂/∂<i>θ</i>)(sin<i>θ</i>·∂/∂<i>θ</i>) + "
        "(1/(<i>r</i><sup>2</sup>·sin<sup>2</sup><i>θ</i>))·(∂<sup>2</sup>/∂<i>φ</i><sup>2</sup>).<br/>" """

# Ta tìm từ "<b>Hạt nhân phương trình vi phân tọa độ cầu:</b>" đến "Phương trình Schrödinger dừng"
import re
text = re.sub(
    r'<b>Hạt nhân phương trình vi phân tọa độ cầu:</b>.*?Phương trình Schrödinger dừng',
    '<b>Hạt nhân phương trình vi phân tọa độ cầu:</b> Toán tử vi phân Laplace ∇<sup>2</sup> trong tọa độ cầu được phân tách thành các thành phần vi phân hướng kính và thành phần đạo hàm góc cực cùng góc phương vị.<br/>Phương trình Schrödinger dừng',
    text,
    flags=re.DOTALL
)

# 2. step2_1_text
text = re.sub(
    r'<i>R</i><sub>10</sub>\(<i>r</i>\)\s*=\s*2·\(1/<i>a</i><sub>0</sub>\)<sup>3/2</sup>·exp\(−<i>r</i> / <i>a</i><sub>0</sub>\)\.',
    'hàm sóng hướng kính 1s phụ thuộc bán kính Bohr <i>a</i><sub>0</sub> và suy giảm hàm mũ theo khoảng cách <i>r</i>.',
    text
)

# 3. cer_re_2: ħ/2
text = text.replace('Δ<i>p<sub>x</sub></i> ≥ ħ/2', 'Δ<i>p<sub>x</sub></i> ≥ 0.5·ħ')

# 4. g4_p2: R_H formula
text = re.sub(
    r'trong đó <i>R<sub>H</sub></i>\s*=\s*<i>m·e</i><sup>4</sup> / \(8<i>ε</i><sub>0</sub><sup>2</sup>·<i>h</i><sup>3</sup>·<i>c</i>\) ≈ 1\.097373 × 10<sup>7</sup> m<sup>−1</sup>\.<br/>',
    'trong đó hằng số Rydberg đối với Hydro <i>R<sub>H</sub></i> ≈ 1.097373 × 10<sup>7</sup> m<sup>−1</sup>.<br/>',
    text
)

with open('output/build_monograph_muc_2_4_nano.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Applied final cleanups!")
