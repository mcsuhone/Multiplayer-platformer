import pyglet
from pyglet.window import key

from player import Player
from network import Network


window = pyglet.window.Window(800, 600)
network = Network()
event_loop = pyglet.app.EventLoop()

texture = pyglet.image.load("./textures/derbiili.png")
texture2 = pyglet.image.load("./textures/bug.png")
texture3 = pyglet.image.load("./textures/snake.png")
textures = {}
textures[0] = texture
textures[1] = texture2
textures[2] = texture3

players = {}
while(True):
    try:
        texture_id = int(input("Enter texture id (0-2): "))
        break
    except:
        pass

def init():
    new_player = Player(textures[texture_id], 100, 100)
    players[int(network.id)] = new_player
    reply = send_data()
    try:
        arr = reply.split('/')
        for p_info in arr:
            pair = p_info.split('=')
            id = int(pair[0])
            coords = pair[1].split(':')
            t_id = int(pair[2])
            if int(network.id) != id:
                new_p = Player(textures[t_id], float(coords[0]), float(coords[1]))
                players[id] = new_p
    except:
        pass

@event_loop.event
def on_window_close(window):
    event_loop.exit()

@window.event
def on_draw():
    parse_data(send_data())

    window.clear()
    for i in players:
        players[i].draw()



def send_data():
    """"""

    data = network.id + '=' + str(players[int(network.id)].x) + ':' + str(players[int(network.id)].y) + '=' + str(texture_id)
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
            
            try:
                #Try to move player
                if int(network.id) != id:
                    p = players[id]
                    p.move_to(float(coords[0]), float(coords[1]))
            except:
                #Failed to move player, add new player
                t_id = int(pair[2])
                new_p = Player(textures[t_id], float(coords[0]), float(coords[1]))
                players[id] = new_p
    except:
        pass

init()
window.push_handlers(players[int(network.id)])
pyglet.clock.schedule_interval(players[int(network.id)].update, 1/120.0)
pyglet.app.run()


