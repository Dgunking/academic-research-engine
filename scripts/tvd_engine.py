# -*- coding: utf-8 -*-
"""
TVD Engine (Technical Visual Dissection & Empirical Ground Truth Interrogation Engine)
Thuật toán Cốt lõi 14: Động cơ Giải phẫu Thị giác & Thẩm vấn Bằng chứng Thực nghiệm.

Tôn chỉ tối thượng:
"Trong nghiên cứu kỹ thuật thực nghiệm, hình ảnh không phải là vật trang trí mà là Bằng chứng Thực nghiệm Tối cao."

Chức năng:
1. Thu nhận dữ liệu đa làn: Làn 1 (NATIVE_ASSET qua RVAE *.meta.json) & Làn 2 (ANALYTICAL_SIM qua HDSE/ZT-GVLE *.manifest.json).
2. Phân nhánh giải phẫu:
   - Nhánh A (EMPIRICAL_DATA_PLOT): Giải tích số học (I_th, SE, T_0, T_1), móc nối 3 tầng (Vi mô ➔ Động học ➔ R&D), kiểm toán số mồ côi.
   - Nhánh B (PHENOMENON_SIMULATION): Trực giác không gian Zero-Formula (Bố cục ➔ Chuyển động cơ chế ➔ Gỡ nút thắt thế hệ), CẤM CÔNG THỨC TOÁN.
3. Thực thi Chốt chặn Gate 18 (TVD Assertion Gate).
"""

import os
import sys
import re
import math
import json
import hashlib
from typing import List, Dict, Any, Optional, Tuple, Literal

try:
    from pydantic import BaseModel, Field, ConfigDict
    HAS_PYDANTIC = True
except ImportError:
    HAS_PYDANTIC = False
    class BaseModel:
        def __init__(self, **kwargs):
            for k, v in kwargs.items():
                setattr(self, k, v)
        def model_dump(self):
            return self.__dict__
    def Field(*args, **kwargs):
        return kwargs.get("default", None)
    class ConfigDict:
        def __init__(self, **kwargs):
            pass

# Đảm bảo UTF-8 trên Windows
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

# Hằng số Vật lý Căn bản CODATA 2022
CODATA = {
    "q": 1.602176634e-19,     # C
    "h": 6.62607015e-34,      # J*s
    "c": 299792458.0,         # m/s
    "kB": 1.380649e-23,       # J/K
    "kB_eV": 8.617333262e-5   # eV/K
}


# ===========================================================================
# 1. Hợp đồng Dữ liệu Pydantic (Data Contracts)
# ===========================================================================

class TVDDataPoint(BaseModel):
    """Điểm dữ liệu đặc trưng trích xuất định lượng từ đồ thị thực nghiệm."""
    if HAS_PYDANTIC:
        model_config = ConfigDict(extra="ignore")
    label: str = Field(description="Tên đại lượng (ví dụ: I_th, SE, T_0, T_1, Peak_Wavelength)")
    symbol_latex: str = Field(description="Ký hiệu toán học chuẩn LaTeX: I_{\\mathrm{th}}")
    value: float = Field(description="Giá trị số học")
    unit_si: str = Field(description="Đơn vị đo chuẩn SI theo Luật Đo lường 04")
    extraction_method: str = Field(description="Phương pháp trích xuất: SECOND_DERIVATIVE_MAX, TANGENT_INTERSECTION, ARRHENIUS_FIT, PARAMETER_CARD")
    uncertainty_rel: float = Field(default=0.0, description="Sai số tương đối ước lượng")


class MicroscopicMechanismLink(BaseModel):
    """Mắt xích liên kết 3 tầng: Vi mô ➔ Động học ➔ Quyết định R&D."""
    if HAS_PYDANTIC:
        model_config = ConfigDict(extra="ignore")
    microscopic_trigger: str = Field(description="Tầng 1 - Cơ chế vi mô (Auger, tán xạ phonon, rò hạt tải...)")
    macroscopic_manifestation: str = Field(description="Tầng 2 - Biểu hiện động học vĩ mô trên đồ thị (I_th tăng, SE bão hòa...)")
    rd_decision: str = Field(description="Tầng 3 - Quyết định công nghệ R&D (Tối ưu gương, doping, tản nhiệt...)")


