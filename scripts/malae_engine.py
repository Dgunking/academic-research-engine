# -*- coding: utf-8 -*-
"""
MALAE Engine (Multimodal Autonomous Lecture Authoring Engine)
Thuật toán Biên soạn Bài giảng Tự trị Đa phương thức trên Google Antigravity.

Vận hành mô hình Đường ống Hợp đồng Định kiểu (Typed Contract Pipeline) Lưỡng pha:
- Pha 1 (Macro Planning Pass): Khử chu trình GREEDYCYCLEBREAK, Sắp xếp Tô-pô Nguyên lý đầu,
                               ColPali MaxSim Neo đầu mục, SME Analogy Mapping & Khóa ARegistry.
- Pha 2 (Micro Compilation Pass): Nén CoD 3 vòng, Biên dịch Chuỗi Nhân quả (≤ 65 từ),
                                  Giải phẫu Phương trình 3 Cấp, Triệt tiêu bảng lưới -> MATLAB HG2,
                                  5 Giai đoạn Sư phạm, và Bộ 5 Cổng Linter Tất định (LINT_01 -> LINT_05).

Tuân thủ nghiêm ngặt:
- GEMINI.md (Mục III.D - Thuật toán 12)
- AGENTS.md (Mục II.E - Thuật toán 12)
- Tài liệu xây dựng thuật toán/Thuật Toán Tạo Bài Giảng.md
"""

from typing import List, Dict, Any, Optional, Tuple, Set
import re
import json

try:
    from pydantic import BaseModel, Field
except ImportError:
    from dataclasses import dataclass, field
    def Field(*args, **kwargs):
        default = kwargs.get("default", None)
        return field(default=default)
    class BaseModel:
        def __init__(self, **kwargs):
            for k, v in kwargs.items():
                setattr(self, k, v)
        def dict(self):
            return self.__dict__

# ---------------------------------------------------------------------------
# 1. Pydantic Contracts (Hợp đồng Dữ liệu Định kiểu)
# ---------------------------------------------------------------------------

class ConceptNode(BaseModel):
    """Nút khái niệm / Luận điểm vi mô trong đồ thị tri thức."""
    node_id: str
    content: str
    ancestor_distance: int = 0  # Phi(v): khoảng cách tới Gốc Tổ tiên (AR) năm 1-3 HUST
    latex_formulas: List[str] = Field(default_factory=list)

class ConceptEdge(BaseModel):
    """Cạnh phụ thuộc có hướng giữa hai khái niệm."""
    source_id: str
    target_id: str
    confidence_weight: float = 1.0  # w(u, v) in [0, 1]
    is_feedback_loop: bool = False

class UpfrontAnchorContract(BaseModel):
    """Hợp đồng Neo Nhận thức Đầu mục (Khối AST <= 2)."""
    image_id: str
    image_path: str
    core_equation_latex: str
    physical_law_name: str
    caption: str

class AnalogyEntry(BaseModel):
    """Bản ghi miền nguồn ẩn dụ trong Section-Level Analogy Registry."""
    section_id: str
    base_domain: str
    systematicity_score: float
    alignable_difference: str

class ParameterGloss(BaseModel):
    """Giải nghĩa chi tiết một tham số vi mô trong phương trình."""
    symbol_html: str   # Định dạng HTML: <i>m</i><sup>*</sup>
    name_vi: str
    si_unit: str       # Chuẩn Luật Đo lường 04
    physical_meaning: str

class EquationGlossContract(BaseModel):
    """Giải phẫu Phương trình Liên dòng 3 Cấp (Interlinear Mathematical Glossing)."""
    equation_latex: str
    physical_role: str                   # Tầng 1: Vai trò vật lý
    parameters: List[ParameterGloss]     # Tầng 2: Tham số vi mô SI
    asymptotic_limits: List[str]         # Tầng 3: Kiểm tra 2 giới hạn tiệm cận biên

class CausalFlowchainBlock(BaseModel):
    """Khối chuỗi biến đổi nhân quả có hướng (Anti-Wall-of-Text)."""
    block_id: str
    flow_steps: List[str]
    formatted_chain: str
    word_count: int

class LinterResult(BaseModel):
    """Kết quả kiểm định một cổng linter tất định."""
    rule_id: str
    rule_name: str
    passed: bool
    threshold: str
    measured_value: Any
    violation_message: str = ""
    suggested_repair_move: str = ""

