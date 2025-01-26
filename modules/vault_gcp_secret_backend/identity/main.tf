resource "vault_gcp_secret_backend" "gcp" {
  identity_token_ttl      = var.identity_token_ttl
  identity_token_audience = var.identity_token_audience
  service_account_email   = var.service_account_email
  path                    = var.path
  description             = var.description
  credentials             = var.vault_gcp_crentials
}
