from models.shared.person import Person
from models.hero.hero import Hero
from helpers.data import *


def getHeroById(id):
    data = getJsonFromFile("heros.json")
    heroJson = getJsonObjectById(data, id)
    hero = Hero(Person(heroJson.['name'], heroJson.['characters']),
                heroJson.['alias'],
                heroJson.['publisher'],
                heroJson.['archenemy'])
    return hero.alias
