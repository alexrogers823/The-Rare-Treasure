from .dialogue import InvDescriptions

class Inventory:
    item_list = {
        "1": ["Crimson Scarf", "Angel's Blood", "Ring of Fire"],
        "2": ["Sun Dial", "Pure Lemon", "Golden Axe", "Warning Light"],
        "3": ["Orange Juice", "Orange Pie", "Orange Rind",
                "Orange Popsicle", "Map of Orange Orchards"],
        "4": ["Sage Stone", "Forest Leaf", "Northern Grass",
                "Dollar Bill", "Healing Potion", "Four-Leaf Clover"],
        "5": ["Cerelean Key", "Azure Lake Sample", "Sky Mist",
                "Teary-Eyed Frog", "Turquoise Shell", "Healing Heart", "Sapphire Necklace"],
        "6": ["Right Arm", "Left Arm", "Right Leg", "Left Leg", "Head", "Heart"],
        "Major": ["Red Orb", "Yellow Orb", "Orange Orb", "Green Orb", "Blue Orb"]
    }

    def __init__(self):
        self.inv_list = []


    def describe(self):
        if self.inv_list:
            for value in self.inv_list:
                InvDescriptions.describe_inventory(value) # From dialogue.py
        else:
            print("There's nothing in here yet. Start collecting some items!")


    def add(self, item):
        self.inv_list.append(item)


    def relinquish(self, item):
        self.inv_list.remove(item)


    def exchange_items(self, level, major_item):
        inv_list_copy = self.inv_list[:]
        for minor_item in inv_list_copy:
            if minor_item in Inventory.item_list[level]:
                self.relinquish(minor_item)

        self.add(major_item)
