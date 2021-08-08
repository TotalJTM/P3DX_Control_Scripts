import socket
import sys

server_ip = '192.168.1.5'
server_port = '12345'

#messages = []

#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect((socket.gethostname(), server_port))

#msg = s.recv(1024)
#print(msg.decode("utf-8"))

#sock = ""

class network_sock:

    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock


    def connect(self, host, port):
        self.sock.connect((host, port))

    def send(self, msg):
        sent = self.sock.send(msg)
        print(sent)

    def receive(self):
        msg = self.sock.recv(256)
        if msg is not None:
            print(msg)
            return msg
        return None



if __name__ == '__main__':

	s = network_sock()
	s.connect(server_ip, server_port)

	while s.sock is not None:

		message = s.receive()
		if message is not None:
			print(message)
			message_to_send = {'command': '10', 'message': 'OK'}
			s.send(message_to_send)




