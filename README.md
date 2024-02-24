# 청각 장애인을 위한 시각 알람, Glow Alarm 💡
스마트 전구를 이용한 시각 알람 어플리케이션

<p align="center">
  <img src="https://github.com/sound-light/Glow-Alarm/assets/131771046/4e50fc5b-7b55-4e1a-9c71-31fbaedeb1bd">
</p>

##Project Overview
In the event of a fire, evacuation alerts are issued but rely solely on sound, becoming ineffectual for those with deaf and hard of hearing, highlighting a critical social inequality. Neuroplasticity suggests that individuals with hearing loss often have enhanced visual capabilities, making visual alarms a preferred method for alerts, as indicated by research in the *Fire Technology journal's* "Alarm Technologies to Wake Sleeping People Who are Deaf or Hard of Hearing (2022)." This underscores the necessity for a visual warning system.


Addressing this need, we developed Glow Alarm, a system providing visual alerts through lights and flashes, aiding those with hearing impairments in recognizing emergency situations promptly. This system utilizes red lights and flashing effects for alerts, seamlessly integrating with current auditory alert systems to ensure quick responses during emergencies, playing a vital role in life-saving situations.


## 주요 기능

- 실시간 재난 정보 제공: 재난API를 활용하여 실시간으로 재난 정보를 받아옵니다.
- 위험도 분석: Gemini를 이용하여 받아온 재난 정보의 위험도를 분석합니다.
- 다양한 전구 설정: 위험도에 따라 다른 전구의 색, 밝기, 빠르기를 제공하여 시각적으로 위험을 알립니다.
- 구글 로그인 지원: 사용자는 구글 로그인을 통해 Glow Alarm에 접속할 수 있습니다.

## 기술 스택

Glow Alarm은 다음과 같은 기술 스택을 사용합니다:

- Gemini: 재난 정보의 위험도를 분석하기 위해 사용됩니다.
- Flutter: Glow Alarm의 프론트엔드 개발에 사용됩니다.
- Firebase: 사용자 인증 및 데이터베이스 관리에 사용됩니다.
- FastAPI: 백엔드 개발에 사용됩니다.
- Google Cloud Platform: Glow Alarm의 배포 및 호스팅에 사용됩니다.

## How To Use

1. Install the Glow Alarm.
2. Prepare the Yeelight smart bulb.
3. Press the icon located in the top right corner of the home screen to check if it is connected to the Yeelight smart bulb.
4. Personalized Alarm:
- Press the + icon on the home screen to set the time you want to wake up.
- You can set the desired color of the bulb.
  
5. Disaster Alarm:
- There are no separate settings! Glow Alarm analyzes disaster messages with AI to determine their importance.
- For disasters requiring immediate evacuation, the red light will wake you up.
- For less urgent disasters that still require your attention, the blue light will wake you up.



## Expectation Effects

1. Deaf and hard of hearing will become safer in disaster situations since they can swiftly respond to emergencies through visual alerts, facilitating smoother prevention and response during accidents.
2. Improve the quality of daily life for deaf and HoH as they can receive various alerts more effectively, not only in disaster situations but also in everyday life, helping boost their confidence and independence.
3.  Enhance social inclusivity by ensuring that all individuals have equal access to information and opportunities to respond in disaster situations, thereby contributing to reducing social inequality among community members.


## Team Members

| 윤병욱 [@speculatingwook](https://github.com/speculatingwook)| 이지민 [@clicelee](https://github.com/clicelee)       | 윤수혁 [@ShuYuns](https://github.com/ShuYuns)        | 강성우 [@KSW-KSM](https://github.com/KSW-KSM)         |
|---------------------------|-----------------------------|-----------------------------|-----------------------------|
| Backend/PM                | Backend/Designer            | Frontend                    | AI                          |

