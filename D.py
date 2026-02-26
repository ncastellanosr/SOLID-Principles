# Before applying the D principle:
# The dependancy of GeometryCalculator on Square is hard-coded

class Square:
    def get_area(self): return 100

class GeometryCalculator:
    def __init__(self):
        self.shape = Square()
    
    def result(self):
        print(f"The area is: {self.shape.get_area()}")


# After applying the D principle:
# Dependancy is now "injected"

class GeometryCalculator:
    def __init__(self, shape):
        self.shape = shape

    def result(self):
        print(f"Area: {self.shape.get_area()}")


# Now we can swap shapes without changing the Calculator class

circ = Square()
app = GeometryCalculator(circ)
app.result()
