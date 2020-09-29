import sys 
sys.path.append('..')

import pyglet
from src.objects.hitbox import Hitbox
from src.vector import Vector
from src.physics import Physics

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
        self.physics = Physics()

    def move(self, dt = 0.01):
        self.x += self.physics.velocity.x * dt * 100
        self.y += self.physics.velocity.y * dt * 100
        self.hitbox.x = self.x
        self.hitbox.y = self.y

    def move_to(self, x, y):
        self.x = x
        self.y = y
        self.hitbox.x = self.x
        self.hitbox.y = self.y

    def check_collisions(self, objects):
        future_hitbox = Hitbox(self.x + self.physics.velocity.x, self.y + self.physics.velocity.y, self.hitbox.width, self.hitbox.height)
        for obj in objects:
            future_hitbox.intersects(obj.hitbox)

        if future_hitbox.collision_directions['left']:
            print("left")
            self.physics.stop()
        if future_hitbox.collision_directions['right']:
            print("right")
            self.physics.stop()
        if future_hitbox.collision_directions['top']:
            print("top")
            self.physics.stop()
        if future_hitbox.collision_directions['bottom']:
            print("bottom")
            self.physics.stop()
            self.physics.in_air = False

    def update_movement(self, dt):
        self.move(dt)
        self.physics.fall()
        

        

