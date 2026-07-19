import os
import glob

base_dir = r'c:\Users\malav\Downloads\Amuthu Dental Website'
css_path = os.path.join(base_dir, 'style.min.css')

with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Replace margin-top:120px with transform: translateY(80px)
old_content = ".hero-content{position:relative;margin-top:120px;"
new_content = ".hero-content{position:relative;margin-top:0;transform:translateY(80px);"
css = css.replace(old_content, new_content)

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

# Bump cache buster in all html files to v=138
html_files = glob.glob(os.path.join(base_dir, '*.html'))
for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = content.replace('style.min.css?v=137', 'style.min.css?v=138')
    content = content.replace('style.min.css?v=136', 'style.min.css?v=138')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Hero content shifted with translateY and cache bumped to 138.")
