# 🌀 Rasengan Hand Tracking using OpenCV & Mediapipe

This project is a **fun computer vision demo** where I implemented a **Naruto-inspired Rasengan effect** using **hand tracking**.
When two hands come close, a glowing Rasengan ball appears in the middle — created with **OpenCV drawing functions**.

---

## 📖 Overview

* Uses **Mediapipe Hands** for real-time hand landmark detection.
* Calculates the **distance between two hands** using basic **math (Euclidean distance)**.
* If the distance is below a threshold, a **Rasengan effect** is displayed.
* Displays glowing ball + text overlay.

---

## 🛠️ Tech Stack

* **Python** 🐍
* **OpenCV** → for image processing & drawing effects
* **Mediapipe** → for real-time hand tracking
* **Math module** → for calculating the distance between hands

---

## ✨ Features

✅ Real-time webcam-based hand tracking
✅ Calculates distance using `math.hypot()`
✅ Generates **Rasengan glow effect** with OpenCV
✅ Customizable ball colors (Blue, Red, Yellow, Rainbow Rasengan 🌈)
✅ Overlay text `"Emmanuel Uzumaki RASENGAN!!!"`

---

## ⚡ Installation

Clone this repository:

```bash
git clone https://github.com/your-username/rasengan-hand-tracking.git
cd rasengan-hand-tracking
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

```bash
python rasengan.py
```

* Press **`q`** to quit.

---

## 📦 Requirements

From `requirements.txt`:

```
opencv-python
mediapipe
```

*(Math module is built-in, no installation needed)*

---

## 🎨 Customization

* Change Rasengan ball color in:

```python
cv2.circle(frame, (cx, cy), 60, (255, 0, 0), -1)   # solid ball
cv2.circle(frame, (cx, cy), 90, (255, 200, 0), 4)  # glowing ring
```

* Change text color in:

```python
cv2.putText(frame, "Emmanuel Uzumaki RASENGAN!!!", (cx - 80, cy - 80),
            cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255, 255, 255), 3)
```

---

## 📸 Example Output

✨ When hands come close together:

* A glowing **blue Rasengan ball** appears
* Text `"Emmanuel Uzumaki RASENGAN!!!"` shows above

---

## 🙌 Credits

* [OpenCV](https://opencv.org/)
* [Mediapipe](https://developers.google.com/mediapipe)
* **Naruto Anime** → inspiration for Rasengan 🌀🔥

---