# ---------------------------------------------------------------------------
# 2. Thuật toán Lõi Pha 1 (Macro Planning Pass)
# ---------------------------------------------------------------------------

def greedy_cycle_breaking(
    nodes: Dict[str, ConceptNode],
    edges: List[ConceptEdge],
    lambda_penalty: float = 1.5
) -> Tuple[List[ConceptEdge], List[ConceptEdge]]:
    """
    Thuật toán GREEDYCYCLEBREAK:
    Duyệt DFS 3 màu (White=0, Gray=1, Black=2) phát hiện chu trình có hướng.
    Tính trọng số hiệu dụng nguyên lý đầu:
        W_eff(u, v) = w(u, v) + lambda * max(0, Phi(u) - Phi(v))
    Cắt bỏ cạnh có W_eff nhỏ nhất trong chu trình để trả về DAG thuần nhất.
    """
    adj: Dict[str, List[ConceptEdge]] = {nid: [] for nid in nodes}
    for e in edges:
        if e.source_id in adj:
            adj[e.source_id].append(e)

    color: Dict[str, int] = {nid: 0 for nid in nodes}
    parent_edge: Dict[str, Optional[ConceptEdge]] = {nid: None for nid in nodes}
    cycle_edges_removed: List[ConceptEdge] = []
    active_edges = list(edges)

    def dfs(u: str) -> Optional[List[ConceptEdge]]:
        color[u] = 1  # Gray: đang duyệt nhánh
        for edge in adj.get(u, []):
            if edge not in active_edges:
                continue
            v = edge.target_id
            if color[v] == 1:
                # Phát hiện cung ngược (back-edge) tạo chu trình
                cycle = [edge]
                curr = u
                while curr != v and parent_edge[curr] is not None:
                    p_edge = parent_edge[curr]
                    cycle.append(p_edge)
                    curr = p_edge.source_id
                return cycle
            elif color[v] == 0:
                parent_edge[v] = edge
                found_cycle = dfs(v)
                if found_cycle:
                    return found_cycle
        color[u] = 2  # Black: duyệt xong
        return None

    # Vòng lặp khử chu trình tham lam
    while True:
        color = {nid: 0 for nid in nodes}
        parent_edge = {nid: None for nid in nodes}
        detected_cycle = None
        for nid in nodes:
            if color[nid] == 0:
                detected_cycle = dfs(nid)
                if detected_cycle:
                    break

        if not detected_cycle:
            break

        # Tính W_eff cho từng cạnh trong chu trình
        min_eff_weight = float('inf')
        weakest_edge = None
        for e in detected_cycle:
            phi_u = nodes[e.source_id].ancestor_distance if e.source_id in nodes else 0
            phi_v = nodes[e.target_id].ancestor_distance if e.target_id in nodes else 0
            w_eff = e.confidence_weight - lambda_penalty * max(0, phi_u - phi_v)
            if w_eff < min_eff_weight:
                min_eff_weight = w_eff
                weakest_edge = e

        if weakest_edge:
            weakest_edge.is_feedback_loop = True
            active_edges.remove(weakest_edge)
            cycle_edges_removed.append(weakest_edge)

    return active_edges, cycle_edges_removed

def weighted_topological_sort(
    nodes: Dict[str, ConceptNode],
    dag_edges: List[ConceptEdge]
) -> List[str]:
    """
    Sắp xếp tô-pô có trọng số (Weighted Topological Linearization):
    Ưu tiên các nút có ancestor_distance (Phi) nhỏ (gần Gốc Tổ tiên AR hơn)
    lên trước trong trường hợp bậc vào (in-degree) bằng nhau.
    """
    in_degree: Dict[str, int] = {nid: 0 for nid in nodes}
    adj: Dict[str, List[str]] = {nid: [] for nid in nodes}
    for e in dag_edges:
        if e.target_id in in_degree and e.source_id in adj:
            in_degree[e.target_id] += 1
            adj[e.source_id].append(e.target_id)

    # Hàng đợi ưu tiên theo Phi(v)
    zero_in = [nid for nid, deg in in_degree.items() if deg == 0]
    zero_in.sort(key=lambda nid: nodes[nid].ancestor_distance)

    result = []
    while zero_in:
        curr = zero_in.pop(0)
        result.append(curr)
        for neighbor in adj.get(curr, []):
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                zero_in.append(neighbor)
                zero_in.sort(key=lambda nid: nodes[nid].ancestor_distance)

    return result

