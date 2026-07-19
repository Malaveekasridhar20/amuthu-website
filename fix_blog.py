import os
import re

base_dir = r'c:\Users\malav\Downloads\Amuthu Dental Website'
blog_list_path = os.path.join(base_dir, 'blog.html')
blog_post_path = os.path.join(base_dir, 'blog-post.html')
bad_blog_path = os.path.join(base_dir, 'blog-post-irrigation-needles.html')

# 1. Delete the bad file
if os.path.exists(bad_blog_path):
    os.remove(bad_blog_path)

# 2. Fix the link in blog.html
with open(blog_list_path, 'r', encoding='utf-8') as f:
    blog_list = f.read()

blog_list = blog_list.replace('href="blog-post-irrigation-needles.html"', 'href="blog-post.html#post=irrigation-needles"')

with open(blog_list_path, 'w', encoding='utf-8') as f:
    f.write(blog_list)

# 3. Add to blog-post.html dictionary
with open(blog_post_path, 'r', encoding='utf-8') as f:
    blog_post = f.read()

# The content to add to POSTS
new_post_js = """
      },
      'irrigation-needles': {
        title: 'Research Spotlight: The Best Irrigation Needles for Root Canal Success',
        category: 'restorative', categoryLabel: 'Research',
        date: 'April 2025', readTime: '5 min read',
        img: 'assets/images/root_canal_myths.webp',
        content: `
          <h2>Advancing Endodontic Care Through Research</h2>
          <p>At Sri Amutha Dental Care, we believe in combining compassionate patient care with rigorous clinical research. Recently, our very own <strong>Dr. P. Raja Rajeswari</strong> and her team published an impactful <em>in vitro</em> study in the <em>Journal of Conservative Dentistry and Endodontics</em> titled "Evaluating the influence of different irrigation needles on the apical cleaning efficacy of endodontic irrigation."</p>

          <p>This study focuses on a crucial but often overlooked step in root canal treatments: <strong>Irrigation</strong>. Let's break down why this matters and how our research ensures you get the best possible care.</p>

          <div class="bp-divider"></div>

          <h2>Why is Irrigation Important?</h2>
          <p>A root canal treatment involves removing infected or inflamed pulp from the inside of a tooth. However, the root canal system is incredibly complex, with tiny branches and curves. Mechanical instruments alone (like dental files) cannot reach every microscopic crevice.</p>

          <blockquote>"Due to the intricate anatomy of root canals, around one-third of the wall surface remains uninstrumented. Irrigation is essential to wash out debris, bacteria, and pulp tissue."</blockquote>

          <p>This is where irrigation comes in. We use specialized liquids (irrigants) to flush out and disinfect the canal. But the <em>way</em> this liquid is delivered—specifically, the type of needle used—can significantly impact how clean the canal gets, especially at the very tip (the apex) of the root.</p>

          <h2>The Study: Testing Different Needles</h2>
          <p>The research team tested three different sizes of double-sided vented irrigation needles:</p>
          <ul>
            <li><strong>27 Gauge (27G):</strong> The thickest needle tested.</li>
            <li><strong>30 Gauge (30G):</strong> A medium-sized needle.</li>
            <li><strong>31 Gauge (31G):</strong> The thinnest and finest needle tested.</li>
          </ul>

          <p>Using advanced digital subtraction radiography, the team filled the root canals with a special radio-opaque contrast medium, performed the irrigation, and then precisely measured how much of the medium was successfully washed away. The results were clear.</p>

          <div class="bp-info-grid">
            <div class="bp-info-card">
              <h4>The Clear Winner: 31G Needles</h4>
              <p>The <strong>31G double-sided vented needle</strong> demonstrated the highest level of effectiveness in cleansing the apical third of the root canal, outperforming both the 27G and 30G needles by a significant margin.</p>
            </div>
            <div class="bp-info-card">
              <h4>Safety First</h4>
              <p>Double-sided vented, closed-ended needles were used because they prevent the dangerous extrusion of irrigant fluids out the bottom of the tooth, minimizing postoperative pain and complications.</p>
            </div>
          </div>

          <h2>What This Means for Our Patients</h2>
          <p>Our commitment to research directly translates into a better experience for you in the dental chair. By utilizing the ultra-fine 31G double-sided vented needles for our root canal procedures, we ensure:</p>

          <div class="bp-services-grid">
            <div class="bp-service-item">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" width="18" height="18"><polyline points="20 6 9 17 4 12"/></svg>
              Maximum Disinfection
            </div>
            <div class="bp-service-item">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" width="18" height="18"><polyline points="20 6 9 17 4 12"/></svg>
              Reduced Risk of Re-infection
            </div>
            <div class="bp-service-item">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" width="18" height="18"><polyline points="20 6 9 17 4 12"/></svg>
              Greater Treatment Success
            </div>
            <div class="bp-service-item">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" width="18" height="18"><polyline points="20 6 9 17 4 12"/></svg>
              Enhanced Patient Safety
            </div>
          </div>

          <p>At Sri Amutha Dental Care, you are treated by experts who don't just follow the standard of care—they help establish it. If you've been told you need a root canal, rest assured that you are in the hands of a true microsurgical specialist.</p>
        `
      }
    };
"""
# Replace the end of the POSTS dictionary
blog_post = blog_post.replace('      }\n    };', new_post_js)

# Add to ALL_POSTS_LIST
new_list_item = """
      { slug: 'gum-disease', img: 'assets/images/gum_disease_signs.webp', cat: 'preventive', title: 'Understanding Gum Disease: Signs & Prevention', date: 'April 2025', readTime: '6 min' },
      { slug: 'irrigation-needles', img: 'assets/images/root_canal_myths.webp', cat: 'restorative', title: 'Research Spotlight: The Best Irrigation Needles for Root Canal Success', date: 'April 2025', readTime: '5 min' }
"""
blog_post = blog_post.replace("{ slug: 'gum-disease', img: 'assets/images/gum_disease_signs.webp', cat: 'preventive', title: 'Understanding Gum Disease: Signs & Prevention', date: 'April 2025', readTime: '6 min' }", new_list_item)

with open(blog_post_path, 'w', encoding='utf-8') as f:
    f.write(blog_post)

print("Fixed blog structure successfully.")
