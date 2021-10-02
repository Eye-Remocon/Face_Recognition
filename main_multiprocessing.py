import cv2, time, os
from camera import capture_image_by_webcam
from face_detection import crop, user_identify, find_faces_in_picture
from common import img_encoding, file_manipulation
from service import categorization, emotion_detection, play_music
from multiprocessing import Process  # 멀티프로세싱 작업
from service import taskoffloading
from service import pose_detection
from service import hw_request

automatic_capture_img_dir = "./img/"  # 1초 마다 촬영되는 사진이 저장되는 디렉터리
cropped_img_dir = "./cropped_img/"  # crop된 이미지 저장 디렉터리
known_img_dir = "./knowns"  # 이 서비스에 등록된 구성원의 사진이 저장되는 디렉터리
save_img_ext = ".jpg"  # 이미지 확장자명

key = 'http://0.0.0.0:9900'
dest = os.getenv('ENV', key)

# 서비스 가동 시작
known_img_encodings = img_encoding.get_known_img_encodings(known_img_dir)  # knowns 폴더에 있는 모든 사진에 대하여 encoding 진행
known_img_list = os.listdir(known_img_dir)  # knowns 폴더에 있는 모든 사진의 이름을 리스트 형태로 저장
# 나중에 카메라에서 촬영된 사진과 knowns에 있는 사진을 비교해서 등록된 사람인지 확인하는데 사용됨


def eye_remocon_service():
    video_capture = cv2.VideoCapture(0)  # 카메라 세팅
    window_name = "cam-test"  # 창 이름
    capture_image_by_webcam.set_window_name(window_name)  # 창 이름 지정

    flag = True  # 음악 재생 플래그. 만약 음악이 재생되고 있지 않을 경우 즉시 flag를 False로 바꾸고 음악이 끝날때까지 감정인식을 진행하지 않는다.

    start_time = time.time()  # 타이머 작동 시(1초가 지나면 카메라 촬영)
    while True:
        capture_image_by_webcam.show_camera_frame(video_capture, window_name)  # 프레임 단위로 카메라 장면을 화면에 나타냄
        k = cv2.waitKey(1)
        
        if time.time() - start_time >= 1:  # 1초마다
            current_time = time.strftime('%y%m%d_%H%M%S', time.localtime(time.time()))  # 현재 시각을 문자열로 저장(예: 210819_122205)
            automatic_capture_img_name = automatic_capture_img_dir + current_time + save_img_ext  # 촬영될 이미지 파일 이름 지정
            capture_image_by_webcam.do_video_capture(video_capture, automatic_capture_img_name)  # 카메라 촬영

            # 방금 촬영한 사진과 knowns 폴더에 있난 사진과 비교 작업, 즉, face distance 측정
            face_distances = user_identify.get_face_distance(known_img_encodings, automatic_capture_img_name)

            if user_identify.is_registered(face_distances):  # 촬영된 사진에 있는 사람이 등록된 사람인지 확인
                # 만약 등록된 사람이라면
                categorization.member_id_categorization(face_distances, known_img_list)  # 카메라에 촬영된 사람이 누구인지 판별하고 출력

                # 감정 인식 과정
                # 'ANGRY', 'DISGUST', 'FEAR', 'HAPPY', 'NEUTRAL', 'SAD', 'SURPRISE' 중 7가지 감정 값 반환
                if flag:  # 음악 재생 플래그가 True일 경우
                    flag = False  # 음악 재생 플래그를 즉시 False로 바꾼다.
                    emotion = emotion_detection.get_emotion(automatic_capture_img_name, dest)  # 감정 인식
                    print(emotion)
                    hw_request.emotion_request(emotion)
                    music_play_process = Process(target=play_music.music_start, args=(emotion, ))
                    music_play_process.start()

                # 행동 인식 과정(taskoffloading)
                offloading_result = taskoffloading.home_edge()
                if offloading_result != 'none':  # taskoffloading 에러 없을 시
                    if pose_detection.check(offloading_result): # ping-pong 성공(서버 살아있을 때)
                        pose = pose_detection.get_pose(automatic_capture_img_name, offloading_result)
                        print(pose)
                        hw_request.pose_request(pose)

                if flag is False and music_play_process.is_alive() is False:  # 음악 재생 플래그가 False이고 music_play_process가 종료되었을 경우
                    flag = True  # 음악 재생 플래그를 True로 바꾸고 다시 감정인식을 진행한다.
                # 이미지 crop 과정, 필요없을 시 생략 가능
                '''
                cropped_img_name = cropped_img_dir + current_time + "_crop" + save_img_ext
                face_locations = find_faces_in_picture.get_face_locations_in_picture(automatic_capture_img_name)
                crop.crop_img(automatic_capture_img_name, face_locations, cropped_img_name)
                '''
                file_manipulation.remove_file(automatic_capture_img_name)  # 방금 촬영한 사진 삭제
            start_time = time.time()  # 타이머 초기화

        if k & 0xFF == ord('q'):  # q키를 누르면 종료
            music_play_process.kill()  # music_play_process를 종료한다.
            break

    video_capture.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    eye_remocon_service()  # eye_remocon_service 메서드 실행
