import os
import glob

base_dir = r'c:\Users\malav\Downloads\Amuthu Dental Website'
css_path = os.path.join(base_dir, 'style.min.css')

with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Replace .hero-section
old_hero_section = ".hero-section{width:100%;height:100vh;background:url('assets/images/hero-desktop.webp') right center / cover no-repeat;position:relative;overflow:hidden;display:flex;align-items:center}"
new_hero_section = ".hero-section{width:100%;min-height:100vh;height:auto;padding:120px 0 60px 0;box-sizing:border-box;background:url('assets/images/hero-desktop.webp') right center / cover no-repeat;position:relative;overflow:hidden;display:flex;align-items:center}"
css = css.replace(old_hero_section, new_hero_section)

# Replace .hero-content
old_hero_content = ".hero-content{position:absolute;left:5%;top:50%;transform:translateY(-50%);z-index:2;max-width:530px;display:flex;flex-direction:column;gap:0}"
new_hero_content = ".hero-content{position:relative;margin-left:5%;z-index:2;max-width:530px;display:flex;flex-direction:column;gap:0}"
css = css.replace(old_hero_content, new_hero_content)

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

# Bump cache buster in all html files to v=134
html_files = glob.glob(os.path.join(base_dir, '*.html'))
for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = content.replace('style.min.css?v=133', 'style.min.css?v=134')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Hero section updated to be responsive on Mac and cache bumped.")
