from gtts import gTTS
import os

# Function to read the translated text file
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Function to convert text to audio using gTTS and show progress
def text_to_audio(text, output_audio_path, lang='zh', chunk_size=500):
    # Split text into chunks of chunk_size characters
    chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
    
    # Create a temporary directory to store audio chunks
    temp_dir = 'temp_audio_chunks'
    os.makedirs(temp_dir, exist_ok=True)
    
    # Process each chunk and save as temporary audio files
    for i, chunk in enumerate(chunks):
        tts = gTTS(text=chunk, lang=lang, slow=False)
        chunk_path = os.path.join(temp_dir, f'chunk_{i}.mp3')
        tts.save(chunk_path)
        print(f"Processed chunk {i + 1} / {len(chunks)}")
    
    # Combine all chunks into the final audio file
    combined = AudioSegment.empty()
    for i in range(len(chunks)):
        chunk_path = os.path.join(temp_dir, f'chunk_{i}.mp3')
        audio_segment = AudioSegment.from_mp3(chunk_path)
        combined += audio_segment
    
    combined.export(output_audio_path, format='mp3')
    
    # Clean up temporary directory
    for file_name in os.listdir(temp_dir):
        file_path = os.path.join(temp_dir, file_name)
        os.remove(file_path)
    os.rmdir(temp_dir)

# Main function to handle text to audio conversion
def main(input_text_path, output_audio_path):
    # Read the translated text
    text = read_file(input_text_path)
    
    # Convert text to audio with progress display
    text_to_audio(text, output_audio_path)

# Replace 'b.txt' and 'output_audio.mp3' with your file paths
input_text_path = 'a.txt'
output_audio_path = 'output_audio2.mp3'

# Run the main function
main(input_text_path, output_audio_path)
