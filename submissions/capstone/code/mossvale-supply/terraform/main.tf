terraform {
  required_version = ">= 1.4.0"

  backend "local" {
    path = "terraform.tfstate"
  }
}

variable "customer_name" {
  type = string
}

variable "development_database_password" {
  type      = string
  sensitive = true
}

variable "production_database_password" {
  type      = string
  sensitive = true
}

resource "terraform_data" "development_database" {
  input = {
    customer    = var.customer_name
    environment = "development"
    database = {
      name     = "mossvale"
      username = "mossvale_app"
      password = var.development_database_password
    }
  }
}

resource "terraform_data" "production_database" {
  input = {
    customer    = var.customer_name
    environment = "production"
    database = {
      name     = "mossvale"
      username = "mossvale_app"
      password = var.production_database_password
    }
  }
}
