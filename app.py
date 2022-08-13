import sys

sys.path.extend(['/tmp/', '/tmp/smg_serverless'])

import json

import numpy as np

from smg_serverless.src.get_genre import main as get_genre  # type: ignore


def handler(event, context):
    melspectrogram = None

    if body := event.get('body'):
        js = json.loads(body)
        melspectrogram = js.get('melspectrogram')

    if not melspectrogram:
        return {
            'statusCode': 400,
            'body': 'No melspectrogram provided in JSON data body'
        }

    S = np.array(melspectrogram, dtype="float32")

    genres = get_genre(S)

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps(genres)
    }
