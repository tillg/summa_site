I want a website:
- For an iOS / iPadOS / macOS app called Summarum
- The app's slack: Keeping track of my wealth across multiple bank accounts, stock accounts and other value stores. Dead simple, no API integration, simple, manual updates.
- The website should be static, hosted on github
- I have bought the domain summarum.app
- The app should be generated from a markdown content skeleton
- The pages I need first are
  - Landing page
  - Legal note
  - Privacy policy (I already have this content)
- I want a python program that generates the content
- I have a logo for the app already: summarum_logo.png The website should have similar colors

---

## Architecture Analysis & Decisions

### Core Approach
Custom minimal Python static site generator - aligns with the "dead simple" philosophy and avoids framework bloat for just 3 pages.

### Architecture Decisions (APPROVED)

#### 1. Static Site Generator
- **Decision**: Custom minimal Python script with jinja2, markdown, and pyyaml
- **Dependencies**:
  ```
  jinja2==3.1.2
  markdown==3.5.1
  pyyaml==6.0.1
  ```

#### 2. CSS Approach
- **Decision**: Tailwind CSS via CDN (no build step required)
- Include in templates: `<script src="https://cdn.tailwindcss.com"></script>`

#### 3. Brand Colors (Extracted from Logo)
From summarum_logo.png, the color palette is:
- **Black Background**: `#000000` (or use Tailwind's `bg-black`)
- **Orange/Peach**: `#f4a261` (top bar in logo)
- **Golden Yellow**: `#f9b94a` (middle bar in logo)
- **Coral Pink**: `#e76f6f` (bottom bar in logo)

Tailwind custom config:
```javascript
tailwind.config = {
  theme: {
    extend: {
      colors: {
        'brand-orange': '#f4a261',
        'brand-yellow': '#f9b94a',
        'brand-coral': '#e76f6f',
      }
    }
  }
}
```
Note: Use Tailwind's built-in `bg-black` and `text-white` for backgrounds.

#### 4. Directory Structure
```
summa_site/
├── content/               # Markdown source files
│   ├── index.md          # Landing page
│   ├── legal.md          # Legal note
│   └── privacy.md        # Privacy policy
├── templates/            # Jinja2 HTML templates
│   ├── base.html         # Base with header/footer/nav
│   ├── landing.html      # Landing page layout
│   └── page.html         # Generic page layout
├── static/               # Static assets
│   ├── css/style.css
│   └── images/summarum_logo.png
├── docs/                 # Generated output (for GitHub Pages)
├── generate_site.py      # Main generator script
└── config.py             # Site configuration
```

#### 5. GitHub Pages Deployment
- **Decision**: Deploy from /docs folder on main branch

#### 6. Content Format
Markdown files with YAML frontmatter:
```markdown
---
title: Welcome to Summarum
template: landing
description: Keep track of your wealth
---

# Your Financial Overview, Simplified

Content here...
```

### Generator Flow
1. Load config (site name, domain, output dir)
2. Initialize Jinja2 with templates/
3. For each .md file in content/:
   - Parse markdown + frontmatter
   - Convert to HTML
   - Render with template
   - Write to docs/
4. Copy static/ assets to docs/
5. Create CNAME file with "summarum.app"

### Content & Features (APPROVED)

#### Navigation Structure
**Question clarification**: Should the navigation menu at the top include all pages (Landing, Legal, Privacy), or should Legal and Privacy only be linked from the footer?
- **Decision pending**: Please clarify which pages should appear in the main navigation

#### Landing Page Sections
- Hero section with app description
- Features section
- Screenshots gallery
- App Store links section (see below)
- Contact email

#### App Store Links
Use placeholders for now (app not yet released):
- **iOS/iPadOS**: Link to TestFlight beta (add real link when available)
- **macOS**: Download link for macOS app (add real link when available)

#### Contact Information
- Display email address for support/inquiries
- **Action needed**: Provide the email address to use

#### Analytics
**Recommendation: Umami Analytics**
- **Why**: 100% free, open source, privacy-focused, GDPR compliant
- No cookies, respects DNT, lightweight
- Self-hosted or use Umami Cloud (free tier: 3 websites, 100k events/month)
- Alternative: Plausible (€9/month, but very popular and simple)
- **Decision**: Use Umami Analytics (free)

#### Social Media & Newsletter
- No social media links
- No newsletter signup

### Domain Setup Guide (GoDaddy + GitHub Pages)

#### Step 1: Add CNAME File to Repository
The generator will automatically create `docs/CNAME` with content: `summarum.app`

#### Step 2: Configure GitHub Pages
1. Go to repository Settings → Pages
2. Under "Source", select "Deploy from a branch"
3. Select branch: `main` and folder: `/docs`
4. Click Save
5. **Don't add custom domain yet** - do this after DNS is configured

#### Step 3: Configure DNS at GoDaddy
1. Log into GoDaddy account
2. Go to "My Products" → "Domains" → Click "DNS" next to summarum.app
3. **Add A Records** (for apex domain):
   - Delete any existing A records for `@`
   - Add 4 new A records, all with Host: `@` and these IPs:
     ```
     185.199.108.153
     185.199.109.153
     185.199.110.153
     185.199.111.153
     ```
   - TTL: 600 seconds (or default)
4. **Add CNAME Record** (for www subdomain):
   - Host: `www`
   - Points to: `YOUR_GITHUB_USERNAME.github.io`
   - TTL: 1 Hour (or default)
5. Save all changes

**Note**: DNS propagation can take 24-48 hours, but often works within an hour.

#### Step 4: Configure Custom Domain in GitHub Pages
1. Wait 10-15 minutes after DNS configuration
2. Go back to repository Settings → Pages
3. Under "Custom domain", enter: `summarum.app`
4. Click Save (GitHub will check DNS configuration)
5. Wait for DNS check to complete (may take a few minutes)
6. Once verified, check "Enforce HTTPS"
   - **Note**: HTTPS option will only appear after DNS is properly configured
   - May take a few hours for certificate to provision

#### Step 5: Test
- Visit `http://summarum.app` and `https://summarum.app`
- Visit `https://www.summarum.app` (should redirect)
- All should work and show your site with HTTPS

### Implementation Order

1. **Set up directory structure**
   - Create content/, templates/, static/, static/images/ directories
   - Move summarum_logo.png to static/images/
   - Create requirements.txt

2. **Create config.py**
   - Site name, domain, output directory
   - Brand colors from logo
   - Email address for contact

3. **Build generate_site.py**
   - Markdown parsing with frontmatter
   - Jinja2 template rendering
   - Static file copying
   - CNAME file generation

4. **Create templates with Tailwind**
   - base.html (with Tailwind CDN and custom color config)
   - landing.html (hero, features, screenshots, app links)
   - page.html (for legal and privacy pages)

5. **Create content files**
   - content/index.md (landing page)
   - content/legal.md (legal note)
   - content/privacy.md (convert existing privacy policy)

6. **Test locally**
   - Run generate_site.py
   - Open docs/index.html in browser
   - Verify all pages render correctly

7. **Push to GitHub**
   - Commit all files (except docs/ can be gitignored or committed)
   - Push to GitHub

8. **Configure GitHub Pages**
   - Follow Domain Setup Guide above
   - Enable GitHub Pages from /docs folder

9. **Configure DNS at GoDaddy**
   - Follow DNS configuration steps above
   - Wait for propagation
   - Enable HTTPS in GitHub Pages
