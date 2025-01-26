module "gcp_credentials" {
  source = "./modules/storage-backend/credentials"
  # vault_gcp_crentials = data.vault_generic_secret.gcp_credentials.data["gcp-terraform-udemy-course"]
  path        = "gcp-credentials-backend"
  description = "GCP secrets engine for issuing temporary credentials using credentials"
}
