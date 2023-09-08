import io
import time
import traceback
from PIL import Image
from django.core.files import File
from clubs.models import Picture


def save_image(image_content, camera):
    try:
        # Этот код сохраняет изображение, переданное в функцию, и связывает его с камерой
        # Вам может потребоваться доработать эту часть кода, чтобы она соответствовала вашим моделям
        image = Image.open(io.BytesIO(image_content))
        buffer = io.BytesIO()
        image.save(buffer, format='JPEG')

        picture = Picture()
        picture.photo = File(buffer, name=f'{camera.ip}_{time.time()}.jpg')
        picture.camera = camera
        picture.save()
    except Exception as e:
        traceback.print_exc()
