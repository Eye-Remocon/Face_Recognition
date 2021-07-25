import face_recognition

CRITICAL_POINT = 0.6


def get_face_distance(known_face_image_encodings, unknown_img_name):
    unknown_img = face_recognition.load_image_file(unknown_img_name)

    if len(known_face_image_encodings) != 0 and len(face_recognition.face_encodings(unknown_img)) != 0:
        unknown_img_face_encoding = face_recognition.face_encodings(unknown_img)[0]
        face_distances = face_recognition.face_distance(known_face_image_encodings, unknown_img_face_encoding)
        return face_distances
    else:
        return []


def is_registered(face_distances):
    for face_distance in face_distances:
        if face_distance < CRITICAL_POINT:
            return True
    return False
