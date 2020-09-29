from vector import Vector



class Physics():
    def __init__(self, velocity = Vector(0,0), acceleration = Vector(0,0)):
        self.gravity = Vector(0,1)
        self.velocity = velocity
        self.acceleration = acceleration
        self.in_air = True

        self.max_speed = 3
        self.friction = 0.5

    def stop(self):
        self.velocity = Vector(0,0)

    def fall(self):
        if self.in_air:
            self.velocity = self.velocity - self.gravity

    def accelerate(self, dir_vector):
        self.velocity = self.velocity + dir_vector
        
        if self.velocity.x > self.max_speed:
            self.velocity.x = self.max_speed
        elif self.velocity.x < -self.max_speed:
            self.velocity.x = -self.max_speed

    def decelerate(self):
        self.velocity.x *= self.friction
        if self.velocity.length() < 2:
            self.velocity.x = 0
