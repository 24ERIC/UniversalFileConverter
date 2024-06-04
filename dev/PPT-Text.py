import os
from pdf2image import convert_from_path
import pytesseract

# Path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'

# Set TESSDATA_PREFIX environment variable to the directory containing the tessdata directory
os.environ['TESSDATA_PREFIX'] = r'/opt/homebrew/share/'

def extract_chinese_text_from_pdf(pdf_path):
    images = convert_from_path(pdf_path)
    chinese_texts = []

    for page_number, image in enumerate(images, start=1):
        print(f"Processing page {page_number}")
        text = pytesseract.image_to_string(image, lang='chi_sim')  # Use 'chi_sim' for Simplified Chinese

        # Filter Chinese text
        for line in text.split('\n'):
            if any('\u4e00' <= char <= '\u9fff' for char in line):
                chinese_texts.append(line)
    
    return chinese_texts

pdf_path = '/Users/icer/Documents/GitHub/UniversalFileConverter/dev/in.pdf'  # Replace with your PDF file path
chinese_texts = extract_chinese_text_from_pdf(pdf_path)

# Print the extracted Chinese text
for text in chinese_texts:
    print(text)

if not chinese_texts:
    print("No Chinese text found in the PDF document.")
