class Building(object):
    def __init__(self, name, max_health, current_health, level, size, sign_ppl):
        self.name = name
        self.max_health = max_health
        self.current_health = current_health
        self.level = level
        self.size = size  # Size of building. Either "small", "medium", or "large"
        self.sign_ppl = sign_ppl  # Assigned population

    def print_info(self):
        return "{0} ({1})\n\tHealth: (2}/{3} - Level: {4}".format(self.name, self.size, self.current_health,
                                                                  self.max_health, self.level)


class MageHall(Building):
    def __init__(self, name, max_health, current_health, level, size, sign_ppl):
        super().__init__(name, max_health, current_health, level, size, sign_ppl)

    # More TBA



