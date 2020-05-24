import pyglet
from pyglet.window import key
from vector import Vector
from projectile import Projectile



class Player(pyglet.sprite.Sprite):
    def __init__(self, texture, x, y, parent=None):
        super().__init__(texture, x, y)
        self.keys = dict(left = False, right = False, up = False, down = False)
        self.projectiles = []

    def move_by(self, dx, dy):
        self.x += dx
        self.y += dy

    def move_to(self, x, y):
        self.x = x
        self.y = y

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
        return self.x + 15, self.y +15

    def on_mouse_press(self, x, y, button, modifiers):
        direction = Vector(x - self.x, y - self.y)
        if button == pyglet.window.mouse.LEFT:
            x, y = self.center_coordinates()
            self.projectiles.append(Projectile(x, y, direction))
        

    def update(self, dt):
        dx = 0
        dy = 0
        if self.keys['up']:
            dy += 100*dt
        if self.keys['down']:
            dy -= 100*dt
        if self.keys['left']:
            dx -= 100*dt
        if self.keys['right']:
            dx += 100*dt
        
        self.move_by(dx, dy)
