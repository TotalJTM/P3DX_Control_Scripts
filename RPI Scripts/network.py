import socket
import sys

class network_sock:

    def __init__(self, message_size=256, sock=None):
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

        self.message_size = message_size
        self.master = False
        self.clientsock = None
        self.clientaddr = None


    def bind(self, host, port):
        self.sock.bind((host, port))
        self.sock.listen(5)

        self.master = True

    def connect(self, host, port):
        self.sock.connect((host, port))

    def send(self, msg):
        if self.master:
            if self.clientsock is None:
                self.clientsock, self.clientaddr = self.sock.accept()
            self.clientsock.send(msg)
        else:
            self.sock.send(msg)

    def receive(self):
        if self.master:
            msg = self.clientsock.recv(self.message_size)
        else:
            msg = self.sock.recv(self.message_size)
        if msg is not None:
            return msg

    def close(self):
        if self.master:
            self.clientsock.close()
            self.clientsock = None 
            self.address = None 
            self.master = False
        else:
            self.sock.close()