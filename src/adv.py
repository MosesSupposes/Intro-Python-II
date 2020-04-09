from room import Room, all_rooms
from player import Player
import sys
from functools import reduce


# Helpers
def display_room_info(room):
    print("\n" + "You have entered the " + room.name)
    print("\n" + room.description)

def display_available_items(room):
    if len(room.items) > 0:
        available_items = reduce(lambda acc, cur: acc + ", " + cur, room.items) 
        print("\n" + "Available items: " + available_items)
    else:
        print("\n " + "Available items: None")

""" 
TODO: Create a function that determines which available directions the player 
      is able to move in.
"""

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
hero = Player(all_rooms['outside'])
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.

print("Enter 'help' for directions. \n\n\n")

while(True):
    display_room_info(hero.current_room)
    display_available_items(hero.current_room)
    next_room = input("\n\n\nChoose a direction to travel in \n")
    hero.move_to(next_room, all_rooms)

    if next_room.lower() == "q": 
        print("You have died of utter cowardice.")
        sys.exit()
    if next_room.lower() == "help":
        print("""
        ================================================================
        Naviagate through the game by choosing a direction when prompted.
        The available directions are [n, e, s, w]

        You can quit the game at any time by pressing the 'q' key
        ================================================================
        """)
        print("\n\n\n")
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

