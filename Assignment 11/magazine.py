class Magazine:
    def __init__(self, name,chief_editor):
        self.name = name
        self.chief_editor = chief_editor


    def print_information(self):
        print(f"Name: {self.name}")
        print(f"Author: {self.chief_editor}\n")
