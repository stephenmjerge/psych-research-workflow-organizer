# Workflow Organizer

Glue repo containing automations, checklists, and shared assets that keep the other labs in sync. Expect:

- Scripts that update dashboards and aggregate LAUNCHPAD metrics.
- Templates/SOPs for documenting experiments and decisions.
- Cross-repo helpers (e.g., shared GitHub Actions, data schemas).

## Quickstart
1. Read `ROADMAP.md` to see which coordination task is active.
2. Run the checklist script before every publish:
   ```bash
   python scripts/run_cross_repo_checklist.py
   ```
   It highlights whether `LAUNCHPAD`, `PortfolioHub.md`, or any repo roadmap is missing before you commit.
3. Work through `checklists/cross-repo-update.md` to capture the manual steps (update PortfolioHub, MASTER_TIMELINE, etc.).

Use LAUNCHPAD for day-to-day tasks; this repo is the glue that keeps those files aligned across every project.

## Files
- `checklists/cross-repo-update.md`: Weekly sweep covering LAUNCHPAD, PortfolioHub, README/ROADMAP sync, and publishing prep.
- `scripts/run_cross_repo_checklist.py`: Dry-run version of the checklist—no edits, just status output so you know what to fix.
- `prompts/codex-guidance.md`: Reminders for contributors (stay lightweight, no secrets, prefer bash/python scripts).

More SOPs (e.g., dashboard refresh, OSF upload flow) will land here as Phase 1 of the roadmap progresses.
