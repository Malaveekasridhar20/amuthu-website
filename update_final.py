import os
import glob

base_dir = r'c:\Users\malav\Downloads\Amuthu Dental Website'
html_files = glob.glob(os.path.join(base_dir, '*.html'))

# Replacements to make in all HTML files
for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Header timing
    content = content.replace('<span>9 AM - 9 PM</span>', '<span>Mon to Sat : 9 AM - 9 PM , Sun : 9am to 1 pm</span>')

    # 2. SmileCare Dental Clinic (in index.html)
    content = content.replace('At SmileCare Dental Clinic, we combine', 'At Sri Amutha Dental Care, we combine')

    # 3. Contact page Sunday timing
    content = content.replace('Sunday: By Appointment</span>', 'Sunday: 9:00 AM - 1:00 PM</span>')

    # 4. FAQ timing
    content = content.replace(
        'We are open Monday to Saturday from 9:30 AM to 8:30 PM, and on Sundays by prior appointment only.',
        'We are open Monday to Saturday from 9:00 AM to 9:00 PM, and on Sundays from 9:00 AM to 1:00 PM.'
    )

    # 5. Stats update
    # In index.html and about.html, replace 20 with 50
    content = content.replace('<span class="wcu-num" data-target="20">0</span>', '<span class="wcu-num" data-target="50">0</span>')
    # Replace 2000+ with 3.5 lakh+
    content = content.replace('<span class="wcu-num" data-target="2000">0</span><span class="wcu-unit">+</span>', '<span class="wcu-num" data-target="3.5" data-float="true">0</span><span class="wcu-unit"> lakh+</span>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

# 6. Update script.js to support floating point targets
script_path = os.path.join(base_dir, 'script.js')
if os.path.exists(script_path):
    with open(script_path, 'r', encoding='utf-8') as f:
        js = f.read()
    
    # We need to change the counter animation logic
    # Find: el.textContent = Math.round(eased * target);
    old_js_line = 'el.textContent = Math.round(eased * target);'
    new_js_line = 'el.textContent = el.hasAttribute("data-float") ? (eased * target).toFixed(1) : Math.round(eased * target);'
    
    if old_js_line in js:
        js = js.replace(old_js_line, new_js_line)
        with open(script_path, 'w', encoding='utf-8') as f:
            f.write(js)

# Do the same for script.min.js if it exists
script_min_path = os.path.join(base_dir, 'script.min.js')
if os.path.exists(script_min_path):
    with open(script_min_path, 'r', encoding='utf-8') as f:
        js_min = f.read()
    
    # The minified version might look slightly different, but let's try replacing it if it matches
    js_min = js_min.replace('el.textContent=Math.round(eased*target)', 'el.textContent=el.hasAttribute("data-float")?(eased*target).toFixed(1):Math.round(eased*target)')
    with open(script_min_path, 'w', encoding='utf-8') as f:
        f.write(js_min)

print("All text replacements completed.")
