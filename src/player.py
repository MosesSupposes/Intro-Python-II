# Write a class to hold player information, e.g. what room they are in
# currently.

import sys
from functools import reduce

class Player:
    def __init__(self, starting_point):
        self.current_room = starting_point 
        self.inventory = []

    def move_to(self, next_direction, all_rooms):
        next_direction = next_direction.lower()

        def print_invalid_direction():
            invalid_direction_msg = "Sorry, you can't go there. \n\n"
            if next_direction == "help" or next_direction == "q":
                pass
            else:
                 print(invalid_direction_msg)



        if self.current_room == all_rooms['outside']:
            if next_direction == "n":
                self.current_room = all_rooms['outside'].n_to

            else:
                print_invalid_direction()

        elif self.current_room == all_rooms['foyer']:
            if next_direction == "n":
                self.current_room = all_rooms["foyer"].n_to

            elif next_direction == "e":
                self.current_room = all_rooms["foyer"].e_to
            
            elif next_direction == "s":
                self.current_room = all_rooms["foyer"].s_to
            
            else:
                print_invalid_direction()

        elif self.current_room == all_rooms["overlook"]:
            if next_direction == "s":
                self.current_room = all_rooms["overlook"].s_to
            
            else: 
                print_invalid_direction()
                
        elif self.current_room == all_rooms["narrow"]:
            if next_direction == "n":
                self.current_room = all_rooms["narrow"].n_to
            
            elif next_direction == "w":
                self.current_room = all_rooms["narrow"].w_to

            else:
                print_invalid_direction()

        elif self.current_room == all_rooms["treasure"]:
            if next_direction == "s":
                self.current_room = all_rooms["treasure"].s_to  
            
            else:
                print_invalid_direction()
        
        else:
            print("Whoops, you fell off a cliff and died.")
            sys.exit()

    def display_inventory(self):
        if len(self.inventory) > 0:
            print("\n" + "Inventory: " + reduce(lambda acc, cur: acc + ", " + cur, self.inventory))
            
        else:
            print("There are no items in your inventory.")

    def pickup_item(self, item):
        if item not in self.inventory and item in self.current_room.items:
            self.inventory.append(item)
            print("\n" + "You picked up a " + item)
            self.display_inventory()

        elif item not in self.current_room.items:
            print("There is no " + item + " in the room.")

        else: 
            print("You already picked up the " + item + ".")

    def drop_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            print("\n" + "You dropped a " + item + ".")
            self.display_inventory()

        else:
            print("\n" + "You don't have a " + item + " in your possession.")