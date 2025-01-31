resource "vault_gcp_secret_backend" "gcp" {
  # credentials = var.vault_gcp_crentials
  path        = var.path
  description = var.description
}
