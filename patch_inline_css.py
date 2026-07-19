import os
import glob

base_dir = r'c:\Users\malav\Downloads\Amuthu Dental Website'

# Fix in all HTML files because they might all have inlined CSS!
html_files = glob.glob(os.path.join(base_dir, '*.html'))

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We are looking for the original inlined CSS or any previous modified CSS
    # Let's use regex to reliably replace the .hero-content rule
    import re
    # We want to change the top/transform to push it down
    # First, let's just do a string replacement for the exact string we saw in index.html
    old_str = ".hero-content{position:absolute;left:5%;top:50%;transform:translateY(-50%);"
    new_str = ".hero-content{position:absolute;left:5%;top:58%;transform:translateY(-50%);"
    
    if old_str in content:
        content = content.replace(old_str, new_str)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
            print(f"Updated inlined CSS in {filepath}")

# Let's also check style.min.css just to be safe and set it to top:58% as well if it was absolute
css_path = os.path.join(base_dir, 'style.min.css')
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# I previously changed it to relative and translateY(80px). Let's change it to absolute and top:58% to match
css = re.sub(r'\.hero-content\{[^\}]+\}', ".hero-content{position:absolute;left:5%;top:58%;transform:translateY(-50%);z-index:2;max-width:530px;display:flex;flex-direction:column;gap:0}", css)
with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)
print("Updated style.min.css")
