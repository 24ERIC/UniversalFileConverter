from pydub import AudioSegment
import os

# Correct path to the input file
input_file = "/Users/icer/Documents/GitHub/UniversalFileConverter/temp/a.m4a"
# Output file path
output_file = "/Users/icer/Documents/GitHub/UniversalFileConverter/temp/trimmed_output.m4a"

# Load the audio file
audio = AudioSegment.from_file(input_file, format="m4a")

# Calculate the duration to remove (2 minutes and 40 seconds)
duration_to_remove_ms = (2 * 60 + 40) * 1000

# Remove the first 2:40
remaining_audio = audio[duration_to_remove_ms:]

# Export the remaining audio to a new file, specify codec and format options
remaining_audio.export(output_file, format="ipod", codec="aac")

print(f"Audio file saved as {output_file}")
