import os
import re

base_dir = r'c:\Users\malav\Downloads\Amuthu Dental Website'
files_to_update = ['index.html', 'contact.html']

for filename in files_to_update:
    filepath = os.path.join(base_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We want to remove everything from <!-- Review 2 --> to the end of <!-- Review 3 -->
    # Since my previous script inserted <!-- Review 2 --> and <!-- Review 3 --> as well, we have to be careful!
    # The new ones have JAGADEESH K and Abdul Jameel. 
    # The old ones have Rahul Menon and Suresh Kumar.
    
    # To be perfectly safe, let's just find the exact block for Rahul Menon and Suresh Kumar and remove it.
    
    # The block starts right after the new Review 3's </div>.
    # It looks like:
    #         <!-- Review 2 -->
    #         <div class="testimonial-card">
    # ...
    #               <strong>Suresh Kumar</strong>
    #               <span>Root Canal Patient</span>
    #             </div>
    #           </div>
    #         </div>
    
    content = re.sub(
        r'<!-- Review 2 -->\s*<div class="testimonial-card">.*?<strong>Rahul Menon</strong>.*?<strong>Suresh Kumar</strong>.*?</div>\s*</div>\s*</div>',
        '',
        content,
        flags=re.DOTALL
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Removed old reviews from {filename}")
