from network import network_sock
from robot_communications import parse_robot_message, send_ok

server_ip = '192.168.1.5'
server_port = 12345


#messages = []

#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect((socket.gethostname(), server_port))

#msg = s.recv(1024)
#print(msg.decode("utf-8"))

#sock = ""




if __name__ == '__main__':

	s = network_sock(message_size=16)
	s.connect(server_ip, server_port)

	run_flag = True

	while run_flag:

		message = s.receive()

		if message is not None:
			print(f'received {message}')
			cmd, vals = parse_robot_message(message)
			print(f'Received command {cmd} with values: {vals}')
			s.send(send_ok(cmd))




