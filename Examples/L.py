# Before applying the L principle:
# The Square breaks the behavior of the Rectangle class
# The get_area method will not work for the Square instances

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

class Square(Rectangle):
    def set_width(self, width):
        self.width = self.height = width

    def set_height(self, height):
        self.width = self.height = height

def double_the_width(rect):
    rect.set_width(10)


# After applying the L principle
# We generalize the Polygon concept so both Rectangles and Squares can
# inherit its porperties correctly

class Shape:
    def get_area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def get_area(self):
        return self.width * self.height

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def get_area(self):
        return self.side * self.side
