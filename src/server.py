import sys

import socket
from _thread import *

class Server:
    def __init__(self, ip, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server = ip
        port = port
        self.server_ip = socket.gethostbyname(server)
        try:
            self.socket.bind((server, port))

        except socket.error as e:
            print(str(e))

        self.positions = {}
        self.positions_count = 0
        self.projectiles = {}
        self.current_id = 0

    def add_player(self):
        """Add player to Server and give it id. Returns the id."""
        self.positions[self.current_id] = str(server.current_id) + ":0:0:0"
        self.current_id += 1
        self.positions_count += 1

        return self.current_id - 1

    def parse_data(self, data, player_id):
        pair = data.split('=')
        data_id = int(pair[0])
        
        if data_id == 0:
            self.parse_player_data(pair[1], player_id)

        elif data_id == 1:
            self.parse_projectile_data(pair[1], player_id)

    def parse_player_data(self, data, player_id):
        self.positions[player_id] = data

    def parse_projectile_data(self, data, player_id):
        for i in self.positions:
            self.projectiles[i] = data


    def convert_player_data(self):
        """Converts player information stored in server class to data string."""
        data = '0='
        for id in self.positions:
            data += self.positions[id]
            data += '/'

        data += '!'

        return data

    def convert_projectile_data(self, player_id):
        """Converts projectile information stored in server class to data string."""
        data = '1='
        if player_id in self.projectiles and self.projectiles[player_id] != None:
            data += self.projectiles[player_id]
            data += '!'
            self.projectiles[player_id] = None

            return data
        else:
            return None

def threaded_client(conn):
    """"""
    global server
    conn.send(str.encode(str(server.current_id)))
    player_id = server.add_player()

    while True:
        try:
            data = conn.recv(2048).decode()
            if not data:
                break
            else:
                server.parse_data(data, player_id)

                player_data = server.convert_player_data()
                projectile_data = server.convert_projectile_data(player_id)

                #print("Data: ", player_data, " and ", projectile_data)
                conn.sendall(str.encode(player_data))
                if projectile_data != None:
                    conn.sendall(str.encode(projectile_data))
        except:
            break

    print("Connection Closed")
    conn.close()

server = Server("78.27.103.28", 5555)

server.socket.listen(4)
print("Waiting for a connections")

while True:
    conn, addr = server.socket.accept()
    print("Connected to: ", addr)

    start_new_thread(threaded_client, (conn,))