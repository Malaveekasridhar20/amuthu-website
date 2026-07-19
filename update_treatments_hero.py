import os

base_dir = r'c:\Users\malav\Downloads\Amuthu Dental Website'
treatments_path = os.path.join(base_dir, 'treatments.html')

with open(treatments_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace desktop background
old_bg = "background: #f4ddc9 url('assets/images/treatments_hero_bg.webp') no-repeat right center / contain;"
new_bg = "background: #f4ddc9 url('assets/images/treatments_hero_desktop_new.jpeg') no-repeat right center / cover;"
# Let's use 'cover' instead of 'contain' if it's a wide image, but wait, the original was 'contain'. Let's stick to 'cover' because usually for bg images it's cover to avoid repeating or empty space, but actually 'contain' was used previously. Wait, I'll keep 'contain' as in original but maybe 'cover' is better if it's a full width photo. I'll use 'cover' for now since it's a standard background image, or I'll just change the URL. Let's just change the URL.
old_bg = "url('assets/images/treatments_hero_bg.webp')"
new_bg = "url('assets/images/treatments_hero_desktop_new.jpeg')"
content = content.replace(old_bg, new_bg)

# Replace mobile image src
old_img = 'src="assets/images/treatments_hero_mobile.webp"'
new_img = 'src="assets/images/treatments_hero_mobile_new.jpeg"'
content = content.replace(old_img, new_img)

with open(treatments_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Treatments hero images updated successfully.")
