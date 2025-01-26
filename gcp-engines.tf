module "vault_gcp_secret_backend" {
  source = "./modules/vault_gcp_secret_backend/credentials"
  # vault_gcp_crentials = data.vault_generic_secret.gcp_credentials.data["gcp-terraform-udemy-course"]
  path        = "gcp-ejb"
  description = "GCP secrets engine for issuing temporary credentials using credentials"
}

module "vault_gcp-ejb2" {
  source = "./modules/vault_gcp_secret_backend/credentials"
  # vault_gcp_crentials = data.vault_generic_secret.gcp_credentials.data["gcp-terraform-udemy-course"]
  path        = "gcp-ejb2"
  description = "GCP secrets engine for issuing temporary credentials using credentials"
}
