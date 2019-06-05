from models.shared.person import Person
from models.hero.hero import Hero
from models.villain.villain import Villain
from helpers.data import getJsonFromFile, getJsonObjectById


def getAllHeroes():
    heroList = []
    heroData = GetHeroData()
    for hero in heroData:
        person = Person(hero['name'], hero['characters'])
        heroList.append(Hero(person,
                             hero['alias'],
                             hero['publisher'],
                             Villain(Person('Name Stub', 'Character Stub'),
                                     'Alias Stub',
                                     hero['publisher'],
                                     'Crimes Stub')))  # stub for getVillainbyId()
    return heroList


def getHeroById(id):
    heroJson = getJsonObjectById(GetHeroData(), id)
    person = Person(heroJson['name'], heroJson['characters'])
    hero = Hero(person,
                heroJson['alias'],
                heroJson['publisher'],
                Villain(Person('Name Stub', 'Character Stub'),
                        'Alias Stub',
                        heroJson['publisher'],
                        'Crimes Stub'))  # stub for getVillainbyId()
    return hero


# Helper functions
def GetHeroData():
    return getJsonFromFile("heros.json")
