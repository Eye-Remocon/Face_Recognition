import cv2
import time
from camera.capture_image_by_webcam import set_window_name, show_camera_frame, do_video_capture
from camera.save_faces_in_picture import save_faces_in_picture

video_capture = cv2.VideoCapture(0)
window_name = "cam-test"
set_window_name(window_name)

automatic_capture_img_name = "./img/opencv_img.jpg"
cropped_img_name = "./img/cropped_img.jpg"

start_time = time.time()
while True:
    show_camera_frame(video_capture, window_name)
    k = cv2.waitKey(1)
    if time.time() - start_time >= 1:  # check if 1 sec passed
        do_video_capture(video_capture, window_name, automatic_capture_img_name)
        save_faces_in_picture(automatic_capture_img_name, cropped_img_name)
        start_time = time.time()

    if k & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
