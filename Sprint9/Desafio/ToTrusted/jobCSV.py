import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import *

# @params: [JOB_NAME]
args = getResolvedOptions(
    sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_OUTPUT_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)

job.init(args['JOB_NAME'], args)

df_dynamic = glueContext.create_dynamic_frame.from_options(
    "s3",
    {
        "paths": [
            args['S3_INPUT_PATH']
        ]
    },
    "csv",
    {"withHeader": True, "separator": "|"},
)

df = df_dynamic.toDF()

df = df.select("*").where(col("genero").contains("Action")
                          | col("genero").contains("Adventure"))

df = df.select("*").where(
    col("nomeArtista").contains("Tom Cruise") |
    col("nomeArtista").contains("Jean-Claude Van Damme") |
    col("nomeArtista").contains("Jason Statham") |
    col("nomeArtista").contains("Dwayne Johnson") |
    col("nomeArtista").contains("Vin Diesel") |
    col("nomeArtista").contains("Keanu Reeves") |
    col("nomeArtista").contains("Jackie Chan") |
    col("nomeArtista").contains("Bruce Willis") |
    col("nomeArtista").contains("Arnold Schwarzenegger") |
    col("nomeArtista").contains("Sylvester Stallone") |
    col("nomeArtista").contains("Angelina Jolie") |
    col("nomeArtista").contains("Linda Hamilton") |
    col("nomeArtista").contains("Michelle Rodriguez") |
    col("nomeArtista").contains("Michelle Yeoh") |
    col("nomeArtista").contains("Milla Jovovich") |
    col("nomeArtista").contains("Scarlett Johansson") |
    col("nomeArtista").contains("Zhang Ziyi") |
    col("nomeArtista").contains("Zoe Saldaña") |
    col("nomeArtista").contains("Uma Thurman") |
    col("nomeArtista").contains("Sigourney Weaver")
)

df = df.drop('id', "tituloPincipal", 'anoFalecimento',
             'titulosMaisConhecidos', "profissao", "generoArtista", "anoNascimento")

df = df.where(col("nomeArtista") != "Jackie Chang")

df = df.withColumn("genero", when(col("genero").contains("Adventure") & col("genero").contains("Action"), "Ação/Aventura").
                   when(col("genero").contains("Action"), "Ação").
                   when(col("genero").contains("Adventure"), "Aventura"))

df.write.mode("overwrite").parquet(args['S3_OUTPUT_PATH'])

job.commit()
