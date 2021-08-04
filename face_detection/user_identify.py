import face_recognition

CRITICAL_POINT = 0.6  # 임계점 설정(두 사람의 face_distance가 임계점 이하일 경우 서로 같은 사람이라고 판별)


# knowns에 있는 사진들과 카메라에서 촬영한 사진 사이의 face_distance를 numpy ndarray 형태로 리턴
def get_face_distance(known_face_image_encodings, unknown_img_name):
    unknown_img = face_recognition.load_image_file(unknown_img_name)  # 카메라에서 촬영한 사진 불러오기

    if len(known_face_image_encodings) != 0 and len(face_recognition.face_encodings(unknown_img)) != 0:
        # knowns에 있는 사진과 카메라에서 촬영한 사진에 얼굴이 인식되었는지 확인
        unknown_img_face_encoding = face_recognition.face_encodings(unknown_img)[0]  # 카메라에서 촬영한 사진 인코딩
        face_distances = face_recognition.face_distance(known_face_image_encodings, unknown_img_face_encoding)
        return face_distances
    else:  # face_distance 측정 불가, 빈 list로 리턴
        return []


# 카메라에서 촬영한 사람이 등록된 사람인지 판단
def is_registered(face_distances):
    for face_distance in face_distances:
        if face_distance < CRITICAL_POINT:
            return True
    return False
