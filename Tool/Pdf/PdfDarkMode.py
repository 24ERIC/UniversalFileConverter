import fitz  # PyMuPDF
from PIL import Image
import io

def invert_pdf_colors(input_pdf, output_pdf):
    doc = fitz.open(input_pdf)
    inverted_images = []

    for page in doc:
        # Convert the PDF page to a pixmap (image) with higher resolution
        pix = page.get_pixmap(matrix=fitz.Matrix(300 / 72, 300 / 72))  # Increase DPI to 300
        img_data = pix.tobytes("png")  # Convert the pixmap to PNG bytes
        img = Image.open(io.BytesIO(img_data))  # Open the image using PIL

        # Invert the colors
        inverted_img = Image.eval(img, lambda x: 255 - x)
        inverted_images.append(inverted_img)

    # Save the inverted images to a new PDF
    inverted_images[0].save(output_pdf, "PDF", resolution=300.0, save_all=True, append_images=inverted_images[1:])

invert_pdf_colors("1_Security Analysis 6th.pdf", "1_Security Analysis 6th_out.pdf")
