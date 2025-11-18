# Cross-Repo Update Checklist

Use this weekly (or before major pushes) to keep every repo + planning doc in sync.

1. **LAUNCHPAD Sweep** (`meta/launchpad/`)
   - [ ] Confirm `meta/launchpad/daily-tasks.md` and `meta/launchpad/next-actions.md` reference the repos you intend to move.
   - [ ] Update `meta/launchpad/project-priorities.md` with the primary/secondary repo names and expected outcomes.
2. **ROADMAP + README Sync**
   - [ ] For each active repo, highlight what shipped this week inside its `ROADMAP.md` and `README.md` (Current Prototype / Figure Workflow, etc.).
   - [ ] Ensure `CHANGELOG.md` has an `[Unreleased]` entry capturing the same work so tagging is easy later.
3. **PortfolioHub / Master Docs**
   - [ ] Add links to any new repos or artifacts (figures, scripts) in `docs/PortfolioHub.md`.
   - [ ] Reflect major milestones in `meta/MASTER_TIMELINE.md` and `meta/PLAYBOOK.md` if strategy shifted.
4. **Publishing Prep**
   - [ ] Run the repo-specific test or lint commands (see each `prompts/codex-guidance.md`).
   - [ ] Stage + commit changes, push to GitHub, and copy the commit/PR URLs back into `next-actions.md` or `ISSUES.md` as proof of completion.
5. **Review + Debrief**
   - [ ] Fill in `meta/launchpad/weekly-review.md` with what shipped and what felt stuck.
   - [ ] Create new tickets in the relevant `ISSUES.md` files for any follow-up work discovered during the sweep.

Owner: Stephen (for now). Revisit after onboarding collaborators.
Cadence: Weekly review or before publishing multiple repos.
