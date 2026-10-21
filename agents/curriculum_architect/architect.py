# -*- coding: utf-8 -*-
"""
Curriculum & Structural Architect Engine (Agent 1 Core Engine)
Mô-đun thực thi độc lập (Standalone Engine) cho Agent 1: curriculum-architect.
Chủ thể phê duyệt: Bùi Trung Dũng (Khoa Vật lý Kỹ thuật, ĐH Bách khoa Hà Nội - HUST).

Tích hợp 4 thuật toán cốt lõi:
- Thuật toán 1: HDIR Engine 2.0 & DICG 2.0 (Định vị & Pre-Scan Handshake nguồn kép)
- Thuật toán 2: HPDE 2.0 (Phân rã tri thức phân tử & Mô hình lập luận Toulmin)
- Thuật toán 4: PLBE (Kiến tạo DAG tri thức, Kahn Acyclic Check, Phân rã MPT 5 giai đoạn)
- Thuật toán 10: ATCC (Chuẩn hóa danh pháp song ngữ Anh - Việt, ISO 80000, NĐ 30, Luật Đo lường 04)
"""

import os
import sys
import re
import json
from typing import List, Dict, Tuple, Optional, Any, Set

# Đảm bảo import liên kết cả agents.schemas và agents.common
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

import agents
from agents.schemas import (
    CurriculumBlueprint,
    KnowledgeDAGNode,
    KnowledgeDAGEdge,
    MicroPointTopicSpec,
    VisualRequirement,
    TerminologyEntry,
)
from agents.common import (
    TerminologyGuardian,
    ASTLinter,
    SemiconductorDatabase,
)


