import math

class Vetor2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, outro):
        return Vetor2D(
            self.x + outro.x,
            self.y + outro.y
        )
    def __eq__(self, outro):
        return self.x == outro.x and self.y == outro.y

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)

v1 = Vetor2D(3, 4)
v2 = Vetor2D(1, 2)

print("v1 =", v1)
print("v2 =", v2)

soma = v1 + v2
print("v1 + v2 =", soma)

print("v1 == v2 ?", v1 == v2)

v3 = Vetor2D(3, 4)
print("v1 == v3 ?", v1 == v3)

print("Magnitude de v1 =", v1.magnitude())