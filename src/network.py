import socket


class Network:
    """"""

    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = "192.168.10.61"
        # For this to work on your machine this must be equal to the ipv4 address of the machine running the server
        # You can find this address by typing ipconfig in CMD and copying the ipv4 address. Again this must be the servers
        # ipv4 address. This feild will be the same for all your clients.
        self.port = 5555
        self.addr = (self.host, self.port)
        self.id = self.connect()

    def connect(self):
        self.client.connect(self.addr)
        return int(self.client.recv(2048).decode())

    def send(self, data):
        try:
            self.client.send(str.encode(data))
        except socket.error as e:
            return str(e)

    def send_player_data(self, player):
        data = "0=" + str(self.id) + ':' + str(player.x) + ':' + str(player.y) + ':' + str(player.texture_id)
        self.send(data)

    def send_projectile_data(self, player):
        if player.projectiles != []:
            data = '1='
            for proj in player.projectiles:
                data += str(self.id) + ':' + str(proj.x) + ':' + str(proj.y) + ':' + str(proj.direction.x) + ':' + str(proj.direction.y) + '/'
            data = data[:-1]
            self.send(data)

    def receive_data(self):
        received_data = []

        try:
            recv_data = self.client.recv(4096).decode()
            received_data = recv_data.split('!')
        except:
            pass
        
        
        return received_data
