def format_robot_message(command, val1=None, val2=None, val3=None, val4=None, val5=None, val6=None):
	msg = []
	msg.append(command)
	if val1 is not None:
		msg.append((int(val1)&0xFF00)>>8)
		msg.append(int(val1)&0x00FF)
	if val2 is not None:
		msg.append((int(val2)&0xFF00)>>8)
		msg.append(int(val2)&0x00FF)
	return bytearray(msg)

def parse_robot_message(msg):
	msg = list(msg)
	command = msg[0]
	val1 = (msg[1]<<8)+msg[2]
	val2 = (msg[3]<<8)+msg[4]
	val3 = (msg[5]<<8)+msg[6]
	val4 = (msg[7]<<8)+msg[8]
	val5 = (msg[9]<<8)+msg[10]
	val6 = (msg[11]<<8)+msg[12]

	return command, [val1,val2,val3,val4,val5,val6]

def send_ok(command):
	return format_robot_message(command,'OK')

def format_motor_command(left_motor_val, right_motor_val):
	return format_robot_message(10,left_motor_val,right_motor_val)