#!/usr/bin/env python3
"""Environment checks for PRWO."""
from __future__ import annotations
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LAB_ROOT = ROOT.parent.parent
REQUIRED = [
    ROOT / "ROADMAP.md",
    ROOT / "checklists" / "cross-repo-update.md",
    LAB_ROOT / "docs" / "PortfolioHub.md",
    LAB_ROOT / "meta" / "MASTER_TIMELINE.md",
]


def main() -> None:
    checks = []
    checks.append(("python>=3.9", sys.version_info >= (3, 9), sys.version))
    for path in REQUIRED:
        checks.append((f"exists: {path.name}", path.exists(), str(path)))
    outdir = ROOT / "outputs"
    try:
        outdir.mkdir(parents=True, exist_ok=True)
        test_file = outdir / ".doctor_write_test"
        test_file.write_text("ok", encoding="utf-8")
        test_file.unlink()
        checks.append(("outdir writable", True, str(outdir)))
    except Exception as exc:  # pragma: no cover
        checks.append(("outdir writable", False, str(exc)))
    passed = True
    for name, ok, note in checks:
        status = "OK" if ok else "FAIL"
        print(f"[{status}] {name} ({note})")
        passed = passed and ok
    if not passed:
        sys.exit("[PRWO] Doctor checks failed. See items marked FAIL.")
    print("[PRWO] Doctor checks passed.")


if __name__ == "__main__":
    main()
