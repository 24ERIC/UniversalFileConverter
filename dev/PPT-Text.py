import pytesseract
from PIL import Image
import os

# 设置Tesseract OCR的路径
pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'

# 确保TESSDATA_PREFIX环境变量正确设置
tessdata_dir_config = '--tessdata-dir "/opt/homebrew/share/tessdata"'
os.environ['TESSDATA_PREFIX'] = '/opt/homebrew/share/'

def extract_text_from_image(image_path):
    # 打开图像文件
    img = Image.open(image_path)
    
    # 使用Tesseract OCR提取文本
    try:
        text = pytesseract.image_to_string(img, lang='chi_sim', config=tessdata_dir_config)
        return text
    except pytesseract.TesseractError as e:
        print("TesseractError:", e)
        return ""

# 示例：从本地图像文件中提取中文文本
image_path = '/Users/icer/Documents/GitHub/UniversalFileConverter/Dev/a.png'  # 修改为实际图像文件路径
extracted_text = extract_text_from_image(image_path)
print("Extracted Text:", extracted_text)
