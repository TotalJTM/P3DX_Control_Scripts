from network import network_sock
from robot_communications import commands
from serial_communications import serial_port
import time, json
from math import pi, sqrt

from robot_buzzer import music_box, songs

from _thread import *
import threading

server_ip = '192.168.1.5'
server_port = 12345

autoreconnect_socket = False

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
		self.motor_update_timer = Timer(0.1)
		self.encoder_update_timer = Timer(0.05)
		self.button_update_timer = Timer(0.1)

		self.left_motor_speed = 0
		self.right_motor_speed = 0
		self.last_left_enc = 0
		self.last_right_enc = 0

		self.last_reset_button_state = 1
		self.last_motor_button_state = 1
		self.last_aux1_switch_state = 1
		self.last_aux2_switch_state = 1

		self.wheel_distance = 13.0
		self.wheel_diam = 7.65
		self.enc_ticks_per_rev = 19105.0
		self.wheel_dist_circum = pi*self.wheel_distance
		self.ticks_per_inch = self.enc_ticks_per_rev/(self.wheel_diam*pi)

		self.kp = 0.85
		self.ki = 0.85
		self.kd = 1

		self.robot_music_box = None
		self.last_buzzer_freq = 0

	def update_values_with_json(self, arr):
		for item in arr:
				#handle motor keys
				if "left_motor_speed" in item:
					self.left_motor_speed = item["left_motor_speed"]
				if "right_motor_speed" in item:
					self.right_motor_speed = item["right_motor_speed"]

	def start_robot_update_timers(self):
		self.motor_update_timer.start()
		self.encoder_update_timer.start()
		self.button_update_timer.start()

	def update_motor_speed(self, forced=False):
		if self.motor_update_timer.check_timer() or forced:
			self.send_message(10, [int(self.left_motor_speed),int(self.right_motor_speed)])
			self.motor_update_timer.start()

	def get_encoder_values(self):
		if self.encoder_update_timer.check_timer():
			self.send_message(11)
			cmd, data = self.robot_controller.receive()
			print(f'cmd: {cmd}. data: {data}')
			self.last_left_enc = int(data[0])
			self.last_right_enc = int(data[1])
			self.encoder_update_timer.start()

	def get_button_values(self):
		if self.button_update_timer.check_timer():
			self.send_message(20)
			cmd, data = self.robot_controller.receive()
			print(f'cmd: {cmd}. data: {data}')
			self.last_reset_button_state = int(data[0])
			self.last_motor_button_state = int(data[1])
			self.last_aux1_switch_state = int(data[2])
			self.last_aux2_switch_state = int(data[3])
			self.button_update_timer.start()

	def handle_buttons(self):
		#if self.last_reset_button_state == 0:
			
		if self.last_motor_button_state == 0:
			self.left_motor_speed = 0
			self.right_motor_speed = 0
			print("Motors reset by robot")
			exit()
		#if self.last_aux1_button_state == 0:
			
		#if self.last_aux2_button_state == 0:

	def start_music_box(self, song_number=0, tempo=160):
		self.robot_music_box = music_box(song=songs[song_number], tempo=tempo)

	def handle_music_box(self,):
		if self.robot_music_box is not None:
			f = self.robot_music_box.get_note()
			if f != self.last_buzzer_freq and f != None:
				self.send_message(21, [f])
				self.last_buzzer_freq = f

		if self.robot_music_box.notes == self.robot_music_box.current_note and self.robot_music_box.note_on == False:
			self.robot_music_box = None
					

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
	try:
		message = message.decode()
		if message.count('arr') > 1:
			return None
		message = json.loads(message)

		items = message["arr"]
		return items
	except:
		return None

#
#arduino_queue = []
#
#def arduino_thread(robot):
#	robot.update_motor_speed()

#
socket_queue = []
#
def socket_thread(socket, robot):
	socket_connected = True
	while socket_connected:
		message = socket.receive()
		if message.decode() == '':
			terminate()
		if message is not None:
			print(f'received {message}')
			message_items = handle_message_commands(message)
			if message_items is not None:
				robot.update_values_with_json(message_items)

	socket.close()



if __name__ == '__main__':

	arduino = serial_port(115200, port=0, prefix='/dev/ttyACM')
	#arduino = serial_port(115200,port=24,prefix='COM')
	print("controller assigned")
	print(arduino.receive())

	robot = P3_DX_robot(robot_controller=arduino)

	#robot.send_message(91, [robot.kp,robot.ki,robot.kd])
	robot.send_message(92, [1])

	s = network_sock()
	s.connect(server_ip, server_port)

	run_flag = True

	sock_thread = threading.Thread(target=socket_thread, args=(s, robot))
	print(sock_thread)
	sock_thread.start()
	robot.start_robot_update_timers()

	robot.start_music_box(1, tempo=160)
	#robot.start_music_box(2, tempo=114)
	#robot.start_music_box(3, tempo=144)

	while run_flag:

		if not sock_thread.is_alive():
			robot.left_motor_speed = 0
			robot.right_motor_speed = 0
			robot.update_motor_speed(forced=True)
			if autoreconnect_socket:
				print("looking for new socket connection")
				s = network_sock()
				s.connect(server_ip, server_port)
				print("new socket connected")
				sock_thread = threading.Thread(target=socket_thread, args=(s, robot))
				sock_thread.start()
			else:
				run_flag = False

		robot.update_motor_speed()
		robot.get_encoder_values()
		robot.get_button_values()
		robot.handle_buttons()
		robot.handle_music_box()