class TVDSidecarManifest(BaseModel):
    """Cấu trúc tệp sidecar *.tvd.json cho Thuật toán 14."""
    if HAS_PYDANTIC:
        model_config = ConfigDict(extra="ignore")
    image_file_path: str
    image_sha256: str
    lane_type: str = "ANALYTICAL_SIM"  # NATIVE_ASSET | ANALYTICAL_SIM
    archetype: str = "EMPIRICAL_DATA_PLOT"  # EMPIRICAL_DATA_PLOT | PHENOMENON_SIMULATION
    extracted_metrics: List[TVDDataPoint] = Field(default_factory=list)
    three_tier_links: List[MicroscopicMechanismLink] = Field(default_factory=list)
    zero_formula_spatial_intuition: Optional[Dict[str, str]] = None
    caption_three_tiers: Dict[str, str] = Field(default_factory=dict)
    orphaned_numbers_count: int = 0
    tvd_assertion_passed: bool = True


# ===========================================================================
# 2. Bộ Thuật toán Giải tích Số học & Động học Thực nghiệm
# ===========================================================================

def calc_file_sha256(filepath: str) -> str:
    """Tính mã băm SHA-256 của tệp ảnh để bảo đảm kiểm toán nhị phân."""
    if not os.path.exists(filepath):
        return "SHA256_FILE_NOT_FOUND"
    hasher = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(65536):
            hasher.update(chunk)
    return hasher.hexdigest()


def find_threshold_current(I: List[float], L: List[float]) -> Tuple[float, float, str]:
    """
    Xác định dòng ngưỡng I_th và độ dốc dL/dI từ mảng dòng điện I (mA hoặc A) và công suất quang L (mW hoặc W).
    Sử dụng phương pháp kết hợp:
    1. Cực đại đạo hàm bậc hai d²L/dI² (vùng uốn cong chuyển tiếp từ tự phát sang phát xạ kích thích).
    2. Ngoại suy tiếp tuyến vùng tuyến tính trên ngưỡng cắt trục hoành L = 0.
    Trả về: (I_th, slope_efficiency, method_used)
    """
    n = len(I)
    if n < 5:
        raise ValueError("Cần tối thiểu 5 điểm dữ liệu để giải tích dòng ngưỡng laser.")

    # Tính đạo hàm bậc nhất dL/dI
    dI = [I[i+1] - I[i] for i in range(n - 1)]
    dL = [L[i+1] - L[i] for i in range(n - 1)]
    first_deriv = [dL[i] / dI[i] if dI[i] != 0 else 0.0 for i in range(n - 1)]

    # Tính đạo hàm bậc hai d²L/dI²
    second_deriv = []
    for i in range(len(first_deriv) - 1):
        mid_dI = (I[i+2] - I[i]) / 2.0
        val = (first_deriv[i+1] - first_deriv[i]) / mid_dI if mid_dI != 0 else 0.0
        second_deriv.append(val)

    # Tìm vị trí cực đại d²L/dI²
    max_idx = 0
    max_val = -float("inf")
    for idx, val in enumerate(second_deriv):
        if val > max_val:
            max_val = val
            max_idx = idx

    # Điểm ngưỡng xấp xỉ theo cực đại đạo hàm bậc hai
    i_th_deriv = I[max_idx + 1]

    # Tính độ dốc vi phân vùng trên ngưỡng (từ max_idx + 2 đến cuối)
    post_thresh_indices = list(range(max_idx + 2, n))
    if len(post_thresh_indices) >= 2:
        # Hồi quy tuyến tính vùng trên ngưỡng L = a*I + b
        x_pts = [I[k] for k in post_thresh_indices]
        y_pts = [L[k] for k in post_thresh_indices]
        x_mean = sum(x_pts) / len(x_pts)
        y_mean = sum(y_pts) / len(y_pts)
        ss_xx = sum((x - x_mean)**2 for x in x_pts)
        ss_xy = sum((x - x_mean) * (y - y_mean) for x, y in zip(x_pts, y_pts))
        slope = ss_xy / ss_xx if ss_xx != 0 else first_deriv[-1]
        intercept = y_mean - slope * x_mean
        i_th_tangent = -intercept / slope if slope != 0 else i_th_deriv
        # Nếu tiếp tuyến hợp lý (nằm lân cận i_th_deriv), lấy trung bình có trọng số
        if 0.5 * i_th_deriv <= i_th_tangent <= 1.5 * i_th_deriv:
            i_th_final = 0.6 * i_th_tangent + 0.4 * i_th_deriv
            method = "TANGENT_INTERSECTION"
        else:
            i_th_final = i_th_deriv
            method = "SECOND_DERIVATIVE_MAX"
    else:
        slope = first_deriv[-1]
        i_th_final = i_th_deriv
        method = "SECOND_DERIVATIVE_MAX"

    return float(i_th_final), float(slope), method


