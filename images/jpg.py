from PIL import Image
import os

input_folder = "png_images"
output_folder = "jpg_images"
os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.lower().endswith(".png"):
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path).convert("RGB")  # 알파 채널 제거
        new_filename = os.path.splitext(filename)[0] + ".jpg"
        img.save(os.path.join(output_folder, new_filename), quality=85)  # 0~100, 낮을수록 더 압축
