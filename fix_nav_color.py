import os
import re

base_dir = r'c:\Users\malav\Downloads\Amuthu Dental Website'
style_path = os.path.join(base_dir, 'style.css')
min_style_path = os.path.join(base_dir, 'style.min.css')

def fix_nav_link_color(filepath):
    if not os.path.exists(filepath):
        return
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We want to replace color: inherit; or color: #ffffff; with color: #0D4842; inside .nav-link { ... }
    # Let's just do a specific replace for the minified file
    content = content.replace('.nav-link{font-size:15px;font-weight:600;color:inherit;', 
                              '.nav-link{font-size:15px;font-weight:600;color:#0D4842;')
    content = content.replace('.nav-link{font-size:15px;font-weight:600;color:#ffffff;', 
                              '.nav-link{font-size:15px;font-weight:600;color:#0D4842;')
    
    # For style.css
    content = re.sub(r'(\.nav-link\s*\{[^}]*?)color:\s*inherit;', r'\1color: #0D4842;', content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

fix_nav_link_color(style_path)
fix_nav_link_color(min_style_path)
print("Fixed nav-link color.")
