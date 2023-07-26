from pyspark.context import SparkContext
from awsglue.context import GlueContext
from pyspark.sql import SparkSession
import time

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

movies_csv = glueContext.create_dynamic_frame.from_catalog(
    database="movies", table_name="tb_moviescsv")
movies_json = glueContext.create_dynamic_frame.from_catalog(
    database="movies", table_name="tb_moviesjson")
tb_person = glueContext.create_dynamic_frame.from_catalog(
    database="movies", table_name="tb_person6")

df_movies_csv = movies_csv.toDF()
df_movies_json = movies_json.toDF()
df_person = tb_person.toDF()

dfTB_csv = df_movies_csv.createOrReplaceTempView("tb_csv")
dfTB_json = df_movies_json.createOrReplaceTempView("tb_json")
dfTB_person = df_person.createOrReplaceTempView("tb_person")

# tb_movies -> Juntando csv com json
spark.sql("""
   CREATE TEMP VIEW tb_movies AS (
     WITH movies AS (
     SELECT DISTINCT
            ROW_NUMBER() OVER (ORDER BY json.titleen) idRating, 
                COALESCE(json.titleen, csv.titulooriginal) AS titulo, 
                COALESCE(CAST(csv.tempominutos as int), json.runtime) AS tempoMinutos, 
                COALESCE(json.release_date, csv.anolancamento) AS DataLancamento, 
                COALESCE(csv.genero, json.genre) AS genero, 
                COALESCE(csv.nomeartista, json.person) AS nomeArtista, 
                COALESCE(csv.personagem, json.character) AS personagem,
                json.voiceactor AS dublador,
                json.specialguest AS participacaoEspecial
                FROM tb_csv as csv 
            RIGHT JOIN tb_json as json ON (json.titleen = csv.titulooriginal) AND csv.nomeartista LIKE json.person 
            ) SELECT *
            FROM movies
            GROUP BY idRating, titulo, nomeartista, personagem, tempominutos, DataLancamento, genero, dublador, participacaoEspecial
            ORDER BY idRating ASC )
""")

spark.sql("""
    CREATE TEMP VIEW dim_tempo AS
    WITH movies AS (
        SELECT
            idRating as id,
            DataLancamento
        FROM tb_movies
    ) SELECT 
        id,
        CAST(SUBSTR((DataLancamento),1,4) AS INT) as ano,
        CAST(SUBSTR(DataLancamento,6,2) AS INT) as mes,
        CAST(SUBSTR(DataLancamento,9,2) AS INT) as dia,
        DATE(DataLancamento) as DataCompleta,
        CASE
            WHEN CAST(SUBSTR(DataLancamento,6,2) as INT) > 6 THEN 2
            ELSE 1
        END AS Semestre
        FROM movies
""")

spark.sql("""
    CREATE TEMP VIEW dim_atores AS (   
        SELECT
       ROW_NUMBER() OVER (ORDER BY name) id,
       *
       FROM tb_person)
""")

spark.sql("""
  CREATE TEMP VIEW dim_movies AS (
     SELECT
            idrating as id,
            titulo,
            tempominutos,
            genero
        FROM tb_movies
        ORDER BY id)
""")

spark.sql("""
CREATE TEMP VIEW dim_rating AS     
    SELECT
            ROW_NUMBER() OVER (ORDER BY csv.numerovotos DESC) id,
            COALESCE(json.titleen, csv.titulooriginal) AS titulo, 
            json.popularitytmdb as popularidadeTMDB,
            json.vote_averagetmdb as notaTMDB,
            json.vote_counttmdb as numerovotosTMDB,
            CAST(csv.numerovotos AS INT) as numerovotosIMDB,
            CAST(csv.notamedia AS DOUBLE) as nota,
            CAST(csv.numerovotos AS INT) + json.vote_counttmdb as TotalDeVotos
        FROM tb_csv as csv
        RIGHT JOIN tb_json as json ON (json.titleen = csv.titulooriginal) AND csv.nomeartista LIKE json.person
""")

spark.sql("""
  CREATE TEMP VIEW fato_papelfilme AS (
      SELECT
        idRating as id,
        datalancamento,
        a.id as idArtista,
        participacaoEspecial,
        dublador
        FROM tb_movies as movies
        JOIN dim_atores as a ON a.name = movies.nomeartista)
""")

spark.sql("""
  CREATE TEMP VIEW dim_personagens AS (
    SELECT
        idRating as id,
        personagem 
        FROM tb_movies
        )
""")

# Carregar as views como DataFrames
fato_movieDF = spark.table("fato_papelfilme")
dim_tempoDF = spark.table("dim_tempo")
dim_movie = spark.table("dim_movies")
dim_atoresDF = spark.table("dim_atores")
dim_ratingDF = spark.table("dim_rating")
dim_personagensDF = spark.table("dim_personagens")

REFINED = "s3://pblabum/REFINED/Movies/"

fato_movieDF.write.parquet(f"{REFINED}fato_papelfilme/", mode="overwrite")
time.sleep(15)
dim_tempoDF.write.parquet(f"{REFINED}dim_tempo/", mode="overwrite")
time.sleep(15)
dim_movie.write.parquet(f"{REFINED}dim_movies/", mode="overwrite")
time.sleep(15)
dim_atoresDF.write.parquet(f"{REFINED}dim_atores/", mode="overwrite")
time.sleep(15)
dim_personagensDF.write.parquet(f"{REFINED}dim_personagens/", mode="overwrite")
time.sleep(15)
