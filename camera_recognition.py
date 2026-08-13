import cv2
import numpy as np

from recognizer import FaceRecognizer


recognizer = FaceRecognizer()

camera = cv2.VideoCapture(0)

while True:

    ret, frame = camera.read()

    if not ret:
        break

    face = cv2.resize(frame, (160, 160))

    embedding = face.flatten() / 255.0

    name, score = recognizer.recognize(embedding)

    cv2.putText(
        frame,
        f"{name}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.imshow("Recognition", frame)

    if cv2.waitKey(1) == 27:
        break

camera.release()
cv2.destroyAllWindows()