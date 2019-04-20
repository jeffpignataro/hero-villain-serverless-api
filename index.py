import json

message = ""


def handler(event, context):
    queryStringParameters = event['queryStringParameters'] or {}
    if queryStringParameters:
        message = queryStringParameters['method']
    returnVal = {
        "statusCode": 200,
        "body": json.dumps(message)
    }
    print(returnVal)
    return returnVal
