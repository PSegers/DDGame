class Troop(object):
    def __init__(self, name, max_health, current_health, level, rng, atk, dfn, spd):
        self.name = name
        self.max_health = max_health
        self.current_health = current_health
        self.level = level
        self.rng = rng # Range of Attack
        self.atk = atk # Attack Power
        self.dfn = dfn # Defense Power
        self.spd = spd # Speed

    def __str__(self):
        return "{0}\n\tHealth: {1}/{2}\n\tLevel: {3}\n\t"\
               "Attack: {4}\n\tDefense: {5}\n\tRange: {6}\n\tSpeed: {7}"\
            .format(self.name, self.current_health, self.max_health, self.level,
                    self.atk, self.dfn, self.rng, self.spd)


class Champion(Troop):
    def __init__(self, name, max_health, current_health, level, rng, atk, dfn, spd):
        super().__init__(name, max_health, current_health, level, rng, atk, dfn, spd)


class Grunt(Troop):
    def __init__(self, name, max_health, current_health, level, rng, atk, dfn, spd):
        super().__init__(name, max_health, current_health, level, rng, atk, dfn, spd)
        self.sign_nr = 0
