#!/usr/bin/env python3
"""Guided cross-repo checklist runner.

This script mirrors `checklists/cross-repo-update.md` and prints reminders for
any steps that need attention. Optionally writes a summary to disk for review.
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LAB_ROOT = ROOT.parent.parent
LAUNCHPAD = LAB_ROOT / "meta" / "launchpad"
PORTFOLIO = LAB_ROOT / "docs" / "PortfolioHub.md"
TIMELINE = LAB_ROOT / "meta" / "MASTER_TIMELINE.md"

STEPS = [
    (
        "LAUNCHPAD Sweep",
        [
            (LAUNCHPAD / "daily-tasks.md", "Daily tasks present"),
            (LAUNCHPAD / "next-actions.md", "Next actions populated"),
            (LAUNCHPAD / "project-priorities.md", "Project priorities set"),
        ],
    ),
    (
        "ROADMAP + README Sync",
        [
            (ROOT.parent / "reinforcement-learning-simulation" / "ROADMAP.md", "RL-Sim roadmap exists"),
            (ROOT.parent / "psych-research-workflow-organizer" / "ROADMAP.md", "Workflow Organizer roadmap exists"),
        ],
    ),
    (
        "PortfolioHub / Master Docs",
        [
            (PORTFOLIO, "PortfolioHub present"),
            (TIMELINE, "MASTER_TIMELINE present"),
        ],
    ),
]


def main() -> None:
    parser = argparse.ArgumentParser(description="Cross-Repo Checklist (dry run)")
    parser.add_argument("--outdir", type=Path, help="Write summary.json/report.md to this directory")
    args = parser.parse_args()

    print("Cross-Repo Checklist (dry run)\n-------------------------------")
    results: list[dict[str, str]] = []
    for section, files in STEPS:
        print(f"\n{section}:")
        for path, description in files:
            status = "OK" if path.exists() else "MISSING"
            print(f"  - {description}: {status} ({path})")
            results.append({
                "section": section,
                "description": description,
                "path": str(path),
                "status": status,
            })

    print("\nNext steps: run repo-specific tests and commit/push changes as needed.")
    if args.outdir:
        args.outdir.mkdir(parents=True, exist_ok=True)
        summary_path = args.outdir / "summary.json"
        summary_path.write_text(json.dumps(results, indent=2), encoding="utf-8")
        report_lines = ["# Cross-Repo Checklist Summary", "", f"Generated: {datetime.utcnow().isoformat()}Z", ""]
        for entry in results:
            report_lines.append(f"- [{entry['status']}] {entry['description']} ({entry['path']})")
        (args.outdir / "report.md").write_text("\n".join(report_lines), encoding="utf-8")
        print(f"[PRWO] Wrote summary to {summary_path}")


if __name__ == "__main__":
    main()
