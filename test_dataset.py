from dataset_loader import DatasetLoader
loader = DatasetLoader()

images, labels = loader.load_dataset()

print("Images :", len(images))
print("Labels :", labels)