import cv2
import time


class LiveDetection:

    def __init__(self):

        self.camera = cv2.VideoCapture(0)

        self.detector = cv2.CascadeClassifier(
            cv2.data.haarcascades +
            "haarcascade_frontalface_default.xml"
        )

        self.previous_time = time.time()

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

                cv2.rectangle(
                    frame,
                    (x, y),
                    (x + w, y + h),
                    (0, 255, 0),
                    2
                )

                cv2.putText(
                    frame,
                    "Face Detected",
                    (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (0, 255, 0),
                    2
                )

            current_time = time.time()

            fps = 1 / (current_time - self.previous_time)

            self.previous_time = current_time

            cv2.putText(
                frame,
                f"FPS : {int(fps)}",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (255, 255, 0),
                2
            )

            cv2.imshow("Smart Attendance System", frame)

            key = cv2.waitKey(1) & 0xFF

            if key == 27 or key == ord("q"):
                break

        self.camera.release()
        cv2.destroyAllWindows()