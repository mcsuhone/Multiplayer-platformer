import socket
from _thread import *
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = "87.100.186.20"
port = 5555

server_ip = socket.gethostbyname(server)

try:
    s.bind((server, port))

except socket.error as e:
    print(str(e))

s.listen(4)
print("Waiting for a connection")

current_id = 0

positions = []
projectiles = {}

def convert_to_data(player_id):
    """"""

    data = ''
    for p in positions:
        data += p
        data += '/'
    data = data[:-1]
    
    try:
        if len(projectiles[player_id]) > 0:
            data += '!'
            while len(projectiles[player_id]) > 0:
                proj = projectiles[player_id].pop(0)
                data += proj + '/'
        data = data[:-1]
    except:
        pass

    return data

def threaded_client(conn):
    """"""
    global positions, current_id
    conn.send(str.encode(str(current_id)))
    positions.append(str(current_id) + "=0:0=0")
    current_id += 1

    while True:
        try:
            data = conn.recv(2048).decode()
            if not data:
                break
            else:
                #print("Recieved: " + data)
                pair = data.split('!')
                player_data = pair[0]
                projectile_error = False
                
                try:
                    projectile_data = pair[1]
                    projectile_error = False
                except:
                    projectile_error = True
                
                player_pair = player_data.split('=')
                player_id = int(player_pair[0])
                for i in range(len(positions)):
                    pair = positions[i].split('=')
                    id = int(pair[0])
                    if id == player_id:
                        coords = player_pair[1].split(':')
                        new_info = str(player_id) + '=' + coords[0] + ':' + coords[1] + '=' + player_pair[2]
                        positions[i] = new_info

                if projectile_error == False:
                    projs = projectile_data.split('/')
                    for i in range(len(positions)):
                        if i != player_id:
                            lst = []
                            for p in projs:
                                lst.append(p)
                            projectiles[i] = lst

                conn.sendall(str.encode(convert_to_data(player_id)))
        except e:
            print(e)
            break

    print("Connection Closed")
    conn.close()

while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)

    start_new_thread(threaded_client, (conn,))