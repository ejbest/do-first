
module "storage-admin-roleset" {
  source                 = "./modules/rolesets"
  roleset_depends_on     = module.gcp_credentials
  backend                = "gcp-credentials-test"
  vault_gcp_roleset_name = "vault_gcp_secret_roleset"
  gcp_project_id         = local.gcp_project_id
  secret_type            = "access_token"
  token_scopes           = ["https://www.googleapis.com/auth/cloud-platform"]
  bindings = [
    {
      resource = "//cloudresourcemanager.googleapis.com/projects/${local.gcp_project_id}"
      roles    = ["roles/viewer", "roles/storage.admin"]
    },
    {
      resource = "//cloudresourcemanager.googleapis.com/projects/${local.gcp_project_id}"

      roles = [
        "roles/editor"
      ]
    }
  ]
}
