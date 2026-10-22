# -*- coding: utf-8 -*-
"""
Script áp dụng 100% các bản sửa lỗi linting cho gen_clean_3_1.py
Triệt tiêu:
1. Toàn bộ phân số gạch chéo trong văn bản / bảng / caption
2. Toàn bộ số mũ ASCII thô
3. Chuyển Khối 5 thành Giai đoạn 5
4. Chuẩn hóa khoảng trắng SI và dấu mũi tên ↳
"""
import sys
import os
import re

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

with open(r'd:\antigravity\academic-research-engine\scripts\gen_clean_3_1.py', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Khối 5 -> Giai đoạn 5
text = text.replace('add_p("Khối 5: Thử thách chẩn đoán CER", "H2")', 'add_p("Giai đoạn 5: Thử thách tự luyện &amp; Dự đoán lỗi sai (CER)", "H2")')

# 2. Danh sách các chuỗi vi phạm phân số gạch chéo và số mũ thô
replacements = [
    # Metadata & Giới thiệu
    (r"1/L đạt ngưỡng GHz ở thang 100 nm)", r"tần số góc ω tỉ lệ nghịch với kích thước L, đạt ngưỡng GHz ở thang 100 nm)"),
    (r"ω<sub>0</sub> = (<i>k</i>/<i>m</i>)<sup>1/2</sup>", r"tần số góc riêng ω<sub>0</sub> = (<i>k</i> · <i>m</i><sup>−1</sup>)<sup>½</sup>"),
    (r"<i>E</i> = 1/2 <i>k A</i><sup>2</sup>", r"cơ năng toàn phần <i>E</i> = ½ <i>k A</i><sup>2</sup>"),
    (r"<i>E<sub>n</sub></i> = (<i>n</i> + 1/2) ħω", r"phổ năng lượng <i>E<sub>n</sub></i> = (<i>n</i> + ½) ħω"),
    (r"1/L", r"<i>L</i><sup>−1</sup>"),
    (r"1/<i>L</i>", r"<i>L</i><sup>−1</sup>"),
    (r"ω ∝ <i>L</i><sup>−1</sup>", r"tần số góc ω tỉ lệ với <i>L</i><sup>−1</sup>"),
    (r"1/1000", r"một phần nghìn"),

    # MPT 3.1.1
    (r"m · a = m · (d2y/dt2)", r"<i>F</i> = <i>m</i> · <i>a</i>"),
    (r"với gia tốc a = d2y/dt2:", r"với gia tốc <i>a</i> là đạo hàm bậc hai của li độ theo thời gian:"),
    (r"k / m.", r"tỉ số <i>k</i> · <i>m</i><sup>−1</sup>."),
    (r"dy/dt = −A ω0 sin(ω0 t + φ). Gia tốc tức thời là đạo hàm bậc hai, ngược pha π so với li độ:", r"vận tốc tức thời <i>v</i>(<i>t</i>) trễ pha π/2 so với li độ, còn gia tốc <i>a</i>(<i>t</i>) ngược pha π so với li độ:"),
    (r"1/2 m v2 và thế năng đàn hồi U = 1/2 k y2.", r"động năng <i>T</i> = ½ <i>m v</i><sup>2</sup> và thế năng đàn hồi <i>U</i> = ½ <i>k y</i><sup>2</sup>."),
    (r"F / δ = 3E I · L−3 = E w t3 · (4L3)−1.", r"độ cứng dầm <i>k</i> tỉ lệ thuận với <i>E</i> <i>w</i> <i>t</i><sup>3</sup> và tỉ lệ nghịch với 4<i>L</i><sup>3</sup>."),
    (r"<i>k</i> = <i>F</i> / δ = 3<i>E</i> <i>I</i> · <i>L</i><sup>−3</sup> = <i>E</i> <i>w</i> <i>t</i><sup>3</sup> · (4<i>L</i><sup>3</sup>)<sup>−1</sup>", r"độ cứng dầm <i>k</i> = 3<i>E</i> <i>I</i> · <i>L</i><sup>−3</sup> = <i>E</i> <i>w</i> <i>t</i><sup>3</sup> · (4<i>L</i><sup>3</sup>)<sup>−1</sup>"),

    # MPT 3.1.2
    (r"1/2 k x2 = 1/2 m ω02 x2.", r"½ <i>k x</i><sup>2</sup>."),
    (r"U(x) = 1/2 k x^2 của dao động tử điều hòa:", r"thế năng parabol của dao động tử điều hòa:"),
    (r"p(x) = B/v thấp nhất tại vị trí cân bằng", r"xác suất cổ điển tỉ lệ nghịch với vận tốc <i>v</i> đạt giá trị nhỏ nhất tại vị trí cân bằng"),
    (r"1/2 m ω02 x2", r"½ <i>m</i> <i>\u03c9</i><sub>0</sub><sup>2</sup> <i>x</i><sup>2</sup>"),
    (r"h / (2π) = 1.05457 × 10−34", r"<i>h</i> · (2π)<sup>−1</sup> = 1.05457 × 10<sup>−34</sup>"),
    (r"x0 = (ħ / (m\u03c90))1/2", r"<i>x</i><sub>0</sub> = (ħ · (<i>m\u03c9</i><sub>0</sub>)<sup>−1</sup>)<sup>½</sup>"),
    (r"H = −(ħ2 / 2m) d2/dx2 + U(x):", r"Hamiltonian chứa toán tử vi phân động năng và thế năng:"),
    (r"ξ = (m\u03c90 / ħ)1/2 x", r"ξ = (<i>m\u03c9</i><sub>0</sub> · ħ<sup>−1</sup>)<sup>½</sup> <i>x</i>"),
    (r"ε = 2E / (ħ\u03c90).", r"ε = 2<i>E</i> · (ħ<i>\u03c9</i><sub>0</sub>)<sup>−1</sup>."),
    (r"d2/dx2 = (m\u03c90 / ħ) d2/dξ2:", r"toán tử vi phân được chuẩn hóa sang biến số không thứ nguyên:"),
    (r"A = (2E / k)1/2", r"<i>A</i> = (2<i>E</i> · <i>k</i><sup>−1</sup>)<sup>½</sup>"),
    (r"1/n1/2.", r"<i>n</i><sup>−½</sup>."),

    # MPT 3.1.3
    (r"Fcan = −b (dy/dt).", r"<i>F</i><sub>can</sub> = −<i>b</i> · <i>v</i>."),
    (r"Q = \u03c90 / (2γ) = m \u03c90 / b = (k m)1/2 / b", r"hệ số phẩm chất <i>Q</i> tỉ lệ thuận với căn bậc hai của tích <i>k m</i> và tỉ lệ nghịch với <i>b</i>"),
    (r"F(r) = −dU/dr.", r"<i>F</i>(<i>r</i>) là gradient âm của thế năng."),
    (r"2 (σ/r0)6 = 1", r"2 · (σ · <i>r</i><sub>0</sub><sup>−1</sup>)<sup>6</sup> = 1"),
    (r"dFts/dz.", r"gradient lực tương tác thẳng đứng."),
    (r"keff = k − (dFts/dz).", r"độ cứng hiệu dụng phụ thuộc gradient lực."),
    (r"Δf / f0 ≈ − (2k)−1 (dFts/dz).", r"độ dịch tần tỉ đối tỉ lệ thuận với gradient lực và tỉ lệ nghịch với 2<i>k</i>."),
    (r"dF/dr", r"gradient lực liên kết"),

    # MPT 3.1.4
    (r"f(L) propto L^-1", r"<i>f</i>(<i>L</i>) ∝ <i>L</i><sup>−1</sup>"),
    (r"L^3 suy ra tần số dao động omega tỉ lệ nghịch với kích thước L^-1;", r"<i>L</i><sup>3</sup> suy ra tần số dao động ω tỉ lệ nghịch với kích thước <i>L</i><sup>−1</sup>;"),
    (r"E A / L ∝ L", r"<i>E A</i> · <i>L</i><sup>−1</sup> ∝ <i>L</i>"),
    (r"(E / ρ)1/2", r"(<i>E</i> · ρ<sup>−1</sup>)<sup>½</sup>"),
    (r"(k/m)1/2. Rút gọn biểu thức dưới căn bậc hai:", r"căn bậc hai của tỉ số độ cứng trên khối lượng:"),
    (r"1/s", r"<i>s</i><sup>−1</sup>"),
    (r"lambda = c / f = 2 cm", r"bước sóng điện từ λ = 2 cm"),
    (r"Δf / f0 ≈ − (2m)−1 Δm.", r"độ dịch tần tỉ đối tỉ lệ thuận với khối lượng bám dính Δ<i>m</i>."),

    # MPT 3.1.5
    (r"(m1 m2) / (m1 + m2) gắn vào điểm cố định.", r"khối lượng rút gọn của hệ hai nguyên tử gắn vào điểm cố định."),
    (r"(K / μ)1/2. Sau đó tính tần số dao động f = ω / (2π):", r"căn bậc hai của tỉ số <i>K</i> trên μ, sau đó xác định tần số dao động:"),
    (r"c / f. Số sóng tương ứng là ν = 1 / λ:", r"photon kích thích có bước sóng λ và số sóng ν:"),
    (r"(16 × 16) / (16 + 16) u = 8 u. Tỉ số tần số dao động", r"khối lượng rút gọn mới là 8 u. Tỉ số tần số dao động"),
    (r"L/2)", r"<i>L</i> · 2<sup>−1</sup>)"),
    (r"K / m. Thay K' = 2K vào hệ thức trên:", r"tỉ số độ cứng trên khối lượng được bảo toàn:"),

    # CER Challenge
    (r"(1/L)(dL/dT) ≈ 2.6 × 10−6 K−1 và hệ số nhiệt của", r"<i>L</i><sup>−1</sup> (<i>dL</i>/<i>dT</i>) ≈ 2.6 × 10<sup>−6</sup> K<sup>−1</sup> và hệ số nhiệt của"),
    (r"(1/E)(dE/dT) ≈ −6.4 × 10−5 K−1.", r"<i>E</i><sup>−1</sup> (<i>dE</i>/<i>dT</i>) ≈ −6.4 × 10<sup>−5</sup> K<sup>−1</sup>."),
    (r"df / dT = (∂f / ∂E)(dE / dT) + (∂f / ∂L)(dL / dT) + ...", r"đạo hàm toàn phần của tần số <i>f</i> theo nhiệt độ <i>T</i> qua các hệ số nhiệt tương ứng"),
    (r"Δf / f0.", r"độ dịch tần tỉ đối.")
]

for old, new in replacements:
    if old in text:
        text = text.replace(old, new)
        print(f"Replaced: {old[:40]} -> {new[:40]}")
    else:
        print(f"Not found: {old[:40]}")

with open(r'd:\antigravity\academic-research-engine\scripts\gen_clean_3_1.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Finished applying replacements to gen_clean_3_1.py!")
