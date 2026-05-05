# 🦠 Malaria Detection Web App using CNN & TensorFlow Lite

A web-based application for detecting malaria-infected blood cells using Convolutional Neural Networks (CNN) and deployed with TensorFlow Lite. Users can upload microscopic cell images and receive instant predictions.

---

## 📌 Project Overview

Malaria remains a serious global health issue. This project aims to assist early detection by leveraging deep learning for image classification of blood smear cells.

The system classifies images into:

* **Parasitized** (infected)
* **Uninfected** (healthy)

The model is trained using CNN and deployed into a lightweight **TensorFlow Lite** model for fast inference in a Flask web application.

---

## 🚀 Features

* 📤 Upload blood cell images via web interface
* 🤖 Automatic classification using CNN model
* ⚡ Fast inference with TensorFlow Lite
* 📊 Displays prediction results with health tips
* 🌐 Simple and user-friendly Flask web app

---

## 🧠 Model Architecture

The CNN model consists of:

* Conv2D + MaxPooling layers
* Dropout layers (for regularization)
* Dense layers
* Sigmoid activation for binary classification

### Training Configuration:

* Input size: **120x120**
* Optimizer: **RMSprop**
* Loss: **Binary Crossentropy**
* Early stopping when accuracy > 91%

---

## 📂 Dataset

Dataset used:

* 📦 Kaggle: *Cell Images for Detecting Malaria*
* Link: [https://www.kaggle.com/datasets/iarunava/cell-images-for-detecting-malaria](https://www.kaggle.com/datasets/iarunava/cell-images-for-detecting-malaria)

Classes:

* Parasitized
* Uninfected

---

## 🛠️ Tech Stack

* Python
* Flask
* TensorFlow / Keras
* TensorFlow Lite
* NumPy
* Matplotlib

---

## 📁 Project Structure

```
malaria-detection/
│
├── models/
│   └── model__v1.tflite
│
├── static/
│   └── uploads/
│
├── templates/
│   ├── index.html
│   ├── hasil.html
│   ├── tentang.html
│   ├── dokumentasi.html
│   └── proses.html
│
├── app.py
├── training.ipynb
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone Repository

```bash
git clone https://github.com/your-username/malaria-detection.git
cd malaria-detection
```

### 2. Install Dependencies

```bash
pip install flask tensorflow keras numpy pillow matplotlib
```

### 3. Run Application

```bash
python app.py
```

### 4. Open in Browser

```
http://127.0.0.1:8080/
```

---

## 🧪 How It Works

1. User uploads an image
2. Image is resized to **120x120**
3. Image is normalized (scaled 0–1)
4. TensorFlow Lite model performs inference
5. Output probability determines class:

   * ≤ 0.5 → Parasitized
   * > 0.5 → Uninfected
6. Result + health tips displayed

---

## 📊 Model Performance

* Training Accuracy: > 91%
* Validation Accuracy: > 91%
* Early stopping applied for optimal performance

---

## 🔄 Model Conversion

Model converted to TensorFlow Lite:

```python
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

with open('model__v1.tflite', 'wb') as f:
    f.write(tflite_model)
```


#
