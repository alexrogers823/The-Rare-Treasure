from Game_Settings.game_interaction import Misc, Summary
from Game_Settings.player_info import Player
from Game_Settings.dialogue import Narration
import time

def intro():
    # some stuff here
    title = '{1}{0}{1}'.format('The Rare Treasure', '~'*3)
    print(title)
    player = create_character()
    gameplay(player)

def create_character():
    player_name = input('What is your name?\n')
    player = Player(player_name)
    return player


def gameplay(player):
    if Misc.game_level < 6:
        play_level(player)
    else:
        final_level(player)

def play_level(player):
    starting_dialogue = Narration.level_prologue(Misc.game_level)
    print(starting_dialogue.format(
        name=player.name,
        message="Hey I really need your help!"[::-1]
        ))
    # Rapid fire questions
    while Misc.items_collected == False:
        Misc.select_door()
        Misc.validate_door()
        Misc.enter_door(player) #Will change later
        Misc.check_item_count()

    exchange_items(player)
    # Narration.level_epilogue(Misc.game_level)

# def final_level():
#     max_items = 5
#     # Ask for password (from the items)
#     if (you still have items left):
#         item = input('{} has {} item{} to sacrifice. Choose which one to give.\n\n')
#         exchange_major_item(item)
#     else:
#         credits(max_items)
#
# def credits(number):
#     show_ending(number)
#     display_credits()


def exchange_items(player):
    print('Exchanged\n')
    time.sleep(1)
    print(Narration.level_epilogue(Misc.game_level))
    Summary.level_summary(player)
    Misc.level_up()
    play_level(player)



intro()
# play_level()
