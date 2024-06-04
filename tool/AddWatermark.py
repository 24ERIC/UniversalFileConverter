from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from PyPDF2 import PdfReader, PdfWriter, PageObject

def create_watermark(text, font_path, filename="temp.pdf"):
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4

    # 注册中文字体
    pdfmetrics.registerFont(TTFont('SimSun', font_path))
    
    c.setFont("SimSun", 40)
    c.setFillColorRGB(0.6, 0.6, 0.6, alpha=0.3)
    
    # 设置水印的垂直和水平间隔
    vertical_gap = 600
    horizontal_gap = 400
    num_vertical_lines = int(height // vertical_gap) + 2
    num_horizontal_lines = int(width // horizontal_gap) + 2
    
    for i in range(num_vertical_lines):
        for j in range(num_horizontal_lines):
            x_position = j * horizontal_gap
            y_position = i * vertical_gap
            c.saveState()
            c.translate(x_position, y_position)
            c.rotate(45)
            c.drawCentredString(0, 0, text)
            c.restoreState()
    
    c.save()

def add_watermark(input_pdf, output_pdf, watermark_pdf):
    watermark = PdfReader(watermark_pdf)
    watermark_page = watermark.pages[0]

    pdf = PdfReader(input_pdf)
    writer = PdfWriter()

    for page_num in range(len(pdf.pages)):
        page = pdf.pages[page_num]
        page.merge_page(watermark_page)
        writer.add_page(page)

    with open(output_pdf, "wb") as output_file:
        writer.write(output_file)

# 自定义水印内容和字体路径
watermark_text = "仅供某某资本参考，敬请保密"
font_path = "../font/simsun.ttc"  # 请将此路径替换为你的字体文件路径
create_watermark(watermark_text, font_path)

# 输入和输出PDF文件
input_pdf = "in.pdf"
output_pdf = "out.pdf"
watermark_pdf = "temp.pdf"

add_watermark(input_pdf, output_pdf, watermark_pdf)
