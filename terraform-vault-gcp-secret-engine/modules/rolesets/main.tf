# Create a roleset in Vault for generating GCP access tokens
resource "vault_gcp_secret_roleset" "vault_gcp_secret_roleset" {
  backend     = var.backend
  depends_on  = [var.roleset_depends_on]
  roleset     = var.vault_gcp_roleset_name
  project     = var.gcp_project_id
  secret_type = var.secret_type

  token_scopes = var.token_scopes

  dynamic "binding" {
    for_each = var.bindings
    content {
      resource = binding.value.resource
      roles    = binding.value.roles
    }
  }
}


