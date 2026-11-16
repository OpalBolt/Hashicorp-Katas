# How grading works

You finish a task. An AI checks it. The AI grades from evidence, so you must produce evidence.

## Slice layout

Each slice has:

- **Why.** Why the goal matters to a client. Read this first.
- **Concepts.** Names of things you must understand. You research them yourself.
- **Tasks.** Each has a goal, constraints, and a **Done when** list. Every line in that list must be true.
- **Explain.** Written questions. These test understanding, not only working code.

## Where your work goes

```
submissions/
  01-workflow/
    code/        your Terraform, compose files, scripts
    evidence/    command output, logs, screenshots as text
    answers.md   your written answers to Explain
```

Use the same pattern for each slice.

## Asking the AI to grade

Give the AI these things:

1. The slice file.
2. The matching `submissions/<slice>/` folder.
3. This instruction:

> Grade my submission against the slice's "Done when" lists and "Explain" questions. Use only my files and, where you can, run the checks yourself. For each task, give PASS, PARTIAL or FAIL with the exact line that failed and why. Do not write the solution. Do not give a fix. If I fail, give one hint that points at the concept, not the answer. Then judge each written answer as solid, shallow or wrong, and say what is missing.

`AGENTS.md` in the repo root gives the same rules to an agent that reads it on its own.

## Rules for you

- Do not paste secrets or real tokens into evidence. Dev-mode tokens and test keys are fine. Real ones are not.
- Evidence must come from your run, not from a guide.
- A pass without understanding does not count. If you cannot explain it, redo it.
- Use the AI for grading and hints only. If you ask it to write the solution, you lose the learning.

## Grades

| Grade | Meaning |
|---|---|
| PASS | Every "Done when" line is true and shown by evidence. |
| PARTIAL | Some lines are true. The rest are missing or unproven. |
| FAIL | The task is not met, or the evidence is not yours or does not show it. |
