#!/usr/bin/env python3
"""Guided cross-repo checklist runner.

This script mirrors `checklists/cross-repo-update.md` and prints reminders for
any steps that need attention. It is intentionally lightweight so it can run in a
plain Python environment without extra dependencies.
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LAUNCHPAD = ROOT.parent / "LAUNCHPAD"
PORTFOLIO = ROOT.parent / "PortfolioHub.md"
TIMELINE = ROOT.parent / "MASTER_TIMELINE.md"

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
    print("Cross-Repo Checklist (dry run)\n-------------------------------")
    for section, files in STEPS:
        print(f"\n{section}:")
        for path, description in files:
            status = "OK" if path.exists() else "MISSING"
            print(f"  - {description}: {status} ({path})")

    print("\nNext steps: run repo-specific tests and commit/push changes as needed.")


if __name__ == "__main__":
    main()
