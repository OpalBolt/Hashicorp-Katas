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
    00-block-types/
    01-workflow/
      code/
      evidence/
        task-01-init.txt
        task-01-plan.txt
      answers.md
    02-state/
    03-modules/
  vault/
    00-foundations/
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

Save command output, logs, screenshots, and written findings in `evidence/`.
No template, per-check write-up, or file conversion is required.
Use descriptive filenames with the task number, such as `task-01-init.txt`
or `task-02-before.json`. One file can support several checks.

Capture output with `>` or `tee`, or move an existing capture into `evidence/`.
These examples show capture syntax only. Replace `your-check` with your own
command. Run from the slice's submission folder after creating `evidence/`.

```bash
your-check > evidence/task-01-check.txt 2>&1
your-check 2>&1 | tee evidence/task-01-check.txt
```

These are alternatives. `>` and `tee` overwrite an existing file.
Use distinct filenames for before and after results.
`2>&1` includes error output. Check the original command's exit status.
In Bash, `set -o pipefail` prevents `tee` from hiding a command failure.

Keep enough context to identify the command, working folder, and relevant
environment. Add a short note only when the capture does not show that context.
The grader maps files to the task's checks. You do not need to repeat each
`Done when` line.

Executable tasks require evidence from your own run.
For text-only tasks, the source artifact itself is valid evidence, including a
diagram in Markdown. Keep source files in `code/` when the task requires them.
Existing `task-NN.md` write-ups remain valid, but they are optional.

Review output before you capture or share it. Redact secrets and any values
the task excludes. Keep raw sensitive captures outside the repository.
Do not submit raw state, saved plans, tokens, or private keys.

## Explain answers

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

## Use the grader

The portable skill lives at `.agents/skills/grader/SKILL.md`.
Open an AI harness with access to this repository and your submission files.
If the harness discovers `.agents/skills/`, ask it to use `grader`.
Otherwise, ask it to read the skill file directly and follow its instructions.
Automatic discovery depends on the harness.

For example:

```text
Read .agents/skills/grader/SKILL.md and follow it.
Grade the terraform track in submissions/terraform/.
```

Replace `terraform` with `vault`, `terraform-vault`, or `adversary`.
You can also request one slice, such as `terraform/01-workflow`, or the capstone.
Track grading covers the numbered slices listed in the guide, not preview pages.
The grader reports missing work instead of silently skipping it.
It reports results in the conversation and leaves your submission unchanged.

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
