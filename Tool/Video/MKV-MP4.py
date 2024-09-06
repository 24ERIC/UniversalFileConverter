import subprocess

def convert_mkv_to_mp4_lossless(input_file: str, output_file: str):
    """
    Converts an MKV file to MP4 format without affecting the video or audio quality.
    This is done by copying the video and audio streams without re-encoding.

    Args:
        input_file (str): Path to the input MKV file.
        output_file (str): Path to the output MP4 file.
    """
    try:
        # ffmpeg command to copy the video (-c:v copy) and audio (-c:a copy) streams
        command = ['ffmpeg', '-i', input_file, '-c:v', 'copy', '-c:a', 'copy', '-strict', 'experimental', output_file]
        
        # Run the command
        subprocess.run(command, check=True)
        print(f"Conversion completed successfully: {output_file}")
    
    except subprocess.CalledProcessError as e:
        print(f"Error occurred during conversion: {e}")

# Example usage
input_mkv = 'input_video.mkv'  # Replace with your input file path
output_mp4 = 'output_video.mp4'  # Replace with your desired output file path
convert_mkv_to_mp4_lossless(input_mkv, output_mp4)
