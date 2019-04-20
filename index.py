import json
import os.path


def handler(event, context):
    queryStringParameters = event['queryStringParameters'] or {}
    pathParameters = event['pathParameters'] or {}

    qsMethodValue = "None"

    if pathParameters and 'proxy' in pathParameters:
        parsedPathParameters = pathParameters['proxy'].split("/")

    if queryStringParameters and 'method' in queryStringParameters:
        qsMethodValue = queryStringParameters['method']

    returnVal = {
        "statusCode": 200,
        "body": json.dumps(f"Path value: {','.join(map(str,parsedPathParameters))}\nQuery string value: {qsMethodValue}")
    }
    # logging for debugging purpose
    print(returnVal)

    return returnVal
