from yeelight import discover_bulbs, Bulb, LightType
import time
# IP 정보 받아오기

# IP 정보에 맞게 Bulb 객체를 유저와 함께 저장

# 주기적으로 깜빡거리는 함수 만들기


# 재난함수(중요도 상)
def disaster_function_high_priority(bulb):
    while True:
        bulb.set_rgb(255, 0, 0)  # 빨간색으로 설정
        bulb.set_brightness(50)  # 밝기를 50%로 설정
        time.sleep(15)  # 15초 대기
        bulb.turn_off()  # 5초 꺼짐
        time.sleep(5)  
        bulb.set_brightness(70)  # 밝기를 70%로 설정
        time.sleep(15)  # 15초 대기
        bulb.turn_off()  # 5초 꺼짐
        time.sleep(5)  
        bulb.set_brightness(100)  # 밝기를 100%로 설정
        time.sleep(15)  # 15초 대기
        bulb.turn_off()  # 5초 꺼짐
        time.sleep(5) 

# 재난함수(중요도 중)
def disaster_function_medium_priority(bulb):
    while True:
        bulb.set_rgb(0, 0, 255)  # 파란색으로 설정
        bulb.set_brightness(10)  # 밝기를 10%로 설정
        time.sleep(10)  # 10초 대기
        bulb.turn_off()  # 5초 꺼짐
        time.sleep(5)  
        bulb.set_brightness(30)  # 밝기를 30%로 설정
        time.sleep(10)  # 10초 대기
        bulb.turn_off()  # 5초 꺼짐
        time.sleep(5)  
        bulb.set_brightness(50)  # 밝기를 50%로 설정
        time.sleep(10)  # 10초 대기
        bulb.turn_off()  # 최종꺼짐

# 개인 알람
def personal_alarm(bulb, selected_color):
    while True:
        # 어플에서 선택한 색상을 설정
        bulb.set_rgb(selected_color[0], selected_color[1], selected_color[2])
        bulb.turn_on()  # 전구 켜기
        time.sleep(4)  # 4초 대기
        bulb.turn_off()  # 전구 끄기
        time.sleep(1)  # 1초 대기
