Face_Recognition
===================================================
- Version1 (Simple Face Detection & Recognition)

개발환경 구축
---------------------------------------------------
# 라즈베리 A(Face Recognition 수행)
1. edge-orchestration build 및 run
- [링크](https://github.com/lf-edge/edge-home-orchestration-go/blob/master/docs/platforms/raspberry_pi3/raspberry_pi3.md#2-build-directly-on-the-raspberry-pi-3-board)
- 설정
```
$ go get github.com/axw/gocov/gocov
$ go get github.com/matm/gocov-html
$ go install honnef.co/go/tools/cmd/staticcheck@latest
$ make distclean
$ make create_context CONFIGFILE=armc
$ make
$ make run
```
2. python3 설치
3. open-cv 설치
- [링크](https://qengineering.eu/install-opencv-4.1-on-raspberry-pi-4.html)
4. 패키지 설치
```
$ sudo apt-get update
$ sudo apt-get upgrade
$ sudo apt-get install python3-pip
$ pip3 install dlib
$ pip3 install face_recognition
$ pip3 install requests
```
5. 코드 변경
- [링크](https://github.com/Eye-Remocon/Face_Recognition/blob/27e4bd02bc198f59c616d9b73bcfae34a43219a2/main_multiprocessing.py#L15) 감정인식 api 돌리는 ip주소로 변경
- [링크](https://github.com/Eye-Remocon/Face_Recognition/blob/27e4bd02bc198f59c616d9b73bcfae34a43219a2/service/hw_request.py#L7) hw_control api 돌리는 ip주소로 변경

# 아두이노 셋팅
1. 아두이노 IDE 설치 및 설정
- [참조](https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=kwangtree&logNo=221163824480)
- LED 및 장치 연결 방법 (@hewun7427)
- Arduino IDE에서 [코드](https://github.com/Eye-Remocon/HW_Control/blob/main/arduino/led.ino) 활용해서 업로드
- 라즈베리파이 B와 아두이노 우노보드 USB로 연결

# 라즈베리 B(HW_Control 수행)
1. 업데이트
```
$ sudo apt-get update
$ sudo apt-get upgrade
```
2. python3 설치
3. 패키지 설치
```
$ sudo apt-get install python3-pip
$ pip3 install flask
$ pip3 install pyserial
```
4. git clone
```
$ git clone https://github.com/Eye-Remocon/HW_Control.git
$ cd hw_control
```
4. main.py 동작시켜서 API 실행

# 우분투(리눅스)
1. virtual box 가상 네트워크 브리지 어댑터로 변경
- [참고](https://technote.kr/213)
2. edge-orchestration build 및 run
- [링크](https://github.com/lf-edge/edge-home-orchestration-go/blob/master/docs/platforms/x86_64_linux/x86_64_linux.md#how-to-build)
3. pose_detection image build
```
$ git clone https://github.com/Eye-Remocon/Pose_Detection.git
$ cd pose_detection
$ docker build --tag eye-remocon/pose_detection:node .
```
4. pose_detection 서비스 등록
- 아래 내용의 파일을 `/var/edge-orchestration/apps/pose_detection/pose_detection.conf`에 저장
```
# Description of service that will be requested
[Version]
ConfVersion=v0.0                    ; Version of Configuration file

[ServiceInfo]
ServiceName=pose_detection          ; Name of distributed service
ExecType=container
ExecCmd=docker run -p 3500:3333 eye-remocon/pose_detection:node
```

# 감정인식 API 
- git clone
``` 
$ git clone https://github.com/Eye-Remocon/Emotion_detection.git
$ cd emotion_detection/emotion_detection
```
- [링크](https://github.com/Eye-Remocon/Emotion_detection)의 README.md에서 개발환경 구축 및 AWS 설정 참조
- main.py 로 API 실행


