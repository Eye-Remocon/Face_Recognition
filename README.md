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
  <code>$ pip install flask</code>
  </pre>



Version1. 내용
---------------------------------------------------
- face_recognition 폴더에 비교할 사진 파일을 저장함 
 <img width="875" alt="스크린샷 2021-05-23 오전 12 59 51" src="https://user-images.githubusercontent.com/54658745/119233168-9bcca000-bb62-11eb-8917-220267ce2823.png">
  
- face_recognition/recognize_faces_in_pictures.py 실행시 biden과 obama, obama2 이미지를 가져와 face_encoding
- biden(known), obama(known)와 obama2(unknown) 인코딩 값을 compare_faces
- 출력 값 
  - biden(known)과 obama2(unknown)는 같은 인물이 아니므로 False값 출력
  - obama(known)와 obama2(unknown)는 같은 인물이므로 True값 출력
  - obama2(unknown)은 obama(known)와 같은 인물이므로 known이라 판단하여 False출력
  <img width="1208" alt="스크린샷 2021-05-23 오전 12 59 20" src="https://user-images.githubusercontent.com/54658745/119233350-873cd780-bb63-11eb-87ec-8379991c7a15.png">


