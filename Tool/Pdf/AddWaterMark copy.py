import pikepdf
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.colors import Color
from io import BytesIO

def create_watermark(text, page_width, page_height):
    # Create a buffer to store the watermark PDF
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=(page_width, page_height))
    
    # Register a font that supports Chinese characters
    pdfmetrics.registerFont(TTFont('SimSun', '/Users/icer/Documents/GitHub/UniversalFileConverter/Font/simsun.ttc'))  # Update path to a valid font file
    c.setFont("SimSun", 40)
    
    # Set the color to green
    c.setFillColor(Color(0, 1, 0, 1))  # RGB green color

    # Draw the text at the bottom center
    text_width = c.stringWidth(text, "SimSun", 40)
    c.drawString((float(page_width) - text_width) / 2, 30, text)
    c.save()

    buffer.seek(0)
    return buffer

def add_watermark(input_pdf_path, output_pdf_path, watermark_text):
    # Open the original PDF
    with pikepdf.open(input_pdf_path) as pdf:
        # Create a new PDF writer
        pdf_writer = pikepdf.Pdf.new()
        
        # Add watermark to each page
        for page in pdf.pages:
            # Calculate the page dimensions
            mediabox = page.mediabox
            width = float(mediabox[2] - mediabox[0])
            height = float(mediabox[3] - mediabox[1])

            # Create the watermark buffer for the current page size
            watermark_buffer = create_watermark(watermark_text, width, height)
            temp_watermark_pdf = pikepdf.open(watermark_buffer)
            temp_watermark_page = temp_watermark_pdf.pages[0]
            
            # Add watermark to the current page
            page.add_overlay(temp_watermark_page)
            
            # Add the modified page to the new PDF writer
            pdf_writer.pages.append(page)
        
        # Save the result
        pdf_writer.save(output_pdf_path)

# Example usage
input_pdf_path = '/Users/icer/Documents/GitHub/UniversalFileConverter/temp/a.pdf'
output_pdf_path = '/Users/icer/Documents/GitHub/UniversalFileConverter/temp/b.pdf'
watermark_text = '仅供参考，敬请保密'  # This is a watermark

# Add the watermark to the input PDF
add_watermark(input_pdf_path, output_pdf_path, watermark_text)
