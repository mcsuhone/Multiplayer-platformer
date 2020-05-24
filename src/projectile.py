from vector import Vector
import pyglet


class Projectile(pyglet.sprite.Sprite):
    def __init__(self, x, y, direction):
        texture = pyglet.image.load("./textures/bullet.png")
        super().__init__(texture, x, y)
        self.direction = direction
        