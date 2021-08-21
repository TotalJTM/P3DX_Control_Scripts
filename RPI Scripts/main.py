from network import network_sock
from robot_communications import commands
from serial_communications import serial_port
import time, json
from math import pi, sqrt

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
		self.robot_controller = robot_controller
		self.motor_update_timer = Timer(0.025)
		self.encoder_update_timer = Timer(0.01)

		self.left_motor_speed = 0
		self.right_motor_speed = 0
		self.last_left_enc = 0
		self.last_right_enc = 0

		self.wheel_distance = 13.0
		self.wheel_diam = 7.65
		self.enc_ticks_per_rev = 19105.0
		self.wheel_dist_circum = pi*self.wheel_distance
		self.ticks_per_inch = self.enc_ticks_per_rev/(self.wheel_diam*pi)

		self.kp = 0.85
		self.ki = 0.85
		self.kd = 1


	#def update_motor_speed(self, left = None, right = None):
	#	if left is not None:
	#		self.left_motor_speed = constrain(left, -100, 100)
	#	if right is not None:
	#		self.right_motor_speed = constrain(right, -100, 100)

	#	self.send_message(10, [self.left_motor_speed,self.right_motor_speed])


	def update_values(self, arr):
		for item in arr:
				#handle motor keys
				if "left_motor_speed" in item:
					self.left_motor_speed = item["left_motor_speed"]
				if "right_motor_speed" in item:
					self.right_motor_speed = item["right_motor_speed"]

	def start_robot_update_timers(self):
		self.motor_update_timer.start()
		#self.encoder_update_timer.start()

	def update_robot_controller(self):
		if self.motor_update_timer.check_timer():
			self.send_message(10, [int(self.left_motor_speed),int(self.right_motor_speed)])
			self.motor_update_timer.start()

	def get_encoder_values(self):
		if self.encoder_update_timer.check_timer():
			self.send_message(11)
			cmd, data = self.robot_controller.receive()
			self.last_left_enc = data[0]
			self.last_right_enc = data[1]
			self.encoder_update_timer.start()

	def distance_moved(self):
		return (self.last_left_enc/self.ticks_per_inch), (self.last_right_enc/self.ticks_per_inch)

	def reset_encoder_values(self, left_enc=False, right_enc=False):
		arr = [0,0]
		if left_enc:
			arr[0] = 1
		if right_enc:
			arr[1] = 1

		self.send_message(13, arr)

	def send_message(self, cmd, vals=[]):
		if self.robot_controller is not None:
			msg = f'<{cmd},'
			for index, vals in enumerate(vals):
				msg += f'{vals},'
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

	#arduino = serial_port(115200, port=0, prefix='/dev/ttyACM')
	arduino = serial_port(115200,port=24,prefix='COM')
	print("controller assigned")
	print(arduino.receive())

	robot = P3_DX_robot(robot_controller=arduino)

	robot.send_message(91, [robot.kp,robot.ki,robot.kd])
	#print(robot.robot_controller.receive())

	s = network_sock()
	s.connect(server_ip, server_port)
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

			s.send(commands.format_arr(commands.ok()))

		robot.update_robot_controller()