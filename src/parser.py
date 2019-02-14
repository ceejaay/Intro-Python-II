from data import room
class Parser:
    def __init__(self, player):
        self.player = player

    def error_response(self):
        print("Sorry, I don't recognize that. \n Try N, S, E, or W. \n Or if you want to quit type Q/q")

    # def check_room(room):
    #     if type(room) == 'room.Room'
    #         return True
    #     else:
    #         return False

    def get_text(self, text):
        if text == 'n' or text == 'N':
            print(type(self.player.room.n_to) is room.Room)
            self.player.room.n_to
            self.player.room = self.player.room.n_to
            print(f"You are in {self.player.room.location}, {self.player.room.desc}")
        elif text == 's' or text == 'S':
            self.player.room.s_to
            self.player.room = self.player.room.s_to
            print(f"You are in {self.player.room.location}, It {self.player.room.desc}")
        elif text == 'w' or text == 'W':
            print(f"You are in {self.player.room.location}, It {self.player.room.desc}")
        elif text == 'e' or text == 'E':
            print(f"You are in {self.player.room.location}, It {self.player.room.desc}")
        elif text == 'l' or text == 'L':
            print(f"You are in {self.player.room.location}, It {self.player.room.desc}")
        elif text == 'q' or text == 'Q':
            return False
        else:
            self.error_response()



