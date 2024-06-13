from pydub import AudioSegment

# Load the two M4A files
audio1 = AudioSegment.from_file("1.m4a", format="m4a")
audio2 = AudioSegment.from_file("2.m4a", format="m4a")

# Merge the audio files
merged_audio = audio1 + audio2

# Export the merged audio to a new M4A file
merged_audio.export("12.m4a", format="m4a")
