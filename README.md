Face_Recognition
===================================================
- Version1 (Simple Face Detection & Recognition)

개발환경 구축
---------------------------------------------------
- python3 version(Anaconda3 추천) 설치 필수
- 패키지 설치 전 가상환경 생성 후 환경 분리 추천(Linux & Mac)
- 필요 패키지 설치(Linux & Mac)
  <pre>
  <code>$ pip install --upgrade pip</code>
  <code>$ pip install opencv-python</code>
  <code>$ pip install opencv-contrib-python</code>
  <code>$ pip install CMake</code>
  <code>$ pip install dlib</code>
  <code>$ pip install face_recognition</code>
  <code>$ pip install pip install flask</code>
  </pre>



Version1. 내용
---------------------------------------------------
- knowns 폴더에 가족 구성원의 사진 파일을 저장함
 <img width="768" alt="KakaoTalk_20210505_151828132" src="https://user-images.githubusercontent.com/54658745/117103565-895a1480-adb5-11eb-884f-4da63480e688.png">
 
 
- who 폴더에 누구인지 확인할 사진 파일을 저장 (iuiu.jpeg, Song.png)
 <img width="769" alt="KakaoTalk_20210505_151828132_01" src="https://user-images.githubusercontent.com/54658745/117103580-8fe88c00-adb5-11eb-9d4d-876549013c78.png">
 
 
- face_recognition1.py 실행시 knowns에서 가족 구성원의 이미지를 가져와 인코딩 값을 저장
- who 폴더에서 아이유, 송중기 사진을 각각 인코딩 한 후 가족구성원의 사진들과 각각 face_distance를 계산
- face_distance를 계산하여 거리가 가장 가까운 가족구성원을 매칭시키고 그 distance가 0.4 미만일 때만 가족구성원의 이름 출력, 0.4 이상이면 Unknown 출력
- 아이유는 Daughter 출력, 송중기는 Unknown 출력된 걸 확인 가능


 <img width="1019" alt="KakaoTalk_20210505_151828132_02" src="https://user-images.githubusercontent.com/54658745/117103598-97a83080-adb5-11eb-94e1-445bf3791433.png">
