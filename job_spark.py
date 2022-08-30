import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
import pandas as pd
import boto3
from pyspark.sql import functions as f

# Settings
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Identifying files from s3 bucket
s3 = boto3.resource('s3')
name_bucket = "test-8302022-01"
my_bucket = s3.Bucket(name=name_bucket)

path = []
for i in my_bucket.objects.all():
    path.append("s3://"+i.bucket_name+"/"+i.key)
    
# Open files from s3 bucket
df = spark.read.csv(path[0],inferSchema = True, header = True)
for i in range(len(path)):
  if path[i] == path[0]:
    pass
  df_a = spark.read.csv(path[i], inferSchema = True, header = True)
  df = df.unionByName(df_a)

# Adding two columns, the price, and variability
# The price column shows if the bitcoin price downed or upped on that day
# The variability shows how much the price changed that day
df = df.withColumn('price_day', f.round(df.close - df.open, 2))
df = df.withColumn('variability', f.round(df.high - df.low, 2))

# Saving the datafame in a new s3 bucket
df = df.coalesce(1)                        
df.write.parquet('s3://test-8302022-03/bitcoin.parquet')

job.commit()