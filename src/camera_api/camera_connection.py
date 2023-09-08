import traceback
import requests
from requests.auth import HTTPDigestAuth
import time
from clubs.models import *
from .set import *
from .image_detection import detect_dirty_places
from .image_processing import save_image

counter = [0]

username = "test"
password = "Rtest3"


def main():
    global counter
    while True:
        try:
            params = {
                "keep_aspect_ratio": 1,
                "resolution": "640x480"
            }
            headers = {
                "Accept": "image/*"
            }

            cameras = Camera.objects.all()
            count = Camera.objects.count()

            if len(counter) != count:
                counter = [0] * count

            for index, camera in enumerate(cameras):
                url = f"http://45.138.163.92:7502/cameras/{camera.ip}/image"

                response = requests.get(url, auth=HTTPDigestAuth(username, password), params=params, headers=headers)

                if response.status_code == 200:
                    image_content = response.content

                    # Проверяем изображение на наличие грязных мест
                    if detect_dirty_places(image_content):
                        counter[index] += 1
                    else:
                        counter[index] = 0

                    if counter[index] == 3:
                        counter[index] = 0
                        # Сохраняем изображение и связываем его с камерой
                        save_image(image_content, camera)
                else:
                    print("Failed to access the image:", response.status_code)
            print(counter)
        except Exception as e:
            traceback.print_exc()
        time.sleep(40)


if __name__ == "__main__":
    main()