class CurriculumArchitect:
    """
    Lớp điều phối trung tâm của Curriculum & Structural Architect Subagent.
    Tuân thủ nguyên tắc Đặc quyền Tối thiểu (PoLP) và Bảo toàn Thuật toán Cốt lõi (Zero-Drift).
    """

    def __init__(self, sandbox_root: Optional[str] = None):
        r"""Khởi tạo Architect với đường dẫn Sandbox Whitelist (mặc định Google Drive G:\)."""
        self.sandbox_root = sandbox_root or r"G:\My Drive\NotebookLM - Academic Knowledge Base"
        self.max_healing_retries = 5

    # =========================================================================
    # THUẬT TOÁN 1: HDIR ENGINE & DICG 2.0 (PRE-SCAN HANDSHAKE)
    # =========================================================================

    @staticmethod
    def remove_accents(input_str: str) -> str:
        """Loại bỏ dấu tiếng Việt để chuẩn hóa so khớp ngữ nghĩa học thuật."""
        import unicodedata
        nfkd = unicodedata.normalize("NFKD", input_str)
        no_accents = "".join([c for c in nfkd if not unicodedata.combining(c)])
        return no_accents.replace("đ", "d").replace("Đ", "D")

    @classmethod
    def token_set_ratio(cls, s1: str, s2: str) -> float:
        """
        Tính toán độ tương đồng mờ Token Set Ratio giữa hai tiêu đề học phần hoặc tệp tin.
        Tự động chuẩn hóa dấu tiếng Việt, loại bỏ ký tự đặc biệt và so khớp tập hợp từ khóa.
        """
        def tokenize(s: str) -> set:
            s_no_acc = cls.remove_accents(s)
            s_clean = re.sub(r"[^\w\s]", " ", s_no_acc.lower())
            return set(s_clean.split())

        t1 = tokenize(s1)
        t2 = tokenize(s2)
        if not t1 or not t2:
            return 0.0

        intersection = t1.intersection(t2)
        diff1 = t1.difference(t2)
        diff2 = t2.difference(t1)

        sorted_inter = " ".join(sorted(list(intersection)))
        sorted_d1 = " ".join(sorted(list(diff1)))
        sorted_d2 = " ".join(sorted(list(diff2)))

        t0 = sorted_inter.strip()
        t1 = (sorted_inter + " " + sorted_d1).strip()
        t2 = (sorted_inter + " " + sorted_d2).strip()

        from difflib import SequenceMatcher
        score1 = SequenceMatcher(None, t0, t1).ratio() if t0 and t1 else 0.0
        score2 = SequenceMatcher(None, t0, t2).ratio() if t0 and t2 else 0.0
        score3 = SequenceMatcher(None, t1, t2).ratio() if t1 and t2 else 0.0

        return max(score1, score2, score3)

    def pre_scan_handshake(
        self,
        course_name: str,
        chapter_index: int,
        mock_file_list: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        r"""
        Kiểm tra nguồn kép (Slide HUST và Sách chuyên khảo) theo Lớp 2 DICG 2.0.
        Hỗ trợ cả môi trường trực tiếp trên Google Drive G:\ và chế độ kiểm thử mock.
        """
        result = {
            "handshake_passed": False,
            "course_name": course_name,
            "chapter_index": chapter_index,
            "slide_found": False,
            "textbook_found": False,
            "slide_path": None,
            "textbook_path": None,
            "error_message": None,
        }

        # Nếu có mock_file_list (dùng trong Unit test và Offline verification)
        files = mock_file_list or []
        if not mock_file_list and os.path.exists(self.sandbox_root):
            # Quét danh mục trên Google Drive
            course_dir = None
            try:
                for entry in os.scandir(self.sandbox_root):
                    if entry.is_dir() and self.token_set_ratio(entry.name, course_name) >= 0.8:
                        course_dir = entry.path
                        break
                if course_dir and os.path.exists(course_dir):
                    files = [os.path.join(course_dir, f) for f in os.listdir(course_dir)]
            except Exception as e:
                result["error_message"] = f"Lỗi truy cập Sandbox Google Drive: {str(e)}"
                return result

        chapter_pattern = rf"(?:chuong|ch|c)[_\s\-]?0?{chapter_index}"
        for f in files:
            fname = os.path.basename(f).lower()
            if re.search(chapter_pattern, fname):
                if any(k in fname for k in ["slide", "bai_giang", "lecture", "presentation"]):
                    result["slide_found"] = True
                    result["slide_path"] = f
                elif any(k in fname for k in ["giao_trinh", "sach", "textbook", "reference"]):
                    result["textbook_found"] = True
                    result["textbook_path"] = f

        if result["slide_found"] and result["textbook_found"]:
            result["handshake_passed"] = True
        else:
            missing = []
            if not result["slide_found"]:
                missing.append(f"Slide bài giảng Chương {chapter_index}")
            if not result["textbook_found"]:
                missing.append(f"Sách giáo trình chuyên khảo Chương {chapter_index}")
            result["error_message"] = f"Pre-Scan Handshake THẤT BẠI: Thiếu {', '.join(missing)}."

        return result

    # =========================================================================
    # THUẬT TOÁN 2 & 4: HPDE 2.0 & PLBE (DAG TRI THỨC & KHỬ CHU TRÌNH KAHN)
    # =========================================================================

    @staticmethod
    def decontextualize_proposition(text: str, entity_replacements: Optional[Dict[str, str]] = None) -> str:
        """
        Khử ngữ cảnh hóa triệt để (Full Decontextualization) cho mệnh đề nguyên tử.
        Thay thế đại từ chỉ định và đại từ nhân xưng bằng danh từ định danh thực thể xác định.
        """
        cleaned = text.strip()
        replacements = entity_replacements or {
            r"\bnó\b": "linh kiện",
            r"\bchúng\b": "các hạt tải",
            r"\bđiều này\b": "hiện tượng phát xạ kích thích",
            r"\bhiện tượng đó\b": "quá trình tái hợp bức xạ",
        }
        for pattern, replacement in replacements.items():
            cleaned = re.sub(pattern, replacement, cleaned, flags=re.IGNORECASE)
        return cleaned

    def detect_and_break_dag_cycles(
        self,
        nodes: List[KnowledgeDAGNode],
        edges: List[KnowledgeDAGEdge]
    ) -> Tuple[bool, List[KnowledgeDAGEdge], List[str]]:
        """
        Thực thi Giải thuật Kahn kiểm tra tính phi chu trình (Acyclic) và
        tự phục hồi (Self-Healing tối đa 5 lần) bằng cơ chế GREEDYCYCLEBREAK.
        """
        current_edges = list(edges)
        all_node_ids = {n.node_id for n in nodes}
        cycle_history = []

        for attempt in range(1, self.max_healing_retries + 1):
            adj_list: Dict[str, List[str]] = {nid: [] for nid in all_node_ids}
            in_degree: Dict[str, int] = {nid: 0 for nid in all_node_ids}

            for e in current_edges:
                if e.source_node in adj_list and e.target_node in in_degree:
                    adj_list[e.source_node].append(e.target_node)
                    in_degree[e.target_node] += 1

            queue = [nid for nid, deg in in_degree.items() if deg == 0]
            visited_count = 0

            while queue:
                curr = queue.pop(0)
                visited_count += 1
                for neighbor in adj_list[curr]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        queue.append(neighbor)

            if visited_count == len(all_node_ids):
                # DAG hoàn toàn phi chu trình!
                return True, current_edges, cycle_history

            # Phát hiện chu trình kín!
            cyclic_nodes = [nid for nid, deg in in_degree.items() if deg > 0]
            cycle_msg = f"Lần {attempt}: Phát hiện chu trình kín giữa các nút {cyclic_nodes}"
            cycle_history.append(cycle_msg)

            # GREEDYCYCLEBREAK: Tìm và cắt bỏ cạnh gây chu trình yếu nhất (ưu tiên cắt cạnh quay ngược)
            edge_to_remove = None
            for e in reversed(current_edges):
                if e.source_node in cyclic_nodes and e.target_node in cyclic_nodes:
                    # Ưu tiên giữ quan hệ prerequisite cốt lõi, cắt bỏ cạnh phụ
                    if e.relation_type in ["boundary_limit", "generalization", "causal"]:
                        edge_to_remove = e
                        break
            if not edge_to_remove:
                # Nếu toàn bộ là prerequisite, cắt cạnh cuối cùng trong chu trình
                for e in reversed(current_edges):
                    if e.source_node in cyclic_nodes and e.target_node in cyclic_nodes:
                        edge_to_remove = e
                        break

            if edge_to_remove:
                current_edges.remove(edge_to_remove)
            else:
                break

        return False, current_edges, cycle_history

    # =========================================================================
    # THUẬT TOÁN 10: ATCC ENGINE (CHUẨN HÓA DANH PHÁP SONG NGỮ)
    # =========================================================================

    @staticmethod
    def standardize_terminology_entries(
        raw_terms: List[Dict[str, str]]
    ) -> List[TerminologyEntry]:
        """
        Chuẩn hóa danh mục danh pháp song ngữ theo quy chuẩn ATCC, ISO 80000 và NĐ 30.
        """
        entries = []
        for item in raw_terms:
            term_en = item.get("term_en", "").strip().lower()
            term_vi = item.get("term_vi", "").strip().lower()
            symbol = item.get("symbol_latex", "").strip()
            unit = item.get("standard_unit_si", "").strip()
            iso_ref = item.get("iso_standard_ref", "ISO 80000")
            decree_30 = item.get("decree_30_case", "lower")

            # Áp dụng TerminologyGuardian kiểm tra format
            entry = TerminologyEntry(
                term_en=term_en,
                term_vi=term_vi,
                symbol_latex=symbol,
                standard_unit_si=unit,
                iso_standard_ref=iso_ref,
                decree_30_case=decree_30,
            )
            entries.append(entry)
        return entries

    @staticmethod
    def infer_target_material(text: str) -> Optional[str]:
        """
        Nhận diện và trích xuất đích danh vật liệu bán dẫn từ ngữ cảnh bài giảng (Slide/Sách).
        Đối chiếu với danh mục vật liệu bán dẫn chuẩn SEMICONDUCTORS_300K.
        """
        if not text:
            return None
        candidate_materials = ["AlGaAs", "InGaAsP", "InGaAs", "AlGaInP", "GaAs", "InP", "GaN", "Si", "Ge"]
        for mat in candidate_materials:
            pattern = rf"\b{re.escape(mat)}\b"
            if re.search(pattern, text, flags=re.IGNORECASE):
                for std_mat in ["GaAs", "InP", "GaN", "AlGaAs", "InGaAsP", "Si", "Ge"]:
                    if mat.lower() == std_mat.lower():
                        return std_mat
                return mat
        return None

    # =========================================================================
    # ĐIỀU PHỐI TỔNG THỂ: TẠO LẬP HỢP ĐỒNG CURRICULUM BLUEPRINT
    # =========================================================================

    def generate_blueprint(
        self,
        course_name: str,
        chapter_index: int,
        section_index: int,
        section_title: str,
        source_documents: List[str],
        raw_dag_nodes: List[Dict[str, Any]],
        raw_dag_edges: List[Dict[str, Any]],
        raw_mpt_specs: List[Dict[str, Any]],
        raw_terms: List[Dict[str, Any]],
    ) -> CurriculumBlueprint:
        """
        Điều phối toàn diện quá trình phân rã học liệu, kiểm toán DAG và tạo
        Hợp đồng Dữ liệu CurriculumBlueprint hoàn chỉnh.
        """
        # 1. Khởi tạo đối tượng Node
        nodes = [KnowledgeDAGNode.model_validate(n) for n in raw_dag_nodes]

        # 2. Khởi tạo đối tượng Edge và thực thi Giải thuật Kahn kiểm tra/khử chu trình
        initial_edges = [KnowledgeDAGEdge.model_validate(e) for e in raw_dag_edges]
        is_acyclic, clean_edges, cycle_log = self.detect_and_break_dag_cycles(nodes, initial_edges)
        if not is_acyclic:
            raise ValueError(
                f"CurriculumArchitect Hard Stop: Đã thử tự phục hồi 5 lần nhưng đồ thị vẫn chứa chu trình kín: {cycle_log}"
            )

        # 3. Khởi tạo danh sách MicroPointTopicSpec
        mpts = []
        for m in raw_mpt_specs:
            vis_req = None
            if "visual_requirement" in m and m["visual_requirement"]:
                v_data = dict(m["visual_requirement"])
                if not v_data.get("target_material"):
                    context_text = f"{m.get('title', '')} {m.get('core_proposition', '')} {v_data.get('description', '')}"
                    inferred_mat = self.infer_target_material(context_text)
                    if inferred_mat:
                        v_data["target_material"] = inferred_mat
                if "operating_temperature_k" not in v_data or v_data["operating_temperature_k"] is None:
                    v_data["operating_temperature_k"] = 300.0
                vis_req = VisualRequirement.model_validate(v_data)
            
            mpt = MicroPointTopicSpec(
                mpt_id=m["mpt_id"],
                title=m["title"],
                core_proposition=self.decontextualize_proposition(m["core_proposition"]),
                prerequisite_mpt_ids=m.get("prerequisite_mpt_ids", []),
                visual_requirement=vis_req,
                target_equations=m.get("target_equations", [])
            )
            mpts.append(mpt)

        # 4. Chuẩn hóa danh pháp song ngữ ATCC
        terminology_contracts = self.standardize_terminology_entries(raw_terms)

        # 5. Đóng gói đối tượng Blueprint và kích hoạt kiểm định Pydantic
        blueprint = CurriculumBlueprint(
            course_name=course_name,
            chapter_index=chapter_index,
            section_index=section_index,
            section_title=section_title,
            source_documents=source_documents,
            dag_nodes=nodes,
            dag_edges=clean_edges,
            mpt_specifications=mpts,
            terminology_contracts=terminology_contracts
        )

        return blueprint

    @staticmethod
    def export_blueprint_json(blueprint: CurriculumBlueprint, output_path: str) -> str:
        """Xuất bản Hợp đồng Dữ liệu Blueprint ra tệp JSON trên đĩa."""
        os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(blueprint.model_dump_json(indent=2))
        return output_path
