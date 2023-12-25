import cv2
import pytesseract
import glob

pytesseract.pytesseract.tesseract_cmd="C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

img=cv2.imread("j.jpg") 
if img is None:
    img = cv2.imread("j.png")

img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
print(pytesseract.image_to_string(img))
cv2.imshow("result",img)
cv2.waitKey(0)
