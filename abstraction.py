from abc import ABC, abstractmethod

class Polygon(ABC):

    @abstractmethod
    def sides(self):
        pass

class Triangle(Polygon):
    def sides(self):
        print(f"A Triangle has 3 sides")

    def area(self):
        print(F"The formula for Area of a triangle is 1/2 * b * h")

class Square(Polygon):
    def sides(self):
        print(f"A Square has 4 sides")
        
    def area(self):
        print(F"The formula for Area of a Square is L**2")

class Hexagon(Polygon):
    def sides(self):
        print(f"A Hexagon has 6 sides")

class Pentagon(Polygon):
    def sides(self):
        print(f"A Pentagon has 5 sides")
        

t1 = Triangle()
s1 = Square()
h1 = Hexagon()
p1 = Pentagon()

t1.sides()
t1.area()

s1.sides()
s1.area()

h1.sides()

p1.sides()