#todo importing class from this file

class Phone:
    def __init__(self, brand, model, colour, price):
        self.brand=brand
        self.model=model
        self.colour=colour
        self.price=price

    def sold(self):
        print(self.brand, self.model, "is sold")
    def not_sold(self):
        print(self.brand, self.model, "is not sold")
    def display(self):
        print(self.brand, self.model, self.colour, self.price)