import requests
import datetime
import logging
import os
import boto3
import json
from botocore.exceptions import ClientError

session = boto3.Session(profile_name="matheus")
s3 = session.client('s3')
date = datetime.datetime.now()


def req(id):
    try:
        api_key = "721b346f73c11fd9715c5f8e5a5561bd"
        url = f"https://api.themoviedb.org/3/person/500/combined_credits?api_key={api_key}&language=pt-BR"
        response = requests.get(url)
        data = response.json()
    finally:
        # print(f'{id} - Finalizado')
        return data


def microBatchData():
    for i in range(len(actorsList)):
        data = req(actorsList[i])

        for media in data["cast"]:
            if media['media_type'] == "movie" and (12 in media['genre_ids'] or 28 in media['genre_ids']):
                data = media["id_actor"] = actorsList[i]
                actorsMovies.append(media)
            elif media['media_type'] == "tv":
                actorsSeries.append(media)


if __name__ in '__main__':
    actorsList = [500, 976, 12835, 18918, 6384, 18897, 62, 1100, 16483]
    actorsMovies = []
    actorsSeries = []

    microBatchData()

    categories = [
        {"type": "Movies", "list": actorsMovies},
        {"type": "Series", "list": actorsSeries}]

    for i in range(0, 2):
        filerLower = categories[i]["type"].lower()
        file = "RAW/TMDB/JSON/{}/{}/{}/{}/{}".format(
            categories[i]["type"], date.year, date.month, date.day, f"{filerLower}.json")
        try:
            print(f"Fazendo Upload em {file} .................")
            response = s3.put_object(Body=json.dumps(
                categories[i]["list"], ensure_ascii=False).encode('utf8'), Bucket='pblabum', Key=file)
        finally:
            print(f"{i + 1} Upload finalizado")
