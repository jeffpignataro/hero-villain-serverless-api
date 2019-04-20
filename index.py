import sys
import json
from importlib import import_module


def handler(event, context):
    queryStringParameters = event['queryStringParameters'] or {}
    pathParameters = event['pathParameters'] or {}

    if pathParameters and 'proxy' in pathParameters:
        parsedPathParameters = pathParameters['proxy'].split("/")

    # This is where the magic happens
    apiResponse = callApiMethod(parsedPathParameters, queryStringParameters)

    returnVal = {
        "statusCode": 200,
        "body": json.dumps(apiResponse)
    }
    # logging for debugging purpose
    print(returnVal)

    return returnVal


def callApiMethod(pathArgs, qsArgs):
    controller = pathArgs[0] or {}
    function = pathArgs[1] or {}
    method = pathArgs[2] or {}
    id = pathArgs[3] or {}

    executingMethod = import_module(
        'functions.{}.{}.{}'.format(controller, function, method))
    executingMethodReturnObject = getattr(executingMethod, method)(id)
    return executingMethodReturnObject
