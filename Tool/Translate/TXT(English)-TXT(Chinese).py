from transformers import MarianMTModel, MarianTokenizer
import torch

# Function to read the input file
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()

# Function to write the translated output to a file
def write_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

# Function to translate a batch of text lines using the MarianMT model
def translate_batch(lines, model, tokenizer):
    # Tokenize the input text
    inputs = tokenizer(lines, return_tensors='pt', padding=True, truncation=True)
    
    # Perform translation
    with torch.no_grad():
        translated = model.generate(**inputs)
    
    # Decode the translated text
    translated_texts = tokenizer.batch_decode(translated, skip_special_tokens=True)
    return translated_texts

# Main function to handle file translation
def main(input_file_path, output_file_path, model_name='Helsinki-NLP/opus-mt-en-zh', batch_size=32):
    # Load model and tokenizer
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)
    
    # Read the input file
    lines = read_file(input_file_path)
    total_lines = len(lines)
    
    # Translate the text in batches
    translated_lines = []
    for i in range(0, total_lines, batch_size):
        batch = lines[i:i + batch_size]
        translated_batch = translate_batch(batch, model, tokenizer)
        translated_lines.extend(translated_batch)
        
        # Print progress
        print(f"Processed {min(i + batch_size, total_lines)} / {total_lines} lines")
    
    # Join all translated lines into a single string
    translated_text = '\n'.join(translated_lines)
    
    # Write the translated text to the output file
    write_file(output_file_path, translated_text)

# Replace 'a.txt' and 'b.txt' with your file paths
input_file_path = 'a.txt'
output_file_path = 'b.txt'

# Run the main function
main(input_file_path, output_file_path)
