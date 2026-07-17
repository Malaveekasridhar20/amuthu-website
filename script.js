/**
 * SmileCare Premium Header Script
 * Adds sticky scroll behaviors, responsive menu, and counter animations.
 */

document.addEventListener('DOMContentLoaded', () => {
  const header = document.querySelector('.main-header');
  const menuToggle = document.getElementById('menuToggle');
  const navMenu = document.getElementById('navMenu');
  const navLinks = document.querySelectorAll('.nav-link');

  // 1. Sticky Header scroll effect
  const handleScroll = () => {
    if (window.scrollY > 20) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
  };

  window.addEventListener('scroll', handleScroll);
  handleScroll();

  // 2. Mobile Nav Drawer Toggle
  menuToggle.addEventListener('click', (e) => {
    e.stopPropagation();
    const isExpanded = menuToggle.getAttribute('aria-expanded') === 'true';
    menuToggle.classList.toggle('active');
    navMenu.classList.toggle('active');
    menuToggle.setAttribute('aria-expanded', !isExpanded);
  });

  // Close mobile menu when clicking outside
  document.addEventListener('click', (e) => {
    if (navMenu.classList.contains('active') && !navMenu.contains(e.target) && !menuToggle.contains(e.target)) {
      menuToggle.classList.remove('active');
      navMenu.classList.remove('active');
      menuToggle.setAttribute('aria-expanded', 'false');
    }
  });

  // Close mobile menu when a nav link is clicked
  navLinks.forEach(link => {
    link.addEventListener('click', () => {
      navLinks.forEach(item => item.classList.remove('active'));
      link.classList.add('active');
      menuToggle.classList.remove('active');
      navMenu.classList.remove('active');
      menuToggle.setAttribute('aria-expanded', 'false');
    });
  });

  // 3. Why Choose Us — Animated Counter (fires once on scroll into view)
  const animateCounter = (el) => {
    const target = parseInt(el.dataset.target, 10);
    const duration = 1800;
    const startTime = performance.now();

    const step = (now) => {
      const elapsed = now - startTime;
      const progress = Math.min(elapsed / duration, 1);
      // ease-out cubic
      const eased = 1 - Math.pow(1 - progress, 3);
      el.textContent = Math.round(eased * target);
      if (progress < 1) requestAnimationFrame(step);
    };

    requestAnimationFrame(step);
  };

  const counters = document.querySelectorAll('.wcu-num');
  if (counters.length && 'IntersectionObserver' in window) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          animateCounter(entry.target);
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.4 });

    counters.forEach(c => observer.observe(c));
  }

  // 4. Pillars Tab switching (About Page)
  const tabButtons = document.querySelectorAll('.pillar-tab-btn');
  const tabContents = document.querySelectorAll('.pillar-tab-content');
  if (tabButtons.length) {
    tabButtons.forEach(btn => {
      btn.addEventListener('click', () => {
        tabButtons.forEach(b => b.classList.remove('active'));
        tabContents.forEach(c => c.classList.remove('active'));
        
        btn.classList.add('active');
        const tabId = btn.dataset.tab;
        const activeContent = document.getElementById(`tab-${tabId}`);
        if (activeContent) activeContent.classList.add('active');
      });
    });
  }

  // 5. FAQ Accordion Toggle
  const faqItems = document.querySelectorAll('.faq-item');
  if (faqItems.length) {
    faqItems.forEach(item => {
      const header = item.querySelector('.faq-header');
      header.addEventListener('click', () => {
        const isOpen = item.classList.contains('active');
        // Close all other items
        faqItems.forEach(other => other.classList.remove('active'));
        // Toggle this item
        if (!isOpen) {
          item.classList.add('active');
        }
      });
    });
  }

  // 6. Appointment Modal Popup
  const modal = document.getElementById('apptModal');
  if (modal) {
    const closeBtn = document.getElementById('apptModalClose');
    const modalForm = document.getElementById('apptModalForm');

    // Open modal when any element with data-modal="apptModal" is clicked
    document.querySelectorAll('[data-modal="apptModal"]').forEach(trigger => {
      trigger.addEventListener('click', (e) => {
        e.preventDefault();

        // Auto-select service if data-service is set on the trigger
        const serviceVal = trigger.dataset.service || '';
        const serviceSelect = document.getElementById('modal-service');
        if (serviceSelect && serviceVal) {
          serviceSelect.value = serviceVal;
        } else if (serviceSelect) {
          serviceSelect.value = '';
        }

        modal.classList.add('active');
        document.body.classList.add('modal-open');

        // Focus first input
        setTimeout(() => {
          const first = modal.querySelector('input, select, textarea');
          if (first) first.focus();
        }, 350);
      });
    });

    // Close on close button
    if (closeBtn) {
      closeBtn.addEventListener('click', () => {
        modal.classList.remove('active');
        document.body.classList.remove('modal-open');
      });
    }

    // Close on overlay background click
    modal.addEventListener('click', (e) => {
      if (e.target === modal) {
        modal.classList.remove('active');
        document.body.classList.remove('modal-open');
      }
    });

    // Close on Escape key
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && modal.classList.contains('active')) {
        modal.classList.remove('active');
        document.body.classList.remove('modal-open');
      }
    });

    // Handle form submission with success message
    if (modalForm) {
      modalForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const name = document.getElementById('modal-name').value.trim();
        const phone = document.getElementById('modal-phone').value.trim();
        const date = document.getElementById('modal-date').value;
        const service = document.getElementById('modal-service').value;
        const timeEl = document.getElementById('modal-time');
        const time = timeEl ? timeEl.value : '';
        const msgEl = document.getElementById('modal-message');
        const message = msgEl ? msgEl.value.trim() : '';

        if (!name || !phone || !date || !service) {
          // Simple validation shake
          modalForm.querySelectorAll('input:invalid, select:invalid').forEach(el => {
            el.style.borderColor = '#e53935';
            setTimeout(() => el.style.borderColor = '', 2000);
          });
          return;
        }

        // Send Email
        sendAppointmentEmail({ name, phone, date, service, time, message });

        // Show success state
        modalForm.style.display = 'none';
        const successHtml = `
          <div style="text-align:center;padding:30px 0 10px;display:flex;flex-direction:column;align-items:center;gap:16px;">
            <div style="width:72px;height:72px;background:linear-gradient(135deg,#0D4842,#1a6b62);border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;box-shadow:0 12px 28px rgba(13,72,66,0.25);animation:successPop 0.5s cubic-bezier(0.34,1.56,0.64,1);">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" width="32" height="32"><polyline points="20 6 9 17 4 12"/></svg>
            </div>
            <h3 style="font-family:'Playfair Display',serif;font-size:24px;font-weight:700;color:#021a1d;">Appointment Requested!</h3>
            <p style="font-size:15px;color:#667876;max-width:300px;margin:0 auto;">Thank you, <strong style="color: #0D4842;">${name}</strong>! We'll call you at <strong style="color: #0D4842;">${phone}</strong> to confirm your slot.</p>
            <button onclick="document.getElementById('apptModal').classList.remove('active');document.body.classList.remove('modal-open');" style="margin-top:10px;background:linear-gradient(90deg,#0D4842,#1a6b62);color:#fff;border:none;border-radius:50px;padding:13px 32px;font-size:15px;font-weight:600;cursor:pointer;font-family:inherit;">Close</button>
          </div>
        `;
        const successDiv = document.createElement('div');
        successDiv.innerHTML = successHtml;
        modal.querySelector('.appt-modal-box').appendChild(successDiv);
      });
    }
  }

  // 7. Handle inline booking form submission
  const inlineForm = document.getElementById('apptForm');
  if (inlineForm) {
    inlineForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const name = document.getElementById('appt-name').value.trim();
      const phone = document.getElementById('appt-phone').value.trim();
      const date = document.getElementById('appt-date').value;
      const service = document.getElementById('appt-service').value;

      if (!name || !phone || !date || !service) {
        inlineForm.querySelectorAll('input:invalid, select:invalid').forEach(el => {
          el.style.borderColor = '#e53935';
          setTimeout(() => el.style.borderColor = '', 2000);
        });
        return;
      }

      // Send Email
      sendAppointmentEmail({ name, phone, date, service });

      // Replace card contents with success message
      const card = inlineForm.closest('.book-appt-card');
      if (card) {
        card.style.minHeight = '360px';
        card.style.display = 'flex';
        card.style.alignItems = 'center';
        card.style.justifyContent = 'center';
        card.innerHTML = `
          <div style="text-align:center;padding:40px 24px;display:flex;flex-direction:column;align-items:center;gap:20px;width:100%;">
            <div style="width:76px;height:76px;background:#DF9B43;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;box-shadow:0 12px 28px rgba(223,155,67,0.35);">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" width="34" height="34"><polyline points="20 6 9 17 4 12"/></svg>
            </div>
            <h3 style="font-family:'Playfair Display',serif;font-size:26px;font-weight:700;color:#fff;margin:0;line-height:1.2;">Request Received!</h3>
            <p style="font-size:15px;color:rgba(255,255,255,0.9);max-width:280px;margin:0 auto;line-height:1.6;">
              Thank you, <strong style="color:#DF9B43;font-weight:700;">${name}</strong>!<br>
              We will contact you at<br><strong style="color:#DF9B43;font-weight:700;">${phone}</strong><br>to confirm your slot.
            </p>
          </div>
        `;
      }
    });
  }

  // 8. Handle academy inquiry form submission
  const academyForm = document.getElementById('academyForm');
  if (academyForm) {
    academyForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const name = document.getElementById('modal-name').value.trim();
      const phone = document.getElementById('modal-phone').value.trim();
      const email = document.getElementById('modal-email') ? document.getElementById('modal-email').value.trim() : '';
      const service = document.getElementById('modal-service').value;
      const message = document.getElementById('modal-message') ? document.getElementById('modal-message').value.trim() : '';

      if (!name || !phone || !service) {
        return;
      }

      // Send Email
      sendAppointmentEmail({
        name,
        phone,
        date: 'Academy Inquiry Request',
        service: `Academy Program: ${service}`,
        time: email || 'No email provided',
        message: message
      });

      // Show success state
      const modalBox = academyForm.closest('.appt-modal-box');
      if (modalBox) {
        modalBox.innerHTML = `
          <button class="appt-modal-close" id="modalClose" aria-label="Close modal" onclick="document.getElementById('apptModal').classList.remove('active');document.body.classList.remove('modal-open');">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" width="20" height="20">
              <line x1="18" y1="6" x2="6" y2="18"/>
              <line x1="6" y1="6" x2="18" y2="18"/>
            </svg>
          </button>
          <div style="text-align:center;padding:40px 20px;display:flex;flex-direction:column;align-items:center;gap:20px;">
            <div style="width:72px;height:72px;background:linear-gradient(135deg,#0D4842,#1a6b62);border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;box-shadow:0 12px 28px rgba(13,72,66,0.25);animation:successPop 0.5s cubic-bezier(0.34,1.56,0.64,1);">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" width="32" height="32"><polyline points="20 6 9 17 4 12"/></svg>
            </div>
            <h3 style="font-family:'Playfair Display',serif;font-size:24px;font-weight:700;color:#021a1d;margin:0;">Inquiry Submitted!</h3>
            <p style="font-size:15px;color:#667876;max-width:320px;margin:0 auto;line-height:1.5;">Thank you, <strong style="color: #0D4842;">${name}</strong>! Our academy coordinator will contact you at <strong style="color: #0D4842;">${phone}</strong> shortly.</p>
            <button onclick="document.getElementById('apptModal').classList.remove('active');document.body.classList.remove('modal-open');" style="margin-top:10px;background:linear-gradient(90deg,#0D4842,#1a6b62);color:#fff;border:none;border-radius:50px;padding:13px 32px;font-size:15px;font-weight:600;cursor:pointer;font-family:inherit;">Close</button>
          </div>
        `;
      }
    });
  }

  // 9. Handle contact page form submission
  const contactForm = document.querySelector('.contact-pro-form');
  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const name = document.getElementById('name').value.trim();
      const phone = document.getElementById('phone').value.trim();
      const email = document.getElementById('email').value.trim();
      const subject = document.getElementById('subject').value.trim();
      const message = document.getElementById('message').value.trim();

      if (!name || !phone || !email || !message) {
        return;
      }

      // Send Email using existing function
      sendAppointmentEmail({
        name,
        phone,
        date: 'Contact Form Message',
        service: subject,
        time: email,
        message: message
      });

      // Show success state
      contactForm.innerHTML = `
        <div style="text-align:center;padding:40px 20px;display:flex;flex-direction:column;align-items:center;gap:20px;">
          <div style="width:72px;height:72px;background:linear-gradient(135deg,#0D4842,#1a6b62);border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;box-shadow:0 12px 28px rgba(13,72,66,0.25);">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" width="32" height="32"><polyline points="20 6 9 17 4 12"/></svg>
          </div>
          <h3 style="font-family:'Playfair Display',serif;font-size:24px;font-weight:700;color:#021a1d;margin:0;">Message Sent!</h3>
          <p style="font-size:15px;color:#667876;max-width:320px;margin:0 auto;line-height:1.5;">Thank you, <strong style="color: #0D4842;">${name}</strong>! We have received your message and will get back to you shortly.</p>
        </div>
      `;
    });
  }
});

