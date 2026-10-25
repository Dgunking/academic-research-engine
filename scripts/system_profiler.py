# -*- coding: utf-8 -*-
r"""
==============================================================================
ACADEMIC RESEARCH ENGINE - HARDWARE & ENVIRONMENT PROFILER
==============================================================================
Scans local host hardware (CPU, RAM, GPU VRAM) and software prerequisites
(Python, Typst, LaTeX, ReportLab, DejaVu Fonts). Automatically initializes
or optimizes .env parameters (MAX_CONCURRENCY, MEMORY_BUFFER_MB).
"""

import os
import sys
import platform
import shutil
import subprocess
import ctypes
from pathlib import Path

# Ensure UTF-8 output on Windows terminal
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


def get_ram_info():
    """Retrieve total and available RAM in GB across Windows, Linux, and macOS."""
    total_gb = 0.0
    avail_gb = 0.0
    system = platform.system()

    try:
        if system == "Windows":
            class MEMORYSTATUSEX(ctypes.Structure):
                _fields_ = [
                    ("dwLength", ctypes.c_ulong),
                    ("dwMemoryLoad", ctypes.c_ulong),
                    ("ullTotalPhys", ctypes.c_ulonglong),
                    ("ullAvailPhys", ctypes.c_ulonglong),
                    ("ullTotalPageFile", ctypes.c_ulonglong),
                    ("ullAvailPageFile", ctypes.c_ulonglong),
                    ("ullTotalVirtual", ctypes.c_ulonglong),
                    ("ullAvailVirtual", ctypes.c_ulonglong),
                    ("ullAvailExtendedVirtual", ctypes.c_ulonglong),
                ]

            stat = MEMORYSTATUSEX()
            stat.dwLength = ctypes.sizeof(MEMORYSTATUSEX)
            if ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(stat)):
                total_gb = stat.ullTotalPhys / (1024 ** 3)
                avail_gb = stat.ullAvailPhys / (1024 ** 3)
        elif system == "Linux":
            with open("/proc/meminfo", "r") as f:
                lines = f.readlines()
            mem_dict = {}
            for line in lines:
                parts = line.split(":")
                if len(parts) == 2:
                    mem_dict[parts[0].strip()] = parts[1].strip()
            total_kb = float(mem_dict.get("MemTotal", "0 kB").split()[0])
            avail_kb = float(mem_dict.get("MemAvailable", "0 kB").split()[0])
            total_gb = total_kb / (1024 ** 2)
            avail_gb = avail_kb / (1024 ** 2)
        elif system == "Darwin":
            cmd = ["sysctl", "-n", "hw.memsize"]
            total_bytes = float(subprocess.check_output(cmd).decode().strip())
            total_gb = total_bytes / (1024 ** 3)
            avail_gb = total_gb * 0.5  # estimate for macOS
    except Exception:
        total_gb = 8.0
        avail_gb = 4.0

    return round(total_gb, 2), round(avail_gb, 2)


def get_gpu_info():
    """Query NVIDIA GPU name and VRAM via nvidia-smi if available."""
    try:
        cmd = ["nvidia-smi", "--query-gpu=name,memory.total,memory.free", "--format=csv,noheader,nounits"]
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
        if result.returncode == 0 and result.stdout.strip():
            lines = result.stdout.strip().split("\n")
            gpus = []
            for line in lines:
                parts = [p.strip() for p in line.split(",")]
                if len(parts) >= 3:
                    gpus.append({
                        "name": parts[0],
                        "vram_total_mb": float(parts[1]),
                        "vram_free_mb": float(parts[2]),
                    })
            return gpus
    except Exception:
        pass
    return []


