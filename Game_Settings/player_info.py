from .items import Inventory

class Player:
    def __init__(self, name):
        # Add inventory and silver here
        self.name = name
        self.silver = 0
        self.backpack = Inventory()

    def solve_problem(self, item):
        print(f'Correct! You received 5 coins and the item: {item}')
        self.silver += 5
        self.backpack.add(item)

    def receive_major_item(self, level):
        major_item = Inventory.item_list["Major"][level-1]
        self.backpack.exchange_items(str(level), major_item)

        print(f'Exchanged all level {level} items for {major_item}')


class Narrator:
    def __init__(self, name):
        self.name = name


    def speak(self, level):
        self.dialogue(level)
