from vector import Vector
from constants import Constants



class Physics():
    def __init__(self, velocity = Vector(0,0), acceleration = Vector(0,0)):
        
        self.velocity = velocity
        self.acceleration = acceleration
        self.in_air = True
        self.weight = 1

        self.max_speed = 3

    def stop(self):
        self.velocity = Vector(0,0)

    def fall(self):
        if self.in_air and self.velocity.y > -Constants.max_fall_speed:
            self.velocity.y -= Constants.gravity*self.weight

    def accelerate(self, dir_vector):
        self.velocity = self.velocity + dir_vector
        
        if self.velocity.x > self.max_speed:
            self.velocity.x = self.max_speed
        elif self.velocity.x < -self.max_speed:
            self.velocity.x = -self.max_speed

    def decelerate(self, amount = Constants.friction):
        self.velocity.x *= amount
        if self.velocity.length() < 2:
            self.velocity.x = 0