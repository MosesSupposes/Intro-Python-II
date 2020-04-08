# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, starting_point):
        self.room = starting_point 

    def move_to(self, next_direction, all_rooms):
        invalid_direction_msg = "Sorry, you can't go there."

        if self.room == all_rooms['outside']:
            if next_direction == "n":
                self.room = all_rooms['outside'].n_to
            else:
                if (next_direction != "help"): 
                    print(invalid_direction_msg) 
                
