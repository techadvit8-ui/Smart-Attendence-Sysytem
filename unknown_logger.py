import cv2
import os
from datetime import datetime


class UnknownLogger:

    def __init__(self):

        self.folder = "unknown_faces"

        os.makedirs(self.folder, exist_ok=True)

        self.last_saved = ""

    def save(self, frame):

        current = datetime.now().strftime("%Y%m%d_%H%M%S")

        if current == self.last_saved:
            return

        self.last_saved = current

        filename = os.path.join(
            self.folder,
            f"{current}.jpg"
        )

        cv2.imwrite(filename, frame)

        print(f"Unknown Face Saved : {filename}")