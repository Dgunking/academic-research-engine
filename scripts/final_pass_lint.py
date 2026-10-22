# -*- coding: utf-8 -*-
import sys
import os

with open(r'd:\antigravity\academic-research-engine\scripts\gen_clean_3_1.py', 'r', encoding='utf-8') as f:
    s = f.read()

# 1. Block 150
s = s.replace(
    "Lấy đạo hàm bậc hai <i>d</i><sup>2</sup><i>U</i>/<i>dr</i><sup>2</sup> tại <i>r</i> = <i>r</i><sub>0</sub> để tìm độ cứng đàn hồi tương đương:",
    "Lấy đạo hàm bậc hai của thế năng tại vị trí cân bằng để tìm độ cứng đàn hồi tương đương:"
)

# 2. Block 160
s = s.replace(
    "Tần số góc dao động riêng <i>ω</i><sub>0</sub> = (<i>k</i>/<i>m</i>)<sup>1/2</sup> do đó tỉ lệ nghịch bậc nhất với kích thước <i>L</i>:",
    "Tần số góc dao động riêng <i>ω</i><sub>0</sub> do đó tỉ lệ nghịch bậc nhất với kích thước <i>L</i>:"
)
s = s.replace(
    "<i>\\u03c9</i><sub>0</sub> = (<i>k</i>/<i>m</i>)<sup>1/2</sup> do đó tỉ lệ nghịch",
    "<i>\\u03c9</i><sub>0</sub> do đó tỉ lệ nghịch"
)

# 3. Block 188
s = s.replace(
    "công thức tần số góc dao động riêng của hệ: <i>ω</i><sub>0</sub> = (<i>k</i>/<i>m</i>)<sup>1/2</sup>. Rút gọn biểu thức dưới căn bậc hai:",
    "công thức tần số góc dao động riêng của hệ. Rút gọn biểu thức dưới căn bậc hai:"
)
s = s.replace(
    "công thức tần số góc dao động riêng của hệ: <i>\\u03c9</i><sub>0</sub> = (<i>k</i>/<i>m</i>)<sup>1/2</sup>. Rút gọn biểu thức dưới căn bậc hai:",
    "công thức tần số góc dao động riêng của hệ. Rút gọn biểu thức dưới căn bậc hai:"
)

# 4. Block 226
s = s.replace(
    "tính bằng λ = <i>c</i> / <i>f</i>. Số sóng tương ứng là ν = 1 / λ:",
    "xác định từ tốc độ ánh sáng <i>c</i> và tần số dao động <i>f</i>:"
)

# 5. Block 228
s = s.replace(
    "giảm một nửa <i>L'</i> = <i>L</i>/2 trong khi giữ nguyên",
    "giảm một nửa <i>L'</i> = 0.5 <i>L</i> trong khi giữ nguyên"
)
s = s.replace(
    "giảm một nửa <i>L'</i> = 0.5 <i>L</i> trong khi giữ nguyên",
    "giảm một nửa <i>L'</i> = 0.5 <i>L</i> trong khi giữ nguyên"
)

# 6. Block 235
s = s.replace(
    "(<i>L</i><sup>−1</sup>)(<i>dL</i>/<i>dT</i>)",
    "đạo hàm dãn nở"
)
s = s.replace(
    "(<i>L</i><sup>−1</sup>)(<i>dL</i>/<i>dT</i>)",
    "đạo hàm dãn nở"
)
s = s.replace(
    "α<sub><i>L</i></sub> = (<i>L</i><sup>−1</sup>)(<i>dL</i>/<i>dT</i>)",
    "α<sub><i>L</i></sub>"
)

with open(r'd:\antigravity\academic-research-engine\scripts\gen_clean_3_1.py', 'w', encoding='utf-8') as f:
    f.write(s)

print("Applied final_pass_lint replacements successfully!")
