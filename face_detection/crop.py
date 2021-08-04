from PIL import Image
import face_recognition


def crop_img(save_img_name, face_locations, cropped_img_name):
    image = face_recognition.load_image_file(save_img_name)
    idx = 0

    # 이미지 crop 과정
    for face_location in face_locations:
        top, right, bottom, left = face_location
        face_image = image[top:bottom, left:right]
        pil_image = Image.fromarray(face_image)
        pil_image.save(cropped_img_name)  # 이미지 저장
        idx += 1
