
class Parser:
    def __init__(self):
        self.name = 'Dungeon Master'


    def error_response(self):
        print("Sorry, I don't recognize that. \n Try N, S, E, or W. \n Or if you want to quit type Q/q")
        # return "Sorry, I don't recognize that. \n Try N, S, E, or W. \n Or if you want to quit type Q/q"

    def get_text(self, text):
        if text == 'n' or text == 'N':
            return "You go north"
        elif text == 's' or text == 'S':
            return "You go south"
        elif text == 'w' or text == 'W':
            return "You go West"
        elif text == 'e' or text == 'E':
            return "You go East"
        elif text == 'l' or text == 'L':
            return "You look around the room"
        elif text == 'q' or text == 'Q':
            return False
        else:
            self.error_response()


