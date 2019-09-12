
class Player:
    def __init__(self, name):
        # Add inventory and silver here
        self.name = name
        self.silver = 0
        self.backpack = Inventory
        pass


class Narrator:
    def __init__(self, name):
        self.name = name


    def speak(self, level):
        self.dialogue(level)