def check_tool(cmd, version_arg="--version"):
    """Check if an executable is in PATH and return its version string."""
    tool_path = shutil.which(cmd)
    if not tool_path:
        return False, "Not Found in PATH"
    try:
        proc = subprocess.run([tool_path, version_arg], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
        out = (proc.stdout or proc.stderr).strip().split("\n")[0]
        return True, f"Found ({out})"
    except Exception as e:
        return True, f"Found at {tool_path} (could not verify version: {e})"


def check_python_dependencies():
    """Verify core Python packages required by the academic engine."""
    required = {
        "reportlab": "ReportLab (DejaVu PDF Publishing Engine)",
        "matplotlib": "Matplotlib (ZT-GVLE Analytical Graphing)",
        "numpy": "NumPy (Numerical Modeling)",
        "sympy": "SymPy (CAS Formal Equation Verification)",
        "pydantic": "Pydantic v2 (Data Contracts)",
        "yaml": "PyYAML (Nomenclature & Configuration)",
    }
    status = {}
    for pkg, desc in required.items():
        try:
            mod = __import__(pkg)
            version = getattr(mod, "__version__", "installed")
            status[desc] = (True, f"v{version}")
        except ImportError:
            status[desc] = (False, "Missing (run: pip install -r requirements.txt)")
    return status


def check_dejavu_fonts():
    """Verify availability of DejaVu Sans fonts in Matplotlib or system."""
    try:
        import matplotlib.font_manager as fm
        dejavu = [f.name for f in fm.fontManager.ttflist if "dejavu" in f.name.lower()]
        if dejavu:
            return True, f"Available ({len(set(dejavu))} styles detected)"
    except Exception:
        pass
    return False, "DejaVu font not found. Please install fonts-dejavu or DejaVuSans.ttf"


def generate_optimized_env(total_ram_gb, cpu_cores):
    """Generate or update .env file with hardware-tailored performance parameters."""
    root_dir = Path(__file__).resolve().parent.parent
    env_file = root_dir / ".env"
    env_example = root_dir / ".env.example"

    # Calculate optimal parameters
    rec_concurrency = max(1, min(cpu_cores - 1, int(total_ram_gb // 2)))
    rec_buffer_mb = max(1024, min(8192, int(total_ram_gb * 1024 * 0.25)))

    content = ""
    if env_file.exists():
        content = env_file.read_text(encoding="utf-8")
    elif env_example.exists():
        content = env_example.read_text(encoding="utf-8")
    else:
        content = (
            f"MAX_CONCURRENCY={rec_concurrency}\n"
            f"MEMORY_BUFFER_MB={rec_buffer_mb}\n"
        )

    # Update or append parameters
    import re
    if re.search(r"^MAX_CONCURRENCY=.*$", content, flags=re.MULTILINE):
        content = re.sub(r"^MAX_CONCURRENCY=.*$", f"MAX_CONCURRENCY={rec_concurrency}", content, flags=re.MULTILINE)
    else:
        content += f"\nMAX_CONCURRENCY={rec_concurrency}"

    if re.search(r"^MEMORY_BUFFER_MB=.*$", content, flags=re.MULTILINE):
        content = re.sub(r"^MEMORY_BUFFER_MB=.*$", f"MEMORY_BUFFER_MB={rec_buffer_mb}", content, flags=re.MULTILINE)
    else:
        content += f"\nMEMORY_BUFFER_MB={rec_buffer_mb}"

    env_file.write_text(content, encoding="utf-8")
    return rec_concurrency, rec_buffer_mb, env_file


def run_profiler(create_env=True):
    """Execute complete system profiling and output report."""
    total_ram_gb, avail_ram_gb = get_ram_info()
    cpu_cores = os.cpu_count() or 4
    gpus = get_gpu_info()

    print("=" * 76)
    print(" ACADEMIC RESEARCH ENGINE - SYSTEM HARDWARE & PREREQUISITES PROFILER")
    print("=" * 76)

    # 1. Hardware Summary
    print("\n[1] HOST HARDWARE ARCHITECTURE:")
    print(f"  • Operating System   : {platform.system()} {platform.release()} ({platform.architecture()[0]})")
    print(f"  • CPU Processor      : {platform.processor() or 'Standard Architecture'}")
    print(f"  • CPU Logical Cores  : {cpu_cores} threads")
    print(f"  • System RAM         : Total {total_ram_gb:.1f} GB (Available: {avail_ram_gb:.1f} GB)")

    if gpus:
        for idx, g in enumerate(gpus):
            print(f"  • GPU [{idx}]           : {g['name']} ({g['vram_total_mb'] / 1024:.1f} GB VRAM, {g['vram_free_mb'] / 1024:.1f} GB Free)")
    else:
        print("  • GPU Acceleration   : No NVIDIA CUDA GPU detected (Analytical CPU Mode active)")

    # 2. Software Prerequisites
    print("\n[2] COMPILERS & EXTERNAL TOOLS:")
    py_ver = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
    py_ok = sys.version_info >= (3, 10)
    print(f"  • Python Interpreter : v{py_ver} [{'PASS' if py_ok else 'FAIL: Python >= 3.10 required'}]")

    typst_ok, typst_desc = check_tool("typst")
    print(f"  • Typst Compiler     : {typst_desc}")

    latex_ok, latex_desc = check_tool("latex", version_arg="-version")
    print(f"  • LaTeX Engine       : {latex_desc}")

    dvipng_ok, dvipng_desc = check_tool("dvipng", version_arg="-version")
    print(f"  • dvipng (DPI Render): {dvipng_desc}")

    # 3. Python Package Status
    print("\n[3] PYTHON SCIENTIFIC ENGINE LIBRARIES:")
    dep_status = check_python_dependencies()
    for name, (ok, detail) in dep_status.items():
        status_tag = "[PASS]" if ok else "[FAIL]"
        print(f"  {status_tag:7} {name:42} : {detail}")

    font_ok, font_desc = check_dejavu_fonts()
    print(f"  {'[PASS]' if font_ok else '[WARN]':7} {'DejaVu Typography Engine':42} : {font_desc}")

    # 4. Hardware Optimization & .env Generation
    if create_env:
        concurrency, mem_mb, env_path = generate_optimized_env(total_ram_gb, cpu_cores)
        print("\n[4] AUTONOMOUS CONCURRENCY & MEMORY CALIBRATION:")
        print(f"  • Calibrated MAX_CONCURRENCY : {concurrency} worker threads")
        print(f"  • Calibrated MEMORY_BUFFER_MB: {mem_mb} MB RAM allocation")
        print(f"  • Configuration saved to     : {env_path}")

    print("\n" + "=" * 76)
    all_ok = py_ok and all(ok for ok, _ in dep_status.values())
    if all_ok:
        print("  STATUS: SYSTEM HARDWARE & LIBRARIES FULLY COMPLIANT WITH RELEASE CRITERIA.")
    else:
        print("  STATUS: PREREQUISITES INCOMPLETE. Please review missing packages above.")
    print("=" * 76 + "\n")
    return all_ok


if __name__ == "__main__":
    success = run_profiler(create_env=True)
    sys.exit(0 if success else 1)
