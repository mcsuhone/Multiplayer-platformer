import socket
from _thread import *
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = "87.100.210.158"
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

def convert_to_data():
    """"""

    data = ''
    for p in positions:
        data += p
        data += '/'
    data = data[:-1]
    return data

def threaded_client(conn):
    """"""

    global positions, current_id
    conn.send(str.encode(str(current_id)))
    positions.append(str(current_id) + "=0:0")
    current_id += 1

    while True:
        try:
            data = conn.recv(2048).decode()
            if not data:
                conn.send(str.encode("Goodbye"))
                break
            else:
                #print("Recieved: " + data)
                data_pair = data.split('=')
                data_id = int(data_pair[0])
                for i in range(len(positions)):
                    pair = positions[i].split('=')
                    id = int(pair[0])
                    if id == data_id:
                        coords = data_pair[1].split(':')
                        new_pos = str(data_id) + "=" + coords[0] + ":" + coords[1]
                        positions[i] = new_pos

            conn.sendall(str.encode(convert_to_data()))
        except:
            break

    print("Connection Closed")
    conn.close()

while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)

    start_new_thread(threaded_client, (conn,))