import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"D:\Programs\tess\tesseract.exe" # path to application

def convert_to_text(path):
    img = Image.open(path)
    text = pytesseract.image_to_string(img)
    return text

print(convert_to_text('path to image'))