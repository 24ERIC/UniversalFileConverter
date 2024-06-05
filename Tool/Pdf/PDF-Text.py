import fitz  # PyMuPDF
from PIL import Image
import pytesseract
import os

# 设置Tesseract OCR的路径
pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'

# 确保TESSDATA_PREFIX环境变量正确设置
tessdata_dir_config = '--tessdata-dir "/opt/homebrew/share/tessdata"'
os.environ['TESSDATA_PREFIX'] = '/opt/homebrew/share/'

def pdf_page_to_image(pdf_path, page_num):
    doc = fitz.open(pdf_path)
    page = doc.load_page(page_num)
    pix = page.get_pixmap()
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    return img

def extract_text_from_image(image):
    # 使用Tesseract OCR提取文本
    try:
        text = pytesseract.image_to_string(image, lang='chi_sim', config=tessdata_dir_config)
        return text
    except pytesseract.TesseractError as e:
        print("TesseractError:", e)
        return ""

def extract_text_from_pdf(pdf_path, output_txt_path):
    doc = fitz.open(pdf_path)
    all_text = ""
    
    for page_num in range(len(doc)):
        print(f"Processing page {page_num + 1} of {len(doc)}")
        img = pdf_page_to_image(pdf_path, page_num)
        text = extract_text_from_image(img)
        all_text += text + "\n"
    
    # 将提取的文本写入文件
    with open(output_txt_path, 'w', encoding='utf-8') as f:
        f.write(all_text)

# 示例：从PDF文件中提取中文文本并保存到新的文件中
pdf_path = '/Users/icer/Documents/GitHub/UniversalFileConverter/Dev/a.pdf'  # 修改为实际PDF文件路径
output_txt_path = '/Users/icer/Documents/GitHub/UniversalFileConverter/Dev/a.txt'  # 修改为输出文本文件路径
extract_text_from_pdf(pdf_path, output_txt_path)
print(f"Extracted text saved to {output_txt_path}")










# # 下载最佳中文模型
# curl -L -o /opt/homebrew/share/tessdata/chi_sim.traineddata https://github.com/tesseract-ocr/tessdata_best/raw/main/chi_sim.traineddata

# # 下载最佳英文模型
# curl -L -o /opt/homebrew/share/tessdata/eng.traineddata https://github.com/tesseract-ocr/tessdata_best/raw/main/eng.traineddata
