from inputs import devices, get_gamepad
import socket
import sys
import time
import socket
import json
from math import pi, cos

server_port = 12345
host_ip = '192.168.1.5'

class network_sock:

    def __init__(self, message_size=256, sock=None):
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

        self.message_size = message_size
        self.master = False
        self.clientsock = None
        self.clientaddr = None


    def bind(self, host, port):
        self.sock.bind((host, port))
        self.sock.listen(5)

        self.master = True

    def connect(self, host, port):
        self.sock.connect((host, port))

    def send(self, msg):
        if self.master:
            if self.clientsock is None:
                self.clientsock, self.clientaddr = self.sock.accept()
            self.clientsock.send(msg)
        else:
            self.sock.send(msg)

    def receive(self):
        if self.master:
            msg = self.clientsock.recv(self.message_size)
        else:
            msg = self.sock.recv(self.message_size)
        if msg is not None:
            return msg

    def close(self):
        if self.master:
            self.clientsock.close()
            self.clientsock = None 
            self.address = None 
            self.master = False
        else:
            self.sock.close()



class commands:
    def motor(left_motor_val=None, right_motor_val=None):
        arr = []
        if left_motor_val is not None:
            arr.append({"left_motor_speed": left_motor_val})
        if right_motor_val is not None:
            arr.append({"right_motor_speed": right_motor_val})

        #print(arr)
        return arr

    def ok():
        return [{"OK": "OK"}]

    def stop():
        return [{"STOP":"STOP"}]

    def format_arr(pay_arr):
        msg = json.dumps({"arr":pay_arr})
        return bytes(msg, 'utf-8')


joystick_max_val = 32767
limit = 10
def normalize_joy(val):
    #NewValue = (((OldValue - OldMin) * (NewMax - NewMin)) / (OldMax - OldMin)) + NewMin
    newval = (((val+joystick_max_val)*(limit*2))/(2*joystick_max_val))-limit
    #print(newval)
    if -2 < newval < 2:
        return 0
    else:
        return newval

deadzone = 10
def mix_joy(xval, yval):
    newx = (((xval+joystick_max_val)*(90*2))/(2*joystick_max_val))-90
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
    print(f'l: {left} ||| r: {right}')
    left = limit * left
    right = limit * right #((newy*limit)/100)

    return left, right


left_motor = 0
right_motor = 0

drive_type = 2 #0:nothing, 1:tank, 2:single stick
x_joy = 0
y_joy = 0

if __name__ == "__main__":
    s = network_sock()
    s.bind(host_ip, server_port)
    try:
        #for dev in devices:
        #    print(dev)
        while s.sock != None:
            #print('started loop')
            #time.sleep(2)
            #print("sending message")

            pay_pack=[]

            #try:
            events = get_gamepad()
            #print(events)
            print(len(events))
            for event in events:
                #print(event.code)
                #print(event.state)
                #print(event.code == "ABS_Y")
                if drive_type == 1:
                    if event.code == "ABS_Y":
                        left_motor = normalize_joy(event.state)
                        for item in commands.motor(left_motor_val=left_motor):
                            pay_pack.append(item)
                    if event.code == "ABS_RY":
                        right_motor = normalize_joy(event.state)
                        for item in commands.motor(right_motor_val=right_motor):
                            pay_pack.append(item)
                    if event.code == "BTN_TR":
                        if event.state == 1:
                            limit = 40
                            left_motor = left_motor*4
                            right_motor = right_motor*4
                        else:
                            limit = 10
                            left_motor = left_motor/4
                            right_motor = right_motor/4

                        for item in commands.motor(right_motor_val=right_motor, left_motor_val=left_motor):
                            pay_pack.append(item)


                elif drive_type == 2:
                    if event.code == "ABS_RX":
                        x_joy = event.state
                        left_motor, right_motor = mix_joy(x_joy, y_joy)
                        for item in commands.motor(left_motor_val=left_motor, right_motor_val=right_motor):
                                pay_pack.append(item)
                        
                    if event.code == "ABS_RY":
                        y_joy = event.state
                        left_motor, right_motor = mix_joy(x_joy, y_joy)
                        for item in commands.motor(left_motor_val=left_motor, right_motor_val=right_motor):
                                pay_pack.append(item)

                    if event.code == "BTN_TR":
                        if event.state == 1:
                            limit = 40
                        else:
                            limit = 10
                            
                        left_motor, right_motor = mix_joy(x_joy, y_joy)
                        for item in commands.motor(left_motor_val=left_motor, right_motor_val=right_motor):
                            pay_pack.append(item)


            #except:
             #   print("no get_gamepad")
            #    time.sleep(2)

            #for item in commands.motor(10,-10): pay_pack.append(item)

            print(pay_pack)
            #if len(pay_pack) == 0:
            #    for item in commands.ok(): pay_pack.append(item)
            if len(pay_pack) > 0:
                print(commands.format_arr(pay_pack))
                s.send(commands.format_arr(pay_pack))
                message = s.receive()
                print(message)
            #s.send(commands.format_arr(pay_pack))
            #message = s.receive()
            #print(message)

            #time.sleep(.1)
            time.sleep(.0001)

    except KeyboardInterrupt:  # this never happens
        print("Script aborted")
        s.send(commands.format_arr(commands.stop()))
        s.close()
        sys.exit(0)





    #     try:
    #     for device in devices:
    #         print(device)
    #     ws = websocket.WebSocket()
    #     ws.connect(esp8266host)
    #     print("Ready !")

    #     speed = 0
    #     steering = 0;
    #     brake = True

    #     while True:
    #         events = get_gamepad()
    #         for event in events:
    #             if event.code is "BTN_TL" and event.state is 1:
    #                 brake = True
    #             if event.code is "BTN_TR" and event.state is 1:
    #                 brake = False
    #             if event.code is "ABS_Y":
    #                 speed = event.state
    #             if event.code is "ABS_RX":
    #                 steering = event.state
    #         payload = {"speed": speed, "steering": steering, "brake": brake}
    #         print(json.dumps(payload))
    #         ws.send(json.dumps(payload))
    #         #ws.send("jtm")
    #         time.sleep(.20)

    #     ws.send(json.dumps({"speed": 0, "steering": 0, "brake": True}))
    #     ws.close()
    #     exit()

    # except KeyboardInterrupt:
    #     ws.send(json.dumps({"speed": 0, "steering": 0, "brake": True}))
    #     ws.close()