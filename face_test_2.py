import math
class Circle:
    def __init__(self,radius):
        self.radius = radius

    def area(self,radius):
        p = radius * radius * math.pi
        return  p

A = Circle(2)
k = A.area(2)
print(k)