import os

index_path = r'c:\Users\malav\Downloads\Amuthu Dental Website\index.html'
with open(index_path, 'r', encoding='utf-8') as f:
    content = f.read()

old_style = 'style="border: 4px solid var(--teal-dark); border-radius: 16px; padding: 12px; background-color: #fff; box-sizing: border-box; object-fit: cover; max-width: 80%; height: auto; display: block; margin: 0 auto;"'
new_style = 'style="border: 4px solid var(--teal-dark); border-radius: 16px; padding: 12px; background-color: #fff; box-sizing: border-box; object-fit: cover; max-width: 80%; height: auto; display: block; margin: 0 auto; filter: none !important; transform: translateY(-40px);"'

content = content.replace(old_style, new_style)

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Image shifted up and shadow removed.")
