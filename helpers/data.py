import json


def getJsonFromFile(filename):
    with open('data/{}'.format(filename), 'r') as jsonFile:
        return json.load(jsonFile)


def getJsonObjectById(obj, id):
    for dict in obj:
        if dict['id'] == id:
            return dict
