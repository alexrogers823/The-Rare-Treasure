

def intro():
    # some stuff here
    create_character()
    gameplay()

def create_character():
    pass

def gameplay():
    if level < 6:
        play_level(level)
    else:
        final_level()

def play_level(level_num):
    # Rapid fire questions
    if all_items_collected == False:
        door_num = input('Which door do you want to open?\n\n')
        validate_door(door_num)
        enter_door()
    else:
        exchange_items()

def final_level():
    max_items = 5
    # Ask for password (from the items)
    if (you still have items left):
        item = input('{} has {} item{} to sacrifice. Choose which one to give.\n\n')
        exchange_major_item(item)
    else:
        credits(max_items)

def credits(number):
    show_ending(number)
    display_credits()
