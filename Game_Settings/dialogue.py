class Narration:

    def level_prologue(level_num):
        start_narration = {
            "1": "This begins the first level",
            "2": "This begins the second level",
            "3": "This begins the third level",
            "4": "This begins the fourth level",
            "5": "This begins the fifth level"
        }

        return start_narration[str(level_num)]

    def level_epilogue(level_num):
        end_narration = {
            "1": "This ends the first level",
            "2": "This ends the second level",
            "3": "This ends the third level",
            "4": "This ends the fourth level",
            "5": "This ends the fifth level"
        }

        return end_narration[str(level_num)]

    # def show_ending(item_number):
    #     if (player number) == item_number:
    #         print('Good ending')
    #     elif (player number) != 0:
    #         print('Neutral ending')
    #     else:
    #         print('Bad ending')


class InvDescriptions:
    descriptions = {
        "Crimson Scarf": "This is a Crimson Scarf",
        "Angel's Blood": "This is a Angel's Blood",
        "Ring of Fire": "This is a Ring of Fire",
        "Sun Dial": "This is a Sun Dial",
        "Pure Lemon": "This is a Pure Lemon",
        "Golden Axe": "This is a Golden Axe",
        "Warning Light": "This is a Warning Light",
        "Orange Juice": "This is a Orange Juice",
        "Orange Pie": "This is a Orange Pie",
        "Orange Rind": "This is a Orange Rind",
        "Orange Popsicle": "This is a Orange Popsicle",
        "Map of Orange Orchards": "This is a Map of Orange Orchards",
        "Sage Stone": "This is a Sage Stone",
        "Forest Leaf": "This is a Forest Leaf",
        "Northern Grass": "This is a Northern Grass",
        "Dollar Bill": "This is a Dollar Bill",
        "Healing Potion": "This is a Healing Potion",
        "Four-Leaf Clover": "This is a Four-Leaf Clover",
        "Cerelean Key": "This is a Cerelean Key",
        "Azure Lake Sample": "This is a Azure Lake Sample",
        "Sky Mist": "This is a Sky Mist",
        "Teary-Eyed Frog": "This is a Teary-Eyed Frog",
        "Turquoise Shell": "This is a Turquoise Shell",
        "Healing Heart": "This is a Healing Heart",
        "Sapphire Necklace": "This is a Sapphire Necklace",
        "Right Arm": "This is a Right Arm",
        "Left Arm": "This is a Left Arm",
        "Right Leg": "This is a Right Leg",
        "Left Leg": "This is a Left Leg",
        "Head": "This is a Head",
        "Heart": "This is a Heart",
        "Red Orb": "This is a Red Orb",
        "Yellow Orb": "This is a Yellow Orb",
        "Orange Orb": "This is a Orange Orb",
        "Green Orb": "This is a Green Orb",
        "Blue Orb": "This is a Blue Orb"
    } # This will have names and descriptions of items

    def describe_inventory(item):
        print(item + '\n - ' + InvDescriptions.descriptions[item])
