import json

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
