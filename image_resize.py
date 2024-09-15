import os
from PIL import Image

# Directory where images are stored
input_dir = 'images1'
# Directory where resized images will be saved
output_dir = 'resized_images'
os.makedirs(output_dir, exist_ok=True)

# Set the desired size for resizing
new_size = (224, 224)

# Loop through all images in the directory
for img_name in os.listdir(input_dir):
    # Create the full input and output paths
    img_path = os.path.join(input_dir, img_name)
    output_path = os.path.join(output_dir, img_name)

    try:
        # Open an image file
        with Image.open(img_path) as img:
            # Resize the image
            img_resized = img.resize(new_size)
            # Save it to the output directory
            img_resized.save(output_path)
            print(f"Resized and saved {img_name}")
    except Exception as e:
        print(f"Failed to process {img_name}: {e}")