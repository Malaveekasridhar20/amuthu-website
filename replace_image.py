import shutil
import os

base_dir = r'c:\Users\malav\Downloads\Amuthu Dental Website'
src_img = r'C:\Users\malav\Downloads\ChatGPT Image Jul 18, 2026, 10_21_08 PM.png'
dst_img = os.path.join(base_dir, 'wcu-chair.png')

# Copy the image
shutil.copy2(src_img, dst_img)

# Update the HTML
index_path = os.path.join(base_dir, 'index.html')
with open(index_path, 'r', encoding='utf-8') as f:
    content = f.read()

old_img_tag = '<img height="423" width="590" src="why_choose.webp" alt="State-of-the-art dental treatment room" class="wcu-img" loading="lazy">'
new_img_tag = '<img height="423" width="590" src="wcu-chair.png" alt="State-of-the-art dental treatment room" class="wcu-img" loading="lazy" style="border: 4px solid var(--teal-dark); border-radius: 16px; padding: 6px; background-color: #fff; box-shadow: 0 10px 30px rgba(0,0,0,0.1); box-sizing: border-box; object-fit: cover;">'

content = content.replace(old_img_tag, new_img_tag)

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Image replaced and styled.")
