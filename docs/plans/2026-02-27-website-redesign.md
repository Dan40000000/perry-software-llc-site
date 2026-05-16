# DermPro Website Redesign Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Transform the Perry Software LLC website into a professional single-page landing site showcasing DermPro dermatology practice management software.

**Architecture:** Static HTML/CSS site. Single `index.html` with four sections (hero, features, benefits, contact). CSS variables for theming, flexbox/grid for layout, mobile-first responsive design.

**Tech Stack:** HTML5, CSS3 (variables, flexbox, grid), vanilla JavaScript (form handling only)

---

## Task 1: Update CSS Variables and Base Styles

**Files:**
- Modify: `styles.css`

**Step 1: Update color variables for medical/professional theme**

Replace the `:root` block with:

```css
:root {
  --bg: #f8fafc;
  --paper: #ffffff;
  --text: #1e293b;
  --muted: #64748b;
  --primary: #0891b2;
  --primary-dark: #0e7490;
  --primary-light: #ecfeff;
  --accent: #06b6d4;
  --line: #e2e8f0;
  --success: #10b981;
  --gradient-start: #ecfeff;
  --gradient-end: #f0f9ff;
}
```

**Step 2: Verify in browser**

Open `index.html` in browser, confirm colors load correctly.

**Step 3: Commit**

```bash
git add styles.css
git commit -m "style: update color palette for medical/professional theme"
```

---

## Task 2: Add Hero Section Styles

**Files:**
- Modify: `styles.css`

**Step 1: Replace hero styles with new design**

Replace `.hero`, `.kicker`, `h1`, and `.lead` rules with:

```css
.hero {
  padding: 5rem 0 4rem;
  background: linear-gradient(135deg, var(--gradient-start) 0%, var(--gradient-end) 100%);
  text-align: center;
}

.hero .wrap {
  max-width: 800px;
}

.brand {
  font-size: 1rem;
  font-weight: 600;
  color: var(--primary);
  letter-spacing: 0.02em;
  margin-bottom: 2rem;
}

h1 {
  margin: 0 0 1rem;
  font-size: clamp(2.2rem, 5vw, 3.5rem);
  line-height: 1.15;
  color: var(--text);
  font-weight: 700;
}

.lead {
  margin: 0 auto 2rem;
  max-width: 600px;
  color: var(--muted);
  font-size: 1.15rem;
  line-height: 1.6;
}

.cta-group {
  display: flex;
  gap: 1rem;
  justify-content: center;
  flex-wrap: wrap;
}

.btn {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.875rem 1.75rem;
  font-size: 1rem;
  font-weight: 600;
  text-decoration: none;
  border-radius: 8px;
  transition: all 0.2s ease;
  cursor: pointer;
  border: none;
}

.btn-primary {
  background: var(--primary);
  color: white;
}

.btn-primary:hover {
  background: var(--primary-dark);
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(8, 145, 178, 0.3);
}

.btn-secondary {
  background: var(--paper);
  color: var(--primary);
  border: 2px solid var(--primary);
}

.btn-secondary:hover {
  background: var(--primary-light);
}
```

**Step 2: Verify styles render correctly**

Refresh browser, confirm hero section has gradient background and button styles ready.

**Step 3: Commit**

```bash
git add styles.css
git commit -m "style: add hero section and button styles"
```

---

## Task 3: Add Features Grid Styles

**Files:**
- Modify: `styles.css`

**Step 1: Add section and features grid styles**

Add after the hero/button styles:

```css
/* Section Styles */
section {
  padding: 4rem 0;
}

.section-header {
  text-align: center;
  margin-bottom: 3rem;
}

.section-header h2 {
  font-size: clamp(1.75rem, 3vw, 2.25rem);
  color: var(--text);
  margin: 0 0 0.5rem;
}

.section-header p {
  color: var(--muted);
  font-size: 1.1rem;
  margin: 0;
}

/* Features Grid */
.features {
  background: var(--paper);
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 2rem;
}

.feature-card {
  text-align: center;
  padding: 1.5rem;
}

.feature-icon {
  width: 56px;
  height: 56px;
  margin: 0 auto 1rem;
  background: var(--primary-light);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.feature-icon svg {
  width: 28px;
  height: 28px;
  stroke: var(--primary);
  fill: none;
  stroke-width: 2;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.feature-card h3 {
  font-size: 1.15rem;
  color: var(--text);
  margin: 0 0 0.5rem;
}

.feature-card p {
  color: var(--muted);
  font-size: 0.95rem;
  line-height: 1.5;
  margin: 0;
}

@media (max-width: 900px) {
  .features-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 600px) {
  .features-grid {
    grid-template-columns: 1fr;
  }
}
```

