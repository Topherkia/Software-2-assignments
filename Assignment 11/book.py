class Book:
    def __init__(self, name, author, page_count):
        self.name = name
        self.author = author
        self.page_count = page_count

    def print_information(self):
        print(f"Name: {self.name}")
        print(f"Author: {self.author}")
        print(f"Page Count: {self.page_count}\n")

