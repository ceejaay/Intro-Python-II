from room import Room
from item import Item
items = {'rope': Item('rope', 'scratchy rope'),
        'flashlight': Item('flashlight', 'batteries are dead'),
        'key': Item('key', 'possibly to and old toyota'),
        'batteries': Item('batteries', 'If only you had a flashlight to put them in.'),
        'ration': Item('ration', 'They smell bad.'),
        'stake': Item('stake', 'Run of the mill stake for vampire hunting.'),

        }

room = {


    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons", items['rope']),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", items['flashlight']),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", items['key']),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", items['ration']),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", items['batteries']),
    'graveyard': Room("Graveyard", "Mist swirls around you. The gravestones quiver, the dead will burst forth any mooment", items['stake'])
}

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
room['outside'].e_to = room['graveyard']
room['graveyard'].w_to = room['outside']



print( hasattr(room['outside'], 's_to') )
