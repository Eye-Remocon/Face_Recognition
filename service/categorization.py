import os


def member_id_categorization(face_distances, known_img_list):
    face_distances = face_distances.tolist()
    min_face_distance_idx = face_distances.index(min(face_distances))
    file_name = known_img_list[min_face_distance_idx]
    member_name, ext = os.path.splitext(file_name)
    print(member_name)
