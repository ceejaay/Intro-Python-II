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
        print("you are trying to pick something up.")
        # if command == 'get':
        #     self.player.get()

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
        elif text == 'l' or text == 'L':
            print(f"You are in {self.player.room.location}, It {self.player.room.desc}")
        elif text == 'q' or text == 'Q':
            print('Thanks for playing')
            self.playing = False
        else:
            self.error_response()



