import json


def handler(event, context):
    message = event['method']
    return {
        "statusCode": 200,
        "body": json.dumps(message)
    }
