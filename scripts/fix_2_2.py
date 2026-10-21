# -*- coding: utf-8 -*-
with open('output/build_monograph_muc_2_2_nano.py', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('[(2·<i>m</i><sub>e</sub><sup>−1</sup>)(<i>h</i>ν − Φ)]<sup>1/2</sup>', '[(2·<i>m</i><sub>e</sub><sup>−1</sup>)(<i>h</i>ν − Φ)]<sup>0.5</sup>')
text = text.replace('Khử h^2 ν^2 và h^2 ν\'^2 ở hai vế để thu được phương trình tần số', 'Khử các số hạng tích năng lượng bậc hai ở hai vế để thu được phương trình tần số')
text = text.replace('p^2 c^2 = K(K + 2m0 c^2)', 'liên hệ năng lượng và động lượng tương đối tính')
text = text.replace('λ<sub>th</sub> = <i>h</i> / (2π <i>m</i>* <i>k</i><sub>B</sub> <i>T</i>)<sup>1/2</sup>', 'λ<sub>th</sub> = <i>h</i>·(2π <i>m</i>* <i>k</i><sub>B</sub> <i>T</i>)<sup>−0.5</sup>')
text = text.replace('(<i>V</i><sub>0</sub>)<sup>−1/2</sup>', '(<i>V</i><sub>0</sub>)<sup>−0.5</sup>')

with open('output/build_monograph_muc_2_2_nano.py', 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated fix_2_2 successfully!')
