# Write a class to hold player information, e.g. what room they are in
# currently.

import sys

class Player:
    def __init__(self, starting_point):
        self.current_room = starting_point 

    def move_to(self, next_direction, all_rooms):
        def print_invalid_direction():
            invalid_direction_msg = "Sorry, you can't go there. \n\n"
            if (next_direction != "help"):
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