import face_recognition
import os


def load_known_img_files(known_img_files_dir):
    known_img = []
    for img in os.listdir(known_img_files_dir):
        known_img.append(face_recognition.load_image_file(known_img_files_dir + "/" + img))
    return known_img


# 이미지 인코딩 작업(knowns에 있는 사진에 대하여 인코딩 진행)
def get_known_img_encodings(known_img_files_dir):
    known_img = load_known_img_files(known_img_files_dir)
    known_images_encodings = []
    for img in known_img:
        if len(face_recognition.face_encodings(img)) > 0:  # 사진에서 얼굴을 1개 이상 찾았을 경우
            known_images_encodings.append(face_recognition.face_encodings(img)[0])
    return known_images_encodings
