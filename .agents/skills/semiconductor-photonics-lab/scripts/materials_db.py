"""
HUST Physics & Semiconductor Photonics Lab - Database Vật liệu Bán dẫn & Hằng số CODATA
"""

# 1. Hằng số Vật lý Căn bản (CODATA 2018/2022)
CODATA = {
    'q': 1.602176634e-19,         # Điện tích nguyên tố [C]
    'hbar': 1.054571817e-34,      # Hằng số Planck rút gọn [J.s]
    'h': 6.62607015e-34,          # Hằng số Planck [J.s]
    'm0': 9.1093837e-31,          # Khối lượng electron tự do [kg]
    'kB': 1.380649e-23,           # Hằng số Boltzmann [J/K]
    'kB_eV': 8.617333262e-5,      # Hằng số Boltzmann [eV/K]
    'eps0': 8.8541878128e-12,     # Độ điện thẩm chân không [F/m]
    'c': 2.99792458e8             # Vận tốc ánh sáng [m/s]
}

# 2. Thông số Bán dẫn ở 300 K
SEMICONDUCTORS_300K = {
    'GaAs': {
        'name': 'Gallium Arsenide',
        'Eg': 1.424,              # Vùng cấm [eV] (trực tiếp)
        'me_eff': 0.067,          # Khối lượng hiệu dụng e (m*/m0)
        'mhh_eff': 0.45,          # Khối lượng hiệu dụng lỗ trống nặng
        'mlh_eff': 0.082,         # Khối lượng hiệu dụng lỗ trống nhẹ
        'eps_r': 12.9,            # Hằng số điện môi tương đối
        'nr': 3.65,               # Chiết suất quang học ở 300 K
        'delta_Ec_ratio': 0.65,   # Tỷ lệ gián đoạn vùng dẫn dE_c / dE_g
        'auger_coeff_C': 1.0e-30, # Hệ số tái hợp Auger C [cm^6/s]
        'varshni_alpha': 5.405e-4,# [eV/K]
        'varshni_beta': 204.0     # [K]
    },
    'InP': {
        'name': 'Indium Phosphide',
        'Eg': 1.344,
        'me_eff': 0.077,
        'mhh_eff': 0.60,
        'mlh_eff': 0.12,
        'eps_r': 12.5,
        'nr': 3.17,
        'delta_Ec_ratio': 0.40,
        'auger_coeff_C': 9.0e-30,
        'varshni_alpha': 4.900e-4,
        'varshni_beta': 327.0
    },
    'AlGaAs': {
        'name': 'Aluminium Gallium Arsenide (x=0.3)',
        'Eg': 1.798,              # Al_0.3Ga_0.7As ở 300 K
        'me_eff': 0.092,
        'mhh_eff': 0.48,
        'mlh_eff': 0.094,
        'eps_r': 12.0,
        'nr': 3.385,
        'delta_Ec_ratio': 0.65,
        'auger_coeff_C': 1.0e-30,
        'varshni_alpha': 5.405e-4,
        'varshni_beta': 204.0
    },
    'InGaAsP': {
        'name': 'Indium Gallium Arsenide Phosphide (1.55 um)',
        'Eg': 0.800,              # Khớp mạng InP phát xạ 1.55 um
        'me_eff': 0.041,
        'mhh_eff': 0.44,
        'mlh_eff': 0.051,
        'eps_r': 13.9,
        'nr': 3.520,
        'delta_Ec_ratio': 0.40,
        'auger_coeff_C': 3.0e-29,
        'varshni_alpha': 4.500e-4,
        'varshni_beta': 280.0
    },
    'GaN': {
        'name': 'Gallium Nitride',
        'Eg': 3.420,
        'me_eff': 0.200,
        'mhh_eff': 0.80,
        'eps_r': 8.9,
        'nr': 2.40,
        'varshni_alpha': 9.090e-4,
        'varshni_beta': 830.0
    },
    'Si': {
        'name': 'Silicon',
        'Eg': 1.120,              # Gián tiếp
        'me_eff': 1.080,
        'mhh_eff': 0.56,
        'eps_r': 11.7,
        'nr': 3.42,
        'varshni_alpha': 4.730e-4,
        'varshni_beta': 636.0
    },
    'Ge': {
        'name': 'Germanium',
        'Eg': 0.660,              # Gián tiếp
        'me_eff': 0.550,
        'mhh_eff': 0.37,
        'eps_r': 16.0,
        'nr': 4.00,
        'varshni_alpha': 4.770e-4,
        'varshni_beta': 235.0
    }
}

def varshni_eg(material, T_K):
    """
    Tính bề rộng vùng cấm Eg(T) theo mô hình thực nghiệm Varshni
    Eg(T) = Eg(0) - alpha * T^2 / (T + beta)
    """
    mat = SEMICONDUCTORS_300K[material]
    alpha = mat['varshni_alpha']
    beta = mat['varshni_beta']
    # Quy đổi ngược Eg(0) từ Eg(300)
    Eg_0 = mat['Eg'] + (alpha * (300.0**2)) / (300.0 + beta)
    return Eg_0 - (alpha * (T_K**2)) / (T_K + beta)
