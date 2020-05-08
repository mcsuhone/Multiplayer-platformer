import pyglet
from pyglet.window import key

from player import Player
from network import Network


window = pyglet.window.Window(800, 600)
network = Network()

texture = pyglet.image.load("./textures/derbiili.png")
texture2 = pyglet.image.load("./textures/bug.png")
texture3 = pyglet.image.load("./textures/snake.png")
players = {}

player = Player(texture3, 0, 0)
player2 = Player(texture2, 100, 100)
player3 = Player(texture, 200, 100)

players[0] = player
players[1] = player2
players[2] = player3

event_loop = pyglet.app.EventLoop()

@event_loop.event
def on_window_close(window):
    event_loop.exit()

@window.event
def on_draw():
    parse_data(send_data())

    window.clear()
    player.draw()
    player2.draw()
    player3.draw()

def send_data():
    """"""

    data = network.id + '=' + str(players[int(network.id)].x) + ':' + str(players[int(network.id)].y)
    reply = network.send(data)
    return reply

def parse_data(data):
    """"""

    try:
        arr = data.split('/')
        for p_info in arr:
            pair = p_info.split('=')
            id = int(pair[0])
            coords = pair[1].split(':')
            if int(network.id) != id:
                p = players[id]
                p.move_to(int(coords[0]), int(coords[1]))
    except:
        pass

window.push_handlers(players[int(network.id)])
pyglet.clock.schedule_interval(players[int(network.id)].update, 1/60.0)
pyglet.app.run()


