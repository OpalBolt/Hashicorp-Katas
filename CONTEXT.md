# Context

Terms used in this guide.

**Slice**
One topic unit. It has Why, Concepts, Tasks, and Explain.

**Topic slice**
One of the ten learning units before the capstone.

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
Files the learner produces from their own run to prove a Done when line.

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
