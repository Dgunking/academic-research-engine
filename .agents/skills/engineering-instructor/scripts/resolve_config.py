"""
resolve_config.py — Thuật toán hợp nhất sâu (Deep-Merge) cho Configurable Agent Skills trên Antigravity.
Hợp nhất config.default.yaml (Khung sư phạm chuẩn) với .agents/skills.config.yaml (Cấu hình dự án cụ thể).
"""
import os
import sys
import json

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

try:
    import yaml
except ImportError:
    yaml = None

def deep_merge(default: dict, override: dict) -> dict:
    """
    Thuật toán hợp nhất sâu:
    - Dictionary: gộp đệ quy theo từng khóa.
    - List và giá trị vô hướng: thay thế toàn bộ bằng giá trị ghi đè của dự án.
    """
    result = dict(default)
    for key, value in override.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = value
    return result

def load_yaml(file_path: str) -> dict:
    if not os.path.exists(file_path):
        return {}
    with open(file_path, "r", encoding="utf-8") as f:
        if yaml:
            return yaml.safe_load(f) or {}
        # Dự phòng phân tích cơ bản nếu thiếu pyyaml
        return json.load(f)

def get_merged_config(skill_dir: str = None, workspace_dir: str = None) -> dict:
    if not skill_dir:
        # __file__ is in .agents/skills/engineering-instructor/scripts/
        script_dir = os.path.dirname(os.path.abspath(__file__))
        skill_dir = os.path.abspath(os.path.join(script_dir, ".."))
    if not workspace_dir:
        workspace_dir = os.path.abspath(os.path.join(skill_dir, "..", "..", ".."))

    default_config_path = os.path.join(skill_dir, "config.default.yaml")
    # Check both <workspace>/.agents/skills.config.yaml and .agents/skills.config.yaml
    project_config_path = os.path.join(workspace_dir, ".agents", "skills.config.yaml")
    if not os.path.exists(project_config_path):
        # Thử fallback lên cấp thư mục cha của skills
        alt_path = os.path.abspath(os.path.join(skill_dir, "..", "..", "skills.config.yaml"))
        if os.path.exists(alt_path):
            project_config_path = alt_path

    default_cfg = load_yaml(default_config_path)
    project_cfg = load_yaml(project_config_path)

    return deep_merge(default_cfg, project_cfg)

def main():
    if "--help" in sys.argv:
        print("Usage: python resolve_config.py [--json] [--yaml]")
        print("Trộn sâu config.default.yaml của kỹ năng với .agents/skills.config.yaml của dự án.")
        return

    merged = get_merged_config()
    
    if "--yaml" in sys.argv and yaml:
        print(yaml.dump(merged, allow_unicode=True, default_flow_style=False))
    else:
        print(json.dumps(merged, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
