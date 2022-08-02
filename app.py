import sys

sys.path.extend(['/tmp/', '/tmp/smg_serverless'])

import os

try:
    os.mkdir('/tmp/numba-cache')
except:
    pass

os.environ['NUMBA_CACHE_DIR'] = '/tmp/numba-cache'

import json
import random
import string

import requests

from smg_serverless.src.get_genre import main as get_genre  # type: ignore


def get_url_and_save(url, filename):
    try:
        r = requests.get(url, timeout=3)
    except requests.ConnectTimeout:
        return {
            'statusCode': 400,
            'body': 'Connection timeout, url took too long (>3s) to respond.'
        }

    # if not r.headers.get('content-type', '').startswith('audio/'):
    #     return {
    #         'statusCode': 400,
    #         'body': 'Invalid content-type'
    #     }

    with open(filename, 'wb') as f:
        f.write(r.content)


def handler(event, context):
    url = None

    if params := event.get('queryStringParameters'):
        url = params.get('url')

    if not url:
        return {
            'statusCode': 400,
            'body': 'No url provided'
        }

    keys = string.ascii_letters + string.digits

    hash = ''.join(random.choices(keys, k=random.randint(25, 50)))

    filename = f'/tmp/{hash}.mp3'

    get_url_and_save(url, filename)

    genres = get_genre([filename])

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps(genres)
    }
