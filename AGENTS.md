# AGENTS.md

## Project overview
This is a Terraform and Vault learning guide built with Markdown, MkDocs Material, mise, and pinned Terraform, Vault, AWS CLI, and Python tools.

## Commands
- Build: `mise run build`
- Test: `mise run build`
- Lint: `mise run build`
- Dev: `mise run serve`

## Artifacts
- Specs/tickets/maps: `.scratch/` (local Markdown, untracked)
- Grading a track, slice, or capstone: load `.agents/skills/grader/SKILL.md`.

## Boundaries
### ✅ Always
- Read `docs/grading.md` before changing the grading contract or learner evidence layout.
- Keep learner tasks free of solution code, solution steps, and prewritten answers.
- Keep generated site output out of source changes.

### ⚠️ Ask first
- Change the slice order, prerequisites, or grading contract.
- Add dependencies or change the mise and container setup.

### 🚫 Never
- Commit secrets or `.env` files.
- Force push to main.
- Duplicate grading instructions from `docs/grading.md` here.

## Code style
Self-documenting code, KISS and human readable above all. Linter is the source of truth (gofmt/golangci-lint, ruff/black, shellcheck). No comments unless critically necessary — to explain a non-obvious why, a workaround, or a hidden risk.
