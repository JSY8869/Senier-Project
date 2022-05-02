import json

import requests

import xy_to_nxny


def ip_to_xy():
    key = 'a3efa2941fb3fcf4f3877cc063439f9b'
    send_url = 'http://api.ipstack.com/check?access_key=' + key
    response = requests.get(send_url)
    response_json = json.loads(response.text)

    # 위도
    nx = response_json['latitude']
    # 경도
    ny = response_json['longitude']

    return xy_to_nxny.map_to_grid(nx, ny)
