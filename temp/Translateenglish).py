# Install necessary libraries
# You can run this in your terminal
# pip install transformers torch sentencepiece

from transformers import MarianMTModel, MarianTokenizer
import torch

# Function to read the input file
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Function to write the translated output to a file
def write_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

# Function to translate text using the MarianMT model
def translate_text(text, model_name='Helsinki-NLP/opus-mt-en-zh'):
    # Load model and tokenizer
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)

    # Tokenize the input text
    inputs = tokenizer(text, return_tensors='pt', padding=True, truncation=True)

    # Perform translation
    with torch.no_grad():
        translated = model.generate(**inputs)

    # Decode the translated text
    translated_text = tokenizer.batch_decode(translated, skip_special_tokens=True)
    return translated_text[0]

# Main function to handle file translation
def main(input_file_path, output_file_path):
    # Read the input file
    text = read_file(input_file_path)
    
    # Translate the text
    translated_text = translate_text(text)
    
    # Write the translated text to the output file
    write_file(output_file_path, translated_text)

# Replace 'input.txt' and 'output.txt' with your file paths
input_file_path = '/mnt/data/input.txt'
output_file_path = '/mnt/data/output.txt'

# Run the main function
main(input_file_path, output_file_path)
