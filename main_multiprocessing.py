import cv2, time, os
from camera import capture_image_by_webcam
from face_detection import user_identify
from common import img_encoding, file_manipulation
from service import categorization, emotion_detection, play_music, taskoffloading, pose_detection, hw_request
from multiprocessing import Process

automatic_capture_img_dir = "./img/"
known_img_dir = "./knowns"
save_img_ext = ".jpg"

offloading_result = 'none'
key = 'http://127.0.0.1:9900'
dest = os.getenv('ENV', key)

known_img_encodings = img_encoding.get_known_img_encodings(known_img_dir)
known_img_list = os.listdir(known_img_dir)


def eye_remocon_service():
    video_capture = cv2.VideoCapture(0)
    window_name = "cam-test"
    capture_image_by_webcam.set_window_name(window_name)
    offloading_result = 'none'

    music_flag = True # True when music is playing, False when music is not playing
    siren_flag = False # True when siren sounds, False when siren doesn't sound.

    start_time = time.time()
    while True:
        capture_image_by_webcam.show_camera_frame(video_capture, window_name)
        k = cv2.waitKey(1)
        
        if time.time() - start_time >= 1:
            current_time = time.strftime('%y%m%d_%H%M%S', time.localtime(time.time()))
            automatic_capture_img_name = automatic_capture_img_dir + current_time + save_img_ext
            capture_image_by_webcam.do_video_capture(video_capture, automatic_capture_img_name)

            face_distances = user_identify.get_face_distance(known_img_encodings, automatic_capture_img_name)
            
            if user_identify.is_registered(face_distances):
                categorization.member_id_categorization(face_distances, known_img_list)

                # 'ANGRY', 'DISGUST', 'FEAR', 'HAPPY', 'NEUTRAL', 'SAD', 'SURPRISE'
                if music_flag and not siren_flag:
                    music_flag = False
                    emotion = emotion_detection.get_emotion(automatic_capture_img_name, dest)
                    print('emotion detection: ', emotion)
                    hw_request.emotion_request(emotion)
                    music_play_process = Process(target=play_music.music_start, args=(emotion, ))
                    music_play_process.start()
                    
                print(offloading_result)
                
                # 행동 인식 과정(taskoffloading)
                if offloading_result == 'none':
                    offloading_result = taskoffloading.home_edge()
                    print('task offloading target : ', offloading_result)
                
                if offloading_result != 'none':  # No error occured with taskoffloading 
                    if pose_detection.check(offloading_result): # ping-pong success(Server is activate)
                        pose = pose_detection.get_pose(automatic_capture_img_name, offloading_result)
                        hw_request.pose_request(pose)
                        if pose != 'none':
                            print('behavior detection : ', pose)
                            if pose == 'emergency' and not siren_flag:
                                siren_flag = True
                                siren_play_process = Process(target=play_music.emergency_siren)
                                music_play_process.terminate()
                                time.sleep(1)
                                siren_play_process.start()
                            
                if not music_flag and music_play_process.is_alive() is False:
                    music_flag = True
                    music_play_process.terminate()

                if siren_flag and siren_play_process.is_alive() is False:
                    siren_flag = False
                    siren_play_process.terminate()

                file_manipulation.remove_file(automatic_capture_img_name)
            start_time = time.time()

        if k & 0xFF == ord('q'):
            music_play_process.kill()
            break

    video_capture.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    eye_remocon_service()
