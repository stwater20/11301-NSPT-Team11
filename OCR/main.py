#python版本 3.7.16
#pip install pytesseract
#pip install pillow

#安裝tesseract-ocr-w64-setup-5.5.0.20241111.exe(一直下一步即可)

#前往 C:\Program Files (x86)\Tesseract-OCR\tessdata 資料夾
#將語系包放到資料夾內

from PIL import Image
import pytesseract

#下面這行依照安裝路徑修改
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

#英文與繁體字
def chinese_tra(file):
    img = Image.open(file)
    text = pytesseract.image_to_string(img, lang='chi_tra')
    return text

#英文與簡體字
def chinese_sim(file):
    img = Image.open(file)
    text = pytesseract.image_to_string(img, lang='chi_sim')
    return text

print(chinese_tra('chinese.jpg'))

