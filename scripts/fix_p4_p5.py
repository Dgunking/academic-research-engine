# -*- coding: utf-8 -*-
with open(r'd:\antigravity\academic-research-engine\scripts\gen_clean_3_1.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Fix p4_step3
old_p4 = '''    p4_step3 = (
        "Xác lập định luật tỉ lệ nghịch bậc nhất của tần số dao động theo kích thước:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: "
        "Thay thế tỉ lệ của độ cứng <i>k</i> ∝ <i>L</i> và khối lượng <i>m</i> ∝ <i>L</i><sup>3</sup> vào công thức tần số góc dao động riêng của hệ: <i>\u03c9</i><sub>0</sub> = (<i>k</i>/<i>m</i>)<sup>1/2</sup>. Rút gọn biểu thức dưới căn bậc hai:"
    )'''

new_p4 = '''    p4_step3 = (
        "Xác lập định luật tỉ lệ nghịch bậc nhất của tần số dao động theo kích thước:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: "
        "Thay thế tỉ lệ của độ cứng <i>k</i> ∝ <i>L</i> và khối lượng <i>m</i> ∝ <i>L</i><sup>3</sup> vào công thức tần số góc riêng của hệ dao động tử điều hòa. Rút gọn biểu thức dưới căn bậc hai:"
    )'''

if old_p4 in text:
    text = text.replace(old_p4, new_p4)
    print("Fixed p4_step3 successfully!")
else:
    print("p4_step3 not found with exact match, doing regex...")
    import re
    text = re.sub(
        r'p4_step3\s*=\s*\(.*?\n\s*\)',
        new_p4.strip(),
        text,
        flags=re.DOTALL
    )
    print("Fixed p4_step3 with regex!")

# Fix p5_step3
old_p5 = '''    p5_step3 = (
        "Tiếp tục Bài toán 1: Tính bước sóng quang học và số sóng hồng ngoại đặc trưng:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: "
        "Bước 3: Bước sóng của photon kích thích có năng lượng tương ứng với lượng tử dao động được tính bằng λ = <i>c</i> / <i>f</i>. "
        "Số sóng tương ứng là ν = 1 / λ:"
    )'''

new_p5 = '''    p5_step3 = (
        "Tiếp tục Bài toán 1: Tính bước sóng quang học và số sóng hồng ngoại đặc trưng:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: "
        "Bước 3: Bước sóng bức xạ λ và số sóng ν tương ứng của photon kích thích:"
    )'''

if old_p5 in text:
    text = text.replace(old_p5, new_p5)
    print("Fixed p5_step3 successfully!")
else:
    print("p5_step3 not found with exact match, doing regex...")
    import re
    text = re.sub(
        r'p5_step3\s*=\s*\(.*?\n\s*\)',
        new_p5.strip(),
        text,
        flags=re.DOTALL
    )
    print("Fixed p5_step3 with regex!")

with open(r'd:\antigravity\academic-research-engine\scripts\gen_clean_3_1.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Done fixing p4_step3 and p5_step3!")
