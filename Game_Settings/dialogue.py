class Narration:
    level = 1

    def beginning(level):
        start_narration = {
            "1": "This begins the first level",
            "2": "This begins the second level",
            "3": "This begins the third level",
            "4": "This begins the fourth level",
            "5": "This begins the fifth level"
        }

        return start_narration[str(level)]

    def ending(level):
        end_narration = {
            "1": "This ends the first level",
            "2": "This ends the second level",
            "3": "This ends the third level",
            "4": "This ends the fourth level",
            "5": "This ends the fifth level"
        }

        return end_narration[str(level)]


class InvDescriptions:
    descriptions = {} # This will have names and descriptions of items