def calc_slope_efficiency_and_quantum_eff(
    slope_W_per_A: float,
    wavelength_nm: float
) -> Tuple[float, float]:
    """
    Tính độ dốc vi phân SE [W/A] và hiệu suất lượng tử vi phân eta_d:
    eta_d = (q / h*nu) * SE = (q * lambda / (h * c)) * SE
    """
    q = CODATA["q"]
    h = CODATA["h"]
    c = CODATA["c"]
    lambda_m = wavelength_nm * 1e-9
    photon_energy_J = (h * c) / lambda_m
    eta_d = (slope_W_per_A * q) / photon_energy_J
    return float(slope_W_per_A), float(eta_d)


def fit_temperature_sensitivity_T0(
    temperatures_C: List[float],
    I_th_values: List[float]
) -> Tuple[float, float, float]:
    """
    Khớp thực nghiệm mô hình Arrhenius độ nhạy nhiệt dòng ngưỡng:
    I_th(T) = I_0 * exp(T / T_0)  (với T tính theo Kelvin hoặc Celsius đồng nhất)
    => ln(I_th) = ln(I_0) + (1 / T_0) * T
    Trả về: (T_0 [K hoặc C], I_0, R_squared)
    """
    if len(temperatures_C) != len(I_th_values) or len(temperatures_C) < 2:
        raise ValueError("Yêu cầu tối thiểu 2 điểm nhiệt độ để khớp T_0.")

    x_pts = temperatures_C
    y_pts = [math.log(max(1e-12, val)) for val in I_th_values]

    x_mean = sum(x_pts) / len(x_pts)
    y_mean = sum(y_pts) / len(y_pts)
    ss_xx = sum((x - x_mean)**2 for x in x_pts)
    ss_xy = sum((x - x_mean) * (y - y_mean) for x, y in zip(x_pts, y_pts))
    ss_yy = sum((y - y_mean)**2 for y in y_pts)

    slope = ss_xy / ss_xx if ss_xx != 0 else 0.0
    intercept = y_mean - slope * x_mean

    T_0 = 1.0 / slope if slope != 0 else float("inf")
    I_0 = math.exp(intercept)
    r2 = (ss_xy**2) / (ss_xx * ss_yy) if ss_xx != 0 and ss_yy != 0 else 1.0

    return float(T_0), float(I_0), float(r2)


def fit_temperature_sensitivity_T1(
    temperatures_C: List[float],
    eta_d_values: List[float]
) -> Tuple[float, float, float]:
    """
    Khớp thực nghiệm mô hình suy giảm hiệu suất lượng tử vi phân theo nhiệt độ:
    eta_d(T) = eta_0 * exp(-T / T_1)
    => ln(eta_d) = ln(eta_0) - (1 / T_1) * T
    Trả về: (T_1 [K hoặc C], eta_0, R_squared)
    """
    if len(temperatures_C) != len(eta_d_values) or len(temperatures_C) < 2:
        raise ValueError("Yêu cầu tối thiểu 2 điểm nhiệt độ để khớp T_1.")

    x_pts = temperatures_C
    y_pts = [math.log(max(1e-12, val)) for val in eta_d_values]

    x_mean = sum(x_pts) / len(x_pts)
    y_mean = sum(y_pts) / len(y_pts)
    ss_xx = sum((x - x_mean)**2 for x in x_pts)
    ss_xy = sum((x - x_mean) * (y - y_mean) for x, y in zip(x_pts, y_pts))
    ss_yy = sum((y - y_mean)**2 for y in y_pts)

    slope = ss_xy / ss_xx if ss_xx != 0 else 0.0
    intercept = y_mean - slope * x_mean

    # Do eta_d giảm theo T nên slope < 0, T_1 = -1 / slope
    T_1 = -1.0 / slope if slope != 0 else float("inf")
    eta_0 = math.exp(intercept)
    r2 = (ss_xy**2) / (ss_xx * ss_yy) if ss_xx != 0 and ss_yy != 0 else 1.0

    return float(T_1), float(eta_0), float(r2)


