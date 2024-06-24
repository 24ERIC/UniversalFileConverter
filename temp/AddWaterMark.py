import pikepdf
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.colors import Color

def create_watermark(watermark_pdf_path, text):
    c = canvas.Canvas(watermark_pdf_path, pagesize=letter)
    
    # Register a font that supports Chinese characters
    pdfmetrics.registerFont(TTFont('SimSun', '/Users/icer/Documents/GitHub/UniversalFileConverter/Font/simsun.ttc'))  # Update path to a valid font file
    c.setFont("SimSun", 40)
    
    # Set the color to green
    c.setFillColor(Color(0, 1, 0, 1))  # RGB green color

    # Draw the text at a specific location
    c.drawString(100, 500, text)
    c.save()

def add_watermark(input_pdf_path, output_pdf_path, watermark_pdf_path):
    # Open the original PDF
    with pikepdf.open(input_pdf_path) as pdf:
        # Open the watermark PDF
        with pikepdf.open(watermark_pdf_path) as watermark:
            watermark_page = watermark.pages[0]
            
            # Add watermark to each page
            for page in pdf.pages:
                page.add_overlay(watermark_page)
            
            # Save the result
            pdf.save(output_pdf_path)

# Example usage
input_pdf_path = '/Users/icer/Documents/GitHub/UniversalFileConverter/temp/a.pdf'
watermark_pdf_path = '/Users/icer/Documents/GitHub/UniversalFileConverter/temp/watermark.pdf'
output_pdf_path = '/Users/icer/Documents/GitHub/UniversalFileConverter/temp/b.pdf'
watermark_text = '仅供参考，敬请保密'  # This is a watermark

# Create the watermark PDF
create_watermark(watermark_pdf_path, watermark_text)

# Add the watermark to the input PDF
add_watermark(input_pdf_path, output_pdf_path, watermark_pdf_path)
