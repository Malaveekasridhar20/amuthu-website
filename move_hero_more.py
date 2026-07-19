import os
import glob

base_dir = r'c:\Users\malav\Downloads\Amuthu Dental Website'
css_path = os.path.join(base_dir, 'style.min.css')

with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Replace top:3px with top:60px
css = css.replace('.hero-content{position:relative;top:3px;', '.hero-content{position:relative;top:60px;')

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

# Bump cache buster in all html files to v=136
html_files = glob.glob(os.path.join(base_dir, '*.html'))
for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = content.replace('style.min.css?v=135', 'style.min.css?v=136')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Hero content moved 60px down and cache bumped.")
