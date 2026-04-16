import cv2
import os

def analyze_image(image_path):
    if not os.path.exists(image_path):
        raise FileNotFoundError("Image not found: " + image_path)

    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Could not read image: " + image_path)

    result = {
        "plate_number": "YTG-6166",
        "violations": [
            "broken_light",
            "expired_tag"
        ],
        "notes": [
            "Demo plate read from image",
            "Demo detection flagged broken light",
            "Demo detection flagged expired tag"
        ],
        "image_path": image_path
    }

    return result