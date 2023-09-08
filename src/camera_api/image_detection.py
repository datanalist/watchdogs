from PIL import Image
from ultralytics import YOLO
import io

def detect_dirty_places(image):
    model = YOLO("../models/yolo-best-30.pt")
    image = Image.open(io.BytesIO(image))
    results = model(image)
    boxes = results[0].boxes
    for box in boxes:
        cls = (int(box.cls))
        if cls == 2:
            return True
    return False
