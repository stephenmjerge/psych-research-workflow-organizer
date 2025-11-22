# Changelog

## [Unreleased]
- Set up the initial skeleton and imported the roadmap narrative.
- Added cross-repo update checklist and Phase 1 roadmap details.
- Added `scripts/run_cross_repo_checklist.py` to automate the weekly sweep.

---

## [v0.1.1] — 2025-11-21
### Added
- `scripts/doctor.py` environment check (Python, required files, writable outputs)
- `docs/quickstart.md` with one-page instructions and troubleshooting
- `--outdir` option for `run_cross_repo_checklist.py` to write summary.json/report.md
- CI workflow (GitHub Actions) to run the checklist on pushes/PRs

### Changed
- README quickstart now highlights doctor and checklist summary output

### Fixed
- N/A
