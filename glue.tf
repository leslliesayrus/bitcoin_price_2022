provider "aws" {
  version = "~> 4.0"
  region  = "us-east-1"
}

resource "aws_glue_job" "job_spark" {
  name     = "job_spark"
  role_arn = "arn:aws:iam::415:role/glue_s3"
  glue_version = "3.0"
  

  command {
    script_location = "s3://script-8302022-2/job_spark.py"
    python_version  = "3"
    }

}
