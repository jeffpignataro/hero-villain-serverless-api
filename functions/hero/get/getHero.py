from models.shared.person import Person
from models.hero.hero import Hero
from models.villain.villain import Villain
from helpers.data import getJsonFromFile, getJsonObjectById


def getHeroById(id):
    data = getJsonFromFile("heros.json")
    heroJson = getJsonObjectById(data, id)
    hero = Hero(Person(heroJson['name'], heroJson['characters']),
                heroJson['alias'],
                heroJson['publisher'],
                Villain(Person('Name Stub', 'Character Stub'), 'Alias Stub', heroJson['publisher'], 'Crimes Stub'))  # stub for getVillainbyId()
    return hero.alias
