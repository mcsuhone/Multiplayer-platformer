import pyglet
from pyglet.window import key
from vector import Vector
from objects.projectiles.projectile import Projectile
from objects.object import Object

class Player(Object):
    def __init__(self, character_id, x, y, owner_id, batch = None, parent=None):
        super().__init__(character_id, x, y, batch = batch)
        
        self.keys = dict(left = False, right = False, up = False, down = False, shoot = False)
        self.owner = owner_id
        self.texture_id = character_id
        self.projectiles = []
        

        self.speed = 0.5
        self.jump_height = 5

    def on_key_press(self, symbol, modifiers):
        if symbol == key.W:
            self.keys['up'] = True
        elif symbol == key.S:
            self.keys['down'] = True
        elif symbol == key.A:
            self.keys['left'] = True
        elif symbol == key.D:
            self.keys['right'] = True

    def on_key_release(self, symbol, modifiers):
        if symbol == key.W:
            self.keys['up'] = False
        elif symbol == key.S:
            self.keys['down'] = False
        elif symbol == key.A:
            self.keys['left'] = False
        elif symbol == key.D:
            self.keys['right'] = False

    def center_coordinates(self):
        return self.x + 15, self.y + 15

    def on_mouse_press(self, x, y, button, modifiers):
        direction = Vector(x - self.x, y - self.y)
        if button == pyglet.window.mouse.LEFT:
            x, y = self.center_coordinates()
            self.projectiles.append(Projectile(x, y, direction, owner_id = self.owner))

    def input(self, dt):
        dx = 0
        dy = 0
        if self.keys['up']:
            if not self.physics.in_air:
                self.physics.in_air = True
                dy = self.jump_height
        if self.keys['left']:
            dx += -self.speed
        if self.keys['right']:
            dx += self.speed

        if dx != 0:
            self.physics.accelerate(Vector(dx, 0))
        elif self.physics.velocity.x != 0:
            self.physics.decelerate()

        if dy != 0:
            self.physics.accelerate(Vector(0, dy))


