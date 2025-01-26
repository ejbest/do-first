terraform {
  backend "s3" {
    skip_region_validation      = true
    skip_credentials_validation = true
    skip_get_ec2_platforms      = true
    skip_requesting_account_id  = true
    use_path_style              = true
  }
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
  address         = local.vault_address
  token           = var.vault_token
}


data "vault_generic_secret" "gcp_credentials" {
  path = "ejbest/gcp"
}
