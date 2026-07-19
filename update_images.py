import os
import re

base_dir = r'c:\Users\malav\Downloads\Amuthu Dental Website'
about_path = os.path.join(base_dir, 'about.html')
clear_path = os.path.join(base_dir, 'clear-aligners.html')

# 1. Update about.html
with open(about_path, 'r', encoding='utf-8') as f:
    about = f.read()

# "our Thuraiyur branch" -> "our clinic"
about = about.replace('our Thuraiyur branch', 'our clinic')

# Clear Aligners card image
about = about.replace('assets/images/clear_aligners.webp', 'assets/images/clear_aligners_new.jpeg')

# Microscopic Precision image
about = about.replace('assets/images/shutterstock_2278446171.webp', 'assets/images/microscopic_precision.jpeg')

with open(about_path, 'w', encoding='utf-8') as f:
    f.write(about)

# 2. Update clear-aligners.html
with open(clear_path, 'r', encoding='utf-8') as f:
    clear = f.read()

# Discrete Path image
clear = clear.replace('assets/images/clear_aligners_straight_smile.webp', 'assets/images/discrete_path.jpeg')

# Removable Trays image (smile1.webp)
clear = clear.replace('src="smile1.webp"', 'src="assets/images/removable_trays.jpeg"')

with open(clear_path, 'w', encoding='utf-8') as f:
    f.write(clear)

print("Text and images updated.")
