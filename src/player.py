import pyglet
from pyglet.window import key


class Player(pyglet.sprite.Sprite):
    def __init__(self, texture, x, y, parent=None):
        super().__init__(texture, x, y)
        self.keys = dict(left = False, right = False, up = False, down = False)

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

    def update(self, dt):
        dx = 0
        dy = 0
        if self.keys['up']:
            dy += 2
        if self.keys['down']:
            dy -= 2
        if self.keys['left']:
            dx -= 2
        if self.keys['right']:
            dx += 2
        
        self.move_by(dx, dy)
