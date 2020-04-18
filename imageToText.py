import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Users\Tesseract-OCR\tesseract.exe'
from PIL import Image

img = Image.open('test_1.jpj')
text = tess.image_to_string(img)

print(text)
