from controller import joy_device, joy_mixing

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
                #message = s.receive()
                #print(message)
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
        exit()