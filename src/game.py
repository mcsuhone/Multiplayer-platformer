import pyglet
from pyglet.window import key

from player import Player
from projectile import Projectile
from blocks.block import Block

from network import Network
from vector import Vector


event_loop = pyglet.app.EventLoop()

class Game:
    def __init__(self, window):
        self.window = window
        self.network = Network()
        self.players = {}
        self.projectiles = []
        self.blocks = []

        self.load_map()

        texture_id = 0
        new_player = Player(texture_id, 100, 100, self.network.id)
        self.players[self.network.id] = new_player

        self.window.push_handlers(self.players[self.network.id])
        self.window.push_handlers(self)
        pyglet.clock.schedule_interval(self.players[self.network.id].update, 1/60.0)
        pyglet.clock.schedule_interval(self.update, 1/60)
        pyglet.app.run()

    def load_map(self):
        for i in range(100):
            block = Block(i*16, 16, 1)
            self.blocks.append(block)
        for i in range(100):
            block = Block(i*16, 0, 2)
            self.blocks.append(block)

    def on_draw(self):
        self.window.clear()
        #Draw players
        for i in self.players:
            self.players[i].draw()
        #Draw projectiles
        for p in self.projectiles:
            p.draw()
        #Draw blocks
        for b in self.blocks:
            b.draw()

    def update(self, dt):
        self.network.send_player_data(self.players[self.network.id])
        self.network.send_projectile_data(self.players[self.network.id])
        self.players[self.network.id].projectiles = []
        
        list_of_data = self.network.receive_data()
        
        for data in list_of_data:
            if data != '':
                self.parse_data(data)

    def parse_data(self, data):
        """"""
        try:
            pair = data.split('=')
            data_id = int(pair[0])
            arr = pair[1].split('/')
            if data_id == 0:
                for player_data in arr:
                    info = player_data.split(':')
                    player_id = int(info[0])
                    if player_id in self.players and player_id != self.network.id:
                        p = self.players[player_id]
                        p.move_to(float(info[1]), float(coords[2]))
                    elif player_id not in self.players:
                        new_p = Player(int(info[3]), float(info[1]), float(info[2]), player_id)
                        self.players[id] = new_p
            elif data_id == 1:
                for proj_data in arr:
                    info = proj_data.split(':')
                    direction = Vector(float(info[3]), float(info[4]))
                    projectile = Projectile(float(info[1]), float(info[2]), direction, int(info[0]))
                    self.projectiles.append(projectile)
                    
        except:
            print("ERROR")

@event_loop.event
def on_window_close(window):
    event_loop.exit()



    






