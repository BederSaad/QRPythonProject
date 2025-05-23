import cv2
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Impossible d’ouvrir la caméra")
    exit()

while True:
    ret, img = cap.read()
    if not ret:
        print("❌ Impossible de lire l’image")
        break

    for barcode in decode(img):
        mydata = barcode.data.decode('utf-8')
        barcodeType = barcode.type
        print(mydata)
        (x, y, w, h) = barcode.rect
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        text = "{} ({})".format(mydata, barcodeType)
        cv2.putText(img, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    cv2.imshow('BarCode Reader', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
