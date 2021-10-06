#-*-coding: utf-8-*-
#-*-coding: euc-kr-*-
import requests

payload = {
    "ServiceName": "pose_detection",
    "ServiceInfo": [
    {
        "ExecutionType": "container",
    }]
}

def home_edge():
    headers = {}
    url = 'http://127.0.0.1:56001/api/v1/orchestration/services'

    r = requests.post(url, json=payload, headers=headers)

    if r.ok:
        result = r.json()
        error = result['Message']
        if error == 'ERROR_NONE':
            ip = result['RemoteTargetInfo']['Target']
            return ip
    return 'none'