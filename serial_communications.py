#import serial as Serial
from serial import Serial

class serial_port:
	def __init__(self, baud=115200, port=None, prefix='/dev/ttyUSB'):
		self.sp = None

		if port:
			try:
				self.sp = Serial(f'{prefix}{port}', baud)
			except:
				print(f'Invalid serial port {prefix}{port}')
		else:
			ports = []
			for port in range(0,32):
				try:
					temp = Serial(f'{prefix}{port}', baud)
					temp.close()
					ports.append(f'{prefix}{port}')
				except:
					continue

			if len(ports) >= 2:
				print(f'The following serial ports are available:\n\t{ports}\nEnter the robot port number:')
				resp = input()
				self.sp = Serial(f'{prefix}{resp}', baud)
			elif len(ports) == 1:
				self.sp = Serial(f'{prefix}{port}', baud)
			else:
				print("No available serial port detected")

	def send(self, message):
		if self.sp:
			self.sp.write(message.encode())
			return True
		else:
			return False

	def receive(self):
		response = self.sp.readline()
		print(response)
		if response:
			resp = response.decode('utf-8').strip('\r\n').strip('<').strip('>')
			resp = resp.split(',')
			return resp[1], resp[2:]
		else:
			return None