#todo polymorphism - greek word that means to have "many faces or forms"
#todo                poly = many
#todo                Morphe = form
#todo                TWO WAYS TO ACHIEVE POLYMORPHISM
#todo                1)Inheritance - an object can be treated of same type as a parent class
#todo                2)"Duck Typing" - object must have necessary attributes and methods


class shape:

    def area(self):
        pass

class circle(shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class rectangle(shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class square(shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class pizza(circle):
    def __init__(self,radius,toppings):
        super().__init__(radius)
        self.toppings = toppings

shapes = [circle(5), rectangle(10,20), square(10), pizza(15,["cheese","tomatoes"])]

for shape in shapes:
    print(shape.area())
