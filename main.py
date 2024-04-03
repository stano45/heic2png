import os
from PIL import Image
from heic2png import HEIC2PNG

def convert_heic_to_png(heic_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(heic_folder):
        if filename.lower().endswith('.heic'):
            # Create the full file path
            file_path = os.path.join(heic_folder, filename)
            
            # Open the HEIC file
            heic_img = HEIC2PNG(file_path, quality=100)
            png_filename = filename[:-5] + '.png'
            heic_img.save(png_filename)

    print(f"Conversion complete. PNG files saved in {output_folder}")

# Usage
heic_folder = './photos'  # Replace with the path to your HEIC files
output_folder = 'output'   # Replace with the path where you want to save PNG files

convert_heic_to_png(heic_folder, output_folder)
