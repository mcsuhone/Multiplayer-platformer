import math



class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def length(self):
        return math.sqrt(abs(self.x*self.x)+abs(self.y*self.y))

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def scale(self, amount):
        return Vector(self.x * amount, self.y * amount)

    def make_unit(self):
        length = self.length()
        if length == 0:
            return Vector(0, 0)
        return Vector(self.x / length, self.y / length)

    def angle_x_axis(self):
        """Returns angle to x-axis from -180 to 180 in degrees"""
        return math.atan2(self.y, self.x) * 180 / math.pi

    def distance(self, other):
        return Vector(abs(other.x - self.x), abs(other.y - self.y)).length()

    def __str__(self):
        return "[" + str(self.x) + ", " + str(self.y) + "]"