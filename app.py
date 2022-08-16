import sys

sys.path.extend(['/tmp/', '/tmp/smg_serverless'])

import json

import boto3
import numpy as np

from smg_serverless.src.get_genre import main as get_genre  # type: ignore


with open('config.json', 'r') as js:
    conf = json.load(js)


def handler(event, context):
    filename = None

    if body := event.get('body'):
        js = json.loads(body)
        filename = js.get('melspectrogram')

    if not filename:
        return {
            'statusCode': 400,
            'body': 'No melspectrogram provided in JSON data body'
        }

    s3 = boto3.client('s3', aws_access_key_id=conf["AWS_ACCESS_KEY_ID"], 
                        aws_secret_access_key=conf["AWS_SECRET_ACCESS_KEY"],
                        region_name=conf["AWS_REGION"], **conf.get("AWS_S3_EXTRAS", {}))

    obj = s3.get_object(Bucket=conf["S3_BUCKET"], Key=filename)

    melspectrogram = json.loads(obj['Body'].read().decode('utf-8'))

    S = np.array(melspectrogram, dtype="float32")

    genres = get_genre(S)

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps(genres)
    }
