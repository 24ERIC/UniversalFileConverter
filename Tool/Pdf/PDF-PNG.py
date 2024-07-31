import os
from pdf2image import convert_from_path

def pdf_to_images(pdf_path, output_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Convert PDF to a list of images
    images = convert_from_path(pdf_path)

    # Save each image
    for i, image in enumerate(images):
        image_path = os.path.join(output_folder, f'page_{i + 1}.png')
        image.save(image_path, 'PNG')

if __name__ == '__main__':
    
    pdf_to_images("/Users/icer/Documents/GitHub/UniversalFileConverter/temp/a.pdf", "/Users/icer/Documents/GitHub/UniversalFileConverter/temp/b")

