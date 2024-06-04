from pydub import AudioSegment

# Load the audio file
audio = AudioSegment.from_mp3("a.mp3")

# Cut the audio to 12 minutes and 27 seconds
cut_audio = audio[:12*60*1000 + 27*1000]  # 12 minutes and 27 seconds in milliseconds

# Export the cut audio
cut_audio.export("a_cut.mp3", format="mp3")