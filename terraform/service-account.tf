module "workflows_service_account" {
  source        = "git::https://github.com/terraform-google-modules/terraform-google-service-accounts"
  project_id    = var.project_id
  prefix        = ""
  names         = ["sa-workflows-instance"]
  description = "Used by Workflows"
  display_name = "SA Workflows Instance"
  project_roles = var.service_account.workflows
}

module "run_service_account" {
  source        = "git::https://github.com/terraform-google-modules/terraform-google-service-accounts"
  project_id    = var.project_id
  prefix        = ""
  names         = ["sa-cloud-run-instance"]
  description = "Used by Cloud Run"
  display_name = "SA Cloud Run Instance"
  project_roles = var.service_account.run
}

module "scheduler_service_account" {
  source        = "git::https://github.com/terraform-google-modules/terraform-google-service-accounts"
  project_id    = var.project_id
  prefix        = ""
  names         = ["sa-workflows-invoker"]
  description = "Used to trigger Workflows"
  display_name = "SA Invoker for Sheduler"
  project_roles = var.service_account.scheduler
}

module "function_service_account" {
  source        = "git::https://github.com/terraform-google-modules/terraform-google-service-accounts"
  project_id    = var.project_id
  prefix        = ""
  names         = ["sa-function-instance"]
  description = "Used by Cloud Functions"
  display_name = "SA Cloud Functions Instance"
  project_roles = var.service_account.function
}



