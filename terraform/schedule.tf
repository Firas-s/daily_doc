resource "google_cloud_scheduler_job" "job" {
  name        = "launch_workflows"
  description = "Triggers workflows job"
  schedule    = "0 8 * * *"
  http_target {
    http_method = "POST"
    uri         = "https://workflowexecutions.googleapis.com/v1/projects/${var.project_id}/locations/${var.workflows.location}/workflows/${var.workflows.name}/executions"
    body        = base64encode("{\"argument\":\"{\\\"bucket_location\\\": \\\"${var.workflows.bucket_location}\\\",\\\"config_location\\\": \\\"${var.workflows.config_location}\\\"}\",\"callLogLevel\":\"LOG_ERRORS_ONLY\"}")
    oauth_token {
        service_account_email = module.scheduler_service_account.email
    }
  }
}
