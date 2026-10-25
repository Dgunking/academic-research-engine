# -*- coding: utf-8 -*-
"""
Common Materials Module (Semiconductor Database & CODATA 2022 Physical Constants)
Cơ sở dữ liệu Vật liệu Bán dẫn 300 K & Hằng số Vật lý Căn bản CODATA 2022.
Đóng gói phi trạng thái (Stateless/Reusable Utility).
Phục vụ: physics-graphic-artist, pedagogical-author, quality-gatekeeper.
"""

import math
from typing import Dict, Any, Optional


# 1. Hằng số Vật lý Căn bản CODATA 2018/2022
CODATA_2022 = {
    "q": 1.602176634e-19,         # Điện tích nguyên tố [C]
    "hbar": 1.054571817e-34,      # Hằng số Planck rút gọn [J·s]
    "h": 6.62607015e-34,          # Hằng số Planck [J·s]
    "m0": 9.1093837e-31,          # Khối lượng nghỉ electron [kg]
    "kB": 1.380649e-23,           # Hằng số Boltzmann [J/K]
    "kB_eV": 8.617333262e-5,      # Hằng số Boltzmann [eV/K]
    "eps0": 8.8541878128e-12,     # Độ điện thẩm chân không [F/m]
    "mu0": 1.25663706212e-6,      # Độ từ thẩm chân không [H/m]
    "c": 299792458.0              # Vận tốc ánh sáng trong chân không [m/s]
}

# 2. Cơ sở dữ liệu Thông số Bán dẫn ở 300 K (SEMICONDUCTORS_300K)
SEMICONDUCTORS_300K = {
    "GaAs": {
        "name": "Gallium Arsenide",
        "chemical_formula": "GaAs",
        "bandgap_type": "direct",
        "Eg": 1.424,               # Vùng cấm ở 300 K [eV]
        "me_eff": 0.067,           # Khối lượng hiệu dụng electron (m*/m0)
        "mhh_eff": 0.45,           # Khối lượng hiệu dụng lỗ trống nặng (m*/m0)
        "mlh_eff": 0.082,          # Khối lượng hiệu dụng lỗ trống nhẹ (m*/m0)
        "eps_r": 12.9,             # Hằng số điện môi tương đối
        "nr": 3.65,                # Chiết suất quang học ở 300 K
        "delta_Ec_ratio": 0.65,    # Tỷ lệ gián đoạn vùng dẫn dE_c / dE_g (GaAs/AlGaAs)
        "auger_coeff_C": 1.0e-30,  # Hệ số tái hợp Auger C ở 300 K [cm^6/s]
        "varshni_alpha": 5.405e-4, # Hệ số Varshni alpha [eV/K]
        "varshni_beta": 204.0,     # Hệ số Varshni beta [K]
        "mobility_e": 8500.0,      # Độ linh động electron [cm^2/(V·s)]
        "mobility_h": 400.0,       # Độ linh động lỗ trống [cm^2/(V·s)]
        "thermal_conductivity": 55.0 # Độ dẫn nhiệt [W/(m·K)]
    },
    "InP": {
        "name": "Indium Phosphide",
        "chemical_formula": "InP",
        "bandgap_type": "direct",
        "Eg": 1.344,
        "me_eff": 0.077,
        "mhh_eff": 0.60,
        "mlh_eff": 0.12,
        "eps_r": 12.5,
        "nr": 3.17,
        "delta_Ec_ratio": 0.40,    # Tỷ lệ gián đoạn vùng dẫn dE_c / dE_g (InGaAsP/InP)
        "auger_coeff_C": 9.0e-30,  # Hệ số tái hợp Auger C ở 300 K [cm^6/s]
        "varshni_alpha": 4.900e-4,
        "varshni_beta": 327.0,
        "mobility_e": 5400.0,
        "mobility_h": 200.0,
        "thermal_conductivity": 68.0
    },
    "AlGaAs": {
        "name": "Aluminium Gallium Arsenide (x=0.3)",
        "chemical_formula": "Al0.3Ga0.7As",
        "bandgap_type": "direct",
        "Eg": 1.798,
        "me_eff": 0.092,
        "mhh_eff": 0.48,
        "mlh_eff": 0.094,
        "eps_r": 12.0,
        "nr": 3.385,
        "delta_Ec_ratio": 0.65,
        "auger_coeff_C": 1.0e-30,
        "varshni_alpha": 5.405e-4,
        "varshni_beta": 204.0,
        "mobility_e": 3000.0,
        "mobility_h": 150.0,
        "thermal_conductivity": 20.0
    },
    "InGaAsP": {
        "name": "Indium Gallium Arsenide Phosphide (1.55 um)",
        "chemical_formula": "In0.53Ga0.47As0.9P0.1",
        "bandgap_type": "direct",
        "Eg": 0.800,
        "me_eff": 0.041,
        "mhh_eff": 0.44,
        "mlh_eff": 0.051,
        "eps_r": 13.9,
        "nr": 3.520,
        "delta_Ec_ratio": 0.40,
        "auger_coeff_C": 3.0e-29,
        "varshni_alpha": 4.500e-4,
        "varshni_beta": 280.0,
        "mobility_e": 6000.0,
        "mobility_h": 120.0,
        "thermal_conductivity": 5.0
    },
    "GaN": {
        "name": "Gallium Nitride",
        "chemical_formula": "GaN",
        "bandgap_type": "direct",
        "Eg": 3.420,
        "me_eff": 0.200,
        "mhh_eff": 0.80,
        "mlh_eff": 0.20,
        "eps_r": 8.9,
        "nr": 2.40,
        "varshni_alpha": 9.090e-4,
        "varshni_beta": 830.0,
        "mobility_e": 1000.0,
        "mobility_h": 30.0,
        "thermal_conductivity": 130.0
    },
    "Si": {
        "name": "Silicon",
        "chemical_formula": "Si",
        "bandgap_type": "indirect",
        "Eg": 1.120,
        "me_eff": 1.080,
        "mhh_eff": 0.56,
        "mlh_eff": 0.16,
        "eps_r": 11.7,
        "nr": 3.42,
        "varshni_alpha": 4.730e-4,
        "varshni_beta": 636.0,
        "mobility_e": 1400.0,
        "mobility_h": 450.0,
        "thermal_conductivity": 149.0
    },
    "Ge": {
        "name": "Germanium",
        "chemical_formula": "Ge",
        "bandgap_type": "indirect",
        "Eg": 0.660,
        "me_eff": 0.550,
        "mhh_eff": 0.37,
        "mlh_eff": 0.044,
        "eps_r": 16.0,
        "nr": 4.00,
        "varshni_alpha": 4.770e-4,
        "varshni_beta": 235.0,
        "mobility_e": 3900.0,
        "mobility_h": 1900.0,
        "thermal_conductivity": 60.0
    }
}


