import datetime
import logging
import os
import boto3
from botocore.exceptions import ClientError


session = boto3.Session(profile_name="matheus")
s3 = session.client('s3')
date = datetime.datetime.now()


def upload_file(bucket, object_name=None):
    categories = ['Movies', 'Series']

    try:
        for i in range(len(categories)):
            make_upload(categories[i], object_name, bucket)
    except ClientError as e:
        logging.error(e)
        return False
    finally:
        print("\nExecução finalizada")

    return True


def make_upload(categories, object_name, bucket):
    if object_name is None:
        object_name = os.path.basename(
            f"{(categories).lower()}.csv")

    file = f"{(categories).lower()}.csv"

    outpath = "RAW/Local/CSV/{}/{}/{}/{}/{}".format(
        categories, date.year, date.month, date.day, object_name)

    print(f'\nIniciando carregamento em {outpath}')
    response = s3.upload_file(file, bucket, outpath)
    print('Carregamento finalizado....')
    return True


if __name__ == '__main__':
    upload_file("pblabum")
