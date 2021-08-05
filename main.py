import cv2
import time
import os
from camera import capture_image_by_webcam
from face_detection import crop, user_identify, find_faces_in_picture
from common import img_encoding, file_manipulation
from service import categorization
from service import emotion_detection

video_capture = cv2.VideoCapture(0)  # 카메라 세팅
window_name = "cam-test"  # 창 이름
capture_image_by_webcam.set_window_name(window_name)  # 창 이름 지정

automatic_capture_img_dir = "./img/"  # 1초 마다 촬영되는 사진이 저장되는 디렉터리
cropped_img_dir = "./cropped_img/"  # crop된 이미지 저장 디렉터리
known_img_dir = "./knowns"  # 이 서비스에 등록된 구성원의 사진이 저장되는 디렉터리
save_img_ext = ".jpg"  # 이미지 확장자명

# 서비스 가동 시작
known_img_encodings = img_encoding.get_known_img_encodings(known_img_dir)  # knowns 폴더에 있는 모든 사진에 대하여 encoding 진행
known_img_list = os.listdir(known_img_dir)  # knowns 폴더에 있는 모든 사진의 이름을 리스트 형태로 저장
# 나중에 카메라에서 촬영된 사진과 knowns에 있는 사진을 비교해서 등록된 사람인지 확인하는데 사용됨

start_time = time.time()  # 타이머 작동 시(1초가 지나면 카메라 촬영)
while True:
    capture_image_by_webcam.show_camera_frame(video_capture, window_name)  # 프레임 단위로 카메라 장면을 화면에 나타냄
    k = cv2.waitKey(1)
    if time.time() - start_time >= 1:  # check if 1 sec passed, 1초마다
        current_time = time.strftime('%y%m%d_%H%M%S', time.localtime(time.time()))  # 촬영될 이미지 파일 이름 지정
        automatic_capture_img_name = automatic_capture_img_dir + current_time + save_img_ext
        capture_image_by_webcam.do_video_capture(video_capture, window_name, automatic_capture_img_name)  # 카메라 촬영

        # 방금 촬영한 사진과 knowns 폴더에 있난 사진과 비교 작업, 즉, face distance 측정
        face_distances = user_identify.get_face_distance(known_img_encodings, automatic_capture_img_name)

        if user_identify.is_registered(face_distances):  # 촬영된 사진에 있는 사람이 등록된 사람인지 확인
            # 만약 등록된 사람이라면
            categorization.member_id_categorization(face_distances, known_img_list)  # 카메라에 촬영된 사람이 누구인지 판별하고 출력

            # 감정 인식 과정
            # 'ANGRY', 'DISGUS', 'FEAR', 'HAPPY', 'NEUTRAL', 'SAD', 'SURPRISE' 중 7가지 감정 값 반환
            emotion = emotion_detection(automatic_capture_img_name)

            # 이미지 crop 과정, 필요없을 시 생략 가능
            cropped_img_name = cropped_img_dir + current_time + "_crop" + save_img_ext
            face_locations = find_faces_in_picture.get_face_locations_in_picture(automatic_capture_img_name)
            crop.crop_img(automatic_capture_img_name, face_locations, cropped_img_name)
            file_manipulation.remove_file(automatic_capture_img_name)  # 방금 촬영한 사진 삭제
        start_time = time.time()  # 타이머 초기

    if k & 0xFF == ord('q'):  # q키를 누르면 종료
        break

video_capture.release()
cv2.destroyAllWindows()
