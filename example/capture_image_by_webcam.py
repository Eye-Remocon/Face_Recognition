import cv2

video_capture = cv2.VideoCapture(0)
cv2.namedWindow("cam-test")

img_counter = 0

while True:
    ret, frame = video_capture.read()

    if ret:
        cv2.imshow("cam-test", frame)

    k = cv2.waitKey(1)

    if k & 0xFF == ord('s'):  # s key pressed
        img_name = "opencv_frame_{}.jpg".format(img_counter)
        cv2.imwrite(img_name, frame)  # frame: img
        print("{} written!".format(img_name))  # print log
        img_counter += 1

        # 이미지 파일 이름을 JSON 형태로 작성
        '''
        data = {
            "img_file_name": img_name
        }
        '''

    if k & 0xFF == ord('q'):
        break


video_capture.release()
cv2.destroyAllWindows()
