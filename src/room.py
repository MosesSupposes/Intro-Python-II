# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, **kwargs):
        self.name = kwargs["name"]
        self.description = kwargs["description"]
        self.items = kwargs["items"]

# Declare all the rooms

all_rooms = {
    'outside':  Room(name="Outside Cave Entrance",
                     description="North of you, the cave mount beckons",
                     items=["stick", "heavy stone"]),

    'foyer':    Room(name="Foyer", 
                     description="""Dim light filters in from the south. Dusty
passages run north and east.""", 
                     items=["rope", "lit torch"]),

    'overlook': Room(name="Grand Overlook", 
                     description="""A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
                      items=["knight's armour", "shield", "sword", "dagger"]),

    'narrow':   Room(name="Narrow Passage", 
                     description="""The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
                      items=[]),

    'treasure': Room(name="Treasure Chamber", 
                     description="""You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
                      items=["empty treasure chest"]),
}


# Link rooms together

all_rooms['outside'].n_to = all_rooms['foyer']
all_rooms['foyer'].s_to = all_rooms['outside']
all_rooms['foyer'].n_to = all_rooms['overlook']
all_rooms['foyer'].e_to = all_rooms['narrow']
all_rooms['overlook'].s_to = all_rooms['foyer']
all_rooms['narrow'].w_to = all_rooms['foyer']
all_rooms['narrow'].n_to = all_rooms['treasure']
all_rooms['treasure'].s_to = all_rooms['narrow']
