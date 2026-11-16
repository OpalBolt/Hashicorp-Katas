# Context

Terms used in this course.

**Slice**
One topic unit. It has Why, Concepts, Tasks and Explain.

**Task**
A goal the learner implements. It has constraints and a Done when list. It never includes the solution.

**Done when**
A list of statements that must all be true for a task to pass.

**Evidence**
Files the learner produces from their own run to prove a Done when line.

**Emulator**
A local program that imitates a cloud API. Floci is the AWS emulator. It shows that Terraform runs. It does not prove IAM is right.

**State**
The file Terraform uses to map code to real resources. It can hold secrets in plain text.

**Seal / unseal**
Vault starts sealed. It cannot read its own data until enough key shares unlock it.

**Dev mode**
A Vault mode that is in memory and already unsealed. For learning only.

**Dynamic secret**
A credential Vault creates on request and removes after its lease ends.

**Community Edition (CE)**
The free Vault build. Enterprise adds features such as namespaces and replication.
