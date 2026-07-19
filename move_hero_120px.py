import os

base_dir = r'c:\Users\malav\Downloads\Amuthu Dental Website'
css_path = os.path.join(base_dir, 'style.min.css')

with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Replace margin-top:40px with margin-top:120px for a much larger top gap
css = css.replace('.hero-content{position:relative;margin-top:40px;', '.hero-content{position:relative;margin-top:120px;')

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("Hero content moved 120px down.")
