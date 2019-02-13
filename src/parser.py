from data import room
class Parser:
    def __init__(self, rm, location):
        self.rm = rm
        self.location = location 

    def error_response(self):
        print("Sorry, I don't recognize that. \n Try N, S, E, or W. \n Or if you want to quit type Q/q")
        # return "Sorry, I don't recognize that. \n Try N, S, E, or W. \n Or if you want to quit type Q/q"

    def get_text(self, text):
        if text == 'n' or text == 'N':
            self.location = self.rm['foyer']
        elif text == 's' or text == 'S':
            return "south"
        elif text == 'w' or text == 'W':
            return "w"
        elif text == 'e' or text == 'E':
            return "e"
        elif text == 'l' or text == 'L':
            return "l"
        elif text == 'q' or text == 'Q':
            return False
        else:
            self.error_response()



p = Parser(room, room['outside'])
print(p.rm)
print(p.location)
print(p.get_text('n'))
print(p.location)
