import math



class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def length(self):
        return math.sqrt(math.pow(self.x,2)+math.pow(self.x,2))

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def scale(self, amount):
        self.x *= amount
        self.y *= amount


    def make_unit(self):
        length = self.length()
        self.x = self.x / length
        self.y = self.y / length

    def x_dir(self):
        if self.x >= 0:
            return 1
        else:
            return -1
    
    def __str__(self):
        return "[" + str(self.x) + ", " + str(self.y) + "]"