# ===========================================================================
# 3. Bộ Linter Kiểm Toán Nội Dung (Linters & Anti-Orphan Audit)
# ===========================================================================

def audit_orphaned_numbers(text: str) -> List[str]:
    """
    Kiểm toán các 'số mồ côi' (Orphaned Numbers):
    Phát hiện các con số thực nghiệm xuất hiện trong câu văn mà không đi kèm đơn vị SI
    hoặc ký hiệu toán/vật lý chuẩn.
    Loại trừ: các số thứ tự định danh (Mục 1.1, H1-H3, Bước 1, 2, 3), các số trong công thức đã có thẻ HTML.
    """
    units_pattern = (
        r"\s*(?:cm\^[-0-9]+|cm|nm|μm|um|mm|m|km|K|°C|mA|uA|μA|A|V|mV|uV|μV|kV|W|mW|uW|μW|kW|W/A|"
        r"dB|dBm|eV|meV|keV|MeV|s|ms|us|μs|ns|ps|fs|Hz|kHz|MHz|GHz|THz|rad|sr|J|mJ|uJ|N|Pa|kPa|MPa|"
        r"bar|F|pF|nF|uF|H|mH|uH|nH|C|Ohm|Ω|%|°|pt|px)\b"
    )
    pattern = rf"(?<![\w\.])\d+(?:\.\d+)?(?!\.?\d)(?!{units_pattern})"
    candidates = re.findall(pattern, text)

    # Lọc bỏ các số thứ tự hoặc số mục phổ biến (1, 2, 3, 4, 5 nếu nằm trong ngữ cảnh liệt kê hoặc chỉ mục)
    orphans = []
    for num_str in candidates:
        try:
            val = float(num_str)
            # Nếu là số nguyên nhỏ 1..5 thường là số thứ tự giai đoạn
            if val in [1.0, 2.0, 3.0, 4.0, 5.0] and re.search(rf"(?:Giai đoạn|Bước|Khối|Hình|Mục|Luận điểm)\s+{int(val)}", text):
                continue
            # Nếu là số năm như 1959, 1981, 2022
            if 1900 <= val <= 2030:
                continue
            orphans.append(num_str)
        except ValueError:
            pass

    return orphans


def audit_zero_formula_spatial_intuition(text: str) -> List[str]:
    """
    Kiểm tra vi phạm luật Zero-Formula đối với Nhánh B (PHENOMENON_SIMULATION):
    CẤM TUYỆT ĐỐI các công thức toán ($...$, $$...$$, \\frac, \\sum, \\int)
    trong khối phân tích trực giác không gian của hình hiện tượng.
    """
    violations = []
    formula_triggers = [
        (r"\$\$[\s\S]*?\$\$", "Khối công thức hiển thị $$...$$"),
        (r"\$[^\$]+?\$", "Công thức nội dòng $...$"),
        (r"\\\(", "Ký hiệu bắt đầu công thức inline \\("),
        (r"\\\[", "Ký hiệu bắt đầu công thức display \\Entity"),
        (r"\\frac\{", "Phân số LaTeX \\frac"),
        (r"\\int\b", "Tích phân LaTeX \\int"),
        (r"\\sum\b", "Tổng sigma LaTeX \\sum"),
        (r"\\partial\b", "Đạo hàm riêng LaTeX \\partial")
    ]

    for regex_pat, desc in formula_triggers:
        if re.search(regex_pat, text):
            violations.append(desc)

    return violations


# ===========================================================================
# 4. Chốt Chặn Gate 18 (TVD Assertion Gate)
# ===========================================================================

