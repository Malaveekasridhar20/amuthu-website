import re
import os

base_dir = r'c:\Users\malav\Downloads\Amuthu Dental Website'
about_path = os.path.join(base_dir, 'about.html')

with open(about_path, 'r', encoding='utf-8') as f:
    about = f.read()

# Add inline style to force white color on the numbers
about = re.sub(
    r'(<span class="wcu-num"[^>]*)>',
    r'\1 style="color: #ffffff !important; display: inline-block;">',
    about
)

# For the 3.5 lakhs+ target specifically, we should also ensure data-float is there.
# It should already be there, but the regex above will just add style.

with open(about_path, 'w', encoding='utf-8') as f:
    f.write(about)

print("Added inline styles to about.html")
