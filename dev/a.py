import os
import pytesseract
from PIL import Image
import requests
from io import BytesIO

# Path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'

# Set TESSDATA_PREFIX environment variable
os.environ['TESSDATA_PREFIX'] = r'/opt/homebrew/share/'

# Valid image URL for testing
image_url = 'https://upload.wikimedia.org/wikipedia/commons/7/7d/Sample_Chinese_text.png'

# Download the image and verify it's a valid image file
try:
    response = requests.get(image_url)
    response.raise_for_status()  # Ensure the request was successful
    image = Image.open(BytesIO(response.content))
    image.verify()  # Verify that it is, in fact, an image
    image = Image.open(BytesIO(response.content))  # Reopen since verify() can be destructive
except requests.exceptions.RequestException as e:
    print(f"Error downloading the image: {e}")
except (IOError, SyntaxError) as e:
    print(f"Error opening the image: {e}")

# Test if Tesseract can load the chi_sim language
try:
    text = pytesseract.image_to_string(image, lang='chi_sim')
    print("Tesseract successfully loaded the chi_sim language.")
    print("Extracted text:", text)
except pytesseract.pytesseract.TesseractError as e:
    print(f"TesseractError: {e}")
except Exception as e:
    print(f"Error: {e}")
