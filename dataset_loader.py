import os
import cv2


class DatasetLoader:

    def __init__(self):

        # Project Root Folder
        self.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        # datasets folder
        self.dataset_path = os.path.join(self.base_dir, "datasets")

        print("Project Folder :", self.base_dir)
        print("Dataset Folder :", self.dataset_path)

    def load_dataset(self):

        images = []
        labels = []

        if not os.path.exists(self.dataset_path):
            print("Dataset folder not found.")
            return images, labels

        for student_name in os.listdir(self.dataset_path):

            student_folder = os.path.join(
                self.dataset_path,
                student_name
            )

            if not os.path.isdir(student_folder):
                continue

            for file in os.listdir(student_folder):

                if file.lower().endswith((".jpg", ".jpeg", ".png")):

                    image_path = os.path.join(
                        student_folder,
                        file
                    )

                    image = cv2.imread(image_path)

                    if image is None:
                        print("Cannot read:", image_path)
                        continue

                    image = cv2.resize(image, (160, 160))

                    images.append(image)
                    labels.append(student_name)

        print(f"\nLoaded {len(images)} images.")
        print(f"Found {len(set(labels))} students.")

        return images, labels