import os

base_dir = r'c:\Users\malav\Downloads\Amuthu Dental Website'
template_path = os.path.join(base_dir, 'blog-post.html')
new_blog_path = os.path.join(base_dir, 'blog-post-irrigation-needles.html')
blog_list_path = os.path.join(base_dir, 'blog.html')

with open(template_path, 'r', encoding='utf-8') as f:
    template_content = f.read()

# 1. Replace title
template_content = template_content.replace(
    '<title>Blog Post | Sri Amutha Dental Care</title>',
    '<title>Research Spotlight: Best Irrigation Needles | Sri Amutha Dental Care</title>'
)
template_content = template_content.replace(
    '<link rel="canonical" href="https://sriamuthadental.com/blog-post.html">',
    '<link rel="canonical" href="https://sriamuthadental.com/blog-post-irrigation-needles.html">'
)

# 2. Replace Hero Title
import re
template_content = re.sub(
    r'<h1 class="bp-hero-title">.*?</h1>',
    '<h1 class="bp-hero-title">Research Spotlight:<br>The Best Irrigation Needles for Root Canal Success</h1>',
    template_content,
    flags=re.DOTALL
)

# 3. Replace Hero Meta
template_content = re.sub(
    r'<div class="bp-hero-meta">.*?</div>',
    '''<div class="bp-hero-meta">
          <span>April 2025</span>
          <span class="bp-meta-dot"></span>
          <span>5 min read</span>
          <span class="bp-meta-dot"></span>
          <span>By Dr. P. Raja Rajeswari</span>
        </div>''',
    template_content,
    flags=re.DOTALL
)

# 4. Replace article body
new_article_body = '''
        <img height="838" width="1250" src="assets/images/root_canal_myths.webp" alt="Root Canal Treatment Irrigation" class="bp-article-img" loading="lazy">
        
        <div class="bp-content">
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
        </div>
'''

template_content = re.sub(
    r'<img.*?class="bp-article-img".*?<div class="bp-cta">',
    new_article_body + '\n\n        <!-- ── CTA ── -->\n        <div class="bp-cta">',
    template_content,
    flags=re.DOTALL
)

with open(new_blog_path, 'w', encoding='utf-8') as f:
    f.write(template_content)


# Now update blog.html
with open(blog_list_path, 'r', encoding='utf-8') as f:
    blog_list = f.read()

new_card = '''
          <!-- Card New — Research -->
          <article class="bl-card bl-item" data-category="restorative">
            <div class="bl-card-img-wrap">
              <img height="528" width="1000" src="assets/images/root_canal_myths.webp" alt="Root Canal Research" class="bl-card-img" loading="lazy">
              <div class="bl-card-img-overlay"></div>
            </div>
            <div class="bl-card-body">
              <h3 class="bl-card-title">Research Spotlight: The Best Irrigation Needles for Root Canal Success</h3>
              <p class="bl-card-excerpt">Discover how our latest published research on 31G double-sided vented needles is advancing endodontic care and ensuring safer, cleaner root canals for our patients.</p>
              <div class="bl-card-footer">
                <div class="bl-card-meta">
                  <span>
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="12" height="12"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
                    5 min read
                  </span>
                  <span>Research</span>
                </div>
                <a aria-label="Link" href="blog-post-irrigation-needles.html" class="bl-card-link">
                  Read
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" width="13" height="13"><polyline points="9 18 15 12 9 6"/></svg>
                </a>
              </div>
            </div>
          </article>
'''

# Insert the new card into the grid
blog_list = blog_list.replace('<div class="bl-grid" id="blogsGrid">', '<div class="bl-grid" id="blogsGrid">\n' + new_card)

with open(blog_list_path, 'w', encoding='utf-8') as f:
    f.write(blog_list)

print("Created new blog post and updated blog list!")
