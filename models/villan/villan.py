from models.shared.person import Person


class Villan(object):
    def __init__(self, person: Person, alias, powers, crimes):
        self.realname = person.name
        self.age = person.age
        self.alias = alias
        self.powers = powers
        self.crimes = crimes
