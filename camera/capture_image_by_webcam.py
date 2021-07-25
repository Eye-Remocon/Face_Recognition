import cv2


def set_window_name(window_name):
    cv2.namedWindow(window_name)


def show_camera_frame(video_capture, window_name):
    ret, frame = video_capture.read()

    if ret:
        cv2.imshow(window_name, frame)


def do_video_capture(video_capture, window_name, save_img_name):
    # video_capture = cv2.VideoCapture(0)
    ret, frame = video_capture.read()

    if ret:
        cv2.imshow(window_name, frame)

    save_img(save_img_name, frame)


def save_img(save_img_name, frame):
    cv2.imwrite(save_img_name, frame)  # frame: img
