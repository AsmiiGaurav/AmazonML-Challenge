import os
from PIL import Image

# Directory where images are stored
input_dir = 'resized_images'
# Directory where resized images will be saved
output_dir = 'grayscale'
os.makedirs(output_dir, exist_ok=True)

# Set the desired size for resizing
new_size = (224, 224)

# Loop through all images in the directory
for img_name in os.listdir(input_dir):
    img_path = os.path.join(input_dir, img_name)
    output_path = os.path.join(output_dir, img_name)

    try:
        with Image.open(img_path) as img:
            # Convert to grayscale
            img_gray = img.convert('L')  # 'L' mode is for grayscale
            # Resize the image
            img_resized = img_gray.resize(new_size)
            # Save it to the output directory
            img_resized.save(output_path)
            print(f"Resized and saved {img_name} as grayscale")
    except Exception as e:
        print("failed")
