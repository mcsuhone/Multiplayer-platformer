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
projectiles = []

'''
while(True):
    try:
        texture_id = int(input("Enter texture id (0-2): "))
        break
    except:
        pass
'''
texture_id = 0


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
    window.clear()
    #Draw players
    for i in players:
        players[i].draw()

    #Draw projectiles
    for p in projectiles:
        p.draw()

def update(dt):
    reply = send_data()
    parse_data(reply)

    while len(players[int(network.id)].projectiles) > 0:
        projectiles.append(players[int(network.id)].projectiles.pop(0))

def send_data():
    """"""
    data = network.id + '=' + str(players[int(network.id)].x) + ':' + str(players[int(network.id)].y) + '=' + str(texture_id)
    if len(players[int(network.id)].projectiles) > 0:
        data += '!'
        for proj in players[int(network.id)].projectiles:
            data += str(proj.x) + ':' + str(proj.y) + ':' + str(proj.direction.x) + ':' + str(proj.direction.y) + '/'
        data = data[:-1]
    print("Sending: ", data)
    reply = network.send(data)
    print("Received: ", reply)
    return reply

def parse_data(data):
    """"""
    try:
        pair = data.split('!')
        arr = pair[0].split('/')
        for player_data in arr:
            data_list = player_data.split('=')
            id = int(data_list[0])
            coords = data_list[1].split(':')
            
            try:
                #Try to move player
                if int(network.id) != id:
                    p = players[id]
                    p.move_to(float(coords[0]), float(coords[1]))
            except:
                #Failed to move player, add new player
                t_id = int(data_list[2])
                new_p = Player(textures[t_id], float(coords[0]), float(coords[1]))
                players[id] = new_p

        arr2 = pair[1].split('/')
        for proj_data in arr2:
            info = proj_data.split(':')
            projectile = Projectile(float(info[0]), float(info[1]), Vector(float(info[2]), float(info[3])))
            projectiles.append(projectile)

    except:
        pass

init()
window.push_handlers(players[int(network.id)])
pyglet.clock.schedule_interval(players[int(network.id)].update, 1/60.0)
pyglet.clock.schedule_interval(update, 1/60)
pyglet.app.run()


