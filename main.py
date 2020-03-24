import pyglet
import player
from pyglet.window import key

window = pyglet.window.Window(800, 600)

texture = pyglet.image.load("derbiili.png")
player = player.Player(texture, 0, 0)

event_loop = pyglet.app.EventLoop()

@event_loop.event
def on_window_close(window):
    event_loop.exit()

@window.event
def on_draw():
    window.clear()
    player.draw()

window.push_handlers(player)
pyglet.clock.schedule_interval(player.update, 1/120.0)
pyglet.app.run()
