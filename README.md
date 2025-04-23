# 📦 QR Python Project

A simple and practical project demonstrating how to generate and read QR codes using Python. This includes two main scripts:

- ✅ `qrcodeMaker.py` – Generate QR codes and save them as images.
- ✅ `qrcodeReader.py` – Read QR codes in real time using your webcam.

---

## 🛠️ Installation

Before running the project, make sure you have Python installed.

Install required libraries via pip:

```bash
pip install -r requirements.txt
```

Or install them manually:

```bash
pip install qrcode
pip install opencv-python
pip install pyzbar
pip install Pillow
```

---

## 🚀 How to Use

### ▶️ Generate a QR Code

Run:

```bash
python qrcodeMaker.py
```

This will generate a QR code image and save it in your project folder.

### 📷 Read QR Code with Webcam

Run:

```bash
python qrcodeReader.py
```

Make sure your webcam is connected. The script will open a live camera feed and scan any QR code it detects.

---

## 📦 File Structure

```
QRPythonProject/
│
├── qrcodeMaker.py        # Generates QR codes
├── qrcodeReader.py       # Reads QR codes via webcam
├── requirements.txt      # Python dependencies
└── README.md             # This file
```

---

## 💻 Technologies Used

- Python 🐍
- [qrcode](https://pypi.org/project/qrcode/)
- [OpenCV](https://opencv.org/)
- [pyzbar](https://github.com/NaturalHistoryMuseum/pyzbar)
- [Pillow](https://python-pillow.org/) for image handling

---

## 👨‍💻 Author

**Saad Beder**  
GitHub: [@BederSaad](https://github.com/BederSaad)

---

## 📄 License

This project is under the MIT License.  
Feel free to use, modify, and share it for learning or personal use.
