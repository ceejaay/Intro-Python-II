# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, location, desc, item=None):
        self.location = location
        self.desc = desc
        self.list_of_items = []
        self.list_of_items.append(item)

    def print_location(self):
        print(f"You are in the {self.location}, {self.desc}")





