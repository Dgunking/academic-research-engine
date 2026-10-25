# -*- coding: utf-8 -*-
r"""
Module Vệ Sinh Google Drive & Khóa Cứng Thư Mục (Zero-Root-Drift Enforcer).
Định vị: scripts/enforce_drive_hygiene.py
Áp dụng: ENGINEERING_DISCIPLINE_WORKFLOW.md [PHA 2 & PHA 3]

Chức năng:
1. Quét duy nhất cấp root \ (non-recursive).
2. Tự động nhận diện các tệp học liệu mồ côi (Chuyen_Khao_*, Ho_So_Kiem_Toan_*, [Mo_Phong]_*, [Goc]_*, v.v.).
3. Định tuyến an toàn về đúng 7 thư mục môn học chuẩn trong NotebookLM - Academic Knowledge Base.
4. Bảo vệ tuyệt đối 100% tệp cá nhân người dùng (.xlsx, .gsheet, .rar, đồ án, ảnh chụp màn hình).
"""

import os
import re
import sys
import shutil
from typing import Dict, Any, Optional, List, Tuple

# Đảm bảo UTF-8 trên Windows console
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass


SUBJECT_ROSTER = {
    "laser_diode": "Laser Diode - Cấu trúc và Nguyên lý",
    "ban_dan": "Vật lý và linh kiện bán dẫn",
    "nano": "Cơ sở vật lý và công nghệ nano",
    "quang_hoc": "Cơ sở quang học và quang điện tử",
    "truong_dien_tu": "Trường điện từ",
    "quang_xuc_tac": "Quang xúc tác",
    "chat_ran": "Vật lý chất rắn",
}

# Tiền tố/Định dạng biểu thị tệp học thuật
ACADEMIC_PATTERNS = [
    re.compile(r"^Chuyen_Khao_.*\.pdf$", re.I),
    re.compile(r"^Muc_\d+.*\.pdf$", re.I),
    re.compile(r"^Ho_[Ss]o_Kiem_[Tt]oan_.*", re.I),
    re.compile(r"^\[(?:Mo_Phong|Goc)\]_.*\.(?:png|jpg|jpeg|svg)$", re.I),
    re.compile(r"^PROGRESS_CHECKPOINT.*", re.I),
    re.compile(r"^master_courseware_.*", re.I),
    re.compile(r"^compiler_engine_.*", re.I),
]

# Tệp cá nhân tuyệt đối cấm can thiệp
PERSONAL_PATTERNS = [
    re.compile(r"\.(?:xlsx|gsheet|rar|zip|gslides)$", re.I),
    re.compile(r"(?:Đồ án|Do an|Screenshot|Báo cáo|Hương|CHUNG_NHAN|EldenRing|ELDENRING|SSDT|F13TG|mcv-jkpo|Python|Danh sách|DanhSach|Tài liệu không có tiêu đề)", re.I),
]

# Từ khóa định tuyến môn học
SUBJECT_KEYWORDS = [
    ("quang_xuc_tac", ["quang_xuc_tac", "xuc_tac", "ag3vo4", "wo3", "c3n4"]),
    ("laser_diode", ["laser_diode", "laser", "vung_tich_cuc", "khoang_cong_huong", "do_loi_quang_hoc", "giam_giu_quang", "clamping", "p_i", "kep_do_loi", "photon", "dieu_che"]),
    ("quang_hoc", ["co_so_quang_hoc", "quang_hoc", "optics", "be_mat_cau", "phan_xa", "khuc_xa"]),
    ("ban_dan", ["ban_dan", "linh_kien_ban_dan", "fermi", "pn_junction"]),
    ("nano", ["nano", "carbon_nanotube", "graphene"]),
    ("truong_dien_tu", ["truong_dien_tu", "maxwell", "song_dien_tu"]),
    ("chat_ran", ["chat_ran", "mang_tinh_the", "brillouin"]),
]


def detect_target_subject(filename: str) -> Optional[str]:
    """Xác định môn học đích từ tên tệp."""
    clean_name = filename.lower()
    for s_key, kw_list in SUBJECT_KEYWORDS:
        for kw in kw_list:
            if kw in clean_name:
                return SUBJECT_ROSTER[s_key]

    # Mặc định cho ảnh mô phỏng/gốc nếu không có từ khóa môn khác nhưng mang tính chất quang/laser
    if filename.startswith(("[Mo_Phong]", "[Goc]")):
        return SUBJECT_ROSTER["laser_diode"]

    return None


