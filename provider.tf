terraform {

  required_providers {
    vault = {
      source  = "hashicorp/vault"
      version = ">= 4.4.0"
    }
    google = {
      source  = "hashicorp/google"
      version = ">=5.10.0"
    }
  }
}


provider "vault" {
  skip_tls_verify = true
  address         = var.vault_address
  token           = var.vault_token
}


# data "vault_generic_secret" "gcp_credentials" {
#   path = "ejbest/gcp"
# }