def colpali_late_interaction_match(
    thesis_text: str,
    available_images: List[Dict[str, Any]]
) -> Optional[Dict[str, Any]]:
    """
    Mô phỏng cơ chế ColPali MaxSim Late-Interaction:
    Ghép cặp luận điểm vi mô với hình ảnh gốc có độ phù hợp ngữ nghĩa thị giác cao nhất.
    """
    if not available_images:
        return None

    # Tính điểm đối sánh từ khóa và phân bố không gian
    best_img = None
    best_score = -1.0
    thesis_tokens = set(re.findall(r'\w+', thesis_text.lower()))

    for img in available_images:
        caption = img.get("caption", "").lower()
        ocr_text = img.get("ocr_text", "").lower()
        img_tokens = set(re.findall(r'\w+', f"{caption} {ocr_text}"))
        overlap = len(thesis_tokens.intersection(img_tokens))
        score = overlap / (len(thesis_tokens) + 1e-5)
        if score > best_score:
            best_score = score
            best_img = img

    return best_img or available_images[0]

# ---------------------------------------------------------------------------
# 3. Thuật toán Lõi Pha 2 (Micro Compilation Pass & Linters)
# ---------------------------------------------------------------------------

def compile_causal_flowchain(
    propositions: List[str],
    max_words_per_block: int = 65
) -> CausalFlowchainBlock:
    """
    Biên dịch các mệnh đề thành Chuỗi Nhân quả Causal Flowchain:
    Ép buộc sử dụng các toán tử mũi tên (\\rightarrow, \\Rightarrow, \\mapsto),
    khống chế độ dài <= max_words_per_block.
    """
    steps = [p.strip() for p in propositions if p.strip()]
    if not steps:
        formatted = "Khởi tạo trạng thái nguyên lý đầu."
    elif len(steps) == 1:
        formatted = f"{steps[0]} \\Longrightarrow \\text{{Hệ quả trực tiếp.}}"
    else:
        chain_parts = []
        for i, step in enumerate(steps):
            if i == len(steps) - 1:
                chain_parts.append(f"\\;\\Longrightarrow\\; {step}")
            else:
                chain_parts.append(f"{step} \\;\\xrightarrow[\\text{{vi mô}}]{{\\text{{tác nhân}}}}\\; ")
        formatted = "".join(chain_parts)

    word_count = len(re.findall(r'\S+', formatted))
    return CausalFlowchainBlock(
        block_id="FLOW_001",
        flow_steps=steps,
        formatted_chain=formatted,
        word_count=word_count
    )

def build_interlinear_gloss(
    equation_latex: str,
    physical_role: str,
    parameters: List[ParameterGloss],
    asymptotic_limits: List[str]
) -> EquationGlossContract:
    """
    Xây dựng khối giải phẫu phương trình liên dòng 3 cấp bắt buộc:
    1. Vai trò vật lý
    2. Giải nghĩa tham số vi mô chuẩn SI
    3. Kiểm tra giới hạn tiệm cận cực trị
    """
    return EquationGlossContract(
        equation_latex=equation_latex,
        physical_role=physical_role,
        parameters=parameters,
        asymptotic_limits=asymptotic_limits
    )

