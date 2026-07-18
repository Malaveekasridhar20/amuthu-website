import os
import glob

base_dir = r'c:\Users\malav\Downloads\Amuthu Dental Website'
html_files = glob.glob(os.path.join(base_dir, '*.html'))

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Bump the cache buster for style.min.css
    content = content.replace('style.min.css?v=131', 'style.min.css?v=132')
    
    # Also bump script.min.js just in case they have old JS cached
    content = content.replace('script.min.js', 'script.min.js?v=2')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Cache busters updated.")
