class Inventory:
    def __init__(self):
        self.inv_list = []


    def describe(self):
        if self.inv_list:
            for value in self.inv_list:
                describe_inventory(value) # From dialogue.py
        else:
            print("There's nothing in here yet. Start collecting some items!")


    def add(self, item):
        self.inv_list.append(item)


    def relinquish(self, item):
        self.inv_list.remove(item)
