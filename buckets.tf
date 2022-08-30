provider "aws" {
  version = "~> 4.0"
  region  = "us-east-1"
}

resource "aws_s3_bucket" "test-8302022-03" {
  bucket = "test-8302022-03"
  acl    = "private"
}

resource "aws_s3_bucket" "test-8302022-01" {
  bucket = "test-8302022-01"
  acl    = "private"
}

resource "aws_s3_bucket" "script-8302022-2" {
  bucket = "script-8302022-2"
  acl    = "private"
}