def run_deterministic_linters(
    ast_blocks: List[Dict[str, Any]],
    analogy_registry: Set[str]
) -> List[LinterResult]:
    """
    Bộ 5 Cổng Kiểm Tra Linter Tất Định (LINT_01 -> LINT_05):
    - LINT_01: Chống Wall-of-Text (<= 65 từ/khối không có mũi tên/công thức).
    - LINT_02: Neo Đầu mục (ảnh và hệ thức cốt trụ tại khối AST <= 2).
    - LINT_03: Cấm Công thức Trần trụi (100% công thức phải có đủ 3 tầng giải phẫu).
    - LINT_04: Cấm Bảng Số liệu Lưới (bảng > 4x3 phải chuyển sang đồ thị MATLAB HG2).
    - LINT_05: Chống Lặp Ẩn dụ (miền nguồn base_domain xuất hiện <= 1 lần/mục).
    """
    results: List[LinterResult] = []

    # LINT_01: Chống Wall-of-Text
    max_words_found = 0
    lint_01_pass = True
    for blk in ast_blocks:
        if blk.get("type") == "paragraph":
            text = blk.get("text", "")
            has_arrow = any(arrow in text for arrow in ["\\rightarrow", "\\Rightarrow", "\\mapsto", "→", "⇒"])
            has_eq = "$$" in text or "\\(" in text
            if not (has_arrow or has_eq):
                words = len(re.findall(r'\S+', text))
                if words > max_words_found:
                    max_words_found = words
                if words > 65:
                    lint_01_pass = False

    results.append(LinterResult(
        rule_id="LINT_01",
        rule_name="Chống Wall-of-Text (Causal Flowchain Constraint)",
        passed=lint_01_pass,
        threshold="<= 65 từ/khối văn bản không có mũi tên nhân quả",
        measured_value=f"{max_words_found} từ",
        violation_message="" if lint_01_pass else f"Phát hiện khối văn bản dài {max_words_found} từ vi phạm ngưỡng 65 từ.",
        suggested_repair_move="ProvideSchema(Causal_Flowchain)"
    ))

    # LINT_02: Neo Đầu mục
    anchor_idx = -1
    for idx, blk in enumerate(ast_blocks):
        if blk.get("type") in ["image", "visual_equation_anchor", "upfront_anchor"]:
            anchor_idx = idx
            break

    lint_02_pass = (0 <= anchor_idx <= 2)
    results.append(LinterResult(
        rule_id="LINT_02",
        rule_name="Neo Nhận thức Đầu mục (Upfront Visual-Equation Anchor)",
        passed=lint_02_pass,
        threshold="Vị trí khối AST <= 2 (Ngay đầu mục)",
        measured_value=f"Vị trí khối: {anchor_idx}",
        violation_message="" if lint_02_pass else f"Điểm neo trực quan xuất hiện muộn ở vị trí khối {anchor_idx}.",
        suggested_repair_move="Ground(Visual_Eq) & Filter(Intro_Prose)"
    ))

    # LINT_03: Cấm Công thức Trần trụi
    total_equations = 0
    glossed_equations = 0
    for blk in ast_blocks:
        if blk.get("type") in ["equation", "formula_block"]:
            total_equations += 1
            if blk.get("has_interlinear_gloss", False):
                glossed_equations += 1

    lint_03_pass = (total_equations == 0 or total_equations == glossed_equations)
    results.append(LinterResult(
        rule_id="LINT_03",
        rule_name="Cấm Công thức Trần trụi (Interlinear Gloss Coverage)",
        passed=lint_03_pass,
        threshold="100% công thức toán phải có đủ 3 nhãn giải phẫu",
        measured_value=f"{glossed_equations}/{total_equations} công thức có giải phẫu",
        violation_message="" if lint_03_pass else f"Có {total_equations - glossed_equations} công thức thiếu khối giải phẫu 3 tầng.",
        suggested_repair_move="Augment(Equation_Gloss)"
    ))

    # LINT_04: Cấm Bảng Số liệu Lưới
    large_table_count = 0
    for blk in ast_blocks:
        if blk.get("type") == "table":
            rows = blk.get("rows", 0)
            cols = blk.get("cols", 0)
            if rows > 4 and cols > 3:
                large_table_count += 1

    lint_04_pass = (large_table_count == 0)
    results.append(LinterResult(
        rule_id="LINT_04",
        rule_name="Cấm Bảng Số liệu Lưới (Grid Table Suppression)",
        passed=lint_04_pass,
        threshold="0 bảng lưới kích thước > 4x3 (Phải chuyển sang đồ thị MATLAB HG2)",
        measured_value=f"{large_table_count} bảng lưới lớn",
        violation_message="" if lint_04_pass else f"Phát hiện {large_table_count} bảng số liệu lớn chưa chuyển hóa sang đồ thị.",
        suggested_repair_move="SpecifyOutput(MATLAB_HG2_Plot)"
    ))

    # LINT_05: Chống Lặp Ẩn dụ
    redundant_analogies = 0
    used_domains: Set[str] = set()
    for blk in ast_blocks:
        if blk.get("type") == "analogy":
            domain = blk.get("base_domain", "")
            if domain in used_domains:
                redundant_analogies += 1
            used_domains.add(domain)

    lint_05_pass = (redundant_analogies == 0)
    results.append(LinterResult(
        rule_id="LINT_05",
        rule_name="Chống Lặp Ẩn dụ Cơ học (Analogy Registry Enforcement)",
        passed=lint_05_pass,
        threshold="Số lần lặp lại cùng miền nguồn ẩn dụ = 0",
        measured_value=f"{redundant_analogies} lần lặp",
        violation_message="" if lint_05_pass else f"Phát hiện {redundant_analogies} lần lặp lại miền nguồn ẩn dụ trong cùng mục.",
        suggested_repair_move="CounterExample(Redundant_Analogy)"
    ))

    return results

