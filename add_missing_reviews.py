import os
import re

base_dir = r'c:\Users\malav\Downloads\Amuthu Dental Website'
files_to_update = ['index.html', 'contact.html']

new_reviews_html = """      <div class="testimonials-grid">

        <!-- Review 1 -->
        <div class="testimonial-card">
          <div class="testimonial-stars">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="#DF9B43"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="#DF9B43"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="#DF9B43"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="#DF9B43"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="#DF9B43"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
          </div>
          <p class="testimonial-text">"I had an excellent experience at Sri Amutha Dental Care for my tooth replacement treatment. From the very first consultation to the final result, everything was handled with the highest level of professionalism and care."</p>
          <div class="testimonial-author">
            <div class="testimonial-avatar" style="background:#0b5c92;">V</div>
            <div class="testimonial-info">
              <strong>Viswanathan Periyasamy</strong>
              <span>3 months ago</span>
            </div>
          </div>
        </div>

        <!-- Review 2 -->
        <div class="testimonial-card">
          <div class="testimonial-stars">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="#DF9B43"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="#DF9B43"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="#DF9B43"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="#DF9B43"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="#DF9B43"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
          </div>
          <p class="testimonial-text">"I recently had a root canal treatment at Sri Amutha Dental Care, and it was a great experience. I was quite nervous before the procedure, but the dentist was very calm, professional, and explained everything clearly."</p>
          <div class="testimonial-author">
            <div class="testimonial-avatar" style="background:#555;">J</div>
            <div class="testimonial-info">
              <strong>JAGADEESH K</strong>
              <span>3 months ago</span>
            </div>
          </div>
        </div>

        <!-- Review 3 -->
        <div class="testimonial-card">
          <div class="testimonial-stars">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="#DF9B43"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="#DF9B43"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="#DF9B43"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="#DF9B43"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="#DF9B43"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
          </div>
          <p class="testimonial-text">"My grandmother recently underwent a total teeth replacement at Sri Amutha Dental Care, and we are extremely happy with the results. The doctor handled her case with great care, patience, and professionalism."</p>
          <div class="testimonial-author">
            <div class="testimonial-avatar" style="background:#039be5;">A</div>
            <div class="testimonial-info">
              <strong>Abdul Jameel</strong>
              <span>3 months ago</span>
            </div>
          </div>
        </div>

      </div>"""

for filename in files_to_update:
    filepath = os.path.join(base_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the entire testimonials-grid div
    content = re.sub(
        r'<div class="testimonials-grid">.*?</div>\s*</div>\s*</section>',
        new_reviews_html + '\n    </div>\n  </section>',
        content,
        flags=re.DOTALL
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Added missing reviews to {filename}")
