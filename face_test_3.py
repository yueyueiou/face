import math
class Triangle:
    def __init__(self,Short_edge,Long_edge):
        self.Short_edge = Short_edge
        self.Long_edge = Long_edge

    def area(self):
        Short = self.Short_edge * self.Short_edge
        Long = self.Long_edge * self.Long_edge
        result = math.sqrt(Short + Long)
        return  result

P = Triangle(3,4)
print(P.area())