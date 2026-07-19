import os
import shutil

base_dir = r'c:\Users\malav\Downloads\Amuthu Dental Website'
source_img = r'C:\Users\malav\Downloads\41598_2021_90430_Fig1_HTML.jpg'
dest_img_name = 'irrigation_needles_research.jpg'
dest_img_path = os.path.join(base_dir, 'assets', 'images', dest_img_name)
dest_img_rel = f'assets/images/{dest_img_name}'

# 1. Copy image
if os.path.exists(source_img):
    shutil.copy2(source_img, dest_img_path)
    print(f"Copied {source_img} to {dest_img_path}")
else:
    print(f"Source image not found: {source_img}")

# 2. Update blog.html
blog_list_path = os.path.join(base_dir, 'blog.html')
with open(blog_list_path, 'r', encoding='utf-8') as f:
    blog_list = f.read()

# Replace the specific image in the Research Spotlight card
# The card has alt="Root Canal Research"
import re
blog_list = re.sub(
    r'(<img[^>]*src=")assets/images/root_canal_myths\.webp("[^>]*alt="Root Canal Research")',
    rf'\1{dest_img_rel}\2',
    blog_list
)
with open(blog_list_path, 'w', encoding='utf-8') as f:
    f.write(blog_list)
print("Updated blog.html")


# 3. Update blog-post.html
blog_post_path = os.path.join(base_dir, 'blog-post.html')
with open(blog_post_path, 'r', encoding='utf-8') as f:
    blog_post = f.read()

# In the POSTS dictionary for 'irrigation-needles'
blog_post = blog_post.replace(
    "img: 'assets/images/root_canal_myths.webp',\n        content:",
    f"img: '{dest_img_rel}',\n        content:"
)
# And in the ALL_POSTS_LIST for 'irrigation-needles'
blog_post = blog_post.replace(
    "{ slug: 'irrigation-needles', img: 'assets/images/root_canal_myths.webp',",
    f"{{ slug: 'irrigation-needles', img: '{dest_img_rel}',"
)

with open(blog_post_path, 'w', encoding='utf-8') as f:
    f.write(blog_post)
print("Updated blog-post.html")

