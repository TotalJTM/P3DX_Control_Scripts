import json

# def format_robot_message(command, val1=None, val2=None, val3=None, val4=None, val5=None, val6=None):
# 	msg = []
# 	msg.append(command)
# 	if val1 is not None:
# 		msg.append((int(val1)&0xFF00)>>8)
# 		msg.append(int(val1)&0x00FF)
# 	else:
# 		msg.append(0)
# 		msg.append(0)

# 	if val2 is not None:
# 		msg.append((int(val2)&0xFF00)>>8)
# 		msg.append(int(val2)&0x00FF)
# 	else:
# 		msg.append(0)
# 		msg.append(0)

# 	if val3 is not None:
# 		msg.append((int(val3)&0xFF00)>>8)
# 		msg.append(int(val3)&0x00FF)
# 	else:
# 		msg.append(0)
# 		msg.append(0)

# 	if val4 is not None:
# 		msg.append((int(val4)&0xFF00)>>8)
# 		msg.append(int(val4)&0x00FF)
# 	else:
# 		msg.append(0)
# 		msg.append(0)

# 	if val5 is not None:
# 		msg.append((int(val5)&0xFF00)>>8)
# 		msg.append(int(val5)&0x00FF)
# 	else:
# 		msg.append(0)
# 		msg.append(0)

# 	if val6 is not None:
# 		msg.append((int(val6)&0xFF00)>>8)
# 		msg.append(int(val6)&0x00FF)
# 	else:
# 		msg.append(0)
# 		msg.append(0)

# 	return bytearray(msg)

# def parse_robot_message(msg):
# 	msg = list(msg)
# 	command = msg[0]
# 	val1 = int((msg[1]<<8)+msg[2])
# 	val2 = int((msg[3]<<8)+msg[4])
# 	val3 = int((msg[5]<<8)+msg[6])
# 	val4 = int((msg[7]<<8)+msg[8])
# 	val5 = int((msg[9]<<8)+msg[10])
# 	val6 = int((msg[11]<<8)+msg[12])

# 	return command, [val1,val2,val3,val4,val5,val6]

# def convert_to_signed(val):
# 	if val&0x8000:
# 		return (~val)-1
# 	else:
# 		return val

# def convert_to_

# def send_ok(command):
# 	return format_robot_message(command,'OK')

# def format_motor_command(left_motor_val, right_motor_val):
# 	return format_robot_message(10,left_motor_val,right_motor_val)

# def parse_message(message):
# 	message_json = json.loads(message.decode())
	
# 	command = 0
# 	message_dict = []

# 	for item in message_json:
# 		if item is "command":
# 			command = item
# 		else:
# 			message_dict.append(item)
# 	return command, message_dict

# def format_motor_command(left_motor_val, right_motor_val):
# 	message_json = {
# 					"command": 10,
# 					"left_motor_speed": left_motor_val,
# 					"right_motor_speed": right_motor_val
# 					}
# 	return json.dumps(message_json).encode(encoding='utf-8')

# def send_ok(command):
# 	return format_robot_message(command,'OK')	

def send_ok():
    return ["OK": "OK"]

def stop_command():
    return ["STOP":"STOP"]

def format_msg_from_arr(pay_arr):
    msg = json.dumps({"arr":pay_arr})
    return msg.encode('utf-8')