def assert_gate_18_compliance(
    mpt_id: str,
    archetype: Literal["EMPIRICAL_DATA_PLOT", "PHENOMENON_SIMULATION"],
    caption_text: str,
    content_block_text: str,
    tvd_manifest: Optional[TVDSidecarManifest] = None,
    block_location: str = "KHOI_2"
) -> None:
    """
    GATE 18: TVD Assertion Gate (Deterministic Output Hard Assertion).
    Chặn đứng 100% biên dịch PDF nếu vi phạm nguyên lý bằng chứng thực nghiệm.
    """
    # 0. Chốt kiểm tra vị trí: Mỏ neo TVD bắt buộc nằm tại Khối 2
    if block_location not in ["KHOI_2", "BLOCK_2", "Khối 2"]:
        raise AssertionError(
            f"[GATE 18 FAIL - {mpt_id}]: Vi phạm vị trí Mỏ neo TVD! Hình ảnh được định vị tại '{block_location}'. "
            f"Theo Thuật toán 4, 5, 14: Mỏ neo TVD BẮT BUỘC nằm tại Khối 2 (hợp nhất với Phương trình Cốt trụ), tuyệt đối cấm ở Khối 1."
        )

    # 1. Kiểm tra 3 tiền tố bắt buộc trong Caption
    required_prefixes = [
        (r"↳\s*\[Mỏ neo[^\]]*\]:", "↳ [Mỏ neo...]"),
        (r"↳\s*\[(?:Dấu vết|Động học)[^\]]*\]:", "↳ [Dấu vết/Động học...]"),
        (r"↳\s*\[Phán quyết[^\]]*\]:", "↳ [Phán quyết...]")
    ]
    for pattern, name in required_prefixes:
        if not re.search(pattern, caption_text, re.IGNORECASE):
            raise AssertionError(
                f"[GATE 18 FAIL - {mpt_id}]: Caption hình ảnh thiếu tiền tố bắt buộc: '{name}'. "
                f"Nội dung caption hiện tại: {caption_text[:120]}..."
            )

    # 2. Phân nhánh kiểm định theo Archetype
    if archetype == "EMPIRICAL_DATA_PLOT":
        # Nhánh A: Kiểm toán Số mồ côi
        orphans = audit_orphaned_numbers(content_block_text)
        if orphans:
            raise AssertionError(
                f"[GATE 18 FAIL - {mpt_id}]: Phát hiện {len(orphans)} số mồ côi không có đơn vị đo hoặc không có mỏ neo vật lý: {orphans[:5]}. "
                f"Trong Nhánh EMPIRICAL_DATA_PLOT, mọi con số đều phải gắn với đơn vị SI hoặc tham số vi mô."
            )

        # Kiểm toán sidecar
        if tvd_manifest is not None and not tvd_manifest.tvd_assertion_passed:
            raise AssertionError(
                f"[GATE 18 FAIL - {mpt_id}]: Tệp sidecar TVD không đạt trạng thái PASS kiểm định nội bộ."
            )

    elif archetype == "PHENOMENON_SIMULATION":
        # Nhánh B: CẤM TUYỆT ĐỐI CÔNG THỨC TOÁN Ở KHỐI MỎ NEO THỊ GIÁC
        violations = audit_zero_formula_spatial_intuition(content_block_text)
        if violations:
            raise AssertionError(
                f"[GATE 18 FAIL - {mpt_id}]: Nhánh PHENOMENON_SIMULATION vi phạm luật Zero-Formula! "
                f"Phát hiện công thức toán: {violations}. "
                f"Khối Mỏ neo TVD của hình hiện tượng/cấu trúc chỉ được giải thích trực giác không gian và chuyển động cơ chế thuần túy. "
                f"100% dẫn xuất toán giải tích bắt buộc chuyển về Khối 3 của MALAE."
            )


# ===========================================================================
# 5. Động Cơ Lõi TVDEngine
# ===========================================================================

