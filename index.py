import json


def handler(event, context):
    message = ""
    queryStringParameters = event['queryStringParameters'] or {}
    if queryStringParameters:
        message = queryStringParameters['method']
    returnVal = {
        "statusCode": 200,
        "body": json.dumps(message)
    }
    # logging for debugging purpose
    print(returnVal)

    return returnVal
