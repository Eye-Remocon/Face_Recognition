import face_recognition


def get_face_locations_in_picture(save_img_name):
    image = face_recognition.load_image_file(save_img_name)
    face_locations = face_recognition.face_locations(image)
    # print("I found {} face(s) in this photograph.".format(len(face_locations)))
    print("face_locations: ", face_locations)

    '''
    for face_location in face_locations:
        # Print the location of each face in this image
        top, right, bottom, left = face_location
        print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))
    '''

    return face_locations
