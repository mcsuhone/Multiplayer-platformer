from pyglet.window import key
import pyglet



class Player(pyglet.sprite.Sprite):
    def __init__(self, texture, x, y, parent=None):
        super().__init__(texture, x, y)
        self.keys = dict(left = False, right = False, up = False, down = False)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def on_key_press(self, symbol, modifiers):
        if symbol == key.UP:
            self.keys['up'] = True
        elif symbol == key.DOWN:
            self.keys['down'] = True
        elif symbol == key.LEFT:
            self.keys['left'] = True
        elif symbol == key.RIGHT:
            self.keys['right'] = True

    def on_key_release(self, symbol, modifiers):
        if symbol == key.UP:
            self.keys['up'] = False
        elif symbol == key.DOWN:
            self.keys['down'] = False
        elif symbol == key.LEFT:
            self.keys['left'] = False
        elif symbol == key.RIGHT:
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
        self.move(dx, dy)
