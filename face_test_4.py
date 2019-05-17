import math
class Hexagon:
    def __init__(self,edge_long):
        self.edge_long = edge_long

    def cacculate_perimeter(self):
        return  self.edge_long * 6

H = Hexagon(3)
print(H.cacculate_perimeter())