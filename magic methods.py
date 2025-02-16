#todo magic methods - dunder method(double underscore) __init__, __str__, __eq__
#todo                 they are automatically called by many of python's built in operations
#todo                 they allow developers to define or customize the behaviour of objects

class book:

    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"{self.title}, {self.author}, {self.price}"

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author and self.price == other.price

    def __add__(self, other):
        return (self.title + other.title, self.author + other.author, self.price + other.price)

    def __lt__(self, other):
        return self.price < other.price

    def __gt__(self, other):
        return self.price > other.price

    def __len__(self):
        return len(self.title)

    def __getitem__(self, key):
        if key == 0:
            return self.title
        elif key == 1:
            return self.author
        elif key == 2:
            return self.price
        else:
            return f"key = {key} is invalid"

    def __setitem__(self, index, value):
        self.title[index] = value

    def __delitem__(self, index):
        del self.title[index]

    def __contains__(self, item):
        return item in self.title

book1 = book("Python", "Joseph", 100)
book2 = book("Java", "Joseph", 100)
print(book1)
print(book1 == book2)
print(book1 + book2)
print(len(book1))
print(book1[1])
# book1[0] = "J"
print(book1)

