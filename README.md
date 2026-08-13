# Smart Attendance System

AI based attendance system using Python, OpenCV, TensorFlow, MediaPipe, CustomTkinter and SQLite.

## 📦 Installation

Install Python 3.11, then run:

```bash
pip install customtkinter
pip install opencv-python
pip install tensorflow
pip install mediapipe
pip install numpy
pip install scikit-learn
pip install pillow
pip install pyttsx3
```

Or create `requirements.txt`:

```text
customtkinter
opencv-python
tensorflow
mediapipe
numpy
scikit-learn
pillow
pyttsx3
```

Then:

```bash
pip install -r requirements.txt
```

## Folder Structure

```text
SmartAttendanceSystem/
│
├── app.py
├── check.py
├── test_database.py
├── test_train.py
├── test_live_recognition.py
├── requirements.txt
│
├── ai/
│   ├── __init__.py
│   ├── face_detector.py
│   ├── face_encoder.py
│   ├── recognizer.py
│   ├── trainer.py
│   └── live_recognition.py
│
├── database/
│   ├── __init__.py
│   ├── database.py
│   ├── attendance.py
│   ├── history.py
│   ├── statistics.py
│   └── attendance.db
│
├── gui/
│   ├── __init__.py
│   ├── splash.py
│   ├── login.py
│   ├── dashboard.py
│   │
│   ├── pages/
│   │   └── register_student.py
│   │
│   └── widgets/
│       └── live_camera.py
│
├── training/
│   ├── __init__.py
│   ├── dataset_loader.py
│   ├── embedding_generator.py
│   ├── test_dataset.py
│   └── test_embedding.py
│
├── utils/
│   ├── __init__.py
│   ├── voice.py
│   └── unknown_logger.py
│
├── datasets/
│   ├── Student_001/
│   │   └── face.jpg
│   ├── Student_002/
│   │   └── face.jpg
│   ├── Student_003/
│   │   └── face.jpg
│   └── Student_004/
│       └── face.jpg
│
├── models/
│   └── embeddings.pkl
│
└── unknown_faces/
    └── captured images
```

##  Run

Open terminal in the project folder:

```bash
cd D:\SmartAttendanceSystem
```

Start the application:

```bash
python app.py
```

Test live recognition:

```bash
python test_live_recognition.py
```

Test training:

```bash
python test_train.py
```

Check embeddings:

```bash
python check.py
```

### Current Embedding Size

```text
1280
```
