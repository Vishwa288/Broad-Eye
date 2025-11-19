# Broad-Eye
Yolo based Intelligent SBC Component Detection System
Real-time detection of Arduino board components using a USB webcam and a lightweight YOLO model deployed on Raspberry Pi 5.
The project includes dataset creation, labeling, model training on Google Colab, and model deployment in NCNN formats.

Here is a **clean, professional, ready-to-upload `README.md`** for your GitHub repository.
It includes **project overview, features, dataset, training, NCNN conversion, installation, usage, folder structure, results, and acknowledgements** — everything required for a proper GitHub project.

You can copy–paste this directly into **README.md**.

---

# 🔍 Real-Time Arduino Component Detection using YOLOv8 & Raspberry Pi 5

This project presents a **real-time component detection system** capable of identifying various **Arduino board components** using a **custom-trained YOLOv8 model**. The system is deployed on a **Raspberry Pi 5** with a **USB webcam**, demonstrating accurate and efficient object detection for educational, prototyping, and automation use cases.

A lightweight YOLO model was trained using a **custom-labelled dataset**, exported to **PyTorch (.pt)** and **NCNN format** for faster inference, and deployed on the Raspberry Pi for real-time detection.

---

## 📌 Features

* ✔️ Real-time detection of Arduino components
* ✔️ Custom dataset created using **Label Studio**
* ✔️ YOLOv8n training on Google Colab
* ✔️ Deployment on Raspberry Pi 5
* ✔️ Supports **.pt** and **NCNN** formats
* ✔️ Achieves **~8 FPS** on Raspberry Pi 5 using webcam
* ✔️ Accurate detection for both small and large components
* ✔️ Clean and modular Python code

---

## 📁 Folder Structure

```
📦 Arduino-Component-Detection
│
├── Yolo.py                 # Inference code for Raspberry Pi
├── best.pt                 # Trained YOLOv8 model
├── Export_ncnn_model.py    # NCNN converted model code
│
├── dataset/                # Images + labels used for training
│   ├── train/
│   ├── valid/
│   └── data.yaml
│
├── images/                 # Sample output images (detections)
│
├── requirements.txt        # All Python dependencies
└── README.md               # Project documentation
```

---

## 📦 Requirements

Install dependencies:

```bash
pip install -r requirements.txt
```

Example `requirements.txt`:

```
opencv-python
ultralytics
numpy
```

> On Raspberry Pi, install OpenCV with
> `sudo apt install python3-opencv`

---

## 🧠 Model Training Workflow

### **🔹 1. Dataset Creation (Label Studio or Roboflow)**

* Images collected from real components + Roboflow Universe
* Manually labeled in **Label Studio**
* Exported in **YOLO format**
* `data.yaml` created with class names & paths

### **🔹 2. Model Training (Google Colab)**

```python
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

model.train(
    data="dataset/data.yaml",
    epochs=50,
    imgsz=640
)
```

Training generated `best.pt` which was downloaded.

---

## 🔄 NCNN Conversion

YOLO model was converted to NCNN using:

```python
model.export(format="ncnn")
```

Output files:

* `model_ncnn/model.param`
* `model_ncnn/model.bin`

These are added to the repository for Raspberry Pi inference.

---

## ▶️ Running on Raspberry Pi 5

Use the following command to start real-time detection:

```bash
python3 Yolo.py
```

---

## 📊 Detection Accuracy Summary

Smaller components (LED, resistors, connectors) show **higher detection accuracy** because:

> The YOLO model learns fine-grained edges, pin patterns, and silkscreen features very effectively.
> Their distinct shapes help the CNN recognize them more confidently.
> Larger components such as microcontrollers or voltage regulators may have more complex, featureless surfaces, causing relatively lower confidence scores.

| Component          | Accuracy (%) |
| ------------------ | ------------ |
| Reset Button       | 74%          |
| USB-TTL Converter  | 28%          |
| Connecting Pins    | 90%          |
| ATmega328P MCU     | 96%          |
| Voltage Regulator  | 92%          |
| Crystal Oscillator | 78%          |
| Poly Fuse          | 72%          |
| DC Power Port      | 92%          |
| CK47 Capacitor     | 97%          |


---

## 🧪 Sample Results

Place your detection images in `/images` Example:

```
![Detection Output](images/sample1.jpg)
```

---

## 🙌 Acknowledgements

* YOLOv8 by **Ultralytics**
* Label Studio (Open Source Dataset Tool)
* Roboflow Universe (Dataset reference)
* Raspberry Pi Foundation

---

## ⭐ Support the Project

If this project helped you, give it a **star ⭐ on GitHub**!





