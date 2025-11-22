# PRWO Quickstart (Ops/Clinicians)

## 1) Run the checklist (dry run)
```bash
python scripts/run_cross_repo_checklist.py --outdir outputs/checklist
```
Shows which files (PortfolioHub, MASTER_TIMELINE, roadmaps) need updates. No edits are made.

## 2) Environment check
```bash
python scripts/doctor.py
```
Verifies Python version, required files, and writable `outputs/`.

## 3) Manual steps
Work through `checklists/cross-repo-update.md` to update PortfolioHub, MASTER_TIMELINE, and README/ROADMAP syncs.

## Troubleshooting
- Missing files: recreate from the templates or pull the latest main branch.
- Locked-down machines: set `PYTHONPATH=.` and run from repo root.
- Permissions: ensure you can write to `outputs/`; doctor will flag issues.
