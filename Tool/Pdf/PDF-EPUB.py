import os
from pdf2image import convert_from_path
from ebooklib import epub
from PIL import Image

# Define paths
pdf_path = 'a.pdf'
output_dir = 'output_images'
epub_path = 'a.epub'

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Convert PDF to images
images = convert_from_path(pdf_path, output_folder=output_dir, fmt='jpeg')

# Initialize EPUB book
book = epub.EpubBook()
book.set_identifier('id123456')
book.set_title('PDF to EPUB')
book.set_language('en')
book.add_author('Your Name')

# Add each image as a separate chapter
for i, image in enumerate(images):
    image_path = os.path.join(output_dir, f'page_{i+1}.jpeg')
    image.save(image_path, 'JPEG')

    with open(image_path, 'rb') as img_file:
        img_content = img_file.read()
        
    img_item = epub.EpubItem(
        uid=f'image_{i+1}', 
        file_name=f'image_{i+1}.jpeg', 
        media_type='image/jpeg', 
        content=img_content
    )
    book.add_item(img_item)
    
    # Add HTML content to reference the image
    html_content = f'<html><body><img src="image_{i+1}.jpeg" /></body></html>'
    chapter = epub.EpubHtml(
        title=f'Page {i+1}', 
        file_name=f'page_{i+1}.xhtml', 
        content=html_content
    )
    book.add_item(chapter)
    book.spine.append(chapter)

# Define Table of Contents
book.toc = (epub.Link(f'page_1.xhtml', 'Page 1', 'page_1'),)

# Add default NCX and NAV files
book.add_item(epub.EpubNcx())
book.add_item(epub.EpubNav())

# Write the EPUB file
epub.write_epub(epub_path, book, {})

print(f'EPUB file created: {epub_path}')
