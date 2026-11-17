variable "release_name" {
  type        = string
  description = "Name supplied by the release job."
}

data "local_file" "template" {
  # The template already exists; Terraform only reads it.
  filename = "${path.module}/release-template.txt"
}

locals {
  # This value is derived from the caller's name and the existing template.
  note = replace(data.local_file.template.content, "RELEASE_NAME", var.release_name)
}

resource "local_file" "release_note" {
  # Terraform manages this generated file.
  filename = "${path.module}/release-note.txt"
  content  = local.note
}

output "release_note_path" {
  # The release job can consume this result.
  value = local_file.release_note.filename
}
