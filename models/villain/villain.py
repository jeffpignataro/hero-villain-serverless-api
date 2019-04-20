from models.shared.person import Person


class Villain(object):
    def __init__(self, person: Person, alias, publisher, crimes):
        self.realname = person.name
        self.charaters = person.characters
        self.alias = alias
        self.publisher = publisher
        self.crimes = crimes
