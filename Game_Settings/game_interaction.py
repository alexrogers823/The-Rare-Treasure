from .math_problems import Problems
from .items import Inventory

class Misc:
    game_level = 1
    item_count = 0
    item_goal = 3
    items_collected = False #Temporary
    door_options = ['1', '2', '3']
    selected_door = ''

    def display_options():
        string = ''
        for num in Misc.door_options:
            string = string + '> ' + num + '\n'

        return string

    def select_door():
        door_num = input('Which door do you want to open?\n' + Misc.display_options())
        Misc.selected_door = door_num
        return door_num

    def validate_door(): #Prevent continuation if invalid
        if Misc.selected_door not in Misc.door_options:
            print('Not a valid door')

    def enter_door(player):
        prize = Inventory.item_list[str(Misc.game_level)][int(Misc.selected_door)-1]
        question = Problems.word_problem()
        answer = input(question + '\n')
        if int(answer) == 4: #Temporary
            print('Correct! You received the item: {}'.format(prize))
            player.backpack.add(prize)
            Misc.item_count += 1
            Misc.update_door_options()
        else:
            print('That is incorrect')

    def update_door_options():
        Misc.door_options.remove(Misc.selected_door)

    def check_item_count():
        if Misc.item_count == Misc.item_goal:
            Misc.items_collected = True

    def level_up():
        Misc.game_level += 1
        Misc.reset_variables()

    def reset_variables():
        Misc.item_count = 0
        Misc.items_collected = False
        Misc.door_options = [str(n) for n in range(1, 3 + Misc.game_level)]
        Misc.item_goal = len(Misc.door_options)
        Misc.selected_door = ''


class Summary:
    def level_summary(player):
        print('Level {} complete'.format(Misc.game_level))
        Summary.player_summary(player)


    def player_summary(player):
        print('{}\'s Stats:'.format(player.name))
        print(player.silver)
        print('Items in inventory:')
        player.backpack.describe()
