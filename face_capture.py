import cv2
import os


class FaceCapture:

    def __init__(self):

        self.camera = cv2.VideoCapture(0)

        self.detector = cv2.CascadeClassifier(
            cv2.data.haarcascades +
            "haarcascade_frontalface_default.xml"
        )

    def capture_faces(self, student_name, total_images=50):

        folder = os.path.join("datasets", student_name)

        os.makedirs(folder, exist_ok=True)

        count = 0

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

                cv2.rectangle(
                    frame,
                    (x, y),
                    (x+w, y+h),
                    (0,255,0),
                    2
                )

                cv2.imshow("Face Capture", frame)

                key = cv2.waitKey(1)

                if key == 32:

                    cv2.imwrite(
                        os.path.join(folder, f"{count}.jpg"),
                        face
                    )

                    count += 1

                    print(f"Captured {count}")

                if count >= total_images:

                    self.camera.release()

                    cv2.destroyAllWindows()

                    return

            cv2.imshow("Face Capture", frame)

            if cv2.waitKey(1) == 27:

                break

        self.camera.release()

        cv2.destroyAllWindows()