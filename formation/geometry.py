class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle:

    def __init__(self, largeur, longueur, origin:Point=Point(0,0)):
        self.largeur = largeur
        self.longueur = longueur
        self.origin = origin

    def surface(self):
        return self.largeur * self.longueur

    def __repr__(self):
        return f"Rectangle {self.largeur}x{self.longueur}"

class Carre(Rectangle):

    def __init__(self, cote):
        super().__init__(cote, cote)

r1 = Rectangle(2,3, Point(3,2))
print(r1)
print(r1.surface())
c1 = Carre(3)
print(c1.surface())