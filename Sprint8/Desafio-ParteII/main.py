import requests
import datetime
import boto3
import json
import os
from botocore.exceptions import ClientError

ACCESS_KEY = os.environ['AWS_ACCESS_KEY_ID']
SECRET_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
SESSION_TOKEN = os.environ['AWS_SESSION_TOKEN']

session = boto3.Session(
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
    aws_session_token=SESSION_TOKEN
)

date = datetime.datetime.now()
s3 = session.client('s3')

actorsList = [500, 976, 12835, 18918, 6384, 18897, 62, 1100,
              16483, 1245, 10205, 8691, 1339, 17647, 63, 11701, 139, 2713]
actorsMovies = []
actorsSeries = []


def lambda_handler(event, context):
    try:
        response = s3.list_buckets()
        print(response)
    except ClientError as e:
        print("Error\n")
        print(e)
    finally:
        print("Conectado ao S3\n Iniciando Batch ")

        microBatchData()

        categories = [{"type": "Movies", "list": actorsMovies},
                      {"type": "Series", "list": actorsSeries}]

        for i in range(0, 2):
            fileLower = categories[i]["type"].lower()
            file = "RAW/TMDB/JSON/{}/{}/{}/{}/{}".format(
                categories[i]["type"], date.year, date.month, date.day, f"{fileLower}.json")
            try:
                print(f"Fazendo Upload em {file}")
                s3.put_object(Body=json.dumps(categories[i]["list"], ensure_ascii=False).encode(
                    'utf8'), Bucket='pblabum', Key=file)
            finally:
                print(f"{i + 1} Upload finalizado")


def req(id):
    try:
        api_key = "721b346f73c11fd9715c5f8e5a5561bd"
        url = f"https://api.themoviedb.org/3/person/{id}/combined_credits?api_key={api_key}&language=pt-BR"
        response = requests.get(url)
        data = response.json()
    finally:
        print(f'Upload {id} - Finalizado')
        return data


def microBatchData():
    for i in range(len(actorsList)):
        data = req(actorsList[i])

        for media in data["cast"]:
            if media['media_type'] == "movie":
                data = media["id_actor"] = actorsList[i]
                actorsMovies.append(media)
            elif media['media_type'] == "tv":
                actorsSeries.append(media)


if __name__ in '__main__':
    lambda_handler()