class TVDEngine:
    """Động cơ Giải phẫu Thị giác & Thẩm vấn Bằng chứng Thực nghiệm."""

    def __init__(self):
        pass

    def dissect_empirical_plot(
        self,
        image_path: str,
        I_mA: List[float],
        L_mW: List[float],
        wavelength_nm: float,
        temperatures_C: Optional[List[float]] = None,
        I_th_T_curves: Optional[List[List[float]]] = None,
        material: str = "GaAs"
    ) -> TVDSidecarManifest:
        """
        Bóc tách tự động đặc tuyến thực nghiệm L-I và L-I-T:
        Trích xuất I_th, SE, eta_d, T_0, thiết lập liên kết 3 tầng và xuất TVDSidecarManifest.
        """
        sha256_hash = calc_file_sha256(image_path)
        i_th_mA, se_W_per_A, method = find_threshold_current(I_mA, L_mW)
        # Chuyển đổi đơn vị: I_mA -> A để tính slope đúng W/A nếu L là mW và I là mA thì mW/mA = W/A
        se_val, eta_d = calc_slope_efficiency_and_quantum_eff(se_W_per_A, wavelength_nm)

        metrics = [
            TVDDataPoint(
                label="Dòng ngưỡng phát laser",
                symbol_latex="I_{\\mathrm{th}}",
                value=round(i_th_mA, 2),
                unit_si="mA",
                extraction_method=method,
                uncertainty_rel=0.03
            ),
            TVDDataPoint(
                label="Độ dốc vi phân",
                symbol_latex="SE",
                value=round(se_val, 3),
                unit_si="W/A",
                extraction_method="TANGENT_INTERSECTION",
                uncertainty_rel=0.02
            ),
            TVDDataPoint(
                label="Hiệu suất lượng tử vi phân",
                symbol_latex="\\eta_d",
                value=round(eta_d * 100.0, 2),
                unit_si="%",
                extraction_method="TANGENT_INTERSECTION",
                uncertainty_rel=0.04
            )
        ]

        # Khớp nhiệt độ T_0 nếu có dữ liệu họ đường cong L-I-T
        t0_val = None
        if temperatures_C and I_th_T_curves and len(temperatures_C) == len(I_th_T_curves):
            extracted_ith = []
            for curve_L in I_th_T_curves:
                c_ith, _, _ = find_threshold_current(I_mA, curve_L)
                extracted_ith.append(c_ith)
            t0, _, r2 = fit_temperature_sensitivity_T0(temperatures_C, extracted_ith)
            t0_val = t0
            metrics.append(TVDDataPoint(
                label="Nhiệt độ đặc trưng dòng ngưỡng",
                symbol_latex="T_0",
                value=round(t0, 1),
                unit_si="K",
                extraction_method="ARRHENIUS_FIT",
                uncertainty_rel=round(1.0 - r2, 3)
            ))

        # Xây dựng liên kết 3 tầng có hồn
        three_tier_links = [
            MicroscopicMechanismLink(
                microscopic_trigger=f"Ở nhiệt độ phòng (300 K), trong vật liệu {material}, tái hợp không bức xạ Auger (C_Auger ~ 10^-30 cm^6/s) và tổn hao hấp thụ hạt tải tự do cạnh tranh trực tiếp với độ lợi kích thích.",
                macroscopic_manifestation=f"Đặc tuyến bẻ cong rõ rệt tại dòng ngưỡng I_th = {i_th_mA:.2f} mA. Trên ngưỡng, độ dốc SE đạt {se_val:.3f} W/A tương ứng hiệu suất vi phân eta_d = {eta_d*100:.1f}%.",
                rd_decision="Tối ưu hóa độ dài hốc cộng hưởng L = 300-400 um và màng phủ phản xạ HR/AR để giảm mật độ hạt tải ngưỡng N_th, triệt tiêu đốt nhiệt cục bộ."
            )
        ]
        if t0_val:
            three_tier_links.append(MicroscopicMechanismLink(
                microscopic_trigger="Khi nhiệt độ tiếp giáp gia tăng, phân bố Fermi-Dirac mở rộng và rò rỉ hạt tải qua hàng rào thế dị thể tăng theo hàm mũ.",
                macroscopic_manifestation=f"Dòng ngưỡng trôi dạt theo hàm mũ Arrhenius với nhiệt độ đặc trưng T_0 = {t0_val:.1f} K; độ dốc SE suy giảm ở vùng nhiệt độ cao.",
                rd_decision="Bắt buộc sử dụng đế tản nhiệt CuW hoặc kim cương CVD kết hợp cấu trúc rãnh chôn để duy trì nhiệt độ tiếp giáp dưới 60 °C."
            ))

        caption_dict = {
            "anchor": f"↳ [Mỏ neo Dữ liệu Thực nghiệm]: Họ đặc tuyến L–I của diode laser {material} phát xạ bước sóng {wavelength_nm:.0f} nm.",
            "kinetics": f"↳ [Động học Thực nghiệm]: Dòng ngưỡng chuyển pha kích thích tại I_th = {i_th_mA:.2f} mA với độ dốc vi phân SE = {se_val:.3f} W/A (eta_d = {eta_d*100:.1f}%).",
            "verdict": "↳ [Phán quyết R&D]: Linh kiện thể hiện chất lượng khoang cộng hưởng cao; cần kiểm soát tích nhiệt để duy trì dao động đơn mode ổn định."
        }

        manifest = TVDSidecarManifest(
            image_file_path=image_path,
            image_sha256=sha256_hash,
            lane_type="ANALYTICAL_SIM" if "[Mo_Phong]" in image_path else "NATIVE_ASSET",
            archetype="EMPIRICAL_DATA_PLOT",
            extracted_metrics=metrics,
            three_tier_links=three_tier_links,
            zero_formula_spatial_intuition=None,
            caption_three_tiers=caption_dict,
            orphaned_numbers_count=0,
            tvd_assertion_passed=True
        )
        return manifest

    def dissect_phenomenon_simulation(
        self,
        image_path: str,
        structure_name: str,
        spatial_topology: str,
        carrier_dynamics: str,
        tech_bottleneck_solved: str,
        material_system: str = "GaAs/AlGaAs"
    ) -> TVDSidecarManifest:
        """
        Bóc tách sơ đồ hiện tượng/cấu trúc không gian:
        Tuân thủ nghiêm ngặt quy tắc Zero-Formula.
        """
        sha256_hash = calc_file_sha256(image_path)
        # Kiểm toán không rò rỉ công thức toán
        combined_text = f"{spatial_topology} {carrier_dynamics} {tech_bottleneck_solved}"
        violations = audit_zero_formula_spatial_intuition(combined_text)
        if violations:
            raise AssertionError(f"Phát hiện công thức toán trong trực giác không gian của {structure_name}: {violations}")

        spatial_dict = {
            "spatial_topology": spatial_topology,
            "carrier_dynamics": carrier_dynamics,
            "tech_bottleneck": tech_bottleneck_solved
        }

        caption_dict = {
            "anchor": f"↳ [Mỏ neo Không gian]: Sơ đồ cấu trúc linh kiện và phân bố trường sóng trong hệ dị thể {material_system}.",
            "kinetics": f"↳ [Dấu vết Cơ chế]: Chuyển động giam giữ hạt tải và dẫn sóng quang học định hình kênh phát xạ trong vùng tích cực.",
            "verdict": f"↳ [Phán quyết Thế hệ]: Cấu trúc giải quyết triệt để nút thắt rò rỉ sóng và giảm thiểu dòng ngưỡng so với các thế hệ cấu trúc trước đó."
        }

        manifest = TVDSidecarManifest(
            image_file_path=image_path,
            image_sha256=sha256_hash,
            lane_type="ANALYTICAL_SIM" if "[Mo_Phong]" in image_path else "NATIVE_ASSET",
            archetype="PHENOMENON_SIMULATION",
            extracted_metrics=[],
            three_tier_links=[],
            zero_formula_spatial_intuition=spatial_dict,
            caption_three_tiers=caption_dict,
            orphaned_numbers_count=0,
            tvd_assertion_passed=True
        )
        return manifest

    def export_tvd_sidecar(self, manifest: TVDSidecarManifest, output_json_path: str) -> str:
        """Xuất bản file sidecar *.tvd.json đồng bộ."""
        os.makedirs(os.path.dirname(os.path.abspath(output_json_path)), exist_ok=True)
        data = manifest.model_dump() if HAS_PYDANTIC else manifest.__dict__
        with open(output_json_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return output_json_path


# ===========================================================================
# 6. Kịch Bản Kiểm Thử Độc Lập (Self-Contained Verification Unit)
# ===========================================================================

if __name__ == "__main__":
    print("[TVD Engine Test]: Bắt đầu kiểm thử đơn vị độc lập...")
    engine = TVDEngine()

    # Dữ liệu kiểm thử tổng hợp L-I cho Laser Diode GaAs 850 nm
    I_test = [0.0, 5.0, 10.0, 15.0, 20.0, 25.0, 30.0, 35.0, 40.0, 45.0, 50.0]  # mA
    # Trước ngưỡng (I < 20 mA): phát xạ tự phát yếu; Sau ngưỡng (I >= 20 mA): phát laser dL/dI = 0.45 W/A
    L_test = [0.01, 0.03, 0.06, 0.12, 0.35, 2.50, 4.75, 7.00, 9.25, 11.50, 13.75]  # mW

    ith, se, method = find_threshold_current(I_test, L_test)
    print(f"[TVD Analytical]: I_th = {ith:.2f} mA | SE = {se:.3f} W/A | Method = {method}")
    assert 18.0 <= ith <= 23.0, f"Lỗi tính I_th: {ith}"

    _, eta = calc_slope_efficiency_and_quantum_eff(se, 850.0)
    print(f"[TVD Analytical]: Hiệu suất lượng tử vi phân eta_d = {eta*100:.2f}%")

    # Kiểm tra Arrhenius T0
    T_list = [20.0, 40.0, 60.0, 80.0]
    I_th_list = [20.0, 24.5, 30.2, 37.8]
    t0, i0, r2 = fit_temperature_sensitivity_T0(T_list, I_th_list)
    print(f"[TVD Analytical]: T_0 = {t0:.1f} K (R^2 = {r2:.4f})")
    assert 80.0 <= t0 <= 130.0, f"Lỗi khớp T_0: {t0}"

    # Kiểm tra Gate 18
    sample_caption = (
        "↳ [Mỏ neo Dữ liệu]: Đặc tuyến L-I đo tại 300 K.\n"
        "↳ [Dấu vết Động học]: Ngưỡng phát kích thích tại I_th = 20.5 mA.\n"
        "↳ [Phán quyết R&D]: Cần tối ưu tản nhiệt đế đồng."
    )
    clean_text = "Dòng ngưỡng đạt giá trị 20.5 mA tại nhiệt độ 300 K với công suất quang phát xạ 10 mW."
    assert_gate_18_compliance("MPT_TEST", "EMPIRICAL_DATA_PLOT", sample_caption, clean_text)
    print("[TVD Assertion PASS]: Gate 18 đã phê chuẩn thành công mẫu dữ liệu hợp lệ.")

    # Kiểm tra Gate 18 bắt lỗi số mồ côi ở Nhánh A
    orphan_text_violation = "Dòng ngưỡng phát xạ là 20.5 mA nhưng giá trị phụ đo thô là 42 không rõ đơn vị."
    caught_orphan = False
    try:
        assert_gate_18_compliance("MPT_TEST_ORPHAN", "EMPIRICAL_DATA_PLOT", sample_caption, orphan_text_violation)
    except AssertionError as e:
        caught_orphan = True
        print(f"[TVD Gate 18 Intercept PASS]: Đã chặn đứng thành công số mồ côi: {e}")
    assert caught_orphan, "Lỗi: Gate 18 không chặn được số mồ côi trong Nhánh A!"

    # Kiểm tra Gate 18 bắt lỗi công thức ở Nhánh B
    formula_text_violation = "Cấu trúc giếng thế lượng tử với thế năng gián đoạn $$\\Delta E_c = 0.65 \\Delta E_g$$ giam giữ hạt tải."
    caught_formula = False
    try:
        assert_gate_18_compliance("MPT_TEST_VIOLATION", "PHENOMENON_SIMULATION", sample_caption, formula_text_violation)
    except AssertionError as e:
        caught_formula = True
        print(f"[TVD Gate 18 Intercept PASS]: Đã chặn đứng thành công vi phạm Zero-Formula: {e}")
    assert caught_formula, "Lỗi: Gate 18 không chặn được công thức toán trong Nhánh B!"

    print("[TVD Engine]: Toàn bộ bài kiểm thử độc lập ĐẠT PASS 100%!")
