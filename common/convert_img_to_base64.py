import base64


def convert_img_to_base64_code(img_name):
    with open(img_name, "rb") as img:
        base64_string = base64.b64encode(img.read())  # image --> base64code
    return base64_string