**Step 2: Verify responsive behavior**

Resize browser window to test 3-col, 2-col, and 1-col layouts.

**Step 3: Commit**

```bash
git add styles.css
git commit -m "style: add features grid section styles"
```

---

## Task 4: Add Benefits Section Styles

**Files:**
- Modify: `styles.css`

**Step 1: Add benefits section styles**

Add after features styles:

```css
/* Benefits Section */
.benefits {
  background: linear-gradient(180deg, var(--bg) 0%, var(--gradient-start) 100%);
}

.benefits-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 2rem;
}

.benefit-item {
  text-align: center;
}

.benefit-icon {
  width: 48px;
  height: 48px;
  margin: 0 auto 1rem;
  color: var(--primary);
}

.benefit-icon svg {
  width: 100%;
  height: 100%;
  stroke: var(--primary);
  fill: none;
  stroke-width: 1.5;
}

.benefit-item h3 {
  font-size: 1rem;
  color: var(--text);
  margin: 0 0 0.5rem;
}

.benefit-item p {
  color: var(--muted);
  font-size: 0.9rem;
  line-height: 1.5;
  margin: 0;
}

@media (max-width: 900px) {
  .benefits-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 500px) {
  .benefits-grid {
    grid-template-columns: 1fr;
  }
}
```

**Step 2: Verify styles**

Refresh browser, confirm benefits section layout ready.

**Step 3: Commit**

```bash
git add styles.css
git commit -m "style: add benefits section styles"
```

---

## Task 5: Add Contact Section Styles

**Files:**
- Modify: `styles.css`

**Step 1: Add contact section and form styles**

Add after benefits styles:

```css
/* Contact Section */
.contact {
  background: var(--paper);
}

.contact-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 4rem;
  align-items: start;
}

.contact-form h3,
.contact-info h3 {
  font-size: 1.25rem;
  color: var(--text);
  margin: 0 0 1.5rem;
}

/* Form Styles */
.form-group {
  margin-bottom: 1rem;
}

.form-group label {
  display: block;
  font-size: 0.9rem;
  font-weight: 500;
  color: var(--text);
  margin-bottom: 0.4rem;
}

.form-group input,
.form-group textarea {
  width: 100%;
  padding: 0.75rem 1rem;
  font-size: 1rem;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: var(--bg);
  color: var(--text);
  font-family: inherit;
  transition: border-color 0.2s, box-shadow 0.2s;
}

.form-group input:focus,
.form-group textarea:focus {
  outline: none;
  border-color: var(--primary);
  box-shadow: 0 0 0 3px rgba(8, 145, 178, 0.1);
}

.form-group input::placeholder {
  color: var(--muted);
}

.btn-submit {
  width: 100%;
  margin-top: 0.5rem;
}

/* Contact Info */
.contact-info-item {
  display: flex;
  align-items: flex-start;
  gap: 1rem;
  margin-bottom: 1.5rem;
}

.contact-info-icon {
  width: 40px;
  height: 40px;
  background: var(--primary-light);
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.contact-info-icon svg {
  width: 20px;
  height: 20px;
  stroke: var(--primary);
  fill: none;
  stroke-width: 2;
}

.contact-info-item a {
  color: var(--primary);
  text-decoration: none;
  font-weight: 500;
  font-size: 1.1rem;
}

.contact-info-item a:hover {
  text-decoration: underline;
}

.contact-info-item span {
  color: var(--muted);
  font-size: 0.9rem;
}

@media (max-width: 760px) {
  .contact-grid {
    grid-template-columns: 1fr;
    gap: 2.5rem;
  }
}
```

**Step 2: Verify form styling**

Refresh browser, confirm form and contact info styles ready.

**Step 3: Commit**

```bash
git add styles.css
git commit -m "style: add contact section and form styles"
```

---

## Task 6: Add Footer Styles

**Files:**
- Modify: `styles.css`

**Step 1: Update footer styles**

Replace existing `.footer` rule:

```css
/* Footer */
.footer {
  background: var(--text);
  color: #94a3b8;
  padding: 2rem 0;
  text-align: center;
}

.footer p {
  margin: 0;
  font-size: 0.9rem;
}

.footer a {
  color: #94a3b8;
  text-decoration: none;
}

.footer a:hover {
  color: white;
}
```

**Step 2: Verify footer**

Refresh browser, confirm dark footer styling.

**Step 3: Commit**

```bash
git add styles.css
git commit -m "style: update footer with dark theme"
```

---

## Task 7: Build Hero Section HTML

**Files:**
- Modify: `index.html`

**Step 1: Replace hero section content**

Replace the `<header class="hero">` section:

