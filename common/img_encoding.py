import face_recognition
import os


def load_known_img_files(known_img_files_dir):
    known_img = []
    for img in os.listdir(known_img_files_dir):
        known_img.append(face_recognition.load_image_file(known_img_files_dir + "/" + img))
    return known_img


def get_known_img_encodings(known_img_files_dir):
    known_img = load_known_img_files(known_img_files_dir)
    known_images_encodings = []
    for img in known_img:
        if len(face_recognition.face_encodings(img)) > 0:
            known_images_encodings.append(face_recognition.face_encodings(img)[0])
    return known_images_encodings
