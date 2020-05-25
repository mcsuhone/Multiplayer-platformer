import pyglet
from pyglet.window import key

from player import Player
from network import Network
from projectile import Projectile
from vector import Vector


window = pyglet.window.Window(800, 600)
network = Network()
event_loop = pyglet.app.EventLoop()

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
    new_player = Player(texture_id, 100, 100, network.id)
    players[network.id] = new_player

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
    network.send_player_data(players[network.id])
    network.send_projectile_data(players[network.id])
    players[network.id].projectiles = []
    
    list_of_data = network.receive_data()
    
    for data in list_of_data:
        if data != '':
            parse_data(data)

def parse_data(data):
    """"""
    try:
        pair = data.split('=')
        data_id = int(pair[0])
        arr = pair[1].split('/')
        if data_id == 0:
            for player_data in arr:
                info = player_data.split(':')
                player_id = int(info[0])
                if player_id in players and player_id != network.id:
                    p = players[player_id]
                    p.move_to(float(info[1]), float(coords[2]))
                elif player_id not in players:
                    new_p = Player(int(info[3]), float(info[1]), float(info[2]), player_id)
                    players[id] = new_p
        elif data_id == 1:
            for proj_data in arr:
                info = proj_data.split(':')
                direction = Vector(float(info[3]), float(info[4]))
                projectile = Projectile(float(info[1]), float(info[2]), direction, int(info[0]))
                projectiles.append(projectile)
                
    except:
        print("ERROR")

init()
window.push_handlers(players[network.id])
pyglet.clock.schedule_interval(players[network.id].update, 1/60.0)
pyglet.clock.schedule_interval(update, 1/60)
pyglet.app.run()


