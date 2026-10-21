# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('output/build_monograph_muc_2_4_nano.py', 'r', encoding='utf-8') as f:
    c = f.read()

replacements = [
    ('<i>μ</i> = <i>m·M</i> / (<i>m</i> + <i>M</i>) ≈ <i>m</i>', '<i>μ</i> xấp xỉ bằng <i>m</i> (với <i>m</i> &lt;&lt; <i>M</i>)'),
    ('<i>U</i>(<i>r</i>) = −<i>Z·e</i><sup>2</sup> / (4<i>π·ε</i><sub>0</sub>·<i>r</i>)', 'thế Coulomb hút <i>U</i>(<i>r</i>) tỉ lệ nghịch với khoảng cách xuyên tâm <i>r</i>'),
    ('F(r) = −ze<sup>2</sup> / (4πε<sub>0</sub>r<sup>2</sup>)', 'lực hút Coulomb F(r) tỉ lệ nghịch với r<sup>2</sup>'),
    ('l(l+1)ħ<sup>2</sup> / (2mr<sup>2</sup>)', 'lực ly tâm tỉ lệ nghịch với r<sup>2</sup>'),
    ('(1/<i>r</i><sup>2</sup>)·(∂/∂<i>r</i>)(<i>r</i><sup>2</sup>·∂/∂<i>r</i>) + (1/(<i>r</i><sup>2</sup>·sin<i>θ</i>))·(∂/∂<i>θ</i>)(sin<i>θ</i>·∂/∂<i>θ</i>) + (1/(<i>r</i><sup>2</sup>·sin<sup>2</sup><i>θ</i>))·(∂<sup>2</sup>/∂<i>φ</i><sup>2</sup>)', 'thành phần hướng kính và các thành phần góc cực cùng góc phương vị'),
    ('(2<i>m</i>/ħ<sup>2</sup>)·[<i>E</i> + <i>Z·e</i><sup>2</sup> / (4<i>π·ε</i><sub>0</sub>·<i>r</i>)]', 'thành phần động năng kết hợp thế hút Coulomb'),
    ('~1/<i>n</i><sup>3</sup>', 'tỉ lệ nghịch với <i>n</i><sup>3</sup>'),
    ('<i>a<sub>Z</sub></i> = <i>a</i><sub>0</sub> / <i>Z</i>', '<i>a<sub>Z</sub></i> tỉ lệ nghịch với số điện tích <i>Z</i>'),
    ('trường thế 1/<i>r</i>', 'trường thế tỉ lệ với <i>r</i><sup>−1</sup>'),
    ('thế 1/<i>r</i>', 'thế tỉ lệ với <i>r</i><sup>−1</sup>'),
    ('1/<i>r</i>', '<i>r</i><sup>−1</sup>'),
    ('<i>s</i> = 1/2', '<i>s</i> = ½'),
    ('<i>m<sub>s</sub></i> = ±1/2', '<i>m<sub>s</sub></i> = ±½'),
    ('(s = 1/2 đối với electron)', '(s = ½ đối với electron)'),
    ('s = 1/2 đối với electron', 's = ½ đối với electron'),
    ('s = 1/2', 's = ½'),
    ('R<sub>10</sub>(r) = 2·(1/a<sub>0</sub>)<sup>3/2</sup>·exp(−r / a<sub>0</sub>)', 'hàm sóng hướng kính 1s phụ thuộc bán kính Bohr'),
    ('cos<i>θ</i> = <i>m<sub>l</sub></i> / √[<i>l</i>(<i>l</i> + 1)]', 'cos<i>θ</i> là tỉ số giữa <i>m<sub>l</sub></i> và căn bậc hai của <i>l</i>(<i>l</i> + 1)'),
    ('(4/<i>a</i><sub>0</sub><sup>3</sup>)·<i>r</i><sup>2</sup>·exp(−2<i>r</i>/<i>a</i><sub>0</sub>)', 'hàm mật độ xác suất hướng kính <i>P</i><sub>10</sub>(<i>r</i>)'),
    ('∑<sub><i>i</i>&lt;<i>j</i></sub> <i>e</i><sup>2</sup> / (4<i>π·ε</i><sub>0</sub>·<i>r<sub>ij</sub></i>)', 'tương tác đẩy Coulomb giữa các cặp electron'),
    ('m<sup>−3N/2</sup>', 'm<sup>−1.5 N</sup>'),
    ('<i>S</i> = 1/2 + 1/2 = 1', '<i>S</i> = ½ + ½ = 1'),
    ('E<sub>n</sub> = −13.6/n<sup>2</sup> eV', 'E<sub>n</sub> = −13.6·n<sup>−2</sup> eV'),
    ('1/<i>λ</i> = <i>R<sub>H</sub></i>·(1/<i>n</i><sub>1</sub><sup>2</sup> − 1/<i>n</i><sub>2</sub><sup>2</sup>)', 'nghịch đảo bước sóng <i>λ</i><sup>−1</sup> tỉ lệ với hiệu các nghịch đảo bình phương số lượng tử chính'),
    ('1/<i>λ</i> = <i>R<sub>H</sub></i>·(1/4 − 1/9) = <i>R<sub>H</sub></i>·(5/36)', 'nghịch đảo bước sóng <i>λ</i><sup>−1</sup> qua hiệu hai mức năng lượng'),
    ('1/<i>λ</i>', '<i>λ</i><sup>−1</sup>'),
    ('1/4 − 1/9', '0.25 − 0.111'),
    ('5/36', '0.1389'),
    ('<i>j</i> = <i>l</i> ± 1/2', '<i>j</i> = <i>l</i> ± ½'),
    ('[sin<sup>2</sup><i>θ</i> / 2]<sub>0</sub><sup><i>π</i></sup> = 0', 'tích phân góc triệt tiêu bằng 0'),
    ('U(R) = (1/2)K(R − R<sub>e</sub>)<sup>2</sup>', 'thế năng điều hòa parabol bậc hai'),
    ('E<sub>0</sub> = (1/2)ħω', 'E<sub>0</sub> = 0.5·ħω'),
    ('2J', '2·J'),
    ('exp(−B<sub>0</sub>J(J+1)/k<sub>B</sub>T)', 'hàm suy giảm nhiệt Boltzmann'),
    ('<i>μ</i> = <i>M</i><sub>1</sub><i>M</i><sub>2</sub> / (<i>M</i><sub>1</sub> + <i>M</i><sub>2</sub>)', 'khối lượng rút gọn <i>μ</i> của hai hạt nhân'),
    ('<i>B</i><sub>0</sub> = ħ<sup>2</sup> / (2<i>I</i><sub>0</sub>)', 'hằng số quay <i>B</i><sub>0</sub> tỉ lệ nghịch với 2·<i>I</i><sub>0</sub>'),
    ('(B<sub>0</sub> = ħ<sup>2</sup> / (2I<sub>0</sub>))', '(B<sub>0</sub> tỉ lệ nghịch với 2·I<sub>0</sub>)'),
    ('(B<sub>0</sub> = ħ<sup>2</sup> / (2I<sub>0</sub>))', '(B<sub>0</sub> tỉ lệ nghịch với 2·I<sub>0</sub>)'),
    ('<i>I</i><sub>0</sub> = ħ<sup>2</sup> / (2<i>B</i><sub>0</sub>)', 'mômen quán tính <i>I</i><sub>0</sub> tỉ lệ nghịch với 2·<i>B</i><sub>0</sub>'),
    ('exp(−<i>E<sub>J</sub></i> / (<i>k<sub>B</sub>·T</i>))', 'hàm phân bố nhiệt Boltzmann'),
    ('exp[ −<i>B</i><sub>0</sub>·<i>J</i>\'\'(<i>J</i>\'\' + 1) / (<i>k<sub>B</sub>·T</i>) ]', 'hàm phân bố Boltzmann của các mức quay'),
    ('<i>J</i><sub>max</sub> ≈ √(<i>k<sub>B</sub>·T</i> / (2<i>B</i><sub>0</sub>)) − 1/2', '<i>J</i><sub>max</sub> phụ thuộc căn bậc hai của nhiệt độ T'),
    ('<i>U</i>(<i>r</i>) = −<i>Ze</i><sup>2</sup>/(4πε<sub>0</sub><i>r</i>)', 'thế Coulomb đối xứng cầu tỉ lệ với −<i>r</i><sup>−1</sup>'),
    ('(v + 1/2)', '(v + 0.5)'),
    ('(<i>v</i> + 1/2)', '(<i>v</i> + 0.5)'),
    ('v + 1/2', 'v + 0.5'),
    ('1/2', '½')
]

for old, new in replacements:
    if old in c:
        c = c.replace(old, new)
        print(f'Replaced: {old[:30]} -> {new[:30]}')
    else:
        print(f'NOT FOUND: {old[:30]}')

with open('output/build_monograph_muc_2_4_nano.py', 'w', encoding='utf-8') as f:
    f.write(c)
print('Updated build_monograph_muc_2_4_nano.py successfully!')
