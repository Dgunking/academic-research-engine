"""
Academic Gate Hook for Antigravity Lifecycle Hooks
Chặn bắt, kiểm toán an toàn và xác thực chuẩn mực trước/sau khi gọi công cụ (write_to_file, replace_file_content, edit_file, write_file).
Tuân thủ nghiêm ngặt tài liệu thiết kế: AI Agent Giảng Dạy & Sáng Tạo Trên Antigravity.md và 13 Thuật toán Cốt lõi.
"""
import sys
import os
import json
import re
import tempfile
from datetime import datetime

def log_audit(message: str):
    temp_dir = tempfile.gettempdir()
    log_file = os.path.join(temp_dir, "academic_agent_audit.log")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] {message}\n")
    except Exception:
        pass

def handle_pre_tool_use(payload: dict) -> dict:
    tool_call = payload.get("toolCall", {})
    tool_name = tool_call.get("name", "")
    args = tool_call.get("args", {})
    
    # Chuẩn hóa tên đường dẫn từ các đối số khác nhau của các tool
    target_file = (
        args.get("TargetFile", "") or 
        args.get("targetFile", "") or 
        args.get("Path", "") or 
        args.get("path", "")
    )
    
    if not target_file:
        return {"decision": "allow"}

    norm_path = os.path.normpath(target_file).lower()

    # 0. KHÓA BẢO MẬT TỐI CAO BẤT BIẾN TOÀN BỘ 13 THUẬT TOÁN CỐT LÕI (LEVEL-0 SUPREME SECURITY MASTER LOCK)
    CORE_ALGO_PATTERNS = [
        "physics_viz_lock.py",
        "13_thuat_toan_cot_loi_master_lock.md",
        "core_13_algorithms.sha256",
        "physics_viz_lock.sha256",
        "hdir_engine.py",
        "hpde_engine.py",
        "malae_engine.py",
        "rvae_engine.py",
        "parallel_scan_engine.py",
        "hust_pdf_engine.py",
        os.path.normpath(".agents/common/cas.py").lower(),
        os.path.normpath(".agents/common/linter.py").lower(),
        os.path.normpath(".agents/common/materials.py").lower(),
        os.path.normpath(".agents/common/terminology.py").lower(),
        os.path.normpath("agents/curriculum_architect").lower(),
        os.path.normpath("agents/orchestration_kernel").lower(),
        os.path.normpath("agents/pedagogical_author").lower(),
        os.path.normpath("agents/quality_gatekeeper").lower(),
        os.path.normpath("agents/physics_graphic_artist").lower(),
        os.path.normpath("agents/curriculum_fidelity_auditor").lower(),
    ]

    is_core_algo = any(pat in norm_path for pat in CORE_ALGO_PATTERNS)
    if is_core_algo:
        auth_granted = False
        auth_type = "NONE"

        # 1. Kiểm tra Token file xác thực tạm thời (%TEMP%/bui_trung_dung_core_auth.token)
        temp_auth = os.path.join(tempfile.gettempdir(), "bui_trung_dung_core_auth.token")
        if os.path.exists(temp_auth):
            try:
                mtime = os.path.getmtime(temp_auth)
                if (datetime.now().timestamp() - mtime) < 300: # 5 phút hiệu lực
                    with open(temp_auth, "r", encoding="utf-8") as af:
                        token_str = af.read()
                        if "BUI_TRUNG_DUNG_CONFIRMED_CORE_OVERRIDE" in token_str or "BUI_TRUNG_DUNG_AUTHORIZED_CORE_ALGORITHM_13" in token_str:
                            auth_granted = True
                            auth_type = "TEMP_TOKEN_FILE"
            except Exception:
                pass

        # 2. Quét kiểm tra lịch sử hội thoại transcript
        if not auth_granted:
            try:
                brain_dir = os.path.expanduser(r"~\.gemini\antigravity\brain")
                if os.path.exists(brain_dir):
                    recent_transcripts = []
                    for entry in os.scandir(brain_dir):
                        if entry.is_dir():
                            t_path = os.path.join(entry.path, ".system_generated", "logs", "transcript.jsonl")
                            if os.path.exists(t_path):
                                recent_transcripts.append((os.path.getmtime(t_path), t_path))
                    recent_transcripts.sort(reverse=True)
                    if recent_transcripts:
                        latest_t = recent_transcripts[0][1]
                        with open(latest_t, "r", encoding="utf-8") as tf:
                            lines = tf.readlines()[-40:]
                            
                            # Xác thực từ khóa chỉ thị / xác nhận tường minh của Bùi Trung Dũng
                            confirmation_keywords = [
                                "xác nhận chỉnh sửa thuật toán cốt lõi",
                                "xác nhận mở khóa thuật toán cốt lõi",
                                "xác nhận vòng 2/2",
                                "xác nhận (vòng 2/2)",
                                "xác nhận (lần 2/2)",
                                "đồng ý chỉnh sửa thuật toán cốt lõi",
                                "tiến hành cập nhật thuật toán 13 vào physics_viz_lock.py",
                                "lệnh chỉ thị trực tiếp của bùi trung dũng"
                            ]
                            for l in lines:
                                l_lower = l.lower()
                                if any(kw in l_lower for kw in confirmation_keywords):
                                    auth_granted = True
                                    auth_type = "TRANSCRIPT_CONFIRMATION"
                                    break
            except Exception:
                pass

        if not auth_granted:
            reason = (
                f"LỆNH BỊ TỪ CHỐI (Level-0 Supreme Security Master Lock): Tệp '{target_file}' trực thuộc danh mục 13 Thuật toán Cốt lõi.\n"
                f"Kỷ luật bảo mật tối cao của Bùi Trung Dũng quy định:\n"
                f"- Nếu CÓ CHỈ THỊ TRỰC TIẾP từ Bùi Trung Dũng: AI Agent BẮT BUỘC phải hỏi lại xác nhận 1 lần trước khi chỉnh sửa.\n"
                f"- Nếu KHÔNG CÓ CHỈ THỊ TRỰC TIẾP từ Bùi Trung Dũng: AI Agent BẮT BUỘC phải hỏi xác nhận 2 lần liên tiếp (Vòng 1: Khởi xướng & Vòng 2: Toàn văn Diff) trước khi chỉnh sửa.\n"
                f"-> Thao tác bị chặn đứng an toàn. Vui lòng hỏi xác nhận với Bùi Trung Dũng trên Chat."
            )
            log_audit(f"DENY PreToolUse: {reason}")
            return {"decision": "deny", "reason": reason}

    # 1. Bảo vệ liên kết ảo Google Drive (.gdoc, .gsheet, .gslides)
    virtual_exts = [".gdoc", ".gsheet", ".gslides"]
    if any(norm_path.endswith(ext) for ext in virtual_exts):
        reason = f"CẤM GHI ĐÈ: Không được can thiệp hoặc ghi đè nhị phân vào tệp liên kết ảo Google Drive ({target_file})."
        log_audit(f"DENY PreToolUse: {reason}")
        return {"decision": "deny", "reason": reason}

    # 2. Kiểm tra Sandbox Whitelist trên Google Drive G:\
    if norm_path.startswith("g:\\"):
        allowed_prefix = os.path.normpath(r"g:\my drive\notebooklm - academic knowledge base").lower()
        if not norm_path.startswith(allowed_prefix):
            reason = f"VI PHẠM SANDBOX: Đường dẫn '{target_file}' nằm ngoài cây thư mục học phần được phép trên Google Drive G:\\."
            log_audit(f"DENY PreToolUse: {reason}")
            return {"decision": "deny", "reason": reason}

    # 3. Cách ly tệp tạm (%TEMP% Isolation): Cấm tạo file tạm thời/cache trực tiếp trên G:\
    if norm_path.startswith("g:\\"):
        temp_markers = [".tmp", ".aux", ".log", "cache", "scratch"]
        if any(marker in os.path.basename(norm_path) for marker in temp_markers):
            reason = f"CÁCH LY TỆP TẠM: Tệp tạm/cache '{target_file}' bắt buộc phải lưu trong %TEMP%, cấm lưu trên Google Drive G:\\."
            log_audit(f"DENY PreToolUse: {reason}")
            return {"decision": "deny", "reason": reason}

    content = (
        args.get("CodeContent", "") or 
        args.get("ReplacementContent", "") or 
        args.get("Content", "") or 
        args.get("Replacement", "")
    )

    # 4. Kiểm tra kịch bản chế bản PDF (build_monograph_*.py hoặc có BookmarkDocTemplate)
    if content and ("def build_monograph_" in content or "BookmarkDocTemplate" in content):
        # 4a. Cấm tuyệt đối cấu trúc 5 Khối cũ (Anti-Old-Blocks Gate)
        old_block_markers = ["Khối 1:", "Khối 2:", "Khối 3:", "Khối 4:", "KHỐI 1:", "KHỐI 2:"]
        for marker in old_block_markers:
            if marker in content:
                reason = (
                    f"VI PHẠM CẤU TRÚC SƯ PHẠM: Phát hiện cấu trúc cũ '{marker}' trong kịch bản chế bản. "
                    f"Bắt buộc 100% chuyên khảo phải tuân thủ Khung Sư phạm Lũy tiến 5 Giai đoạn "
                    f"(Giai đoạn 1: Giới thiệu khái niệm -> Giai đoạn 2: Ví dụ tối giản -> "
                    f"Giai đoạn 3: Thực hành có hướng dẫn -> Giai đoạn 4: Phân tích biến thể -> "
                    f"Giai đoạn 5: Thử thách tự luyện) theo tài liệu thiết kế AI Agent Giảng Dạy & Sáng Tạo Trên Antigravity.md."
                )
                log_audit(f"DENY PreToolUse: {reason}")
                return {"decision": "deny", "reason": reason}

        # 4b. Kiểm tra phân số gạch chéo trong Paragraph (Luật 14 — Zero-Slash-Fractions Gate)
        p_slash = re.search(
            r"Paragraph\s*\(\s*(?:wrap_math_glyphs\s*\(\s*)?f?['\"][^'\"]*?(?:"
            r"[∂d]\s*[A-Za-z0-9_α-ωΑ-Ω]\s*/\s*[∂d]\s*[A-Za-z0-9_α-ωΑ-Ω]|"
            r"[=≈∝≤≥]\s*[^,;\n<>'\"]{1,30}/|"
            r"/\s*(?:r[²2]|r\^2|ε_?0|ε₀|k_?[Bb]|c[²2]|c\^2|4πε₀|4π)"
            r")",
            content,
            re.IGNORECASE,
        )
        if p_slash:
            matched_sample = p_slash.group(0)[:60].replace('"', "'").replace("\n", " ")
            reason = (
                f"CẤM PHÂN SỐ GẠCH CHÉO (Luật 14): Phát hiện công thức chứa phân số gạch chéo trong Paragraph ({matched_sample}). "
                f"Bắt buộc dùng phân số gạch ngang \\frac{{a}}{{b}} qua LaTeX Mathtext."
            )
            log_audit(f"DENY PreToolUse: {reason}")
            return {"decision": "deny", "reason": reason}

        # 4c. Kiểm tra rò rỉ mã lệnh LaTeX thô vào Paragraph (Luật 15)
        raw_latex_re = re.compile(
            r"Paragraph\s*\([^)]*?(?:\\frac|\\tau|\\eta|\\mu|\\sigma|\\Omega|\\hbar|\\partial|\\infty|\\nabla)\b"
        )
        if raw_latex_re.search(content):
            reason = (
                "RÒ RỈ MÃ LATEX THÔ (Luật 15): Phát hiện lệnh LaTeX thô trong thẻ Paragraph của ReportLab. "
                "100% ký hiệu và biến số trong text phải định dạng bằng thẻ HTML (<i>...</i>, <sub>...</sub>, <sup>...</sup>)."
            )
            log_audit(f"DENY PreToolUse: {reason}")
            return {"decision": "deny", "reason": reason}

        # 4d. Kiểm tra biến số gạch dưới ASCII thô (Regex L3)
        raw_ascii_re = re.compile(
            r"Paragraph\s*\([^)]*?\b(?:E_c\(z\)|N_th|I_th|V_j|BN\^2|t_d|v_g|g_th)\b"
        )
        if raw_ascii_re.search(content):
            reason = (
                "CẤM BIẾN CODE ASCII THÔ: Phát hiện biến số dạng lập trình (E_c(z), N_th, I_th...). "
                "Bắt buộc định dạng chuẩn Typography: <i>E<sub>c</sub></i>(<i>z</i>), <i>N</i><sub>th</sub>, <i>I</i><sub>th</sub>."
            )
            log_audit(f"DENY PreToolUse: {reason}")
            return {"decision": "deny", "reason": reason}

        # 4e. Kiểm tra Arrow Linebreak Gate: Ký hiệu ↳ không được dính liền câu trước
        arrow_inline_re = re.compile(r"[^\n<>]\s*↳")
        if arrow_inline_re.search(content):
            reason = (
                "ARROW LINEBREAK GATE: Ký hiệu chú giải '↳' bắt buộc phải đứng đầu khối hoặc có thẻ <br/> đứng liền trước; "
                "cấm dính dòng trực tiếp với câu văn trước đó."
            )
            log_audit(f"DENY PreToolUse: {reason}")
            return {"decision": "deny", "reason": reason}

        # 4f. Kiểm tra Zero-Raw-HTML-Entities Gate: Cấm thực thể HTML đặt tên thô
        raw_entity_re = re.compile(
            r"&(?:beta|nu|tau|mu|Delta|delta|sigma|ndash|mdash|minus|times|middot|asymp|omega|Omega|alpha|gamma);",
            re.IGNORECASE
        )
        if raw_entity_re.search(content):
            reason = (
                "ZERO-RAW-HTML-ENTITIES GATE: Phát hiện thực thể HTML đặt tên thô (&beta;, &nu;, &tau;, &ndash;...). "
                "100% ký hiệu Hy Lạp và phép toán bắt buộc dùng trực tiếp ký tự Unicode bản địa hoặc giải mã qua wrap_math_glyphs."
            )
            log_audit(f"DENY PreToolUse: {reason}")
            return {"decision": "deny", "reason": reason}

        # 4h. Kiểm tra cấm gộp giai đoạn sư phạm (Luật 16 - Anti-Merged-Stages Gate)
        merged_stages_re = re.compile(r"Giai đoạn\s+\d+\s*(?:&|và|\+)\s*\d+", re.IGNORECASE)
        if merged_stages_re.search(content):
            reason = (
                "CẤM GỘP GIAI ĐOẠN (Luật 16 - Anti-MPT-Compression): Phát hiện hành vi gộp giai đoạn (ví dụ: 'Giai đoạn 2 & 3'). "
                "Bắt buộc 100% mỗi giai đoạn sư phạm phải được triển khai thành từng tiểu mục riêng biệt."
            )
            log_audit(f"DENY PreToolUse: {reason}")
            return {"decision": "deny", "reason": reason}

        # 4g. Kiểm tra mật độ Luận điểm Vi mô (Elastic Depth Gate)
        mpt_matches = re.findall(r'Paragraph\s*\(\s*f?["\']Luận điểm\s*\d+\.\d+\.\d+', content)
        if mpt_matches and len(mpt_matches) < 1:
            reason = (
                "VI PHẠM UNBOUNDED DEPTH: Kịch bản chế bản không chứa Luận điểm Vi mô (MPT) nào. "
                "Quy chuẩn bắt buộc tối thiểu >= 1 MPT cho mỗi chuyên khảo bám sát tài liệu gốc."
            )
            log_audit(f"DENY PreToolUse: {reason}")
            return {"decision": "deny", "reason": reason}

    log_audit(f"ALLOW PreToolUse: {tool_name} -> {target_file}")
    return {"decision": "allow"}

def handle_post_tool_use(payload: dict) -> dict:
    tool_call = payload.get("toolCall", {})
    tool_name = tool_call.get("name", "")
    args = tool_call.get("args", {})
    error = payload.get("error", None)
    
    target_file = (
        args.get("TargetFile", "") or 
        args.get("targetFile", "") or 
        args.get("Path", "") or 
        args.get("path", "")
    )
    
    if error:
        log_audit(f"ERROR PostToolUse: {tool_name} -> {target_file} | Error: {error}")
    else:
        log_audit(f"SUCCESS PostToolUse: {tool_name} -> {target_file}")
        
    return {}

def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "pre"
    try:
        input_data = sys.stdin.read()
        if not input_data.strip():
            payload = {}
        else:
            payload = json.loads(input_data)
    except Exception as e:
        log_audit(f"JSON Parse Error in academic_gate_hook: {e}")
        payload = {}

    if mode == "pre":
        result = handle_pre_tool_use(payload)
    elif mode == "post":
        result = handle_post_tool_use(payload)
    else:
        result = {"decision": "allow"} if mode == "pre" else {}

    sys.stdout.write(json.dumps(result))
    sys.stdout.flush()

if __name__ == "__main__":
    main()
