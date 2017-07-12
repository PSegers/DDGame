import troop
import battalion


class Army(object):
    def __init__(self):
        self.army = list()

    def add_troop(self, troop_to_add):
        if len(self.army) >= 7:
            print("No more troops can be added.")
        else:
            self.army.append(troop_to_add)

    def insert_troop(self, troop_to_add, spot):
        if spot > 7 or spot < 1:
            print("That is not a valid spot.")
        else:
            self.army.insert(spot-1, troop_to_add)

    def __str__(self):
        for element in self.army:
            return element.name

    __repr__ = __str__
