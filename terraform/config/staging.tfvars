project_id = "flows-yext-dev"
location = "europe-west2"

service_account = {
    "run" = [
        "flows-yext-dev=>roles/secretmanager.secretAccessor",
        "flows-yext-dev=>roles/bigquery.jobUser",
        "flows-yext-dev=>roles/bigquery.dataEditor"
    ],
    "workflows" = [
        "flows-yext-dev=>roles/run.invoker",
        "flows-yext-dev=>roles/bigquery.jobUser",
        "flows-yext-dev=>roles/storage.admin",
        "flows-yext-dev=>roles/bigquery.dataEditor",
        "flows-yext-dev=>roles/cloudfunctions.invoker",
        "flows-yext-dev=>roles/secretmanager.secretAccessor",
        "bi-chantelle=>roles/bigquery.dataEditor"
    ],
    "scheduler": [
        "flows-yext-dev=>roles/workflows.invoker", 
        "flows-yext-dev=>roles/logging.logWriter"
    ],
    "function" = [
        "flows-yext-dev=>roles/iam.serviceAccountUser",
        "flows-yext-dev=>roles/workflows.invoker"
    ],

}

workflows = {
    "name" = "yext",
    "location" = "europe-west1",
    "bucket_location" = "flows-yext-dev-source",
    "config_location" = "config-staging.json"
}

gcs = {
    "config" = "flows-yext-dev-source"
}