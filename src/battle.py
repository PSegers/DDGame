class Battle(object):

    def __init__(self, army1, army2):
        self.army1 = army1
        self.army2 = army2
        self.big_army = list()
        self.big_army.extend(army1)
        self.big_army.extend(army2)
        self.determine_speeds()

    def determine_speeds(self):
        self.big_army = sorted(self.big_army, key=lambda troop: troop.spd, reverse=True)

    def __str__(self):
        for element in self.big_army:
            print(element)
        return "List Printed"

    __repr__ = __str__
