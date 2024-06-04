from moviepy.editor import *

# Load the video file
video = VideoFileClip('a.mp4')

# Extract the audio
audio = video.audio

# Save the audio file as mp3
audio.write_audiofile('a.mp3')

# Close the video file
video.close()
