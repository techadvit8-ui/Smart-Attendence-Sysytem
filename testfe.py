import os
import cv2

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

image_path = os.path.join(BASE_DIR, "datasets", "Student_001", "face.jpg")

print(image_path)
print(os.path.exists(image_path))

image = cv2.imread(image_path)