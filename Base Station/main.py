from controller import joy_device
from robot_communications import commands
from network import network_sock
from inputs import devices
import time

host_ip = '192.168.1.5'
server_port = 12345
drive_type = 1

if __name__ == "__main__":
	s = network_sock()
	s.bind(host=host_ip, port=server_port)

	try:
		joy = joy_device(devices.gamepads[0])
		joy.start_gamepad_thread()
	except:
		print("no gamepads")


	try:
		x_joy_L = 0
		y_joy_L = 0

		x_joy_R = 0
		y_joy_R = 0

		left_motor = 0
		right_motor = 0

		while s.sock != None:

			pay_pack=[]

			events = joy.pop_gamepad_queue()

			print(len(events))
			print(events)
			for event in events:

				if drive_type == 1:

					if event["event"] == "ABS_Y":
						left_motor = joy.normalize_joy(event["value"])
						for item in commands.motor(left_motor_val=left_motor):
							pay_pack.append(item)

					if event["event"] == "ABS_RY":
						right_motor = joy.normalize_joy(event["value"])
						for item in commands.motor(right_motor_val=right_motor):
							pay_pack.append(item)

					if event["event"] == "BTN_TR":
						if event["value"] == 1:
							joy.limit = 40
							left_motor = left_motor*4
							right_motor = right_motor*4
						else:
							joy.limit = 15
							left_motor = left_motor/(40/15)
							right_motor = right_motor/(40/15)

						for item in commands.motor(right_motor_val=right_motor, left_motor_val=left_motor):
							pay_pack.append(item)


				elif drive_type == 2:
					if event["event"] == "ABS_RX":
						x_joy_R = event["event"]
						left_motor, right_motor = joy.mix_joy(x_joy_R, y_joy_R)
						for item in commands.motor(left_motor_val=left_motor, right_motor_val=right_motor):
							pay_pack.append(item)

					if event["event"] == "ABS_RY":
						y_joy_R = event["event"]
						left_motor, right_motor = joy.mix_joy(x_joy_R, y_joy_R)
						for item in commands.motor(left_motor_val=left_motor, right_motor_val=right_motor):
							pay_pack.append(item)

					if event["event"] == "BTN_TR":
						if event["event"] == 1:
							joy.limit = 40
						else:
							joy.limit = 10

						left_motor, right_motor = joy.mix_joy(x_joy_R, y_joy_R)
						for item in commands.motor(left_motor_val=left_motor, right_motor_val=right_motor):
							pay_pack.append(item)


			print(pay_pack)
			if len(pay_pack) > 0:
				print(commands.format_arr(pay_pack))
				s.send(commands.format_arr(pay_pack))

			time.sleep(.0001)

	except:  # this never happens KeyboardInterrupt
		print("Script aborted")
		joy.stop_thread()
		print("joy stopped")
		abcd_1234()
		s.send(commands.format_arr(commands.stop()))
		print("socket sent")
		s.close()
		print("socket close")
		
		#sys.exit(0)
		terminate()
		print("reached end")
		abcd_1234()