// ── EmailJS Configuration ─────────────────────────────────────────────────
const EMAILJS_SERVICE_ID  = 'service_etdbizl'; // Please verify this Service ID!
const EMAILJS_TEMPLATE_ID = 'template_scohuh1';
const EMAILJS_PUBLIC_KEY  = 'npMMjam_2H3MR9OFm';

function sendAppointmentEmail(details) {
  fetch('https://api.emailjs.com/api/v1.0/email/send', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      service_id:  EMAILJS_SERVICE_ID,
      template_id: EMAILJS_TEMPLATE_ID,
      user_id:     EMAILJS_PUBLIC_KEY,
      template_params: {
        patient_name:      details.name    || 'Not provided',
        patient_phone:     details.phone   || 'Not provided',
        preferred_date:    details.date    || 'Not specified',
        preferred_time:    details.time    || 'Not specified',
        service_requested: details.service || 'Not specified',
        message:           details.message || 'None',
        to_email:          'sriamuthadentalcare@gmail.com'
      }
    })
  })
  .then(res => res.text().then(text => ({ status: res.status, text })))
  .then(({ status, text }) => {
    if (status === 200) {
      console.log('✅ Email sent successfully!');
    } else {
      console.error('❌ EmailJS API error:', status, text);
    }
  })
  .catch(err => console.error('❌ Network error:', err));
}



// Flatpickr accessibility fix
setTimeout(() => {
  document.querySelectorAll('.flatpickr-mobile, .flatpickr-input').forEach(el => {
    el.removeAttribute('tabindex');
    el.setAttribute('aria-label', 'Select Date');
  });
}, 1500);
