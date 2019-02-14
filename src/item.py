class Item:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc


    def on_take(self):
        print(f"This is a {self.name}.")

    def on_drop(self):
        print(f"You dropped {self.name}.")
