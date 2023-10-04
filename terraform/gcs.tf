module "gcs_bucket_config" {
  source  = "git::https://github.com/terraform-google-modules/terraform-google-cloud-storage"
  names = [var.gcs.config]
  project_id = var.project_id
  prefix = ""
  storage_class = "STANDARD"
  location = var.location
}