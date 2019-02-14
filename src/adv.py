from room import Room
from player import Player
from parser import Parser
from data import room
# Declare all the rooms


# initalize the player
# intitialize the items in rooms
# initialize the relation of the rooms
# initialize the dictionary
r = Room('hello', "world")
print(type(r) is Room)

p = Player(room['outside'])

parse_text = Parser(p)

if type(p) is Player:
    print("Player")
#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:

while parse_text.get_text is not False:
    command = input(">> ")
    print(parse_text.get_text(command))

#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
