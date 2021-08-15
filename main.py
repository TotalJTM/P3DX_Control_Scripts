from network import network_sock
from robot_communications import commands
from serial_communications import serial_port
import time

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

class Timer:
	def __init__(self, interval):
		self.interval = interval
		self.start_time = 0

	def start(self):
		self.start_time = time.perf_counter()

	def check_timer(self):
		if (self.start_time+self.interval) <= time.perf_counter():
			return True
		else:
			return False


class P3_DX_robot:
	def __init__(self, robot_controller = None):
		self.left_motor_speed = 0
		self.right_motor_speed = 0
		self.robot_controller = robot_controller
		#self.motormessage_interval = 0.1
		self.motor_update_timer = Timer(0.1)



	#def update_motor_speed(self, left = None, right = None):
	#	if left is not None:
	#		self.left_motor_speed = constrain(left, -100, 100)
	#	if right is not None:
	#		self.right_motor_speed = constrain(right, -100, 100)

	#	self.send_message(10, [self.left_motor_speed,self.right_motor_speed])


	def update_values(self, arr):
		for item in message_items:
				#handle motor keys
				if "left_motor_speed" in item:
					self.left_motor_speed = message_items["left_motor_speed"]
				if "right_motor_speed" in item:
					self.right_motor_speed = message_items["right_motor_speed"]

	def start_robot_update_timers(self):
		self.motor_update_timer.start()

	def update_robot_controller(self):
		if self.motor_update_timer.check_timer():
			self.send_message(10, [self.left_motor_speed,self.right_motor_speed])



	def send_message(self, cmd, vals):
		if self.robot_controller is not None:
			msg = f'<{cmd},'
			for index, vals in enumerate(vals):
				msg += f'{int(vals)},'
			msg = msg[:-1] + '>'
			print(msg)
			print(self.robot_controller.send(msg))
			#print(self.robot_controller.receive())
			return True
		else:
			print(f'message could not be sent, no controller')
			return False


def handle_message_commands(message):
    message = json.loads(message.decode())
    items = message["arr"]
    return items


if __name__ == '__main__':

	s = network_sock()
	s.connect(server_ip, server_port)
	arduino = serial_port(115200, port=0, prefix='/dev/ttyACM')
	#arduino = serial_port(115200,port=24,prefix='COM')
	print(arduino.receive())
	robot = P3_DX_robot(robot_controller=arduino)
	print("controller assigned")
	#robot.update_motor_speed(left=0)

	run_flag = True

	robot.start_robot_update_timers()

	while run_flag:

		message = s.receive()

		if message is not None:
			print(f'received {message}')
			message_items = handle_message_commands(message)
			
			robot.update_values(message_items)



			#print(arduino.receive())

			s.send(commands.format_arr(commands.send_ok()))

		robot.update_robot_controller()
