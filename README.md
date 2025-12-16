# Summarum Website

Static website for **Summarum**, an iOS/iPadOS/macOS app for tracking wealth across multiple accounts.

## Overview

This repository contains a custom Python-based static site generator that builds the Summarum website from markdown content files. The site uses Tailwind CSS for styling and is designed to be hosted on GitHub Pages at [summarum.app](https://summarum.app).

## Requirements

- Python 3.13+ (tested with 3.13.7)
- pip (Python package manager)

## Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd summa_site
   ```

2. **Create and activate virtual environment**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Development

### Quick Start (Recommended)

Run the development server with auto-rebuild:

```bash
python3 dev_server.py
```

This will:
- Build the site initially
- Start watching for file changes in `content/`, `templates/`, `static/`, and config files
- Automatically rebuild the site when changes are detected (with 1-second debouncing)
- Serve the site at http://localhost:8000
- Provide colored console output showing rebuild status

Simply edit your files and refresh your browser to see changes!

**What it watches:**
- `content/` - Markdown content files
- `templates/` - Jinja2 HTML templates
- `static/` - Static assets (CSS, JS, images, SVG)
- `design_variables.py` - Design system variables
- `config.py` - Site configuration
- `generate_site.py` - Site generator script

Press `Ctrl+C` to stop the development server.

### Manual Build

Generate the static site manually:

```bash
python3 generate_site.py
```

This will:
- Parse all markdown files in `content/`
- Apply Jinja2 templates from `templates/`
- Copy static assets (images, CSS, JS) to the output
- Generate HTML files in `docs/` directory
- Create a CNAME file for GitHub Pages

### Preview Without Auto-Rebuild

After building manually, you can serve with Python's built-in HTTP server:

```bash
cd docs
python3 -m http.server 8000
```

Then visit http://localhost:8000 in your browser. Note: You'll need to manually rebuild and refresh when files change.

## Project Structure

```
summa_site/
├── content/               # Markdown source files
│   ├── index.md          # Landing page
│   ├── legal.md          # Legal note
│   └── privacy.md        # Privacy policy
├── templates/            # Jinja2 HTML templates
│   ├── base.html         # Base template
│   ├── landing.html      # Landing page template
│   └── page.html         # Generic page template
├── static/               # Static assets
│   └── images/           # Images (logo.svg, screenshots)
├── docs/                 # Generated site (output directory)
├── generate_site.py      # Site generator script
├── dev_server.py         # Development server with auto-rebuild
├── design_variables.py   # Centralized design system variables
├── config.py             # Site configuration
└── requirements.txt      # Python dependencies
```

## Configuration

### Site Configuration (`config.py`)

Edit `config.py` to customize:
- Site metadata (name, tagline, description)
- Contact email
- App Store links
- Analytics settings

### Design System (`design_variables.py`)

All design tokens are centralized in `design_variables.py`:
- Brand colors (extracted from logo)
- Background colors (neutral grays)
- Text colors
- Border colors
- Typography (font sizes, weights, families)
- Spacing and sizing
- Shadows and transitions
- Component-specific styles

This ensures consistent styling across the entire site. Simply update values in this file and regenerate the site.

## Content Management

Content files are in markdown format with YAML frontmatter:

```markdown
---
title: Page Title
template: page
description: Page description
---

# Content in Markdown

Your content here...
```

### Available Templates

- `landing.html` - For the homepage (hero, features, screenshots)
- `page.html` - For generic content pages (legal, privacy)

## Deployment to GitHub Pages

1. **Build the site**
   ```bash
   python3 generate_site.py
   ```

2. **Commit and push**
   ```bash
   git add .
   git commit -m "Build site"
   git push origin main
   ```

3. **Configure GitHub Pages**
   - Go to repository Settings → Pages
   - Source: Deploy from a branch
   - Branch: `main`, Folder: `/docs`
   - Save

4. **Configure custom domain** (see Specs/01_BASIC_SITE.md for detailed DNS setup)

## Development

### Adding a New Page

1. Create a markdown file in `content/` (e.g., `content/about.md`)
2. Add YAML frontmatter with title and template
3. Write content in markdown
4. Run `python3 generate_site.py`
5. The page will be generated as `docs/about.html`

### Modifying Templates

Templates are in `templates/` and use Jinja2 syntax. After editing templates, regenerate the site:

```bash
python3 generate_site.py
```

### Brand Colors

The site uses colors extracted from the Summarum logo (logo.svg):
- **Orange**: `#FB923C`
- **Yellow**: `#F59E0B`
- **Coral**: `#EF4444`

Background colors use pure neutral grays (no blue tint):
- **Primary**: `#000000` (pure black)
- **Secondary**: `#1a1a1a` (darker neutral gray)
- **Tertiary**: `#2a2a2a` (logo gray - for cards/panels)
- **Quaternary**: `#3a3a3a` (lighter neutral gray)

These are defined in `design_variables.py` and made available as both Tailwind custom colors and CSS variables.

## Todo

- [ ] Add actual privacy policy content
- [ ] Add legal note/Impressum content
- [ ] Provide contact email address
- [ ] Add screenshots when available
- [ ] Configure App Store/TestFlight links
- [ ] Set up Umami Analytics

## Documentation

See `Specs/01_BASIC_SITE.md` for:
- Architecture decisions
- Implementation details
- Domain setup guide (GoDaddy + GitHub Pages)

## License

© 2025 Summarum. All rights reserved.