def detect_target_path(filename: str, drive_root: str = r"") -> Optional[str]:
    """
    Phân tích tên tệp và trả về đường dẫn đích chuẩn trong NotebookLM - Academic Knowledge Base.
    Nếu là tệp cá nhân hoặc không thuộc diện học thuật mồ côi, trả về None.
    """
    # 1. Kiểm tra cấm tệp cá nhân
    for p_pat in PERSONAL_PATTERNS:
        if p_pat.search(filename):
            return None

    # 2. Kiểm tra khớp pattern học thuật
    is_academic = any(a_pat.search(filename) for a_pat in ACADEMIC_PATTERNS)
    if not is_academic:
        return None

    # 3. Xác định môn học
    subject_folder = detect_target_subject(filename)
    if not subject_folder:
        return None

    academic_base = os.path.join(drive_root, "NotebookLM - Academic Knowledge Base", subject_folder)

    # 4. Xác định thư mục con
    clean_lower = filename.lower()
    is_archive = any(k in clean_lower for k in ["_v2", "c1_v2", "master_courseware", "compiler_engine", "lo_trinh"])

    if is_archive:
        subfolder = "Kho_Luu_Tru_File_Rac_Archive"
    elif filename.endswith(".pdf") and (filename.startswith("Chuyen_Khao_") or filename.startswith("Muc_")):
        subfolder = "Bai_Giang_Dong_Goi"
    elif filename.startswith(("[Mo_Phong]", "[Goc]")) or filename.lower().endswith((".png", ".jpg", ".jpeg", ".svg")):
        subfolder = "Kho_Hinh_Anh"
    else:
        # File docx kiểm toán, checkpoint gốc nằm tại root của môn học
        return os.path.join(academic_base, filename)

    return os.path.join(academic_base, subfolder, filename)


def scan_and_relocate_orphans(
    drive_root: str = r"",
    dry_run: bool = False
) -> Dict[str, Any]:
    """
    Quét duy nhất cấp root (non-recursive) của drive_root, di chuyển các tệp mồ côi học thuật
    về đúng thư mục môn học tương ứng.
    """
    if not os.path.exists(drive_root):
        raise FileNotFoundError(f"Đường dẫn drive_root không tồn tại: {drive_root}")

    relocated_files: List[Dict[str, str]] = []
    skipped_personal_files: List[str] = []

    # Quét không đệ quy duy nhất cấp root
    for entry in os.scandir(drive_root):
        if not entry.is_file():
            continue

        filename = entry.name
        target_path = detect_target_path(filename, drive_root)

        if not target_path:
            skipped_personal_files.append(filename)
            continue

        src_path = entry.path

        if not dry_run:
            dest_dir = os.path.dirname(target_path)
            os.makedirs(dest_dir, exist_ok=True)

            # Nếu tệp đích đã tồn tại và không phải chính nó
            final_target = target_path
            if os.path.exists(target_path) and os.path.abspath(target_path) != os.path.abspath(src_path):
                # Chuyển vào Archive để tránh ghi đè làm mất mát
                subject_dir = os.path.dirname(dest_dir) if "Bai_Giang_Dong_Goi" in dest_dir or "Kho_Hinh_Anh" in dest_dir else dest_dir
                archive_dir = os.path.join(subject_dir, "Kho_Luu_Tru_File_Rac_Archive")
                os.makedirs(archive_dir, exist_ok=True)
                final_target = os.path.join(archive_dir, filename)

            shutil.move(src_path, final_target)

        relocated_files.append({
            "filename": filename,
            "source": src_path,
            "destination": target_path
        })

    return {
        "drive_root": drive_root,
        "relocated_count": len(relocated_files),
        "relocated_files": relocated_files,
        "skipped_personal_count": len(skipped_personal_files),
        "dry_run": dry_run
    }


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Google Drive Root Hygiene Enforcer")
    parser.add_argument("--apply", action="store_true", help="Thực thi di dời thực tế (không dry-run)")
    args = parser.parse_args()

    is_dry = not args.apply
    mode_str = "DRY-RUN (Thử nghiệm)" if is_dry else "LIVE EXECUTION (Thực thi)"
    print(f"=== QUÉT VÀ VỆ SINH GOOGLE DRIVE ROOT [{mode_str}] ===")
    rep = scan_and_relocate_orphans(r"", dry_run=is_dry)
    print(f"-> Đã xử lý {rep['relocated_count']} tệp học thuật mồ côi.")
    print(f"-> Bỏ qua an toàn {rep['skipped_personal_count']} tệp cá nhân người dùng.")
    for it in rep["relocated_files"]:
        action_prefix = "[DRY-RUN]" if is_dry else "[MOVED]"
        print(f"   {action_prefix} {it['filename']} -> {it['destination']}")
