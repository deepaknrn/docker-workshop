variable "credentials" {
  description = "The path to the GCP credentials JSON file is ./keys/mycreds.json"
  default     = "./keys/mycreds.json"
}

variable "project_id" {
  description = "The GCP Project ID where resources will be created via Terraform is terrademo-485501"
  default     = "terraformdemo-485501"
}

variable "location" {
  description = "The location for GCP resources created via Terraform is ASIA-SOUTHEAST2"
  default     = "ASIA-SOUTHEAST2"
}

variable "bq_dataset_name" {
  description = "The name of the BigQuery dataset created via Terraform is demo_dataset"
  default     = "demo_dataset"
}

variable "gcs_bucket_name" {
  description = "The GCS Bucket Name for the bucket created via Terraform is terraformdemo-485501-terra-bucket"
  default     = "terraformdemo-485501-terra-bucket"
}

variable "gcs_storage_class" {
  description = "The GCS Storage class for the bucket created via Terraform is STANDARD"
  default     = "STANDARD"
}

