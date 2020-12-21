import sys 
sys.path.append('..')

from vector import Vector
from src.objects.object import Object
import pyglet


class Projectile(Object):
    def __init__(self, x, y, direction, batch = None, owner_id = None):
        texture_id = 20
        super().__init__(texture_id, x, y, batch = batch)
        self.physics.velocity = direction.scale(2)
        self.owner = owner_id
        self.physics.weight = 0.1
        
    def update(self, dt, obstacles):
        if self.physics.in_air:
            self.physics.fall()
        else:
            self.physics.decelerate(0.5)
        
        self.move(dt, obstacles)

class Bullet(Projectile):
    def __init__(self, x, y, direction, batch = None, owner_id = None):
        texture_id = 20
        direction = direction.scale(8)
        super().__init__(x, y, direction, texture_id, batch, owner_id)