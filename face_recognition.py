import cv2

from recognizer import FaceRecognizer


class LiveRecognition:

    def __init__(self):

        self.camera = cv2.VideoCapture(0)

        self.detector = cv2.CascadeClassifier(
            cv2.data.haarcascades +
            "haarcascade_frontalface_default.xml"
        )

        self.recognizer = FaceRecognizer()

    def start(self):

        while True:

            ret, frame = self.camera.read()

            if not ret:
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = self.detector.detectMultiScale(
                gray,
                scaleFactor=1.2,
                minNeighbors=5
            )

            for (x, y, w, h) in faces:

                face = frame[y:y+h, x:x+w]

                face = cv2.resize(face, (160, 160))

                name, confidence = self.recognizer.recognize(face)

                color = (0, 255, 0)

                if name == "Unknown":
                    color = (0, 0, 255)

                cv2.rectangle(
                    frame,
                    (x, y),
                    (x+w, y+h),
                    color,
                    2
                )

                cv2.putText(
                    frame,
                    f"{name} ({confidence}%)",
                    (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    color,
                    2
                )

            cv2.imshow(
                "Smart Attendance System",
                frame
            )

            key = cv2.waitKey(1) & 0xFF

            if key == 27 or key == ord("q"):
                break

        self.camera.release()
        cv2.destroyAllWindows()