import os
import base64

files = os.listdir('./who')

if len(files) != 0:
    filename = "./who/" + files[0]
    with open(filename, "rb") as img:
        base64_string = base64.b64encode(img.read())  # image --> base64code
