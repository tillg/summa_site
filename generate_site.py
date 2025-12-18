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


def validate_landing_page(frontmatter, filepath):
    """Validate landing page frontmatter has all required fields"""
    errors = []

    # Check required top-level fields
    required_fields = ['tagline', 'hero_description', 'cta_buttons', 'features', 'screenshots', 'contact_section']
    for field in required_fields:
        if field not in frontmatter:
            errors.append(f"Missing required field: '{field}'")

    # Validate cta_buttons
    if 'cta_buttons' in frontmatter:
        if not isinstance(frontmatter['cta_buttons'], list):
            errors.append("'cta_buttons' must be a list/array")
        elif len(frontmatter['cta_buttons']) == 0:
            errors.append("'cta_buttons' array cannot be empty")
        else:
            for i, button in enumerate(frontmatter['cta_buttons']):
                button_required = ['label', 'url', 'color', 'icon']
                for field in button_required:
                    if field not in button:
                        errors.append(f"cta_buttons[{i}] missing required field: '{field}'")

    # Validate features
    if 'features' in frontmatter:
        if not isinstance(frontmatter['features'], list):
            errors.append("'features' must be a list/array")
        elif len(frontmatter['features']) == 0:
            errors.append("'features' array cannot be empty")
        else:
            for i, feature in enumerate(frontmatter['features']):
                feature_required = ['title', 'description', 'icon', 'color']
                for field in feature_required:
                    if field not in feature:
                        errors.append(f"features[{i}] missing required field: '{field}'")

    # Validate screenshots
    if 'screenshots' in frontmatter:
        if not isinstance(frontmatter['screenshots'], list):
            errors.append("'screenshots' must be a list/array")
        elif len(frontmatter['screenshots']) == 0:
            errors.append("'screenshots' array cannot be empty - if the array is empty, this is a configuration error")
        else:
            for i, screenshot in enumerate(frontmatter['screenshots']):
                screenshot_required = ['image', 'alt']
                for field in screenshot_required:
                    if field not in screenshot:
                        errors.append(f"screenshots[{i}] missing required field: '{field}'")

    # Validate contact_section
    if 'contact_section' in frontmatter:
        if not isinstance(frontmatter['contact_section'], dict):
            errors.append("'contact_section' must be an object/dictionary")
        else:
            contact_required = ['title', 'description', 'email']
            for field in contact_required:
                if field not in frontmatter['contact_section']:
                    errors.append(f"contact_section missing required field: '{field}'")

    if errors:
        error_message = f"\n❌ Validation failed for {filepath}:\n"
        for error in errors:
            error_message += f"   • {error}\n"
        raise ValueError(error_message)

    print(f"   ✅ Validation passed for landing page")


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
        'google_analytics_id': config.GOOGLE_ANALYTICS_ID,
        'enable_analytics': config.ENABLE_ANALYTICS,
        'current_year': datetime.now().year,
        # Design system variables
        'brand_colors': config.BRAND_COLORS,
        'background_colors': config.BACKGROUND_COLORS,
        'text_colors': config.TEXT_COLORS,
        'border_colors': config.BORDER_COLORS,
        'font_sizes': config.FONT_SIZES,
        'font_weights': config.FONT_WEIGHTS,
        'spacing': config.SPACING,
        'icon_sizes': config.ICON_SIZES,
        'logo_sizes': config.LOGO_SIZES,
        'border_radius': config.BORDER_RADIUS,
        'shadows': config.SHADOWS,
        'button_styles': config.BUTTON_STYLES,
        'feature_card_styles': config.FEATURE_CARD_STYLES,
        'gradients': config.GRADIENTS,
        'tailwind_config': config.get_tailwind_config(),
    }

    # Process markdown files
    markdown_files = list(content_dir.glob('*.md'))
    print(f"📄 Found {len(markdown_files)} content files")

    for md_file in markdown_files:
        print(f"   Processing {md_file.name}...")
        frontmatter, html_content = parse_markdown_file(md_file)

        # Validate landing page (index.md) has required fields
        if md_file.stem == 'index' and frontmatter.get('template') == 'landing':
            validate_landing_page(frontmatter, md_file.name)

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
        # Pass all frontmatter to page context, with content added
        page_context = {
            **frontmatter,
            'content': html_content,
        }
        # Ensure title and description have defaults if not in frontmatter
        if 'title' not in page_context:
            page_context['title'] = config.SITE_NAME
        if 'description' not in page_context:
            page_context['description'] = config.SITE_DESCRIPTION

        context = {
            **template_context,
            'page': page_context
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
