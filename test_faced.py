import cv2

from face_detector import FaceDetector

camera = cv2.VideoCapture(0)

detector = FaceDetector()

while True:

    ret, frame = camera.read()

    if not ret:
        break

    faces = detector.detect(frame)

    for (x, y, w, h) in faces:

        cv2.rectangle(
            frame,
            (x, y),
            (x+w, y+h),
            (0,255,0),
            2
        )

    cv2.imshow(
        "MediaPipe Detection",
        frame
    )

    key = cv2.waitKey(1) & 0xFF

    if key == 27 or key == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()