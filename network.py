import socket
import sys

server_ip = '192.168.1.5'
server_port = '12345'

messages = []

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), server_port))

msg = s.recv(1024)
print(msg.decode("utf-8"))

sock = ""

def init(server_ip, server_port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(server_ip, server_port)