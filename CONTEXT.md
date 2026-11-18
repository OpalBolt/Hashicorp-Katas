# Context

Terms used in this guide.

**Slice**
One topic unit. It has Why, Concepts, Tasks, and Explain.

**Topic**
A group of related slices, such as Terraform or Vault.

**Foundations slice**
The `00` slice that teaches the basic concepts for a topic.

**Starter**
Material the guide provides for a task. It never satisfies the task's Done when
on its own. It is either a Scaffold or a Fix-it starter. A working example is
not a starter and is not allowed after the foundations slices.

**Scaffold**
A Starter with blanks. A blank is any piece the learner must author: a value, a
block, or a whole file. Every blank has a Done when line.

**Fix-it starter**
A Starter that is deliberately broken. The learner repairs it.

**Warm-up**
A guided Task that comes before a Task that introduces a new skill. It uses a
Starter on a different mini-problem, with its own short Done when and its own
evidence. It is required. The Task after it stays the graded one.

**Topic slice**
One of 12 learning units grouped into four topics before the capstone. Topic
slices use numbering local to their topic.

**Capstone**
The final work. It has a written diagnosis stage and a build stage.

**Prerequisite**
Earlier work that must be complete before a slice starts.

**Task**
A goal the learner implements. It has constraints and a Done when list. It never includes the solution.

**Done when**
A list of statements that must all be true for a task to pass.

**Explain**
Written questions that test understanding, not only working code.

**Evidence**
Files or source artifacts the learner produces to prove a Done when line.
Text-only artifacts, such as a Markdown diagram, are valid evidence when the
task checks text.

**Submission**
One slice folder under `submissions/`. It contains code, evidence, and written answers.

**Grading skill**
The learner's AI grading instructions. It checks tasks and Explain answers against the slice.

**Concept hint**
One pointer to a concept after a failed task. It does not give a fix or solution.

**Emulator**
A local program that imitates a cloud API. Floci is the AWS emulator. It shows that Terraform runs. It does not prove IAM is right.

**State**
The file Terraform uses to map code to real resources. It can hold secrets in plain text.

**Seal / unseal**
Vault starts sealed. It cannot read its own data until enough key shares unlock it.

**Dev mode**
A Vault mode that is in memory and already unsealed. Use it for learning only.

**Dynamic secret**
A credential Vault creates on request and removes after its lease ends.

**Community Edition (CE)**
The free Vault build. Enterprise adds features such as namespaces and replication.
