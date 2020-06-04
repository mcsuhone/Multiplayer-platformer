import sys 
sys.path.append('..')

import pyglet
from src.objects.hitbox import Hitbox

#Player sprites
texture = pyglet.image.load("./textures/derbiili.png")
texture2 = pyglet.image.load("./textures/bug.png")
texture3 = pyglet.image.load("./textures/snake.png")
#Blocks
texture4 = pyglet.image.load("./textures/stone.png")
texture5 = pyglet.image.load("./textures/grass.png")
texture6 = pyglet.image.load("./textures/dirt.png")
#Projectiles
texture7 = pyglet.image.load("./textures/bullet.png")
#Add them to dictionary
textures = {}
textures[0] = texture
textures[1] = texture2
textures[2] = texture3

textures[10] = texture4
textures[11] = texture5
textures[12] = texture6

textures[20] = texture7

class Object(pyglet.sprite.Sprite):
    def __init__(self, texture_id, x, y, batch = None, collidable = True):
        texture = textures[texture_id]
        super().__init__(texture, x, y, batch = batch)
        self.hitbox = Hitbox(x, y, texture.width, texture.height)
        self.collidable = True