```html
<header class="hero">
  <div class="wrap">
    <div class="brand">Perry Software</div>
    <h1>Practice Management Built for Dermatology</h1>
    <p class="lead">
      Streamline scheduling, clinical documentation, billing, and patient engagement — all in one modern, touch-friendly platform.
    </p>
    <div class="cta-group">
      <a href="#contact" class="btn btn-primary">Request a Demo</a>
      <a href="tel:541-231-8693" class="btn btn-secondary">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>
        </svg>
        Call 541-231-8693
      </a>
    </div>
  </div>
</header>
```

**Step 2: Update page title and meta**

Update `<title>` and `<meta name="description">`:

```html
<title>DermPro by Perry Software | Dermatology Practice Management</title>
<meta
  name="description"
  content="DermPro is a modern EHR and practice management system built specifically for dermatology. Scheduling, clinical notes, billing, and patient engagement in one platform."
/>
```

**Step 3: Verify hero renders**

Refresh browser, confirm hero section displays correctly with CTAs.

**Step 4: Commit**

```bash
git add index.html
git commit -m "feat: add new hero section with DermPro branding"
```

---

## Task 8: Build Features Section HTML

**Files:**
- Modify: `index.html`

**Step 1: Replace main content with features section**

Replace `<main class="wrap grid">` and its contents with:

```html
<main>
  <section class="features">
    <div class="wrap">
      <div class="section-header">
        <h2>Everything Your Practice Needs</h2>
      </div>
      <div class="features-grid">
        <div class="feature-card">
          <div class="feature-icon">
            <svg viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
          </div>
          <h3>Smart Scheduling</h3>
          <p>Drag-and-drop calendar, provider availability, waitlist auto-fill, and appointment reminders.</p>
        </div>
        <div class="feature-card">
          <div class="feature-icon">
            <svg viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/></svg>
          </div>
          <h3>Clinical Documentation</h3>
          <p>Touch-friendly notes, templates, vitals, and streamlined visit workflows.</p>
        </div>
        <div class="feature-card">
          <div class="feature-icon">
            <svg viewBox="0 0 24 24"><circle cx="12" cy="8" r="5"/><path d="M20 21v-2a7 7 0 0 0-7-7h-2a7 7 0 0 0-7 7v2"/><circle cx="12" cy="8" r="2"/></svg>
          </div>
          <h3>Derm-Specific Tools</h3>
          <p>Body mapping, lesion tracking, photo timeline comparison, and pathology integration.</p>
        </div>
        <div class="feature-card">
          <div class="feature-icon">
            <svg viewBox="0 0 24 24"><line x1="12" y1="1" x2="12" y2="23"/><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
          </div>
          <h3>Billing & Coding</h3>
          <p>Charge capture, CPT/ICD linking, claims management, and financial dashboards.</p>
        </div>
        <div class="feature-card">
          <div class="feature-icon">
            <svg viewBox="0 0 24 24"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
          </div>
          <h3>Patient Portal</h3>
          <p>Online check-in, secure messaging, document access, and bill pay.</p>
        </div>
        <div class="feature-card">
          <div class="feature-icon">
            <svg viewBox="0 0 24 24"><polygon points="23 7 16 12 23 17 23 7"/><rect x="1" y="5" width="15" height="14" rx="2" ry="2"/></svg>
          </div>
          <h3>Telehealth Ready</h3>
          <p>Built-in video visits, virtual waiting room, and integrated notes.</p>
        </div>
      </div>
    </div>
  </section>
```

**Step 2: Verify features section**

Refresh browser, confirm 6 feature cards display with icons.

**Step 3: Commit**

```bash
git add index.html
git commit -m "feat: add features grid section"
```

---

## Task 9: Build Benefits Section HTML

**Files:**
- Modify: `index.html`

**Step 1: Add benefits section after features**

Add immediately after the `</section>` closing the features:

```html
  <section class="benefits">
    <div class="wrap">
      <div class="section-header">
        <h2>Why Dermatology Practices Choose DermPro</h2>
      </div>
      <div class="benefits-grid">
        <div class="benefit-item">
          <div class="benefit-icon">
            <svg viewBox="0 0 24 24"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
          </div>
          <h3>Built for Dermatology</h3>
          <p>Not a generic EHR — designed specifically for skin care workflows, body mapping, and photo documentation.</p>
        </div>
        <div class="benefit-item">
          <div class="benefit-icon">
            <svg viewBox="0 0 24 24"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
          </div>
          <h3>HIPAA Compliant</h3>
          <p>Enterprise-grade security, audit logging, and PHI protection built in from day one.</p>
        </div>
        <div class="benefit-item">
          <div class="benefit-icon">
            <svg viewBox="0 0 24 24"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>
          </div>
          <h3>Modern & Fast</h3>
          <p>Clean interface your staff will actually enjoy using — no clunky legacy software.</p>
        </div>
        <div class="benefit-item">
          <div class="benefit-icon">
            <svg viewBox="0 0 24 24"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>
          </div>
          <h3>Interoperability</h3>
          <p>FHIR/HL7 ready, lab integrations, e-prescribing, and seamless data exchange.</p>
        </div>
      </div>
    </div>
  </section>
```

