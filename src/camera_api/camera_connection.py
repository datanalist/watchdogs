import requests
from requests.auth import HTTPDigestAuth


def get_image(camera):
    params = {
        "keep_aspect_ratio": 1,
        "resolution": "640x480"
    }
    headers = {
        "Accept": "image/*"
    }

    url = f"http://45.138.163.92:7502/cameras/{camera}/image"
    username = "test"
    password = "Rtest3"
    response = requests.get(url, auth=HTTPDigestAuth(username, password), params=params, headers=headers)
    print(response.status_code)
    