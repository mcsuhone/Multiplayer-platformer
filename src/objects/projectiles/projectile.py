import sys 
sys.path.append('..')

from vector import Vector
from src.objects.object import Object
import pyglet


class Projectile(Object):
    def __init__(self, x, y, direction, owner_id = None, batch = None):
        texture_id = 20
        super().__init__(texture_id, x, y, batch = batch)
        self.direction = direction
        self.owner = owner_id
        