**Step 2: Verify benefits section**

Refresh browser, confirm 4 benefit items display correctly.

**Step 3: Commit**

```bash
git add index.html
git commit -m "feat: add benefits section"
```

---

## Task 10: Build Contact Section HTML

**Files:**
- Modify: `index.html`

**Step 1: Add contact section after benefits**

Add immediately after benefits `</section>`:

```html
  <section class="contact" id="contact">
    <div class="wrap">
      <div class="section-header">
        <h2>See DermPro in Action</h2>
        <p>Schedule a personalized demo or give us a call — we'd love to show you what DermPro can do for your practice.</p>
      </div>
      <div class="contact-grid">
        <div class="contact-form">
          <h3>Request a Demo</h3>
          <form id="demo-form" action="https://formspree.io/f/placeholder" method="POST">
            <div class="form-group">
              <label for="name">Name</label>
              <input type="text" id="name" name="name" required placeholder="Your name">
            </div>
            <div class="form-group">
              <label for="email">Email</label>
              <input type="email" id="email" name="email" required placeholder="you@practice.com">
            </div>
            <div class="form-group">
              <label for="practice">Practice Name</label>
              <input type="text" id="practice" name="practice" required placeholder="Your practice name">
            </div>
            <div class="form-group">
              <label for="phone">Phone (optional)</label>
              <input type="tel" id="phone" name="phone" placeholder="(555) 123-4567">
            </div>
            <button type="submit" class="btn btn-primary btn-submit">Request Demo</button>
          </form>
        </div>
        <div class="contact-info">
          <h3>Get in Touch</h3>
          <div class="contact-info-item">
            <div class="contact-info-icon">
              <svg viewBox="0 0 24 24"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
            </div>
            <div>
              <a href="tel:541-231-8693">541-231-8693</a><br>
              <span>Call or text anytime</span>
            </div>
          </div>
          <div class="contact-info-item">
            <div class="contact-info-icon">
              <svg viewBox="0 0 24 24"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
            </div>
            <div>
              <a href="mailto:danperry1988@gmail.com">danperry1988@gmail.com</a><br>
              <span>We'll respond within 24 hours</span>
            </div>
          </div>
          <div class="contact-info-item">
            <div class="contact-info-icon">
              <svg viewBox="0 0 24 24"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
            </div>
            <div>
              <span>Lehi, Utah</span><br>
              <span>United States</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</main>
```

**Step 2: Verify contact section**

Refresh browser, confirm form and contact info display correctly.

**Step 3: Commit**

```bash
git add index.html
git commit -m "feat: add contact section with demo request form"
```

---

## Task 11: Update Footer HTML

**Files:**
- Modify: `index.html`

**Step 1: Update footer content**

Replace the footer section:

```html
<footer class="footer">
  <div class="wrap">
    <p>© <span id="year"></span> Perry Software LLC. All rights reserved.</p>
  </div>
</footer>

<script>
  document.getElementById('year').textContent = new Date().getFullYear();
</script>
```

**Step 2: Verify footer**

Refresh browser, confirm footer displays correctly.

**Step 3: Commit**

```bash
git add index.html
git commit -m "feat: update footer"
```

---

## Task 12: Final Review and Deploy

**Files:**
- All files

**Step 1: Full visual review**

- Open `index.html` in browser
- Test all sections scroll smoothly
- Test "Request a Demo" button scrolls to contact
- Test phone link opens dialer
- Test responsive at 1200px, 900px, 600px, 400px widths

**Step 2: Validate HTML**

Open browser dev tools console, check for any errors.

**Step 3: Push to GitHub**

```bash
git push origin main
```

**Step 4: Verify live site**

Visit https://dan40000000.github.io/perry-software-llc-site/ and confirm deployment.

---

## Summary

| Task | Description |
|------|-------------|
| 1 | Update CSS variables for medical theme |
| 2 | Add hero section styles |
| 3 | Add features grid styles |
| 4 | Add benefits section styles |
| 5 | Add contact section styles |
| 6 | Add footer styles |
| 7 | Build hero section HTML |
| 8 | Build features section HTML |
| 9 | Build benefits section HTML |
| 10 | Build contact section HTML |
| 11 | Update footer HTML |
| 12 | Final review and deploy |
