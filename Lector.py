import pytesseract as pyt
import cv2
img = cv2.imread("Texto Prueba.jpeg")
pyt.pytesseract.tesseract_cmd ="C:\\Users\\ANept\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"
text = pyt.image_to_string(img)
print(text)
