import cv2
import time
from find_faces_in_picture import save_faces_in_picture

video_capture = cv2.VideoCapture(0)
cv2.namedWindow("cam-test")
start_time = time.time()

while True:
    ret, frame = video_capture.read()

    if ret:
        cv2.imshow("cam-test", frame)

    k = cv2.waitKey(1)

    if time.time() - start_time >= 1:  # check if 1 sec passed
        img_name = "opencv_img.jpg"
        cv2.imwrite(img_name, frame)  # frame: img
        save_faces_in_picture(img_name)
        start_time = time.time()

    if k & 0xFF == ord('q'):
        break


video_capture.release()
cv2.destroyAllWindows()
