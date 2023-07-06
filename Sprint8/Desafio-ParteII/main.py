import requests
import datetime
import boto3
import json
import os
from botocore.exceptions import ClientError

API_KEY = os.environ["API_KEY"]

session = boto3.Session()

date = datetime.datetime.now()
s3 = session.client('s3')

actorsList = [1620, 63, 193, 11701, 17647, 1339, 8691, 10205, 1245, 2713, 500, 976, 12835, 18918, 6384, 18897, 62, 1100,
              16483, 15111, 139]
actorsMedia = []


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
        file = f"RAW/TMDB/JSON/{date.year}/{date.month}/{date.day}/actorsAction.json"
        
        try:
            print(f"Fazendo Upload em {file}")
            s3.put_object(Body=json.dumps(actorsMedia, ensure_ascii=False).encode('utf8'), Bucket='pblabum', Key=file)
        finally:
            print(f"Upload finalizado") 


def req(id):
    try:
        url = f"https://api.themoviedb.org/3/person/{id}?append_to_response=movie_credits%2Cexternal_ids&language=pt-BR&api_key={API_KEY}"
        response = requests.get(url)
        data = response.json()
    finally:
        print(f'Upload {id} - Finalizado')
        return data


def microBatchData():
    for i in range(len(actorsList)):
        data = req(actorsList[i])

        for media in data:
            actorsMedia.append(data)
           

if __name__ in '__main__':
    lambda_handler()
    