class SemiconductorDatabase:
    """Động cơ Tra cứu & Tính toán Vật liệu Bán dẫn Lab Quang điện tử."""

    @staticmethod
    def get_material(material: str) -> Dict[str, Any]:
        """Lấy thông số chi tiết của vật liệu bán dẫn ở 300 K."""
        mat_key = material.strip()
        if mat_key not in SEMICONDUCTORS_300K:
            raise KeyError(
                f"Vật liệu '{material}' không có trong cơ sở dữ liệu 300 K ({list(SEMICONDUCTORS_300K.keys())})"
            )
        return SEMICONDUCTORS_300K[mat_key]

    @classmethod
    def varshni_eg(cls, material: str, T_K: float) -> float:
        """
        Tính bề rộng vùng cấm Eg(T) theo mô hình thực nghiệm Varshni:
        Eg(T) = Eg(0) - alpha * T^2 / (T + beta)
        """
        mat = cls.get_material(material)
        alpha = mat["varshni_alpha"]
        beta = mat["varshni_beta"]
        # Quy đổi ngược Eg(0) từ Eg(300)
        Eg_0 = mat["Eg"] + (alpha * (300.0 ** 2)) / (300.0 + beta)
        # Tính Eg tại nhiệt độ T_K
        Eg_T = Eg_0 - (alpha * (T_K ** 2)) / (T_K + beta)
        return float(Eg_T)

    @staticmethod
    def thermal_voltage(T_K: float = 300.0) -> float:
        """Tính thế nhiệt V_t = k_B * T / q [V]. (ở 300 K xấp xỉ 25.85 mV)."""
        kB = CODATA_2022["kB"]
        q = CODATA_2022["q"]
        return (kB * T_K) / q

    @classmethod
    def effective_density_of_states(cls, m_eff_ratio: float, T_K: float = 300.0) -> float:
        """
        Tính mật độ trạng thái hiệu dụng (N_c hoặc N_v) [cm^-3]:
        N = 2 * (2 * pi * m* * kB * T / h^2)^(3/2)
        """
        m_eff = m_eff_ratio * CODATA_2022["m0"]
        kB = CODATA_2022["kB"]
        h = CODATA_2022["h"]
        
        factor = (2.0 * math.pi * m_eff * kB * T_K) / (h ** 2)
        density_m3 = 2.0 * (factor ** 1.5)
        # Quy đổi từ m^-3 sang cm^-3 (chia cho 10^6)
        return density_m3 * 1e-6

    @classmethod
    def intrinsic_carrier_concentration(cls, material: str, T_K: float = 300.0) -> float:
        """
        Tính nồng độ hạt tải nội sinh n_i [cm^-3]:
        n_i = sqrt(N_c * N_v) * exp(-Eg / (2 * kB * T))
        """
        mat = cls.get_material(material)
        Eg_eV = cls.varshni_eg(material, T_K)
        Nc = cls.effective_density_of_states(mat["me_eff"], T_K)
        Nv = cls.effective_density_of_states(mat["mhh_eff"], T_K)
        
        kB_eV = CODATA_2022["kB_eV"]
        exponent = -Eg_eV / (2.0 * kB_eV * T_K)
        ni = math.sqrt(Nc * Nv) * math.exp(exponent)
        return ni

    @staticmethod
    def photon_energy_to_wavelength_nm(E_eV: float) -> float:
        """
        Chuyển đổi năng lượng photon (eV) sang bước sóng (nm):
        lambda = h * c / E = 1239.841984 / E
        """
        if E_eV <= 0:
            raise ValueError("Năng lượng photon phải lớn hơn 0")
        h = CODATA_2022["h"]
        c = CODATA_2022["c"]
        q = CODATA_2022["q"]
        lambda_m = (h * c) / (E_eV * q)
        return lambda_m * 1e9
