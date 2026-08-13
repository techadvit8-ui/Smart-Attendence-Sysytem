import os
import pickle

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(BASE_DIR, "models", "embeddings.pkl")

print(model_path)

with open(model_path, "rb") as f:
    data = pickle.load(f)

print("Students:", len(data))
print("Keys:", data[0].keys())
print("Embedding Length:", len(data[0]["embedding"]))