class Poly_Area:
    def __init__(self,perimeter,approach):
        self.perimeter = perimeter
        self.approach = approach
    def displayInfo(self):
        print(f"Area of Polygon is {0.5*self.perimeter*self.approach}")

p1 = Poly_Area(20,10)
p1.displayInfo()