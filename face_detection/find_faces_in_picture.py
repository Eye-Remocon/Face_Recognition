import face_recognition


# 사진에서 모든 얼굴을 찾아 해당 얼굴의 위치를 반환
def get_face_locations_in_picture(save_img_name):
    image = face_recognition.load_image_file(save_img_name)  # 이미지 불러오기
    face_locations = face_recognition.face_locations(image)  # 이미지에 있는 모든 얼굴의 위치를 face_locations에 저장
    
    # 테스트 코드
    # print("I found {} face(s) in this photograph.".format(len(face_locations)))  # 이미지에 있는 얼굴의 개수 출력
    # print("face_locations: ", face_locations)  # 얼굴 위치 출력

    return face_locations
