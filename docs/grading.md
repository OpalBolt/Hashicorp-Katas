---
icon: material/clipboard-check-outline
---

# How grading works

The grading skill checks your work against the slice file, including its tasks
and Explain questions. It reads your source artifacts and run captures without
running your configuration.

## Submission layout

Use one folder for each slice:

```text
submissions/
  terraform/
    00-block-types/
    01-workflow/
      code/
      evidence/
        task-01-plan.txt
        task-01-resources.txt
      warmup/
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
Keep each slice's artifacts, run captures, and answers in its own folder.
Keep final code and authored task artifacts, including Markdown findings,
in `code/`. Keep only transient run captures in `evidence/`.
Slices that start a new tool track can start with an empty `code/` folder.

Warm-up artifacts use the provisional path
`submissions/<track>/<slice>/warmup/`. Keep that folder separate from the
graded task's `code/` and `evidence/` folders. Do not use warm-up output as
graded-task code or evidence.

## Starters and warm-ups

A Starter is material the guide provides before a task. It never satisfies a
`Done when` on its own. The learner must author the required result and provide
the evidence that the task asks for.

A Starter is either:

- a **Scaffold**, an intentionally incomplete structure with blanks for the
  learner to author
- a **Fix-it starter**, a deliberately broken structure for the learner to
  repair

Each Scaffold blank must have a corresponding `Done when` line. A blank can be
a value, a block, or a whole file.

Starters are allowed in any slice. They must not provide the completed answer.
Slices after the foundations slice (`00`) must not include working examples.
A working example is not a Starter.

A slice has one required Warm-up. It comes before the graded Task that
introduces the slice's main new skill. A slice that teaches two unrelated
skills can have a second Warm-up. The Warm-up uses a Starter and a different
mini-problem. It has its own concise `Done when` and its own evidence. Grade
the Warm-up and the graded Task as separate units. The graded Task keeps its
existing task number.

For a Starter task or Warm-up, `Done when` and `Evidence` apply to the learner's
completed artifact, not merely to filled blanks or supplied material. The
grader checks every requirement against the relevant artifacts and captures.
For text-only tasks, the authored artifact itself can prove the requirement,
such as a diagram in Markdown.

## Evidence format

Save command output, logs, and screenshots from a run in `evidence/`.
No template, per-check write-up, or file conversion is required.
Use descriptive filenames with the task number, such as `task-01-plan.txt`
or `task-02-before.json`. One capture can support several checks.
Keep authored findings and other task artifacts in `code/`.

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
environment. Put any context the capture omits in a short Markdown file in
`code/`. The grader maps files to the task's checks. You do not need to repeat
each `Done when` line.

Executable tasks require captures from your own run when the task asks for
runtime proof. The grader reads source and authored artifacts in `code/` first.
It uses `evidence/` to verify results that source files cannot prove, such as
created resources, a denied request, or an earlier state of a resource.

### Terraform evidence without duplicate logs

You do not need separate initialization or apply logs for routine resource
creation and updates. Submit the configuration and `.terraform.lock.hcl`.
Capture the safe state or target checks requested by the task to show the
resulting resources or changed values. One capture can support several checks.
A successful plan also demonstrates that the working folder was initialized.
The lock file records the selected provider version.

The presence of a `.tfstate` file alone does not prove a successful apply.
An apply can save partial state before failing. State can also remain after
destroy or become stale when resources change outside Terraform.
Keep raw state locally or in its backend, not in the submission.
Capture only the relevant addresses, identifiers, or attributes, with secrets
removed.

Keep plans when a task asks you to review proposed actions. Keep captures of
historical events that final state cannot prove, such as migration, locking,
import, or destroy. Keep failure results and before-and-after checks when
requested. Later tasks may change or remove resources, so capture each result
while it is available.

Review output before you capture or share it. Redact secrets and any values
the task excludes. Keep raw sensitive captures outside the repository.
Do not submit raw state, saved plans, tokens, or private keys.

## Explain answers

Each Explain question gives a situation, asks one question, and lists what a
solid answer covers. The list names the points to address, not the answer.
Answer in your own words. Use the situation, not a definition from the docs.

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
2. Checks every `Done when` line against source files and required run captures.
3. Reports checks it cannot verify without running your configuration.
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
