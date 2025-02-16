#todo super() - function used in a child class to call methods from a parent class(superclass)
#todo           allows you to extend the functionality of inheritance method
# from turtle import Shape  # Note: Commented out to avoid conflicts


class Shape:
    def __init__(self,name, colour, is_filled):
        self.name = name
        self.colour = colour
        self.is_filled = is_filled

    def describe(self):
     print(f"Created {self.name} with colour {self.colour} and is filled: {self.is_filled}")

class Square(Shape):

    def __init__(self, name, colour, is_filled, side):
        super().__init__(name, colour, is_filled)
        self.side = side

    def describe(self):
     super().describe()
     print(f"The side of the square is {self.side}")

class Triangle(Shape):
 def __init__(self,name, colour, is_filled, base, height):
        super().__init__(name, colour, is_filled)
        self.base = base
        self.height = height

class Circle(Shape):
  def __init__(self,name, colour, is_filled, radius):
        super().__init__(name, colour, is_filled)
        self.radius = radius


square = Square("Square", "Blue", True, 10)
triangle = Triangle("Triangle", "Red", False, 5, 10)
circle = Circle("Circle", "Yellow", True, 5)

square.describe()
triangle.describe()
circle.describe()

print(square.side)
print(triangle.base)
print(circle.radius)




