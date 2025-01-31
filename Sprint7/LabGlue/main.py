import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql.functions import *
# @params: [JOB_NAME]

args = getResolvedOptions(
    sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)
source_file = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']


df_dynamic = glueContext.create_dynamic_frame.from_options(
    "s3",
    {
        "paths": [
            source_file
        ]
    },
    "csv",
    {"withHeader": True, "separator": ","},

)


def uppercase(rec):
    rec["nome"] = rec["nome"].upper()
    return rec


df = Map.apply(frame=df_dynamic, f=uppercase)

df_spark = df.toDF()

df_spark.write.option("header", True) \
        .partitionBy("sexo", "ano") \
        .mode("overwrite") \
        .json(target_path)


job.commit()

# Arquivo para transformar coluna nome, e realizar o particionamento para o S3
