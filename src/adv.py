from room import Room
from player import Player
from parser import Parser
from data import room
# Declare all the rooms


# initalize the player
# intitialize the items in rooms
# initialize the relation of the rooms
# initialize the dictionary
directions = ('n', 's', 'e', 'w',)
keywords = ('look', 'get', 'help',)


p = Player(room['outside'])

par = Parser(p)

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:

while par.playing: 
    command = input(">> ").lower().split()
    if len(command) == 0:
        par.error_response()
    elif len(command) == 1:
        if command[0] in directions:
            par.get_text(command[0])
        elif command[0] in keywords:
            par.execute_command(command[0])
    elif command[0] == 'q':
        par.playing = False
    else:
        par.error_response()

    # if len(command) > 2:
    #     print("don't understand")
    #     par.error_response()
    # elif len(command) == 0:
    #     par.error_response()
    # elif len(command) == 2:
    #     if command[0] in directions:
    #         par.get_text(command[0])
    #     elif command[0] in keywords:
    #         par.execute_command(command[0])
    #     else:
    #         par.error_response()
    # elif len(command) == 1:
    #     par.get_text(command[0])
    # else:
    #     par.error_response()



#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
