import troop


class Battalion(object):
    def __init__(self, name, grunt, count):
        self.bat_list = list()
        self.name = name
        self.grunt = grunt # Soort grunt
        self.count = count # Aantal troops in het batallion
        self.max_health = grunt.max_health * count
        self.current_health = self.max_health
        self.level = grunt.level
        self.rng = grunt.rng  # Range of Attack
        self.atk = grunt.atk  # Attack Power
        self.dfn = grunt.dfn  # Defense Power
        self.spd = grunt.spd  # Speed
        self.create()

    def create(self):
        if isinstance(self.grunt, troop.Grunt):
            for x in range(0,  self.count):
                grunt_to_add = self.grunt
                grunt_to_add.sign_nr = x
                self.bat_list.append(grunt_to_add)
        else:
            print("This isn't a troop.")

    def __str__(self):
        return "{0}\n\tTroop: {1}\n\tTotal Health: {2}/{3}" .format(self.name, self.grunt,
                                                                    self.current_health, self.max_health,)

    __repr__ = __str__

