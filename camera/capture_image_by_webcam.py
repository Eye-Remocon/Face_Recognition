import cv2


# 윈도우 이름 설정
def set_window_name(window_name):
    cv2.namedWindow(window_name)


# 프레임 단위로 카메라 장면을 화면에 나타냄
def show_camera_frame(video_capture, window_name):
    ret, frame = video_capture.read()

    if ret:
        cv2.imshow(window_name, frame)


# 사진 촬영
def do_video_capture(video_capture, window_name, save_img_name):
    # video_capture = cv2.VideoCapture(0)
    ret, frame = video_capture.read()

    if ret:
        cv2.imshow(window_name, frame)

    save_img(save_img_name, frame)


# 이미지 저장
def save_img(save_img_name, frame):
    cv2.imwrite(save_img_name, frame)  # frame: img
