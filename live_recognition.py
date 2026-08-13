import cv2

from ai.face_detector import FaceDetector
from ai.recognizer import Recognizer
from database.attendance import AttendanceManager
from utils.voice import VoiceAssistant
from utils.unknown_logger import UnknownLogger


class LiveRecognition:

    def __init__(self):

        self.camera = cv2.VideoCapture(0)

        if not self.camera.isOpened():
            raise Exception("Could not open camera.")

        self.detector = FaceDetector()
        self.recognizer = Recognizer()
        self.attendance = AttendanceManager()
        self.voice = VoiceAssistant()
        self.logger = UnknownLogger()

        # Prevent duplicate attendance during the current session
        self.marked_today = set()

    def start(self):

        print("=" * 50)
        print(" Smart Attendance System")
        print(" Live Face Recognition Started")
        print(" Press Q or ESC to Exit")
        print("=" * 50)

        while True:

            ret, frame = self.camera.read()

            if not ret:
                print("Failed to capture frame.")
                break

            faces = self.detector.detect(frame)

            for (x, y, w, h) in faces:

                face = frame[y:y+h, x:x+w]

                if face.size == 0:
                    continue

                try:

                    name, confidence = self.recognizer.recognize(face)

                except Exception as e:

                    print("Recognition Error:", e)
                    continue

                # ------------------------------
                # Unknown Person
                # ------------------------------

                if name == "Unknown":

                    color = (0, 0, 255)

                    self.logger.save(frame)

                # ------------------------------
                # Known Person
                # ------------------------------

                else:

                    color = (0, 255, 0)

                    if name not in self.marked_today:

                        marked = self.attendance.mark_attendance(name)

                        if marked:

                            print(f"Attendance Marked : {name}")

                            self.voice.speak(
                                f"Welcome {name}. Attendance Marked."
                            )

                        self.marked_today.add(name)

                # Draw Face Rectangle

                cv2.rectangle(
                    frame,
                    (x, y),
                    (x + w, y + h),
                    color,
                    2
                )

                # Display Name and Confidence

                cv2.putText(
                    frame,
                    f"{name} ({confidence:.2f}%)",
                    (x, y - 10),
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

            if key == ord("q") or key == 27:
                break

        self.camera.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":

    app = LiveRecognition()
    app.start()