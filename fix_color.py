import os

index_path = r'c:\Users\malav\Downloads\Amuthu Dental Website\index.html'

with open(index_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the color variable reference in index.html
content = content.replace('style="color: var(--teal-dark);"', 'style="color: #0D4842 !important;"')

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Color fixed in index.html")
