import os
import glob

base_dir = r'c:\Users\malav\Downloads\Amuthu Dental Website'
css_path = os.path.join(base_dir, 'style.min.css')

with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Replace .hero-content to add top:3px
old_hero_content = ".hero-content{position:relative;margin-left:5%;z-index:2;max-width:530px;display:flex;flex-direction:column;gap:0}"
new_hero_content = ".hero-content{position:relative;top:3px;margin-left:5%;z-index:2;max-width:530px;display:flex;flex-direction:column;gap:0}"
css = css.replace(old_hero_content, new_hero_content)

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

# Bump cache buster in all html files to v=135
html_files = glob.glob(os.path.join(base_dir, '*.html'))
for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = content.replace('style.min.css?v=134', 'style.min.css?v=135')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Hero content moved 3px down and cache bumped.")
