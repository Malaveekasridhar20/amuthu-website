import re
import os

base_dir = r'c:\Users\malav\Downloads\Amuthu Dental Website'
about_path = os.path.join(base_dir, 'about.html')
style_path = os.path.join(base_dir, 'style.css')
min_style_path = os.path.join(base_dir, 'style.min.css')

# 1. Fix about.html
with open(about_path, 'r', encoding='utf-8') as f:
    about = f.read()

# Fix Happy Patients
# Current: <span class="wcu-num" data-target="2000">0</span>+</div>
#      OR: <span class="wcu-num" data-target="2000">0</span>+
about = re.sub(
    r'<span class="wcu-num" data-target="2000">0</span>\+',
    r'<span class="wcu-num" data-target="3.5" data-float="true">0</span><span style="color: var(--gold-primary);"> lakhs+</span>',
    about
)

# Fix Advanced Treatments (accidentally set to 50 instead of 20 previously)
# We need to be careful because Years of Experience is also 50.
# We will use regex to find "Advanced Treatments" block.
about = re.sub(
    r'<span class="wcu-num" data-target="50">0</span>\+(</div>\s*<div class="about-stat-label">Advanced Treatments</div>)',
    r'<span class="wcu-num" data-target="20">0</span>+\1',
    about
)

with open(about_path, 'w', encoding='utf-8') as f:
    f.write(about)

# 2. Fix style.css wcu-num color
with open(style_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Replace color: #0D4842; in .wcu-num block
# We find .wcu-num { ... color: #0D4842; ... }
css = re.sub(r'(\.wcu-num\s*\{[^}]*?)color:\s*#0D4842;', r'\1color: inherit;', css)

with open(style_path, 'w', encoding='utf-8') as f:
    f.write(css)

# Also ensure style.min.css is perfectly fixed (I did it earlier but let's be sure)
with open(min_style_path, 'r', encoding='utf-8') as f:
    min_css = f.read()
min_css = re.sub(r'(\.wcu-num\s*\{[^}]*?)color:\s*#0D4842;', r'\1color: inherit;', min_css)
with open(min_style_path, 'w', encoding='utf-8') as f:
    f.write(min_css)

print("HTML and CSS fixed robustly.")
