import sys 
sys.path.append('..')

import pyglet
from src.objects.hitbox import Hitbox
from src.vector import Vector
from src.physics import Physics

#Player sprites
texture = pyglet.image.load("./textures/derbiili.png") # 27x22 pixels
texture1 = pyglet.image.load("./textures/bug.png")
texture2 = pyglet.image.load("./textures/snake.png") # 24x24 pixels
#Blocks
texture10 = pyglet.image.load("./textures/stone.png") # 16x16
texture11 = pyglet.image.load("./textures/grass.png") # 16x16
texture12 = pyglet.image.load("./textures/dirt.png") # 16x16
#Projectiles
texture20 = pyglet.image.load("./textures/bullet.png")
#Add them to dictionary
textures = {}
textures[0] = texture
textures[1] = texture1
textures[2] = texture2

textures[10] = texture10
textures[11] = texture11
textures[12] = texture12

textures[20] = texture20

class Object(pyglet.sprite.Sprite):
    def __init__(self, texture_id, x, y, batch = None, collidable = True):
        texture = textures[texture_id]
        super().__init__(texture, x, y, batch = batch)
        self.hitbox = Hitbox(x, y, texture.width, texture.height)
        self.collidable = True
        self.physics = Physics()
        self.can_move = {'left':True, 'right':True, 'up':True, 'down':True}

    def move(self, dt, obstacles):
        self.check_collisions(dt, obstacles)

        self.x += self.physics.velocity.x * 100 * dt
        self.y += self.physics.velocity.y * 100 * dt
        self.hitbox.move_to(self.x, self.y)

    def move_to(self, x, y):
        self.x = x
        self.y = y
        self.hitbox.move_to(x, y)

    def check_collisions(self, dt, objects):
        print(self.pos(), " vel: ", self.physics.velocity)
        velocity = self.physics.velocity.scale(100 * dt)

        future_hitbox = Hitbox(self.x + velocity.x, self.y + velocity.y, self.width, self.height)

        self.can_move = {'left':True, 'right':True, 'up':True, 'down':True}
        self.physics.in_air = True

        hb_under = Hitbox(self.x, self.y-1, self.width, self.height)
        hb_top = Hitbox(self.x, self.y+1, self.width, self.height)
        hb_left = Hitbox(self.x-1, self.y, self.width, self.height)
        hb_right = Hitbox(self.x+1, self.y, self.width, self.height)

        
        for obj in objects:
            future_hitbox.collision(obj.hitbox, velocity)
            
            if future_hitbox.collision_directions['x'] != None:
                self.x = future_hitbox.collision_directions['x']
                self.physics.velocity.x = 0

            if future_hitbox.collision_directions['y'] != None:
                self.y = future_hitbox.collision_directions['y']
                self.physics.velocity.y = 0

            result = hb_under.intersects(obj.hitbox)
            if result:
                self.physics.in_air = False
                self.can_move['down'] = False
            result = hb_left.intersects(obj.hitbox)
            if result:
                self.can_move['left'] = False
            result = hb_right.intersects(obj.hitbox)
            if result:
                self.can_move['right'] = False
            result = hb_top.intersects(obj.hitbox)
            if result:
                self.can_move['up'] = False

        #print(future_hitbox.collision_directions)

        

        #print(self.can_move)
        #print("-----------------------------------------------------")

    def pos(self):
        return Vector(self.x, self.y)

    def distance(self, other):
        return self.pos().distance(other.pos())

        

        

