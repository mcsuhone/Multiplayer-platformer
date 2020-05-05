import pyglet
from pyglet.window import key
import socket
from _thread import *

from player import Player
from network import Network


window = pyglet.window.Window(800, 600)
network = Network()

texture = pyglet.image.load("./textures/derbiili.png")
player = Player(texture, 0, 0)
player2 = Player(texture, 100, 100)

event_loop = pyglet.app.EventLoop()

@event_loop.event
def on_window_close(window):
    event_loop.exit()

@window.event
def on_draw():
    x, y = parse_data(send_data())
    player2.move_to(x,y)

    window.clear()
    player.draw()
    player2.draw()

def send_data():
    """
    Send position to server
    :return: None
    """
    data = str(network.id) + ":" + str(player.x) + "," + str(player.y)
    reply = network.send(data)
    return reply

def parse_data(data):
    try:
        d = data.split(":")[1].split(",")
        return int(d[0]), int(d[1])
    except:
        return 0,0

window.push_handlers(player)
pyglet.clock.schedule_interval(player.update, 1/120.0)
pyglet.app.run()


