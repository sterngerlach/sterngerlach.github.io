# coding: utf-8
# resize.py

import glob
import os

from PIL import Image

target_width = 600
pattern = "Tulip*.jpg"

for file_name in glob.glob(pattern):
    file_name_stem, file_ext = os.path.splitext(file_name)
    file_name_new = f"{file_name_stem}-{target_width}px{file_ext}"

    if f"{target_width}px" in file_name:
        continue

    with Image.open(file_name) as img:
        scale = target_width / float(img.width)
        target_height = int(float(img.height) * scale)

        img_resized = img.resize((target_width, target_height),
                                 Image.Resampling.LANCZOS)
        img_resized.save(file_name_new, format="JPEG", quality=95)

        print(file_name_new)
