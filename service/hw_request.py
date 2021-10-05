import requests

def emotion_request(emotion):
    payload = {'emotion': emotion}
    headers = {}
    url = 'http://localhost:4000/emotion'
    r = requests.post(url, json=payload, headers=headers)

def pose_request(pose):
    payload = {'pose': pose}
    headers = {}
    url = 'http://localhost:4000/pose'
    r = requests.post(url, json=payload, headers=headers)
