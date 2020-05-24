import math



class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def length(self):
        return math.sqrt(math.pow(self.x,2)+math.pow(self.x,2))

    def plus(self, vector):
        self.x += vector.x
        self.y += vector.y

    def minus(self, vector):
        self.x -= vector.x
        self.y -= vector.y

    def scale(self, amount):
        self.x *= amount
        self.y *= amount

    def make_unit(self):
        length = self.length()
        self.x = self.x / length
        self.y = self.y / length