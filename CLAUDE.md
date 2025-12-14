# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository contains the static website for **Summarum**, an iOS/iPadOS/macOS app for tracking wealth across multiple accounts. The website is generated from markdown content using a Python-based static site generator.

**Key Requirements:**
- Static site hosted on GitHub Pages
- Domain: summarum.app
- Content-driven architecture using markdown
- Brand colors derived from summarum_logo.png

## Project Architecture

### Content Generation Pipeline

The website is built using a Python program that:
1. Reads markdown content files
2. Applies HTML templates
3. Generates static HTML pages
4. Outputs files ready for GitHub Pages deployment

### Pages Structure

Required pages (as per Specs/01_BASIC_SITE.md):
- Landing page (main marketing/product page)
- Legal note (Impressum/legal information)
- Privacy policy (content already exists)

## Development Commands

### Building the Site

```bash
python generate_site.py  # Main site generator script
```

### Deployment

The site is deployed via GitHub Pages. Push to the appropriate branch (typically `gh-pages` or configure in repository settings) to publish changes.

## Content Management

- Specification documents are stored in `Specs/` directory
- Markdown source files for pages should be organized logically (e.g., `content/` directory)
- The generator should preserve the branding colors from summarum_logo.png

## Design Guidelines

- Keep the design simple and clean to match the app's "dead simple" philosophy
- Extract and use colors from summarum_logo.png for consistent branding
- Ensure responsive design for mobile and desktop viewing
- Focus on clarity and ease of navigation
