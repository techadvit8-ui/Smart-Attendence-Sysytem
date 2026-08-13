import cv2
import os


class CameraCapture:

    def __init__(self):
        self.camera = cv2.VideoCapture(0)

    def capture_images(self, student_name, total_images=50):

        folder = os.path.join("datasets", student_name)

        os.makedirs(folder, exist_ok=True)

        count = 0

        print("Press SPACE to capture image.")
        print("Press ESC to cancel.")

        while True:

            ret, frame = self.camera.read()

            if not ret:
                break

            cv2.putText(
                frame,
                f"Images : {count}/{total_images}",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2
            )

            cv2.imshow("Camera", frame)

            key = cv2.waitKey(1)

            if key == 27:
                break

            if key == 32:

                filename = os.path.join(
                    folder,
                    f"{count+1}.jpg"
                )

                cv2.imwrite(filename, frame)

                count += 1

                print(f"Captured {count}")

                if count >= total_images:
                    break

        self.camera.release()
        cv2.destroyAllWindows()

        print("Capture Completed")