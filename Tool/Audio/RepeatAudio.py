from pydub import AudioSegment

# Load the audio file
audio_file_path = 'a.mp3'
audio = AudioSegment.from_mp3(audio_file_path)

# Repeat the audio 5 times
audio_repeated = audio * 5

# Export the repeated audio
audio_repeated.export('a_repeated.mp3', format='mp3')