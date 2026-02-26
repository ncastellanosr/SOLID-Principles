# Before applying the I principle:
# A preview to implement 3D figures in the future forces 2D figures
# To behave in that way too, which is never going to be used

class Polygon:
    def area(self): pass
    def volume(self): pass

class Triangle(Polygon):
    def area(self): print("Calculating area...")
    def volume(self): raise Exception("Triangles don't have volume!")


# After applying the I principle:
# Now 2D classes won't have an extra feature they will not use

class AreaOnly:
    def area(self): pass

class VolumeEnabled:
    def volume(self): pass

class FlatTriangle(AreaOnly):
    def area(self): print("Calculating 2D area.")

class Cube(AreaOnly, VolumeEnabled):
    def area(self): print("Surface area...")
    def volume(self): print("3D Volume...")
