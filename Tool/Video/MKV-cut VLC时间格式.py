import subprocess

def cut_video(input_file, start_time, end_time, output_file):
    # Construct the ffmpeg command to cut the video
    command = [
        'ffmpeg',
        '-i', input_file,          # Input file
        '-ss', start_time,         # Start time in HH:MM:SS or MM:SS format
        '-to', end_time,           # End time in HH:MM:SS or MM:SS format
        '-c', 'copy',              # Copy codec to avoid re-encoding for faster processing
        output_file                # Output file
    ]

    try:
        # Run the command and wait for it to complete
        subprocess.run(command, check=True)
        print(f"Video cut successfully: {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error cutting video: {e}")

# Example usage
input_video = "a.mkv"
start_time = "00:04:38"  # Start time (in hours, minutes, seconds)
end_time = "00:06:12"    # End time (in hours, minutes, seconds)
output_video = "output_video.mkv"

cut_video(input_video, start_time, end_time, output_video)
