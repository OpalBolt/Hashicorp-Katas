---
status: proposed
---

# Allow starters and warm-ups after the foundations slices

Slices 01 and later had no starter material, so learners copied from the
Terraform Registry and learned little. We allow Starters (Scaffolds and Fix-it
starters) in any slice, and require a Warm-up before tasks that introduce a new
skill. We still ban working examples after `00`, because learners run them and
skip. This replaces the rule "scaffolds only in foundations slices".

## Consequences

- A Warm-up uses a different mini-problem from its Task, so its result cannot be
  pasted into the graded Task.
- The grading contract, the grader skill, and the slice template must change
  together.
- This is an experiment on a branch. Revert by reverting commits.
