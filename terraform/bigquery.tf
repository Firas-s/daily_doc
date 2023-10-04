module "bigquery_ingestion" {
  source  = "git::https://github.com/terraform-google-modules/terraform-google-bigquery"
  dataset_id                  = "ingestion"
  dataset_name                = "ingestion"
  description                 = ""
  project_id                  = var.project_id
  location                    = "EU"
  access                      = [
    {role = "OWNER", special_group = "projectOwners"},
    {role = "READER", special_group = "projectReaders"},
    {role = "WRITER", special_group = "projectWriters"}
  ]
}

module "bigquery_raw" {
  source  = "git::https://github.com/terraform-google-modules/terraform-google-bigquery"
  dataset_id                  = "raw"
  dataset_name                = "raw"
  description                 = ""
  project_id                  = var.project_id
  location                    = "EU"
  access                      = [
    {role = "OWNER", special_group = "projectOwners"},
    {role = "READER", special_group = "projectReaders"},
    {role = "WRITER", special_group = "projectWriters"}
  ]
}

module "bigquery_bronze" {
  source  = "git::https://github.com/terraform-google-modules/terraform-google-bigquery"
  dataset_id                  = "bronze"
  dataset_name                = "bronze"
  description                 = ""
  project_id                  = var.project_id
  location                    = "EU"
  access                      = [
    {role = "OWNER", special_group = "projectOwners"},
    {role = "READER", special_group = "projectReaders"},
    {role = "WRITER", special_group = "projectWriters"}
  ]
}

module "bigquery_silver" {
  source  = "git::https://github.com/terraform-google-modules/terraform-google-bigquery"
  dataset_id                  = "silver"
  dataset_name                = "silver"
  description                 = ""
  project_id                  = var.project_id
  location                    = "EU"
  access                      = [
    {role = "OWNER", special_group = "projectOwners"},
    {role = "READER", special_group = "projectReaders"},
    {role = "WRITER", special_group = "projectWriters"}
  ]
}
module "bigquery_monitoring" {
  source  = "git::https://github.com/terraform-google-modules/terraform-google-bigquery"
  dataset_id                  = "monitoring"
  dataset_name                = "monitoring"
  description                 = ""
  project_id                  = var.project_id
  location                    = "EU"
  access                      = [
    {role = "OWNER", special_group = "projectOwners"},
    {role = "READER", special_group = "projectReaders"},
    {role = "WRITER", special_group = "projectWriters"}
  ]
}

module "bigquery_gold" {
  source  = "git::https://github.com/terraform-google-modules/terraform-google-bigquery"
  dataset_id                  = "gold"
  dataset_name                = "gold"
  description                 = ""
  project_id                  = var.project_id
  location                    = "EU"
  access                      = [
    {role = "OWNER", special_group = "projectOwners"},
    {role = "READER", special_group = "projectReaders"},
    {role = "WRITER", special_group = "projectWriters"}
  ]
}