import json


def handler(event, context):
    queryStringParameters = event['queryStringParameters'] or {}
    pathParameters = event['pathParameters'] or {}

    qsMethodValue = "None"
    pathMethodValue = "None"

    if pathParameters and 'proxy' in pathParameters:
        pathMethodValue = pathParameters['proxy']

    if queryStringParameters and 'method' in queryStringParameters:
        qsMethodValue = queryStringParameters['method']

    returnVal = {
        "statusCode": 200,
        "body": json.dumps(f"Path value: {pathMethodValue}\nQuery string value: {qsMethodValue}")
    }
    # logging for debugging purpose
    print(returnVal)

    return returnVal
