---
icon: material/clipboard-check-outline
---

# How grading works

The grading skill checks your work against the slice file. It checks both the tasks and your written Explain answers.
It uses your files and runs checks when it can.

## Submission layout

Use one folder for each slice:

```text
submissions/
  terraform/
    01-workflow/
      code/
      evidence/
        task-01.md
        task-02.md
      answers.md
    02-state/
    03-modules/
  vault/
    01-vault-first-contact/
    02-vault-server/
    03-dynamic-secrets/
    04-pki-transit/
  terraform-vault/
    01-terraform-vault/
    02-ci/
  adversary/
    01-advisory/
```

Copy the previous slice's `code/` into the new slice, then extend it.
Keep each slice's evidence and answers in its own folder.
Slices that start a new tool track can start with an empty `code/` folder.

## Foundations scaffolds

A scaffold is an intentionally incomplete starting structure with blanks for the
learner to complete. Scaffolds are allowed only in foundations slices (`00`).
They must not provide the completed answer. Slices `01` and later contain no
solutions or scaffolds.

For a scaffolded task, `Done when` and `Evidence` apply to the learner's
completed artifact, not merely to filled blanks. The grader checks every
`Done when` line and Evidence requirement. Evidence may come from the
learner's own work or from an execution when the task can be run; source
artifacts are valid evidence for tasks that are checked as text, such as a
diagram in Markdown.

## Evidence format

Create one Markdown file per task at `evidence/task-NN.md`.
Use the task number from the slice file. Keep the sections in this order:

```markdown
# Task NN evidence

## Done when 1
- Result:
- Source:

## Done when 2
- Result:
- Source:

## Notes
```

Write the observed result under `Result`.
Point `Source` to a command, output file, log, or screenshot.
Use one `Done when` section for every line in the task.
Evidence must come from your own run. Do not paste real secrets or tokens.

Write one answer for each question in `answers.md`:

```markdown
# Explain

## Explain 1
Answer:

## Explain 2
Answer:
```

## Grading checklist

The grading skill:

1. Reads the slice file, submission folder, and relevant source files.
2. Checks every `Done when` line against evidence.
3. Runs safe checks when the environment supports them.
4. Reports each task as `PASS`, `PARTIAL`, or `FAIL`.
5. Names the exact unmet line and explains why it is unmet.
6. Judges each Explain answer as `solid`, `shallow`, or `wrong`.
7. States what an incomplete Explain answer is missing.

Evidence does not turn a failed check into a pass.
The grader may reject evidence that does not prove the claim.

## Hints

For a failed task, the grading skill gives exactly one hint.
The hint names one concept to study. It does not give a fix, a command, or solution code.
If you still cannot explain the result, redo the task.

Ask the grading skill to grade only. Asking it to write a solution removes the learning goal.

## Grades

| Grade | Meaning |
|---|---|
| PASS | Every `Done when` line is true and supported by evidence. |
| PARTIAL | Some lines are true. Other lines are missing or unproven. |
| FAIL | The task is not met, or its evidence does not prove the result. |
