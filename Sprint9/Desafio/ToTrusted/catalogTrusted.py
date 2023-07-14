import boto3
from botocore.exceptions import ClientError

session = boto3.Session(profile_name="matheus")
glue_client = session.client('glue')

DB = 'movies'

schemaMoviesCSV = [
    {'Name': 'tituloOriginal', 'Type': 'string'},
    {'Name': 'anoLancamento', 'Type': 'string'},
    {'Name': 'tempoMinutos', 'Type': 'string'},
    {'Name': 'genero', 'Type': 'string'},
    {'Name': 'notaMedia', 'Type': 'string'},
    {'Name': 'numeroVotos', 'Type': 'string'},
    {'Name': 'personagem', 'Type': 'string'},
    {'Name': 'nomeArtista', 'Type': 'string'},
]
schemaMoviesJSON = [
    {'Name': 'titleen', 'Type': 'string'},
    {'Name': 'title', 'Type': 'string'},
    {'Name': 'character', 'Type': 'string'},
    {'Name': 'genre', 'Type': 'string'},
    {'Name': 'release_date', 'Type': 'string'},
    {'Name': 'popularityTMDB', 'Type': 'int'},
    {'Name': 'vote_averageTMDB', 'Type': 'double'},
    {'Name': 'vote_countTMDB', 'Type': 'int'},
    {'Name': 'runtime', 'Type': 'int'},
    {'Name': 'person', 'Type': 'string'},
    {'Name': 'VoiceActor', 'Type': 'tinyint'},
    {'Name': 'VoiceActorYourself', 'Type': 'tinyint'},
    {'Name': 'SpecialGuest', 'Type': 'tinyint'},
]
schemaPerson = [
    {'Name': 'name', 'Type': 'string'},
    {'Name': 'gender', 'Type': 'string'},
    {'Name': 'birthday', 'Type': 'string'},
    {'Name': 'city', 'Type': 'string'},
    {'Name': 'country', 'Type': 'string'},
    {'Name': 'popularityTMDB', 'Type': 'int'}]

DATALIST = [
    {"tb": "tb_person", "schema": schemaPerson, "path": "s3://pblabum/TRT/TMDB/JSON/Atores/2023/7/6/"},
    {"tb": "tb_moviesCSV", "schema":  schemaMoviesCSV, "path": "s3://pblabum/TRT/Movies/"},
    {"tb": "tb_moviesJSON", "schema":  schemaMoviesJSON, "path": "s3://pblabum/TRT/TMDB/JSON/2023/7/12/"}
]


def botoCrawler(DATABASE, DATA):
    for i, field in enumerate(DATA):
        try:
            response = glue_client.create_table(
                DatabaseName=DATABASE,
                TableInput={
                    'Name': field["tb"],
                    'StorageDescriptor': {
                        'Columns': field["schema"],
                        'Location': field["path"],
                        'InputFormat': 'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat',
                        'OutputFormat': 'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat',
                        'SerdeInfo': {
                            'SerializationLibrary': 'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe'
                        }
                    },
                    'TableType': 'EXTERNAL_TABLE',
                    'Parameters': {
                        'classification': 'parquet'
                    }
                }
            )
        except ClientError as e:
            if e.response['Error']['Code'] == 'AlreadyExistsException':
                print("Table already exists")
            else:
                print("Unexpected error: %s" % e)
        finally:
            print(f"Tabela {field['tb']} criada com sucesso!")
       

botoCrawler(DB, DATALIST)