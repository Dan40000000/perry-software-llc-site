# Perry Software Website Redesign - Design Document

**Date:** 2026-02-27
**Status:** Approved

## Overview

Redesign the Perry Software LLC website to professionally showcase DermPro, a dermatology-focused practice management EHR/PM system. The site will be a single-page landing site optimized for lead generation.

## Target Audience

- Dermatology practices (primary)
- Other medical specialties (future expansion)

## Goals

1. Communicate DermPro's value proposition clearly
2. Generate demo requests and phone inquiries
3. Establish credibility and professionalism

## Contact Information

- **Phone:** 541-231-8693
- **Email:** danperry1988@gmail.com
- **Location:** Lehi, Utah

## Design Direction

- Clean & modern aesthetic
- Professional blues/teals color palette
- White space, subtle gradients
- Healthcare SaaS industry standard look

## Page Structure

### Section 1: Hero

**Headline:** "Practice Management Built for Dermatology"

**Subheadline:** "Streamline scheduling, clinical documentation, billing, and patient engagement — all in one modern, touch-friendly platform."

**CTAs:**
- Primary button: "Request a Demo" (filled, blue)
- Secondary button: "Call 541-231-8693" (outlined)

**Visual:** Clean gradient background (white to light blue/teal), optional app screenshot or abstract medical pattern.

**Branding:** "Perry Software" or "DermPro by Perry Software" top left.

### Section 2: Features Grid

**Header:** "Everything Your Practice Needs"

**6 Feature Cards** (2 rows x 3 columns):

| Feature | Description |
|---------|-------------|
| Smart Scheduling | Drag-and-drop calendar, provider availability, waitlist auto-fill, and appointment reminders |
| Clinical Documentation | Touch-friendly notes, templates, vitals, and streamlined visit workflows |
| Derm-Specific Tools | Body mapping, lesion tracking, photo timeline comparison, and pathology integration |
| Billing & Coding | Charge capture, CPT/ICD linking, claims management, and financial dashboards |
| Patient Portal | Online check-in, secure messaging, document access, and bill pay |
| Telehealth Ready | Built-in video visits, virtual waiting room, and integrated notes |

**Design:** Line-style icons in teal/blue accent. White cards with subtle shadow on hover.

### Section 3: Why Choose Us

**Header:** "Why Dermatology Practices Choose DermPro"

**4 Benefits** (horizontal layout):

| Benefit | Description |
|---------|-------------|
| Built for Dermatology | Not a generic EHR — designed specifically for skin care workflows, body mapping, and photo documentation |
| HIPAA Compliant | Enterprise-grade security, audit logging, and PHI protection built in from day one |
| Modern & Fast | Clean interface your staff will actually enjoy using — no clunky legacy software |
| Interoperability | FHIR/HL7 ready, lab integrations, e-prescribing, and seamless data exchange |

**Design:** Light gray or soft blue background. Icon left, text right.

### Section 4: Contact / Demo Request

**Header:** "See DermPro in Action"

**Subheader:** "Schedule a personalized demo or give us a call — we'd love to show you what DermPro can do for your practice."

**Layout:** Two columns

**Left column - Form fields:**
- Name (required)
- Email (required)
- Practice Name (required)
- Phone (optional)
- Submit: "Request Demo"

**Right column - Direct contact:**
- Phone: 541-231-8693 (prominent, clickable)
- Email: danperry1988@gmail.com
- Location: Lehi, Utah

### Footer

- © 2026 Perry Software LLC
- Future: Privacy Policy, Terms links

## Technical Approach

- Static HTML/CSS (matches current setup)
- Single index.html file
- Modern CSS (flexbox/grid, CSS variables for theming)
- Responsive design (mobile-first)
- Form handling: Simple mailto or future Formspree/Netlify Forms integration

## Out of Scope (for now)

- Multiple pages
- Blog
- Customer testimonials
- Pricing page
- Backend/CMS
