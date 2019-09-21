

class Controls:
    show_backpack = False

    def open_backpack(player):
        player.backpack.describe()

    def user_gameplay_options():
        user_option = 'Press any key to return' if show_backpack \
        else 'Press B to open backpack and view items'

        print(user_option)

    def view_items(player):
        Controls.open_backpack(player)
        Controls.user_gameplay_options()
