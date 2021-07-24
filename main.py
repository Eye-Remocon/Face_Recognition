import cv2
import time
import os
from camera import capture_image_by_webcam
from face_detection import crop, user_identify, find_faces_in_picture
from common import img_encoding, file_manipulation
from service import categorization

video_capture = cv2.VideoCapture(0)
window_name = "cam-test"
capture_image_by_webcam.set_window_name(window_name)

automatic_capture_img_dir = "./img/"
cropped_img_dir = "./cropped_img/"
known_img_dir = "./knowns"
save_img_ext = ".jpg"

known_img_encodings = img_encoding.get_known_img_encodings(known_img_dir)
known_img_list = os.listdir(known_img_dir)

start_time = time.time()
while True:
    capture_image_by_webcam.show_camera_frame(video_capture, window_name)
    k = cv2.waitKey(1)
    if time.time() - start_time >= 1:  # check if 1 sec passed
        current_time = time.strftime('%y%m%d_%H%M%S', time.localtime(time.time()))
        automatic_capture_img_name = automatic_capture_img_dir + current_time + save_img_ext
        capture_image_by_webcam.do_video_capture(video_capture, window_name, automatic_capture_img_name)

        face_distances = user_identify.get_face_distance(known_img_encodings, automatic_capture_img_name)

        if user_identify.is_registered(face_distances):
            categorization.member_id_categorization(face_distances, known_img_list)
            cropped_img_name = cropped_img_dir + current_time + "_crop" + save_img_ext
            face_locations = find_faces_in_picture.get_face_locations_in_picture(automatic_capture_img_name)
            crop.crop_img(automatic_capture_img_name, face_locations, cropped_img_name)
            file_manipulation.remove_file(automatic_capture_img_name)
        start_time = time.time()

    if k & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
