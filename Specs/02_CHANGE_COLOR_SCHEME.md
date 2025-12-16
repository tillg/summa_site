# Change Color Scheme

## Background

The logo has been updated from a dark blue background to a dark gray/black background. The new logo is available as `logo/logo.svg` and needs to be integrated into the website with an updated color scheme.

**Important Discovery**: The current website has a **blue tint** because it uses Tailwind CSS's default gray scale, which has blue undertones (e.g., `#111827`, `#1f2937`). The new logo uses **neutral grays** (e.g., `#2A2A2A`) without any color tint. This color scheme change needs to address this blue-to-neutral transition.

## Current State

### Current Logo
- **File**: `static/images/summarum_logo.png`
- **Colors**:
  - Orange: `#f4a261`
  - Yellow: `#f9b94a`
  - Coral: `#e76f6f`
- **Background**: Pure black (`#000000`)

### New Logo
- **File**: `logo/logo.svg`
- **Format**: SVG (Scalable Vector Graphics)
- **Colors**:
  - Bar 1 (Orange): `#FB923C`
  - Bar 2 (Amber/Yellow): `#F59E0B`
  - Bar 3 (Red/Coral): `#EF4444`
- **Background**: Dark gray (`#2A2A2A`)

### Current Website Colors (Blue-Tinted)

```python
# Brand colors (from old logo)
BRAND_COLORS = {
    "orange": "#f4a261",
    "yellow": "#f9b94a",
    "coral": "#e76f6f",
}

# Background colors (blue-tinted)
BACKGROUND_COLORS = {
    "primary": "#000000",    # Pure black
    "secondary": "#111827",  # gray-900 (blue-tinted)
    "tertiary": "#1f2937",   # gray-800 (blue-tinted)
}

# Text colors (blue-tinted)
TEXT_COLORS = {
    "primary": "#ffffff",
    "secondary": "#d1d5db",  # gray-300 (blue-tinted)
    "tertiary": "#9ca3af",   # gray-400 (blue-tinted)
    "muted": "#374151",      # gray-700 (blue-tinted)
    "dark": "#000000",
}

# Border colors (blue-tinted)
BORDER_COLORS = {
    "primary": "#1f2937",    # gray-800 (blue-tinted)
}
```

## Goals

1. Replace the logo across the website with SVG format
2. Update brand colors to match the new logo exactly
3. Replace all blue-tinted grays with pure neutral grays
4. Maintain visual consistency and accessibility
5. Create depth through contextual use of black and gray backgrounds

## Approved Design Changes

### 1. Logo Format

**Decision: Use SVG directly**

- Scalable without quality loss (perfect for all screen sizes and Retina displays)
- Smaller file size than PNG
- Modern browsers have excellent SVG support
- Can be styled with CSS if needed

**Implementation**:
- Copy `logo/logo.svg` to `static/images/logo.svg`
- Update all `<img>` tags to reference `logo.svg` instead of `summarum_logo.png`
- Keep PNG version for favicon only

### 2. Brand Colors

**Decision: Match logo colors exactly**

```python
BRAND_COLORS = {
    "orange": "#FB923C",   # Match logo bar 1
    "yellow": "#F59E0B",   # Match logo bar 2
    "coral": "#EF4444",    # Match logo bar 3
}
```

**Rationale**: Exact color matching ensures perfect brand consistency between logo and site.

### 3. Neutral Gray Scale

**Decision: Pure neutral grays (no color tint)**

Replace all blue-tinted Tailwind grays with true neutral grays, using the logo's `#2A2A2A` as an anchor point.

```python
BACKGROUND_COLORS = {
    "primary": "#000000",    # Pure black (main background)
    "secondary": "#1a1a1a",  # Darker neutral gray
    "tertiary": "#2a2a2a",   # Logo gray (cards, panels)
    "quaternary": "#3a3a3a", # Lighter neutral gray (accents)
}

TEXT_COLORS = {
    "primary": "#ffffff",    # White
    "secondary": "#cccccc",  # Light neutral gray (secondary text)
    "tertiary": "#999999",   # Mid neutral gray (muted text)
    "muted": "#666666",      # Dark neutral gray (very subtle text)
    "dark": "#000000",       # Black (for light backgrounds)
}

BORDER_COLORS = {
    "primary": "#3a3a3a",    # Neutral gray (visible separation)
    "subtle": "#2a2a2a",     # Darker neutral (subtle borders)
}
```

**Rationale**:
- Removes the blue tint that clashes with the logo
- Creates a cohesive neutral aesthetic
- Maintains excellent contrast and readability
- Logo's gray (`#2A2A2A`) serves as the anchor for the scale

### 4. Background Strategy

**Decision: Adaptive/Contextual backgrounds**

