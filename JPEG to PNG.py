import os
from PIL import Image

image_folder = "INPUT"   
output_folder = "OUTPUT"  


if not os.path.exists(output_folder):
    os.makedirs(output_folder)


for filename in os.listdir(image_folder):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
        img = Image.open(os.path.join(image_folder, filename))
        clean_name = os.path.splitext(filename)[0]
        img.save(os.path.join(output_folder, f"{clean_name}.png"), "PNG")
        print(f"Converted: {filename}")

print("All done!")