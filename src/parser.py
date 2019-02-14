from data import room
from room import Room
class Parser:
    def __init__(self, player):
        self.player = player
        self.user_input = ""
        self.text = None
        self.message = ""
        self.directions = ('n', 's', 'e', 'w',)
        self.keywords = ('look', 'get', 'help',)
        self.playing = True




    def execute_command(self, command):
        first_word = command[0]
        second_word = command[1]
        if first_word == 'get':
            if second_word in self.player.room.list_of_items:
                player.get(second_word)
            else:
                print(f"There is no {second_word} here.")
        else:
            self.error_response()

    def error_response(self):
        print("Sorry, I don't recognize that. \n Try N, S, E, or W. \n Or if you want to quit type Q")

    def check_room(self, room, direction):
        if hasattr(room, direction):
            return True
        else:
            return False


    def get_text(self, text):
        if text == 'n' or text == 'N':
            if self.check_room(self.player.room, 'n_to'):
                self.player.room.n_to
                self.player.room = self.player.room.n_to
                print(f"You are in {self.player.room.location}, {self.player.room.desc}")
            else:
                print("You can't go that way")

        elif text == 's' or text == 'S':
            if self.check_room(self.player.room, 's_to'):
                self.player.room.s_to
                self.player.room = self.player.room.s_to
                print(f"You are in {self.player.room.location}, {self.player.room.desc}")
            else:
                print("You can't go that way")

        elif text == 'w' or text == 'W':
            if self.check_room(self.player.room, 'w_to'):
                self.player.room.w_to
                self.player.room = self.player.room.w_to
                print(f"You are in {self.player.room.location}, {self.player.room.desc}")
            else:
                print("You can't go that way")
        elif text == 'e' or text == 'E':
            if self.check_room(self.player.room, 'e_to'):
                self.player.room.e_to
                self.player.room = self.player.room.e_to
                print(f"You are in {self.player.room.location}, {self.player.room.desc}")
            else:
                print("You can't go that way")
        elif text == 'l' or text == 'look':
            print(f"You are in {self.player.room.location}, It {self.player.room.desc}")
            if len(self.player.room.list_of_items) > 0:
                for item in self.player.room.list_of_items:
                    print(f"You see a {item.name}")
        elif text == 'get':
            print('What do you want to get? \n Use look to look around')
        elif text == 'q' or text == 'Q':
            print('Thanks for playing')
            self.playing = False
        else:
            self.error_response()



