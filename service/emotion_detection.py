#-*-coding: utf-8-*-
#-*-coding: euc-kr-*-
import requests
import base64
import json

def get_emotion(img_name, dest):
    # 저장된 캡쳐 이미지 불러온 후base64코드로 인코드
    with open(img_name, 'rb') as f:
        im_b64 = base64.b64encode(f.read())

    # 이미지 payload 형태로 만든 후 flask 서버에post 요청
    payload = {'image': im_b64}
    url = dest + '/main'
    r = requests.post(url, data=payload)

    # 서버에 request 후 반환된 감정인식 값을 반환
    if r.ok:
        emotion = r.json()['emotion']
        return emotion

