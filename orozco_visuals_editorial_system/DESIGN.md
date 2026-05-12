---
name: Orozco Visuals Editorial System
colors:
  surface: '#f9f9f9'
  surface-dim: '#dadada'
  surface-bright: '#f9f9f9'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f3f4'
  surface-container: '#eeeeee'
  surface-container-high: '#e8e8e8'
  surface-container-highest: '#e2e2e2'
  on-surface: '#1a1c1c'
  on-surface-variant: '#444748'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f0f1f1'
  outline: '#747878'
  outline-variant: '#c4c7c7'
  surface-tint: '#5f5e5e'
  primary: '#000000'
  on-primary: '#ffffff'
  primary-container: '#1c1b1b'
  on-primary-container: '#858383'
  inverse-primary: '#c9c6c5'
  secondary: '#5e5e5b'
  on-secondary: '#ffffff'
  secondary-container: '#e1dfdb'
  on-secondary-container: '#63635f'
  tertiary: '#000000'
  on-tertiary: '#ffffff'
  tertiary-container: '#221a13'
  on-tertiary-container: '#8e8277'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e5e2e1'
  primary-fixed-dim: '#c9c6c5'
  on-primary-fixed: '#1c1b1b'
  on-primary-fixed-variant: '#474646'
  secondary-fixed: '#e4e2dd'
  secondary-fixed-dim: '#c8c6c2'
  on-secondary-fixed: '#1b1c19'
  on-secondary-fixed-variant: '#474744'
  tertiary-fixed: '#f0e0d3'
  tertiary-fixed-dim: '#d3c4b8'
  on-tertiary-fixed: '#221a13'
  on-tertiary-fixed-variant: '#4f453c'
  background: '#f9f9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e2e2e2'
typography:
  display-lg:
    fontFamily: Playfair Display
    fontSize: 84px
    fontWeight: '400'
    lineHeight: 92px
    letterSpacing: -0.02em
  display-md:
    fontFamily: Playfair Display
    fontSize: 64px
    fontWeight: '400'
    lineHeight: 72px
    letterSpacing: -0.01em
  headline-lg:
    fontFamily: Playfair Display
    fontSize: 48px
    fontWeight: '400'
    lineHeight: 56px
  headline-lg-mobile:
    fontFamily: Playfair Display
    fontSize: 32px
    fontWeight: '400'
    lineHeight: 40px
  headline-md:
    fontFamily: Playfair Display
    fontSize: 32px
    fontWeight: '400'
    lineHeight: 40px
  body-lg:
    fontFamily: Hanken Grotesk
    fontSize: 20px
    fontWeight: '300'
    lineHeight: 32px
    letterSpacing: 0.01em
  body-md:
    fontFamily: Hanken Grotesk
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 26px
  label-sm:
    fontFamily: Hanken Grotesk
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.1em
spacing:
  unit: 8px
  container-max: 1440px
  gutter: 24px
  margin-desktop: 80px
  margin-tablet: 40px
  margin-mobile: 20px
  section-gap: 160px
---

## Brand & Style

The visual identity of this design system centers on "Cinematic Editorialism." It bridges the gap between the precision of high-end technology brands and the soulful, timeless nature of luxury wedding photography. The goal is to evoke an emotional response through clarity and focus, treating every screen as a curated gallery frame.

The design style is **Minimalism** enriched with **High-Contrast Editorial** elements. It prioritizes imagery above all else, using generous whitespace to give the photography room to breathe. The aesthetic is intentional, quiet, and premium, signaling a high level of craftsmanship and trustworthiness to a discerning clientele.

## Colors

The palette is rooted in a "Warm Monochrome" philosophy. The foundation is built on a sharp contrast between **Deep Charcoal (#0A0A0A)** and **Pure White (#FFFFFF)**, mirroring the classic look of black-and-white film.

To soften the interface and provide a sense of luxury and warmth, a **Subtle Cream (#F9F7F2)** is utilized for secondary surfaces and background sections. **Muted Beige (#D4C5B9)** acts as a tertiary accent for interactive states or thin borders, providing a sophisticated alternative to traditional grays. This combination ensures the interface feels approachable and romantic, yet professionally sharp.

## Typography

This design system employs a sophisticated typographic pairing to balance tradition and modernity. 

**Playfair Display** is used for all high-level headings. Its high-contrast serifs and elegant curves provide a literary, editorial feel. Large-scale "Display" sizes should use slight negative letter spacing to mimic high-end fashion mastheads.

**Hanken Grotesk** serves as the functional workhorse. As a clean, geometric sans-serif, it provides a modern, Apple-inspired clarity for body copy and UI elements. Body text should maintain a light weight (300) and generous line-height to preserve the airy, minimalist feel. Labels use an uppercase treatment with increased tracking to denote professional categorization.

## Layout & Spacing

The layout follows a **Fixed Grid** model centered within the viewport, utilizing a 12-column structure for desktop and a 4-column structure for mobile. 

A "Cinematic Framing" approach is applied to imagery, often spanning the full 12 columns or intentionally breaking the grid to create asymmetrical interest. Spacing is governed by a strict 8px base unit, but the defining characteristic is the **Section Gap (160px)**, which forces a slow, intentional scroll rhythm. This mimics the experience of flipping through a premium physical photo album. High-margin desktop layouts (80px) ensure the content never feels crowded against the edge of the screen.

## Elevation & Depth

This design system eschews heavy shadows in favor of **Tonal Layering** and **Subtle Outlines**. Depth is created through the purposeful stacking of the Cream and White surfaces. 

Interactive elements like cards or buttons use a "Ghost Border" technique—ultra-thin (1px) lines in a muted beige or soft gray (#E0E0E0) that define the shape without adding visual weight. On hover, elements may transition to a very soft, diffused ambient shadow (0px 10px 30px rgba(0,0,0,0.03)) to suggest a tactile lift. Large-scale imagery is treated as the lowest layer, with typography sometimes overlapping on cream-colored containers to create a sense of physical collage.

## Shapes

The shape language is primarily **Sharp (0px)**. Hard corners reinforce the editorial, "printed magazine" aesthetic and allow the rectangular frames of photography to sit naturally within the UI. 

While the system is strictly sharp-edged for structural elements (containers, buttons, images), circular elements may be used exclusively for "Play" buttons on cinematic reels or decorative floating icons to provide a single point of organic contrast against the rigid grid.

## Components

**Buttons**  
Primary buttons are solid charcoal with white text, featuring sharp corners. Secondary buttons use the "Ghost" style: a 1px charcoal or beige border with no fill. Labels are always uppercase with wide tracking.

**Input Fields**  
Form inputs are minimal, consisting of a single 1px bottom border rather than a full box. Labels float above in the `label-sm` style. This maintains the clean, "uncluttered" aesthetic of a luxury boutique.

**Cards**  
Imagery cards occupy the majority of the component's footprint. Captions are placed either directly below in a centered `body-md` serif or as a small, left-aligned `label-sm` sans-serif. Borders around cards should be avoided; let the image define the shape.

**Image Reels**  
A custom component for displaying wedding stories. These are horizontal-scroll sections that use "Letterbox" aspect ratios (2.35:1) to enhance the cinematic feel, often accompanied by a floating "View Film" button.

**Navigation**  
The header is transparent or pure white with a thin bottom stroke. Navigation links use `label-sm` and are spaced widely to reflect the system's focus on air and luxury.