import json
import requests
from geolocate import *

def handler(event, context):
    body = json.loads(event['body'])
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps({
            'method': 'sendMessage',
            'chat_id': body['message']['chat']['id'],
            'text':  index(str(body['message']['text']))
        }),
        'isBase64Encoded': False
    }
