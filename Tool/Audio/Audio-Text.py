import deepspeech
from scipy.io import wavfile
import numpy as np
from pydub import AudioSegment
import os

def convert_to_wav(input_file, output_file="temp.wav"):
    # Determine the file extension
    file_extension = os.path.splitext(input_file)[1].lower()
    
    # Load audio file using pydub
    if file_extension == ".mp3":
        audio = AudioSegment.from_mp3(input_file)
    elif file_extension == ".m4a":
        audio = AudioSegment.from_file(input_file, "m4a")
    else:
        audio = AudioSegment.from_file(input_file)
    
    # Export as WAV
    audio.export(output_file, format="wav")
    return output_file

def read_audio(file_path):
    # Convert to WAV if necessary
    if not file_path.endswith(".wav"):
        file_path = convert_to_wav(file_path)
    
    # Read audio file
    fs, audio = wavfile.read(file_path)
    audio = np.frombuffer(audio, np.int16)
    
    return fs, audio

def main(input_file):
    model_file_path = '/Users/icer/Documents/GitHub/UniversalFileConverter/Model/deepspeech-0.9.3-models.pbmm'
    scorer_file_path = '/Users/icer/Documents/GitHub/UniversalFileConverter/Model/deepspeech-0.9.3-models.scorer'

    # Load the DeepSpeech model
    model = deepspeech.Model(model_file_path)
    model.enableExternalScorer(scorer_file_path)

    # Read and convert the audio file
    fs, audio = read_audio(input_file)

    # Perform speech-to-text
    text = model.stt(audio)
    print(text)

if __name__ == "__main__":
    input_file = 'a.m4a'  # Replace with your audio file path
    main(input_file)




# import deepspeech
# from scipy.io import wavfile
# import numpy as np

# # Paths to the model and scorer files
# model_file_path = '/Users/icer/Documents/GitHub/UniversalFileConverter/Model/deepspeech-0.9.3-models.pbmm'
# scorer_file_path = '/Users/icer/Documents/GitHub/UniversalFileConverter/Model/deepspeech-0.9.3-models.scorer'

# # Load the DeepSpeech model
# model = deepspeech.Model(model_file_path)

# # Load the scorer for improved accuracy
# model.enableExternalScorer(scorer_file_path)

# # Read the audio file
# fs, audio = wavfile.read('your_audio_file.wav')
# audio = np.frombuffer(audio, np.int16)

# # Perform speech-to-text
# text = model.stt(audio)
# print(text)
