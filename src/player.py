# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, room):
        self.room = room
        self.items = []


    def get(self, item_name):
        if item_name in self.room.list_of_items:
            self.items.append(items[item_name])
            self.room.list_of_items.remove(items[item_name])




