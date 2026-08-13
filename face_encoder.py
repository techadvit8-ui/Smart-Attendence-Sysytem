import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input


class FaceEncoder:

    def __init__(self):

        self.model = MobileNetV2(
            weights="imagenet",
            include_top=False,
            pooling="avg",
            input_shape=(160, 160, 3)
        )

    def encode(self, face):

        face = cv2.resize(face, (160, 160))

        face = face.astype("float32")

        face = preprocess_input(face)

        face = np.expand_dims(face, axis=0)

        embedding = self.model.predict(
            face,
            verbose=0
        )

        embedding = embedding.flatten()

        embedding = embedding / np.linalg.norm(embedding)

        return embedding