import json


def handler(event, context):
    message = event['method']
    returnVal = {
        "statusCode": 200,
        "body": json.dumps(message)
    }
    print(returnVal)
    return returnVal
