import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql import Row, DataFrame
from pyspark.sql.functions import *
from functools import reduce
from pyspark.sql.types import DoubleType, IntegerType, ByteType, StringType
import time


# @params: [JOB_NAME]
args = getResolvedOptions(
    sys.argv, ['JOB_NAME', "S3_PATH_JSON", "S3_PATH_ATORES"])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

df1 = spark.read.json(f'{args["S3_PATH_JSON"]}actorsAction1.json')
df2 = spark.read.json(f'{args["S3_PATH_JSON"]}actorsAction2.json')
df3 = spark.read.json(f'{args["S3_PATH_JSON"]}actorsAction3.json')

df = reduce(DataFrame.unionAll, [df1, df2, df3])

str = args['S3_PATH_JSON']
replacedS3PATH = str.replace("RAW", "TRT")

dfPerson = df.drop_duplicates(["name"])
dfPerson = dfPerson.withColumnRenamed("popularity", "popularityTMDB")
dfPerson = dfPerson.withColumn("popularityTMDB", round(
    col("popularityTMDB"), 0).cast(IntegerType()))

dfPerson = dfPerson.withColumn(
    "place_of_birth", split(col("place_of_birth"), ","))

dfPerson = dfPerson.withColumn("city", when(size(col("place_of_birth")) > 2, lit(
    col("place_of_birth")[1])).otherwise(lit(col("place_of_birth")[0])).cast(StringType()))
dfPerson = dfPerson.withColumn("country", when(size(col("place_of_birth")) > 2, lit(
    col("place_of_birth")[2])).otherwise(lit(col("place_of_birth")[1])).cast(StringType()))
dfPerson = dfPerson.drop("adult", "also_known_as", "biography", "homepage", "profile_path", "imdb_id",
                         "known_for_department",  "external_ids", "id", "movie_credits", "place_of_birth", "deathday")
dfPerson = dfPerson.withColumn("gender", when(
    col("gender") == 1, 'F').otherwise("M").cast(StringType()))
dfPerson = dfPerson.select(
    "name", "gender", "birthday", "city", "country", "popularityTMDB")

df_temp = df.drop("also_known_as", "biography",
                  "deathday", "homepage", "profile_path")
df_temp = df.select("name", "gender", "known_for_department",
                    "place_of_birth", "popularity", "movie_credits")

df_temp = df_temp.drop_duplicates(subset=["name"])

moviesList = []

moviesCredits = df_temp.select("movie_credits").orderBy(asc("name")).collect()

actor = df_temp.select("name").orderBy(asc("name")).collect()

for i in range(len(moviesCredits)):
    for y in range(len(moviesCredits[i][0]["cast"]) - 1):
        movieKeys = moviesCredits[i][0]["cast"][y]
        moviesList.append(Row(movieKeys["original_title"], movieKeys["title"], movieKeys["character"], movieKeys["genre_ids"], movieKeys["popularity"],
                          movieKeys["release_date"], movieKeys["vote_average"], movieKeys["vote_count"], movieKeys["runtime"], actor[i][0]))

moviesSchema = ["titleEn", "title", "character", "genre_ids", "popularityTMDB",
                "release_date", "vote_averageTMDB", "vote_countTMDB", "runtime", "person"]
moviesOG = spark.createDataFrame(moviesList, schema=moviesSchema)

movies = moviesOG

movies = movies.select("*").where(array_contains(col("genre_ids"),
                                                 28) | array_contains(col("genre_ids"), 12))

movies = movies.withColumn("genre_ids", when(array_contains(col("genre_ids"), 12) & array_contains(col("genre_ids"), 28), "Ação/Aventura").
                           when(array_contains(col("genre_ids"), 28), "Ação").
                           when(array_contains(col("genre_ids"), 12), "Aventura"))

movies = movies.withColumnRenamed("genre_ids", "genre")

movies = movies.withColumn(
    "vote_averageTMDB", round(col("vote_averageTMDB"), 1))
movies = movies.withColumn("popularityTMDB", round(
    col("popularityTMDB"), 0).cast("int"))

movies = movies.withColumn("VoiceActor", when(
    col("character").contains("(voice)"), 1).otherwise(0).cast(ByteType()))
movies = movies.withColumn("VoiceActorYourself", when(
    col("character").contains(col("person")), 1).otherwise(0).cast(ByteType()))
movies = movies.withColumn("character", regexp_replace(
    col("character"), '\s*\(voice\)', ""))

movies = movies.withColumn("SpecialGuest", when(
    col("character").contains("(uncredited)"), 1).otherwise(0).cast(ByteType()))
movies = movies.withColumn("character", regexp_replace(
    col("character"), '\s*\(uncredited\)', ""))
movies = movies.withColumn("vote_countTMDB", col(
    "vote_countTMDB").cast(IntegerType()))

movies = movies.where(substring(col("release_date"), 1, 4).cast("int") <= 2023)
movies = movies.withColumn("runtime", col("runtime").cast("int"))
movies = movies.filter(~movies.titleEn.contains("WWE"))

movies.write.mode("overwrite").parquet(replacedS3PATH)
time.sleep(15)
dfPerson.write.mode("overwrite").parquet(args["S3_PATH_ATORES"])
time.sleep(15)

job.commit()
