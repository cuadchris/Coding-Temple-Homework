class Strings():

    def __init__(self, string):
        self.string = string

    def get_String(self):
        self.string = input("Set a new string: ")

    def print_String(self):
        print(self.string.upper())