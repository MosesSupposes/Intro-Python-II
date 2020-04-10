import sys
from functools import reduce

from room import Room, all_rooms
from player import Player


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

def parse_item_to_pickup_or_remove(input):
    words = input.rsplit(" ")

    if "get" in words:
        words.remove("get")

    if "drop" in words:
        words.remove("drop")
    
    item = reduce(lambda acc, cur: acc + " " +  cur, words)

    return item 
    


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
    
    command = input("\n\n\nChoose a direction to travel in \n")

    if command == "n" or command == "e" or command == "s" or command == "w":
        hero.move_to(command, all_rooms)
    
    elif "get" in command:
        hero.pickup_item(parse_item_to_pickup_or_remove(command))
    
    elif "drop" in command:
        hero.drop_item(parse_item_to_pickup_or_remove(command))


    elif command.lower() == "q": 
        print("You have died of utter cowardice.")
        sys.exit()

    elif command.lower() == "help":
        print("""
        ================================================================
        Naviagate through the game by choosing a direction when prompted.
        The available directions are [n, e, s, w]
        If there are items in a room, you can pick them up with the 
        command "get [ITEM_NAME]". You can drop an item with the command
        "drop [ITEM_NAME]".

        You can quit the game at any time by pressing the 'q' key
        ================================================================
        """)
        print("\n\n\n")

    else: 
        print("Not a valid command. Enter 'help' for instructions.")
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
