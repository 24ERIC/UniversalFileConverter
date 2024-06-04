from PIL import Image

input_image_path = 'a.webp'
output_image_path = 'a.png'

with Image.open(input_image_path) as image:
    image.save(output_image_path, 'PNG')

print(f"Image successfully converted to {output_image_path}")
