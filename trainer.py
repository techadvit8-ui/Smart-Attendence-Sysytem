import os
import cv2
import pickle

from face_encoder import FaceEncoder


class Trainer:

    def __init__(self):
        self.encoder = FaceEncoder()

        # Project root folder
        self.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        # datasets folder
        self.dataset_path = os.path.join(self.base_dir, "datasets")

        # models folder
        self.models_path = os.path.join(self.base_dir, "models")

    def train(self):

        embeddings = []

        print("Dataset Path:", self.dataset_path)

        if not os.path.exists(self.dataset_path):
            print("Dataset folder not found!")
            return

        for student in os.listdir(self.dataset_path):

            student_folder = os.path.join(self.dataset_path, student)

            if not os.path.isdir(student_folder):
                continue

            for file in os.listdir(student_folder):

                if file.lower().endswith((".jpg", ".jpeg", ".png")):

                    image_path = os.path.join(student_folder, file)

                    image = cv2.imread(image_path)

                    if image is None:
                        continue

                    embedding = self.encoder.encode(image)

                    print(f"{student} -> {len(embedding)}")

                    embeddings.append({
                        "name": student,
                        "embedding": embedding
                    })

        os.makedirs(self.models_path, exist_ok=True)

        output_file = os.path.join(self.models_path, "embeddings.pkl")
        print("Saving to:", output_file)
        with open(output_file, "wb") as f:
            pickle.dump(embeddings, f)

        print("\nTraining Completed Successfully!")
        print("Saved to:", output_file)