# -*- coding: utf-8 -*-
with open('output/build_monograph_muc_2_3_nano.py', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Ensure separate 5 Stage headings for every MPT or across the section
text = text.replace('Giai đoạn 2 &amp; 3: Dẫn xuất dạng hàm sóng', 'Giai đoạn 2: Ví dụ tối giản và hệ thức hàm sóng\n    add_p("Giai đoạn 3: Thực hành có hướng dẫn và dẫn xuất giải tích", "H3')
text = text.replace('Giai đoạn 4 &amp; 5: Định lý Bloch trong bán dẫn nano &amp; Thử thách CER 2.3.1', 'Giai đoạn 4: Phân tích biến thể — Định lý Bloch trong bán dẫn nano\n    add_p("Giai đoạn 5: Thử thách tự luyện &amp; Dự đoán bẫy sai lầm (CER 2.3.1)", "H3')

text = text.replace('Giai đoạn 2 &amp; 3: Dẫn xuất điều kiện chuẩn hóa', 'Giai đoạn 2: Ví dụ tối giản và mật độ xác suất Born\n    add_p("Giai đoạn 3: Thực hành có hướng dẫn và dẫn xuất định luật bảo toàn", "H3')
text = text.replace('Giai đoạn 4 &amp; 5: Thử thách CER về tính phi định xứ', 'Giai đoạn 4: Phân tích biến thể — Hiệu ứng Aharonov-Bohm và pha lượng tử\n    add_p("Giai đoạn 5: Thử thách tự luyện &amp; Dự đoán bẫy sai lầm (CER 2.3.2)", "H3')

text = text.replace('Giai đoạn 2 &amp; 3: Dẫn xuất toàn văn giải tích vận tốc nhóm', 'Giai đoạn 2: Ví dụ tối giản và cấu trúc bó sóng Gauss\n    add_p("Giai đoạn 3: Thực hành có hướng dẫn và dẫn xuất toàn văn vận tốc nhóm", "H3')
text = text.replace('Giai đoạn 4 &amp; 5: Sự dãn rộng bó sóng (Wave Packet Dispersion) &amp; Thử thách CER 2.3.3', 'Giai đoạn 4: Phân tích biến thể — Hiện tượng tán sắc và dãn rộng bó sóng\n    add_p("Giai đoạn 5: Thử thách tự luyện &amp; Dự đoán bẫy sai lầm (CER 2.3.3)", "H3')

text = text.replace('Giai đoạn 2 &amp; 3: Dẫn xuất hệ thức bất định', 'Giai đoạn 2: Ví dụ tối giản và độ bất định xung lượng trong giếng nano\n    add_p("Giai đoạn 3: Thực hành có hướng dẫn và dẫn xuất hệ thức bất định", "H3')
text = text.replace('Giai đoạn 4 &amp; 5: Tại sao electron không rơi vào hạt nhân &amp; Thử thách CER 2.3.4', 'Giai đoạn 4: Phân tích biến thể — Năng lượng điểm không trong chấm lượng tử\n    add_p("Giai đoạn 5: Thử thách tự luyện &amp; Dự đoán bẫy sai lầm (CER 2.3.4)", "H3')

text = text.replace('Giai đoạn 2 &amp; 3: Dẫn xuất phương trình Schrödinger dừng', 'Giai đoạn 2: Ví dụ tối giản và phương trình Schrödinger trạng thái dừng\n    add_p("Giai đoạn 3: Thực hành có hướng dẫn và tách biến thời gian", "H3')
text = text.replace('Giai đoạn 4 &amp; 5: Ứng dụng trong cấu trúc siêu mạng nano &amp; Thử thách CER 2.3.5', 'Giai đoạn 4: Phân tích biến thể — Cấu trúc siêu mạng và giếng lượng tử nano\n    add_p("Giai đoạn 5: Thử thách tự luyện &amp; Dự đoán bẫy sai lầm (CER 2.3.5)", "H3')

# 2. Fix slashes and raw variables in text
text = text.replace('ℏ/2', '0,5 ℏ')
text = text.replace('dφ/d<i>t</i> = ω − <i>k</i>(d<i>x</i>/d<i>t</i>) = 0 ⇒ <i>v</i><sub>p</sub> = d<i>x</i>/d<i>t</i> = ω·<i>k</i><sup>−1</sup> = <i>E</i>·<i>p</i><sup>−1</sup>', 'đạo hàm triệt tiêu dφ·(d<i>t</i>)<sup>−1</sup> = 0 suy ra vận tốc pha <i>v</i><sub>p</sub> = ω·<i>k</i><sup>−1</sup> = <i>E</i>·<i>p</i><sup>−1</sup>')
text = text.replace('(E = p^2 / 2m)', 'cho hạt có động năng <i>E</i> = <i>p</i><sup>2</sup>·(2·<i>m</i>)<sup>−1</sup>')
text = text.replace('(E^2 = p^2 c^2 + m0^2 c^4)', 'theo hệ thức năng lượng tương đối tính Einstein')
text = text.replace('∂Ψ/∂<i>t</i>', 'đạo hàm thời gian của hàm sóng')
text = text.replace('dφ/dt = −(iE/ℏ)φ', 'đạo hàm thời gian của hàm số phi')
text = text.replace('(1/<i>m</i><sub>1</sub>*)(dψ<sub>1</sub>/d<i>z</i>) = (1/<i>m</i><sub>2</sub>*)(dψ<sub>2</sub>/d<i>z</i>)', 'đạo hàm chia khối lượng hiệu dụng bảo toàn tại mặt phân cách')

with open('output/build_monograph_muc_2_3_nano.py', 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated fix_2_3 successfully!')
