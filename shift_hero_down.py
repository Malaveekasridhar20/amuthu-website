import os
import glob

base_dir = r'c:\Users\malav\Downloads\Amuthu Dental Website'
css_path = os.path.join(base_dir, 'style.min.css')

with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Replace top:60px with margin-top:40px to ensure flexbox reacts to it
css = css.replace('.hero-content{position:relative;top:60px;', '.hero-content{position:relative;margin-top:40px;')
# Also if it was top:3px somehow
css = css.replace('.hero-content{position:relative;top:3px;', '.hero-content{position:relative;margin-top:40px;')

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

# Bump cache buster in all html files to v=137
html_files = glob.glob(os.path.join(base_dir, '*.html'))
for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = content.replace('style.min.css?v=136', 'style.min.css?v=137')
    content = content.replace('style.min.css?v=135', 'style.min.css?v=137')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Hero content shifted with margin-top and cache bumped to 137.")