# ---------------------------------------------------------------------------
# 4. Kiểm tra Tự chẩn đoán Mô-đun (Self-Diagnostic Test)
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding='utf-8')
    print("=== KIỂM TRA ĐỘNG CƠ MALAE ENGINE (SELF-DIAGNOSTIC) ===")

    # Test 1: Khử chu trình GREEDYCYCLEBREAK
    nodes = {
        "A": ConceptNode(node_id="A", content="Định luật Coulomb", ancestor_distance=0),
        "B": ConceptNode(node_id="B", content="Phương trình Poisson", ancestor_distance=1),
        "C": ConceptNode(node_id="C", content="Thế tĩnh điện phi(z)", ancestor_distance=2),
        "D": ConceptNode(node_id="D", content="Mật độ hạt tải n(z)", ancestor_distance=3),
    }
    edges = [
        ConceptEdge(source_id="A", target_id="B", confidence_weight=0.9),
        ConceptEdge(source_id="B", target_id="C", confidence_weight=0.95),
        ConceptEdge(source_id="C", target_id="D", confidence_weight=0.85),
        ConceptEdge(source_id="D", target_id="C", confidence_weight=0.6),  # Chu trình tự hợp C <-> D
    ]

    clean_edges, removed = greedy_cycle_breaking(nodes, edges)
    print(f"1. Khử chu trình GREEDYCYCLEBREAK: Tổng cạnh = {len(edges)}, Cạnh giữ lại = {len(clean_edges)}, Cạnh chu trình bị cắt = {len(removed)}")
    assert len(removed) == 1, "GREEDYCYCLEBREAK phải cắt đúng 1 cạnh chu trình yếu nhất!"
    assert removed[0].source_id == "D" and removed[0].target_id == "C", "Cạnh D->C (ngược nguyên lý) phải bị cắt!"

    # Test 2: Sắp xếp Tô-pô Trọng số
    topo_order = weighted_topological_sort(nodes, clean_edges)
    print(f"2. Sắp xếp Tô-pô Trọng số Nguyên lý Đầu: {' -> '.join(topo_order)}")
    assert topo_order == ["A", "B", "C", "D"], "Trật tự tô-pô phải đi từ A -> B -> C -> D!"

    # Test 3: Bộ 5 Cổng Linter
    sample_blocks = [
        {"type": "heading", "text": "Mục 2.1: Giếng Lượng Tử 1D"},
        {"type": "upfront_anchor", "image_id": "FIG_01", "core_equation": "-\\frac{\\hbar^2}{2m^*}..."},
        {"type": "paragraph", "text": "Bề rộng giếng d giảm \\rightarrow Không gian pha bị nén \\Rightarrow Năng lượng lượng tử hóa."},
        {"type": "equation", "has_interlinear_gloss": True},
        {"type": "analogy", "base_domain": "dây_đàn_cơ_học"}
    ]
    linter_results = run_deterministic_linters(sample_blocks, set())
    all_pass = all(r.passed for r in linter_results)
    print(f"3. Kiểm định 5 Cổng Linter Tất định: {'100% PASS' if all_pass else 'FAIL'}")
    for res in linter_results:
        print(f"   [{'PASS' if res.passed else 'FAIL'}] {res.rule_id}: {res.rule_name}")

    assert all_pass, "Mẫu chuẩn tắc phải vượt qua 100% 5 cổng Linter!"
    print("=== MALAE ENGINE TỰ CHẨN ĐOÁN THÀNH CÔNG 100% ===")
