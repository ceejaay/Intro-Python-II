
class Parser:

    def error_response(self):
        print("Sorry, I don't recognize that. \n Try N, S, E, or W. \n Or if you want to quit type Q/q")
        # return "Sorry, I don't recognize that. \n Try N, S, E, or W. \n Or if you want to quit type Q/q"

    def get_text(self, text):
        if text == 'n' or text == 'N':
            return "You go north"

        elif text == 's' or text == 'S':
            return "s"
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


