import cv2

def analyze_image(image_path):
    image_data = cv2.imread(image_path)

    if image_data is None:
        raise FileNotFoundError("Could not read image: " + image_path)

    height_val, width_val, _ = image_data.shape

    result_data = {
        "plate_number": "ABC123",
        "violations": ["broken_light", "expired_tag"],
        "notes": [
            "Demo plate text found from test image",
            "Demo broken light flag added",
            "Demo expired tag flag added"
        ],
        "image_size": {
            "width": width_val,
            "height": height_val
        }
    }

    return result_data