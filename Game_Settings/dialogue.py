class Narration:
    level_num = 1

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


class InvDescriptions:
    descriptions = {
        "Item 1": "This is item one",
        "Item 2": "This is item two",
        "Item 3": "This is item three",
        "Major Item": "This is a major item"
    } # This will have names and descriptions of items