- **Pure black** (`#000000`) for main page sections (hero, contact)
- **Logo gray** (`#2a2a2a`) for cards, feature panels, and footer
- **Darker gray** (`#1a1a1a`) for mobile menu and dropdowns
- **Lighter gray** (`#3a3a3a`) for hover states and accents

**Rationale**: Creates visual depth and hierarchy while maintaining the dark, professional aesthetic.

### 5. Gradients

**Decision: Update to use new brand colors**

```python
GRADIENTS = {
    "brand_primary": "linear-gradient(to right, #FB923C, #F59E0B, #EF4444)",
    "brand_secondary": "linear-gradient(to right, #FB923C, #F59E0B)",
    "brand_tertiary": "linear-gradient(to right, #F59E0B, #EF4444)",
    "brand_accent": "linear-gradient(to right, #EF4444, #FB923C)",
}
```

## Implementation Plan

### Phase 1: Logo Replacement

1. Copy `logo/logo.svg` to `static/images/logo.svg`
2. Update all `<img>` tags in templates:
   - `templates/base.html` (navigation and footer)
   - `templates/landing.html` (hero section)
3. Test rendering across all pages
4. Verify SVG displays correctly at all sizes

### Phase 2: Color Variables Update

1. Update `design_variables.py`:
   - Replace `BRAND_COLORS` with new logo colors
   - Replace all background colors with neutral grays
   - Replace all text colors with neutral grays
   - Replace border colors with neutral grays
   - Update `GRADIENTS` to use new brand colors
2. Run `python3 generate_site.py` to rebuild site
3. Verify Tailwind config picks up new colors

### Phase 3: Visual Review & Refinement

1. Review all pages for visual consistency:
   - Landing page
   - Legal page
   - Privacy page
2. Verify components use appropriate backgrounds:
   - Feature cards: `#2a2a2a` (logo gray)
   - Navigation: `#000000` (black)
   - Footer: `#2a2a2a` (logo gray)
   - Mobile menu: `#1a1a1a` (darker gray)
3. Check border visibility and adjust if needed
4. Test hover states and transitions

### Phase 4: Testing & Validation

1. Visual review on different screen sizes (mobile, tablet, desktop)
2. Test on multiple browsers (Chrome, Safari, Firefox)
3. Verify color contrast meets WCAG AA standards
4. Check SVG rendering quality on Retina displays
5. Test site performance (load times should remain fast)

## Complete New Color Palette

```python
# Brand Colors (from logo)
BRAND_COLORS = {
    "orange": "#FB923C",
    "yellow": "#F59E0B",
    "coral": "#EF4444",
}

# Background Colors (neutral grays)
BACKGROUND_COLORS = {
    "primary": "#000000",    # Pure black
    "secondary": "#1a1a1a",  # Darker neutral gray
    "tertiary": "#2a2a2a",   # Logo gray
    "quaternary": "#3a3a3a", # Lighter neutral gray
}

# Text Colors (neutral grays)
TEXT_COLORS = {
    "primary": "#ffffff",    # White
    "secondary": "#cccccc",  # Light neutral gray
    "tertiary": "#999999",   # Mid neutral gray
    "muted": "#666666",      # Dark neutral gray
    "dark": "#000000",       # Black
}

# Border Colors (neutral grays)
BORDER_COLORS = {
    "primary": "#3a3a3a",    # Neutral gray
    "subtle": "#2a2a2a",     # Darker neutral
}

# Gradients (new brand colors)
GRADIENTS = {
    "brand_primary": "linear-gradient(to right, #FB923C, #F59E0B, #EF4444)",
    "brand_secondary": "linear-gradient(to right, #FB923C, #F59E0B)",
    "brand_tertiary": "linear-gradient(to right, #F59E0B, #EF4444)",
    "brand_accent": "linear-gradient(to right, #EF4444, #FB923C)",
}
```

## Success Criteria

- [x] Logo format decided (SVG)
- [x] Color palette defined (pure neutral grays)
- [x] Background strategy determined (adaptive/contextual)
- [ ] New logo displays correctly on all pages
- [ ] Logo is crisp on all screen sizes (Retina displays)
- [ ] Brand colors match the new logo exactly
- [ ] All blue tints removed, replaced with neutral grays
- [ ] Color scheme feels cohesive and professional
- [ ] All text meets WCAG AA contrast standards
- [ ] Visual hierarchy is clear and intentional
- [ ] Site maintains fast load times

## Files to Modify

1. `logo/logo.svg` → `static/images/logo.svg` (copy)
2. `design_variables.py` (update all color values)
3. `templates/base.html` (update logo references)
4. `templates/landing.html` (update logo reference in hero)
5. `docs/*` (regenerated by build process)
