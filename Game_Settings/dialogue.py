class Narration:

    def level_prologue(level_num):
        start_narration = {
            "1": "Are you the one they call {name}? I need your help. I've had some key items taken\
            from me. I believe they're in each of these rooms. Return these items to me {name}, \
            and I can give you something in return...",
            "2": "Ahh Yellow! The color of happiness! Friendship! I feel so yellow, don't you? \
            What's your name again? {name}? Right. Well...I need more yellow. There's some more \
            in here somewhere...",
            "3": "{message} Oh I'm sorry {name}, I've been speaking backwards and not in the \
            right frame of mind. I need orange ASAP. I'm losing my mind!",
            "4": "Money, nature, healing...you know {name}, life itself is surrounded by the \
            color green. I'm one step closer to ridding the world of all sickness! I just need \
            a little more...",
            "5": "I'm sad all the time {name}...I'm just brooding in my sorrow. I don't know \
            how else I can feel. I used to know the happier sides of blue, but they were \
            stolen from me. But now that you're here, maybe you can help me get them back..."
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
