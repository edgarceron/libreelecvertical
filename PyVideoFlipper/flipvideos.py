import os
from moviepy.editor import VideoFileClip
from moviepy.video.fx import mirror_x

# Input and output folder paths
input_folder = r"C:\Users\Edgar\Documents\LibreElec\videos"
output_folder = r"C:\Users\Edgar\Documents\LibreElec\flipped"

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Get a list of all video files in the input folder
video_files = [f for f in os.listdir(input_folder) if f.endswith((".mp4", ".avi", ".mov"))]

# Process each video file
for video_file in video_files:
    # Get the full path of the input video
    input_path = os.path.join(input_folder, video_file)
    
    # Set the output path and filename
    output_path = os.path.join(output_folder, f"flipped_{video_file}")
    
    # Load the video clip
    clip = VideoFileClip(input_path)
    
    # Flip the video horizontally (to the right)
    flipped_clip = clip.rotate(90)
    
    # Save the flipped video to the output folder
    flipped_clip.write_videofile(output_path, codec="libx264")
    
    # Close the clips
    clip.close()
    flipped_clip.close()


print("Video flipping complete!")