project_id = "flows-yext-prod"
location = "europe-west2"

service_account = {
    "run" = [
        "flows-yext-prod=>roles/secretmanager.secretAccessor",
        "flows-yext-prod=>roles/bigquery.jobUser",
        "flows-yext-prod=>roles/bigquery.dataEditor"
    ],
    "workflows" = [
        "flows-yext-prod=>roles/run.invoker",
        "flows-yext-prod=>roles/bigquery.jobUser",
        "flows-yext-prod=>roles/storage.admin",
        "flows-yext-prod=>roles/bigquery.dataEditor",
        "flows-yext-prod=>roles/cloudfunctions.invoker",
        "flows-yext-prod=>roles/secretmanager.secretAccessor",
        "bi-chantelle=>roles/bigquery.dataEditor"
    ],
    "scheduler": [
        "flows-yext-prod=>roles/workflows.invoker", 
        "flows-yext-prod=>roles/logging.logWriter"
    ],
    "function" = [
        "flows-yext-prod=>roles/iam.serviceAccountUser",
        "flows-yext-prod=>roles/workflows.invoker"
    ],

}

workflows = {
    "name" = "yext",
    "location" = "europe-west1",
    "bucket_location" = "flows-yext-prod-source",
    "config_location" = "config-prod.json"
}

gcs = {
    "config" = "flows-yext-prod-source"
}