# Write a class to hold player information, e.g. what room they are in
# currently.
from data import items

class Player:
    def __init__(self, room):
        self.room = room
        self.items = []


    def get(self, item_name):
        for thing in self.room.list_of_items:
            if thing.name == item_name:
                self.items.append(items[item_name])
                self.room.list_of_items.remove(items[item_name])
            else:
                print(f"There is no {item_name} in this room.")
        print("Here's the things in your inventory")
        for player_items in self.items:
            print(player_items.name)




