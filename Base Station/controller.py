#https://inputs.readthedocs.io/en/latest/user/quickstart.html
from inputs import devices, get_gamepad
from math import pi, cos

from _thread import *
import threading
#this class is not fully tested yet, assume multithreading does not currently work
class joy_device():
	def __init__(self, device):
		self.joystick_max_val = 32767
		self.speed_limit = 10
		self.deadzone = 10
		self.gamepad_queue = []
		self.device_id = device.manager
		self.gamepad_thread = None
		self.gamepad_thread_active = False

def queue_gamepade_input(self):
	while self.gamepad_thread_active:
		new_input = get_gamepad_input()
		for item in new_input:
			self.gamepad_queue.append(item)
	else:
		print("gamepad thread stopped")

def get_gamepad_input(self):
	list_events = []
	events = get_gamepad()
	for event in events:
		if event.device.manager == self.device_id:
			list_events.append({"event":event.code,"value":event.state})
	return list_events

def start_gamepad_thread(self):
	self.gamepad_thread_active = True
	self.gamepad_thread = threading.Thread(target=queue_gamepade_input)
	self.gamepad_thread.start()

def stop_gamepad_thread(self):
	self.gamepad_thread_active = False
	self.gamepad_thread = None

class joy_mixing():
	def normalize_joy(val, joystick_max_val, limit):
	    #NewValue = (((OldValue - OldMin) * (NewMax - NewMin)) / (OldMax - OldMin)) + NewMin
	    newval = (((val+joystick_max_val)*(limit*2))/(2*joystick_max_val))-limit
	    #print(newval)
	    if -2 < newval < 2:
	        return 0
	    else:
	        return newval

	#https://home.kendra.com/mauser/joystick.html

	def mix_joy(xval, yval, deadzone):
	    newx = (((xval+joystick_max_val)*(100*2))/(2*joystick_max_val))-100
	    newy = (((yval+joystick_max_val)*(100*2))/(2*joystick_max_val))-100

	    if -deadzone < newx < deadzone:
	        newx = 0
	    if -deadzone < newy < deadzone:
	        newy = 0

	    newx = -1 * newx
	    V = (100-abs(newx))*(newy/100)+newy
	    W = (100-abs(newy))*(newx/100)+newx
	    left = ((V-W)/2)/100
	    right = ((V+W)/2)/100
	    #print(f'l: {left} ||| r: {right}')
	    left = limit * left
	    right = limit * right #((newy*limit)/100)

	    return left, right