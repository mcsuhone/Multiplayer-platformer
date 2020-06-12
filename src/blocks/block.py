import sys
sys.path.append('../')
import pyglet
from hitbox import Hitbox

texture = pyglet.image.load("./textures/stone.png")
texture2 = pyglet.image.load("./textures/grass.png")
texture3 = pyglet.image.load("./textures/dirt.png")
textures = {}
textures[0] = texture
textures[1] = texture2
textures[2] = texture3

class Block(pyglet.sprite.Sprite):
    def __init__(self, x, y, texture_id = 0):
        super().__init__(textures[texture_id], x, y)
        self.hitbox = Hitbox(x, y, self.image.width, self.image.height)

