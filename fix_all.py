import os
import glob
import re

base_dir = r'c:\Users\malav\Downloads\Amuthu Dental Website'
html_files = glob.glob(os.path.join(base_dir, '*.html'))

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Fix header timings case
    content = content.replace('Sun : 9am to 1 pm', 'Sun : 9 AM to 1 PM')

    # 2. Fix lakhs unit color in index.html and about.html
    # In index.html
    content = content.replace(
        '<span class="wcu-unit"> lakh+</span>',
        '<span class="wcu-unit" style="color: var(--teal-dark);"> lakhs+</span>'
    )
    # Just in case they had lakhs already
    content = content.replace(
        '<span class="wcu-unit"> lakhs+</span>',
        '<span class="wcu-unit" style="color: var(--teal-dark);"> lakhs+</span>'
    )

    # In about.html, fix the stats block explicitly
    if 'about.html' in filepath:
        # Years of experience is already data-target="50"
        
        # Happy Patients
        old_patients = '<div class="about-stat-number"><span class="wcu-num" data-target="2000">0</span>+</div>\n              <div class="about-stat-label">Happy Patients</div>'
        new_patients = '<div class="about-stat-number"><span class="wcu-num" data-target="3.5" data-float="true">0</span><span style="color: var(--gold-primary);"> lakhs+</span></div>\n              <div class="about-stat-label">Happy Patients</div>'
        content = content.replace(old_patients, new_patients)
        
        # Advanced Treatments (fix the accidental change to 50)
        old_adv = '<div class="about-stat-number"><span class="wcu-num" data-target="50">0</span>+</div>\n              <div class="about-stat-label">Advanced Treatments</div>'
        new_adv = '<div class="about-stat-number"><span class="wcu-num" data-target="20">0</span>+</div>\n              <div class="about-stat-label">Advanced Treatments</div>'
        content = content.replace(old_adv, new_adv)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

# 3. Fix script.js and script.min.js for floats
for js_file in ['script.js', 'script.min.js']:
    js_path = os.path.join(base_dir, js_file)
    if os.path.exists(js_path):
        with open(js_path, 'r', encoding='utf-8') as f:
            js = f.read()
        
        # Replace parseInt with parseFloat
        js = re.sub(r'parseInt\((el\.dataset\.target),\s*10\)', r'parseFloat(\1)', js)
        
        # Replace the rounding logic safely using regex to ignore spaces
        # Old: el.textContent = Math.round(eased * target);
        # New: el.textContent = el.hasAttribute("data-float") ? (eased * target).toFixed(1) : Math.round(eased * target);
        # Only replace if not already replaced
        if 'data-float' not in js:
            js = re.sub(
                r'el\.textContent\s*=\s*Math\.round\(\s*eased\s*\*\s*target\s*\)\s*;',
                'el.textContent = el.hasAttribute("data-float") ? (eased * target).toFixed(1) : Math.round(eased * target);',
                js
            )
        
        with open(js_path, 'w', encoding='utf-8') as f:
            f.write(js)

# 4. Fix invisible wcu-num issue in CSS
style_path = os.path.join(base_dir, 'style.css')
if os.path.exists(style_path):
    with open(style_path, 'r', encoding='utf-8') as f:
        css = f.read()
    
    # ensure wcu-num inherits color properly and displays correctly
    if 'color: inherit;' not in css.split('.wcu-num {')[1]:
        css = css.replace('.wcu-num {\n  font-family:', '.wcu-num {\n  color: inherit;\n  display: inline-block;\n  font-family:')
        with open(style_path, 'w', encoding='utf-8') as f:
            f.write(css)

print("Fixes applied.")
