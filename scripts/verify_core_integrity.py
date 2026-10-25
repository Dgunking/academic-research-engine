# -*- coding: utf-8 -*-
r"""
==============================================================================
ACADEMIC RESEARCH ENGINE - CORE INTEGRITY & ANTI-TAMPERING GUARD
==============================================================================
Calculates, locks, and verifies SHA-256 checksums of core system components:
- agents/ (Central Orchestration Kernel, Authors, Artists, Gatekeeper)
- .agents/rules/ (Supreme Mandates, Invariant Algorithms, Behavior Rules)
- .agents/schemas/ (Pydantic v2 Data Contracts)
- gemini-spark/instructions.txt (Gemini Spark System Instructions)
- scripts/ core algorithmic engines (*_engine.py, pillar_equation_utils.py)

If any unauthorized modification or tampering is detected, the engine halts
immediately with exit code 1 to protect algorithmic rigor and academic fidelity.
"""

import os
import sys
import hashlib
from pathlib import Path

# Ensure UTF-8 output
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

ROOT_DIR = Path(__file__).resolve().parent.parent
HASH_FILE = ROOT_DIR / ".agents" / "hashes" / "distribution_core.sha256"

# Core assets subject to cryptographic anti-tampering verification
CORE_TARGET_PATTERNS = [
    ROOT_DIR / "gemini-spark" / "instructions.txt",
    ROOT_DIR / "gemini-spark" / "01_Co_So_Du_Lieu_Ban_Dan_Va_Hang_So_CODATA_300K.md",
    ROOT_DIR / "gemini-spark" / "02_Chuan_Danh_Phap_Thuat_Ngu_ATCC_Song_Ngu.md",
]


def collect_target_files():
    """Discover all protected source files across core directories."""
    targets = []

    # 1. Agents directory
    agents_dir = ROOT_DIR / "agents"
    if agents_dir.exists():
        for p in agents_dir.rglob("*.py"):
            if "__pycache__" not in p.parts:
                targets.append(p)

    # 2. .agents/rules
    rules_dir = ROOT_DIR / ".agents" / "rules"
    if rules_dir.exists():
        for p in rules_dir.rglob("*.md"):
            targets.append(p)

    # 3. .agents/schemas
    schemas_dir = ROOT_DIR / ".agents" / "schemas"
    if schemas_dir.exists():
        for p in schemas_dir.rglob("*.py"):
            if "__pycache__" not in p.parts:
                targets.append(p)

    # 4. Core scripts
    scripts_dir = ROOT_DIR / "scripts"
    if scripts_dir.exists():
        for p in scripts_dir.glob("*_engine.py"):
            targets.append(p)
        for extra in ["pillar_equation_utils.py", "system_profiler.py", "docx_audit_generator.py"]:
            ep = scripts_dir / extra
            if ep.exists():
                targets.append(ep)

    # 5. Gemini Spark
    for p in CORE_TARGET_PATTERNS:
        if p.exists():
            targets.append(p)

    return sorted(list(set(targets)))


def compute_sha256(file_path: Path) -> str:
    """Compute SHA-256 hexadecimal digest for a given file with normalized line endings."""
    content = file_path.read_bytes()
    # Normalize CRLF to LF for deterministic hashes across operating systems
    normalized = content.replace(b"\r\n", b"\n")
    return hashlib.sha256(normalized).hexdigest()


def generate_distribution_hashes():
    """Lock all target files into .agents/hashes/distribution_core.sha256."""
    targets = collect_target_files()
    HASH_FILE.parent.mkdir(parents=True, exist_ok=True)

    lines = []
    lines.append("# ACADEMIC RESEARCH ENGINE - CORE INTEGRITY HASH MANIFEST")
    lines.append(f"# Total Protected Assets: {len(targets)}")
    lines.append("# Format: <SHA-256>  <Relative_Path>")
    lines.append("")

    for target in targets:
        rel_path = target.relative_to(ROOT_DIR).as_posix()
        digest = compute_sha256(target)
        lines.append(f"{digest}  {rel_path}")

    HASH_FILE.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"[OK] Locked {len(targets)} core assets into {HASH_FILE}")
    return len(targets)


def verify_core_integrity(strict: bool = True) -> bool:
    """
    Verify core components against the locked SHA-256 distribution manifest.
    Halt system execution if tampering or modification is detected.
    """
    if not HASH_FILE.exists():
        print(f"[SECURITY ALERT] Core hash manifest missing: {HASH_FILE}")
        if strict:
            sys.exit(1)
        return False

    manifest_text = HASH_FILE.read_text(encoding="utf-8")
    expected = {}
    for line in manifest_text.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split(maxsplit=1)
        if len(parts) == 2:
            expected[parts[1].strip()] = parts[0].strip()

    tampered = []
    missing = []
    verified_count = 0

    for rel_path_str, expected_hash in expected.items():
        file_path = ROOT_DIR / Path(rel_path_str)
        if not file_path.exists():
            missing.append(rel_path_str)
            continue

        actual_hash = compute_sha256(file_path)
        if actual_hash != expected_hash:
            tampered.append((rel_path_str, expected_hash, actual_hash))
        else:
            verified_count += 1

    if tampered or missing:
        print("\n" + "=" * 76)
        print(" [CRITICAL SECURITY BREACH] CORE ALGORITHMIC INTEGRITY VIOLATION")
        print("=" * 76)
        if missing:
            print(f"Missing Core Assets ({len(missing)} files):")
            for m in missing:
                print(f"  [-] {m}")
        if tampered:
            print(f"Tampered / Modified Core Assets ({len(tampered)} files):")
            for rel, exp, act in tampered:
                print(f"  [!] {rel}")
                print(f"      Expected : {exp}")
                print(f"      Actual   : {act}")
        print("=" * 76)
        print("Self-termination triggered: Core algorithm safeguards cannot be bypassed.")
        print("Please restore unmodified distribution files or re-run with official credentials.")
        print("=" * 76 + "\n")
        if strict:
            sys.exit(1)
        return False

    print(f"[PASS] Core Integrity Verified: 100% of {verified_count} core components match official cryptographic signature.")
    return True


if __name__ == "__main__":
    if "--generate" in sys.argv or "--lock" in sys.argv:
        generate_distribution_hashes()
    else:
        success = verify_core_integrity(strict=True)
        sys.exit(0 if success else 1)
