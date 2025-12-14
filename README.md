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

## Building the Site

Generate the static site by running:

```bash
python3 generate_site.py
```

This will:
- Parse all markdown files in `content/`
- Apply Jinja2 templates from `templates/`
- Copy static assets (images, CSS, JS) to the output
- Generate HTML files in `docs/` directory
- Create a CNAME file for GitHub Pages

## Preview Locally

After building, open the generated site in your browser:

```bash
open docs/index.html  # macOS
# or
xdg-open docs/index.html  # Linux
# or simply open docs/index.html in your browser
```

For a better preview experience with a local web server:

```bash
cd docs
python3 -m http.server 8000
```

Then visit http://localhost:8000 in your browser.

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
│   ├── images/           # Images (logo, screenshots)
│   └── css/              # Additional CSS (if needed)
├── docs/                 # Generated site (output directory)
├── generate_site.py      # Site generator script
├── config.py             # Site configuration
└── requirements.txt      # Python dependencies
```

## Configuration

Edit `config.py` to customize:
- Site metadata (name, tagline, description)
- Brand colors
- Contact email
- App Store links
- Analytics settings

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

The site uses colors extracted from the Summarum logo:
- **Orange**: `#f4a261`
- **Yellow**: `#f9b94a`
- **Coral**: `#e76f6f`
- **Background**: Black

These are defined as Tailwind custom colors in the templates.

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
