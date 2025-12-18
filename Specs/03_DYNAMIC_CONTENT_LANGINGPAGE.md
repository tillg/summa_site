# Dynamic Content on Landing Page

## Objective

Move landing page content from hardcoded HTML template to structured markdown/YAML, enabling content updates without template changes.

**Content to be made dynamic:**
* Product short description (hero section)
* Call-to-action buttons (TestFlight Beta, macOS Download)
* Feature tiles with icons
* Screenshots
* "Get in Touch" section

---

## Implementation Analysis

### Current Architecture

The site generator (`generate_site.py`) already:
- Parses YAML frontmatter from markdown files
- Converts markdown content to HTML
- Passes frontmatter data to Jinja2 templates
- Pulls configuration from `config.py` (links, email, etc.)

The landing page template (`templates/landing.html`) currently has all content hardcoded in the HTML, while `content/index.md` only contains minimal frontmatter (title, template, description).

### Approach: YAML Frontmatter with Structured Data

Use structured YAML in the frontmatter of `content/index.md`. This leverages the existing architecture without requiring changes to the generator itself.

**Benefits:**
- No changes needed to `generate_site.py`
- Single source file for all landing page content
- Easy to version control and review changes
- Template can iterate over data structures naturally

### Data Structure Design

Here's the proposed YAML structure for `content/index.md`:

```yaml
---
title: Welcome to Summarum
template: landing
description: Keep track of your wealth...

# Hero section
tagline: "Your Financial Overview, Simplified"
hero_description: "Keep track of your wealth across multiple bank accounts, stock accounts and other value stores. Dead simple, no API integration, simple, manual updates."

# Call-to-action buttons
cta_buttons:
  - label: "TestFlight Beta (iOS/iPadOS)"
    url: "https://testflight.apple.com/join/..."
    color: "orange"
    icon: "/static/icons/plus.svg"
  - label: "Download for macOS"
    url: "https://example.com/download/macos"
    color: "coral"
    icon: "/static/icons/download.svg"

# Feature tiles
features:
  - title: "Simple Tracking"
    description: "Track all your wealth across multiple bank accounts, stock portfolios, and value stores in one place."
    icon: "/static/icons/chart-bar.svg"
    color: "orange"
  - title: "Privacy First"
    description: "No API integrations, no automatic syncing. Your financial data stays private and under your control."
    icon: "/static/icons/lock.svg"
    color: "yellow"
  - title: "Dead Simple"
    description: "Manual updates, straightforward interface. No complexity, no learning curve. Just simple wealth tracking."
    icon: "/static/icons/lightning.svg"
    color: "coral"

# Screenshots
screenshots:
  - image: "/static/images/screenshot-1.png"
    alt: "Main dashboard view"
  - image: "/static/images/screenshot-2.png"
    alt: "Account details"

# Contact section
contact_section:
  title: "Get in Touch"
  description: "Have questions or feedback? We'd love to hear from you."
  email: "contact@summarum.app"
---
```

### Design Decisions

#### 1. **Icon System**
Use icon file references (e.g., `/static/icons/chart-bar.svg`). Icons are stored as separate SVG files in `/static/icons/`.

#### 2. **URL Handling**
Use full URLs directly in markdown frontmatter. No template interpolation or config references needed.

#### 3. **Screenshot Handling**
Simple array of image objects with path and alt text. Array must not be empty (errors should be visible if misconfigured).

#### 4. **Feature Tiles**
- Support variable number of features via array
- Fixed 3-column layout
- No links to detail pages (may be added later)

#### 5. **Content Organization**
All landing page content in `content/index.md` frontmatter as a single source file.

### Implementation Steps

1. **Create Icon Files**
   - Create `/static/icons/` directory
   - Add SVG icon files (plus.svg, download.svg, chart-bar.svg, lock.svg, lightning.svg)

2. **Update `content/index.md`**
   - Add structured YAML frontmatter with all landing page content
   - Use full URLs for links
   - Reference icon files with paths (e.g., `/static/icons/chart-bar.svg`)

3. **Update `templates/landing.html`**
   - Replace hardcoded content with Jinja2 loops over frontmatter data
   - Render icons by including the SVG file content or using `<img>` tags
   - Ensure errors are visible if screenshots array is empty

4. **Enhance `generate_site.py`**
   - Add validation for required frontmatter fields with clear error messages
   - Fail build if required data is missing

5. **Testing**
   - Verify all sections render correctly
   - Test with varying numbers of features/buttons/screenshots
   - Verify validation catches missing required fields

### Future Enhancements

- **Markdown in YAML**: Allow markdown syntax within YAML strings (e.g., bold, links in descriptions)
- **Conditional Sections**: Hide entire sections if data is absent
- **Multiple CTA Styles**: Support different button styles/layouts
- **Section Ordering**: Allow frontmatter to control section order
- **i18n Support**: Structure for multiple languages
- **Feature Links**: Optional URLs on feature tiles to link to detail pages

### Validation Requirements

The site generator must validate required frontmatter fields and fail with clear error messages when:
- Required fields are missing (tagline, hero_description, cta_buttons, features, screenshots, contact_section)
- Screenshots array is empty
- Invalid data structure (e.g., features without required fields)

No backwards compatibility needed - clean break from current implementation.

