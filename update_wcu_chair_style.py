import os

index_path = r'c:\Users\malav\Downloads\Amuthu Dental Website\index.html'
with open(index_path, 'r', encoding='utf-8') as f:
    content = f.read()

old_img_tag = '<img height="423" width="590" src="wcu-chair.png" alt="State-of-the-art dental treatment room" class="wcu-img" loading="lazy" style="border: 4px solid var(--teal-dark); border-radius: 16px; padding: 6px; background-color: #fff; box-shadow: 0 10px 30px rgba(0,0,0,0.1); box-sizing: border-box; object-fit: cover;">'
new_img_tag = '<img height="423" width="590" src="wcu-chair.png" alt="State-of-the-art dental treatment room" class="wcu-img" loading="lazy" style="border: 4px solid var(--teal-dark); border-radius: 16px; padding: 12px; background-color: #fff; box-sizing: border-box; object-fit: cover; max-width: 80%; height: auto; display: block; margin: 0 auto;">'

content = content.replace(old_img_tag, new_img_tag)

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Image style updated.")
