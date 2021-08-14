from network import network_sock
from robot_communications import commands
from serial_communications import serial_port

server_ip = '192.168.1.5'
server_port = 12345


#messages = []

#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect((socket.gethostname(), server_port))

#msg = s.recv(1024)
#print(msg.decode("utf-8"))

#sock = ""

def constrain(n, minn, maxn):
    return max(min(maxn, n), minn)


class P3_DX_robot:
	def __init__(self, robot_controller = None):
		self.left_motor_speed = 0
		self.right_motor_speed = 0
		self.robot_controller = robot_controller

	def update_motor_speed(self, left = None, right = None):
		if left:
			self.left_motor_speed = constrain(left, -100, 100)
		if right:
			self.right_motor_speed = constrain(right, -100, 100)

		if self.robot_controller:
			self.send_message(10, [self.left_motor_speed,self.right_motor_speed])

	def send_message(self, cmd, vals):
		msg = f'<{cmd},'
		for index, vals in enumerate(vals):
			msg += f'{int(vals)},'
		msg = msg[:-1] + '>'
		print(msg)
		print(self.robot_controller.send(msg))
		print(self.robot_controller.receive())

def handle_message_commands(message):
    message = json.loads(message.decode())
    items = message["arr"]


if __name__ == '__main__':

	#s = network_sock()
	#s.connect(server_ip, server_port)
	arduino = serial_port(115200,prefix='/dev/ttyUSB')
	#arduino = serial_port(115200,port=24,prefix='COM')
	#print(arduino.receive())
	robot = P3_DX_robot(robot_controller=arduino)
	print("controller assigned")
	robot.update_motor_speed(left=0)

	run_flag = True

	while run_flag:

		message = s.receive()

		if message is not None:
			print(f'received {message}')

			if "left_motor_speed" in message:
				robot.update_motor_speed(left=message["left_motor_speed"])
			if "right_motor_speed" in message:
				robot.update_motor_speed(right=message["right_motor_speed"])

			print(arduino.receive())

			s.send(commands.format_arr(commands.send_ok()))

