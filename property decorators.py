#todo @property - decorator used to define a method as a property (it can be accessed like an attribute)
#todo             benefit: add additional logic when read, write, or delete attributes
#todo             gives you getter, setter, and deleter method

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        return f"{self._width:.1f}cm"
    @property
    def height(self):
        return f"{self._height:.1f}cm"
    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater than 0")
    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be greater than 0")
    @width.deleter
    def width(self):
        del self._width
    @height.deleter
    def height(self):
        del self._height

rectangle = Rectangle(5, 10)

# print(rectangle._width)
# print(rectangle._height)

rectangle.width = 10
rectangle.height = 20
del rectangle.width
del rectangle.height


