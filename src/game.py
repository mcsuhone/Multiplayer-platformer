import pyglet
from pyglet.window import key

from player import Player
from objects.projectiles.projectile import Projectile
from objects.blocks.block import Block

from network import Network
from vector import Vector


event_loop = pyglet.app.EventLoop()

class Game:
    def __init__(self, window):
        self.window = window
        self.network = Network()
        self.players = {}
        self.players_batch = pyglet.graphics.Batch()
        self.projectiles = []
        self.projectiles_batch = pyglet.graphics.Batch()
        self.blocks = []
        self.blocks_batch = pyglet.graphics.Batch()
        self.load_map()

        texture_id = 0
        new_player = Player(texture_id, 100, 100, self.network.id, self.players_batch)
        self.players[self.network.id] = new_player

        self.fps_display = pyglet.window.FPSDisplay(window = self.window)

        self.window.push_handlers(self.players[self.network.id])
        self.window.push_handlers(self)
        pyglet.clock.schedule_interval(self.players[self.network.id].input, 1/60)
        pyglet.clock.schedule_interval(self.update, 1/60)
        pyglet.app.run()

    def load_map(self):
        for i in range(100):
            block = Block(11, i*16, 16, self.blocks_batch)
            self.blocks.append(block)

        for i in range(100):
            block = Block(12, i*16, 0, self.blocks_batch)
            self.blocks.append(block)

    def on_draw(self):
        self.window.clear()
        #Draw players
        for i in self.players:
            self.players[i].draw()
        #Draw projectiles
        self.blocks_batch.draw()
        self.projectiles_batch.draw()

        self.fps_display.draw()

    def update(self, dt):
        self.network.send_player_data(self.players[self.network.id])
        self.network.send_projectile_data(self.players[self.network.id])
        self.players[self.network.id].projectiles = []
        
        list_of_data = self.network.receive_data()
        i = 0
        while list_of_data[i] != '':
            self.parse_data(list_of_data[i])
            i += 1

        self.players[self.network.id].check_collisions(self.blocks + self.projectiles)
        self.players[self.network.id].move()
        

    def parse_data(self, data):
        """"""
        try:
            pair = data.split('=')
            data_id = int(pair[0])
            arr = pair[1].split('/')
            
            i = 0
            if data_id == 0:
                while arr[i] != '':
                    info = arr[i].split(':')
                    player_id = int(info[0])
                    if player_id in self.players and player_id != self.network.id:
                        p = self.players[player_id]
                        p.move_to(float(info[1]), float(coords[2]))
                    elif player_id not in self.players:
                        new_p = Player(int(info[3]), float(info[1]), float(info[2]), player_id, self.players_batch)
                        self.players[id] = new_p
                    
                    i += 1

            elif data_id == 1:
                while arr[i] != '':
                    info = arr[i].split(':')
                    direction = Vector(float(info[3]), float(info[4]))
                    projectile = Projectile(float(info[1]), float(info[2]), direction, self.projectiles_batch, int(info[0]))
                    self.projectiles.append(projectile)

                    i += 1
            
        except:
            print("ERROR")

@event_loop.event
def on_window_close(window):
    event_loop.exit()



    






