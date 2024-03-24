import os
import numpy as np
from PIL import Image

def convert_folder_to_npz(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # List all JPEG images in the input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            # Construct the full input path and load the image
            input_path = os.path.join(input_folder, filename)
            image = Image.open(input_path)
            
            # Convert the image to a NumPy array
            image_array = np.array(image)
            
            # Construct the output path
            output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.npz")
            
            # Save the image array (and any additional arrays) to an NPZ file
            np.savez(output_path, image=image_array)
            
            print(f"Converted {filename} to NPZ format and saved to {output_path}")

# Specify your input and output directories
input_folder = '/home/rainer/dev/fiery/example_data/Abstadt/'
output_folder = '/home/rainer/dev/fiery/example_data'

# Convert all images in the folder
convert_folder_to_npz(input_folder, output_folder)
