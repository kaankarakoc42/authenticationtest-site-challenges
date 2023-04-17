import requests
from PIL import Image
import os
from subprocess import run
from io import BytesIO
import cv2


tesseract_path = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def image_to_string(response):
    img = Image.open(BytesIO(response.content))
    img.save("./te.png")
    x=run(f'"{tesseract_path}" ./te.png  - pm20', capture_output=True, text=True,shell=True).stdout
    os.remove("./te.png")
    return x.strip()


def read_qr_code(response):
    img = Image.open(BytesIO(response.content))
    img.save("./te.png")
    try:
        img = cv2.imread("./te.png")
        detect = cv2.QRCodeDetector()
        value, points, straight_qrcode = detect.detectAndDecode(img)
        os.remove("./te.png")
        return value
    except:
        os.remove("./te.png")
        return
    
if __name__ == "__main__":
    url = "https://authenticationtest.com/ocrChallenge/captcha.php"
    response = requests.get(url)
    code = image_to_string(response)
    print(code)