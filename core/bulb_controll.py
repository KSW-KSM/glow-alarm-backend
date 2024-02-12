from yeelight import discover_bulbs, Bulb, LightType
import time
# IP 정보 받아오기

# IP 정보에 맞게 Bulb 객체를 유저와 함께 저장

# 주기적으로 깜빡거리는 함수 만들기


print(discover_bulbs())


bulb = Bulb('172.30.1.64')


def blink_periodically(bulb, interval_seconds, total_blinks):
    for _ in range(total_blinks):
        bulb.toggle()  # 불 켜기/끄기
        time.sleep(interval_seconds)  # 주기적으로 깜빡이기 위한 대기


def control_bulb(bulb, action, *args):
    if action == 'turn_on':
        bulb.turn_on()
    elif action == 'turn_off':
        bulb.turn_off()
    elif action == 'toggle':
        bulb.toggle()
    elif action == 'set_brightness':
        if len(args) == 1:
            bulb.set_brightness(args[0])
        elif len(args) == 2:
            bulb.set_brightness(args[0], light_type=LightType.Ambient)
    elif action == 'set_rgb':
        if len(args) == 3:
            bulb.set_rgb(*args)
    elif action == 'set_hsv':
        if len(args) == 2:
            bulb.set_hsv(args[0], args[1])
        elif len(args) == 3:
            bulb.set_hsv(args[0], args[1], args[2])
    elif action == 'set_color_temp':
        if len(args) == 1:
            bulb.set_color_temp(args[0])
    elif action == 'set_default':
        bulb.set_default()
    else:
        print("Invalid action")


# control_bulb(bulb, 'set_brightness' ,100)
# control_bulb(bulb, 'turn_on')
blink_periodically(bulb, 0.5, 10)
