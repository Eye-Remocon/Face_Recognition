import requests
import base64

def check(ip):
    url = 'http://'+ip+':3500/ping'

    r = requests.post(url)
    if r.ok:
        result = r.json()['result']
        if result == 'pong': # 서버 살아있으면
            return True
    return False # 서버 죽었으면

def get_pose(img_name, ip):
    # 저장된 캡쳐 이미지 불러온 후base64코드로 인코드
    with open(img_name, 'rb') as f:
        im_b64 = base64.b64encode(f.read())

    # 이미지 payload 형태로 만든 후 flask 서버에 post 요청
    payload = {'image': im_b64}
    headers = {}
    url = 'http://' + ip + ':3500/pose_detection'

    r = requests.post(url, json=payload, headers=headers)

    if r.ok:
        pose = r.json()
        if pose[1]['probability'] > 0.8:
            return result.append(pose[0]['className'])
    return 'none'




