#!/usr/bin/env python3
"""
Static site generator for Summarum website
"""

import os
import shutil
from pathlib import Path
from datetime import datetime
import yaml
import markdown
from jinja2 import Environment, FileSystemLoader

import config


def parse_markdown_file(filepath):
    """Parse markdown file with YAML frontmatter"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split frontmatter and content
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            frontmatter = yaml.safe_load(parts[1])
            markdown_content = parts[2].strip()
        else:
            frontmatter = {}
            markdown_content = content
    else:
        frontmatter = {}
        markdown_content = content

    # Convert markdown to HTML
    html_content = markdown.markdown(markdown_content, extensions=['extra', 'codehilite'])

    return frontmatter, html_content


def generate_site():
    """Main site generation function"""
    print("🚀 Generating Summarum website...")

    # Setup paths
    content_dir = Path(config.CONTENT_DIR)
    template_dir = Path(config.TEMPLATE_DIR)
    static_dir = Path(config.STATIC_DIR)
    output_dir = Path(config.OUTPUT_DIR)

    # Clean and create output directory
    if output_dir.exists():
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Initialize Jinja2
    env = Environment(loader=FileSystemLoader(template_dir))

    # Add config to template context
    template_context = {
        'site': {
            'name': config.SITE_NAME,
            'tagline': config.SITE_TAGLINE,
            'description': config.SITE_DESCRIPTION,
            'domain': config.DOMAIN,
        },
        'contact_email': config.CONTACT_EMAIL,
        'testflight_link': config.TESTFLIGHT_LINK,
        'macos_download_link': config.MACOS_DOWNLOAD_LINK,
        'brand_colors': config.BRAND_COLORS,
        'umami_website_id': config.UMAMI_WEBSITE_ID,
        'umami_script_url': config.UMAMI_SCRIPT_URL,
        'current_year': datetime.now().year,
    }

    # Process markdown files
    markdown_files = list(content_dir.glob('*.md'))
    print(f"📄 Found {len(markdown_files)} content files")

    for md_file in markdown_files:
        print(f"   Processing {md_file.name}...")
        frontmatter, html_content = parse_markdown_file(md_file)

        # Determine output filename
        if md_file.stem == 'index':
            output_file = output_dir / 'index.html'
        else:
            output_file = output_dir / f'{md_file.stem}.html'

        # Get template name from frontmatter or use default
        template_name = frontmatter.get('template', 'page.html')
        if not template_name.endswith('.html'):
            template_name = f'{template_name}.html'

        # Render template
        template = env.get_template(template_name)
        context = {
            **template_context,
            'page': {
                'title': frontmatter.get('title', config.SITE_NAME),
                'description': frontmatter.get('description', config.SITE_DESCRIPTION),
                'content': html_content,
            }
        }

        rendered_html = template.render(**context)

        # Write output file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(rendered_html)

        print(f"   ✅ Generated {output_file}")

    # Copy static files
    print(f"📦 Copying static assets...")
    if static_dir.exists():
        # Copy entire static directory to output
        static_output = output_dir / 'static'
        if static_output.exists():
            shutil.rmtree(static_output)
        shutil.copytree(static_dir, static_output)
        print(f"   ✅ Copied static files to {static_output}")

    # Generate CNAME file for GitHub Pages
    cname_file = output_dir / 'CNAME'
    with open(cname_file, 'w') as f:
        f.write(config.DOMAIN)
    print(f"📝 Generated CNAME file with domain: {config.DOMAIN}")

    print(f"\n✨ Site generation complete!")
    print(f"📂 Output directory: {output_dir.absolute()}")
    print(f"🌐 Open {output_dir.absolute()}/index.html in your browser to preview")


if __name__ == '__main__':
    generate_site()
