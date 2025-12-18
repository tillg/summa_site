#!/usr/bin/env python3
"""
App Icon Generator for Summarum

Generates all required iOS, iPadOS, and macOS app icon sizes from the logo design.
Creates an AppIcon.appiconset directory with all sizes and Contents.json for Xcode.

This script uses pure Python (Pillow) to recreate the logo at different sizes,
avoiding the need for system-level SVG rendering libraries.

Usage:
    python3 generate_icons.py
"""

import os
import json
import shutil
from pathlib import Path
from PIL import Image, ImageDraw

# Icon size specifications
# Format: (base_size, scale, idiom, role)
# base_size: base dimension (e.g., 20 for 20x20)
# scale: @1x, @2x, or @3x
# idiom: iphone, ipad, ios-marketing, or mac
# role: None for app icons, or specific role like "notificationCenter"

ICON_SPECIFICATIONS = [
    # iPhone - App Icon
    {"size": "60x60", "scale": "2x", "idiom": "iphone"},
    {"size": "60x60", "scale": "3x", "idiom": "iphone"},

    # iPhone - Spotlight & Settings
    {"size": "40x40", "scale": "2x", "idiom": "iphone"},
    {"size": "40x40", "scale": "3x", "idiom": "iphone"},
    {"size": "29x29", "scale": "2x", "idiom": "iphone"},
    {"size": "29x29", "scale": "3x", "idiom": "iphone"},

    # iPhone - Notifications
    {"size": "20x20", "scale": "2x", "idiom": "iphone"},
    {"size": "20x20", "scale": "3x", "idiom": "iphone"},

    # iPad - App Icon
    {"size": "76x76", "scale": "1x", "idiom": "ipad"},
    {"size": "76x76", "scale": "2x", "idiom": "ipad"},

    # iPad Pro - App Icon
    {"size": "83.5x83.5", "scale": "2x", "idiom": "ipad"},

    # iPad - Spotlight
    {"size": "40x40", "scale": "1x", "idiom": "ipad"},
    {"size": "40x40", "scale": "2x", "idiom": "ipad"},

    # iPad - Settings
    {"size": "29x29", "scale": "1x", "idiom": "ipad"},
    {"size": "29x29", "scale": "2x", "idiom": "ipad"},

    # iPad - Notifications
    {"size": "20x20", "scale": "1x", "idiom": "ipad"},
    {"size": "20x20", "scale": "2x", "idiom": "ipad"},

    # Mac - App Icon
    {"size": "512x512", "scale": "1x", "idiom": "mac"},
    {"size": "512x512", "scale": "2x", "idiom": "mac"},
    {"size": "256x256", "scale": "1x", "idiom": "mac"},
    {"size": "256x256", "scale": "2x", "idiom": "mac"},
    {"size": "128x128", "scale": "1x", "idiom": "mac"},
    {"size": "128x128", "scale": "2x", "idiom": "mac"},
    {"size": "32x32", "scale": "1x", "idiom": "mac"},
    {"size": "32x32", "scale": "2x", "idiom": "mac"},
    {"size": "16x16", "scale": "1x", "idiom": "mac"},
    {"size": "16x16", "scale": "2x", "idiom": "mac"},

    # App Store / Marketing
    {"size": "1024x1024", "scale": "1x", "idiom": "ios-marketing"},
]


def parse_size(size_str):
    """Parse size string like '60x60' into integer pixel dimensions."""
    parts = size_str.split('x')
    return int(float(parts[0])), int(float(parts[1]))


def parse_scale(scale_str):
    """Parse scale string like '2x' into integer multiplier."""
    return int(scale_str.replace('x', ''))


def get_pixel_size(size_str, scale_str):
    """Calculate actual pixel size from base size and scale."""
    base_width, base_height = parse_size(size_str)
    scale = parse_scale(scale_str)
    return base_width * scale, base_height * scale


def generate_filename(spec):
    """Generate filename for an icon based on specification."""
    size = spec['size'].replace('.', '_')  # Handle 83.5x83.5
    scale = spec['scale']
    return f"icon_{size}@{scale}.png"


def draw_logo(size):
    """
    Draw the Summarum logo at specified size using Pillow.

    The logo consists of:
    - Dark gray background (#2A2A2A)
    - Three rounded rectangles with brand colors

    Args:
        size: Tuple of (width, height) in pixels

    Returns:
        PIL Image object
    """
    width, height = size

    # Create image with gray background
    img = Image.new('RGB', (width, height), '#2A2A2A')
    draw = ImageDraw.Draw(img)

    # Brand colors (from logo.svg)
    colors = [
        '#FB923C',  # Orange
        '#F59E0B',  # Yellow/Amber
        '#EF4444',  # Red/Coral
    ]

    # Calculate proportions based on original 180x180 SVG
    # Original bars: x=40, width=100, heights=26, y positions: 41, 77, 112
    scale = width / 180.0

    bar_x = int(40 * scale)
    bar_width = int(100 * scale)
    bar_height = int(26 * scale)
    bar_y_positions = [int(41 * scale), int(77 * scale), int(112 * scale)]
    corner_radius = int(13 * scale)  # rx/ry in SVG

    # Draw each colored bar
    for i, (color, y_pos) in enumerate(zip(colors, bar_y_positions)):
        bbox = [
            bar_x,
            y_pos,
            bar_x + bar_width,
            y_pos + bar_height
        ]
        draw.rounded_rectangle(bbox, radius=corner_radius, fill=color)

    return img


def generate_icon(output_path, width, height):
    """
    Generate an app icon at specified dimensions.

    Args:
        output_path: Path for output PNG file
        width: Target width in pixels
        height: Target height in pixels
    """
    img = draw_logo((width, height))
    img.save(output_path, 'PNG')


def create_contents_json(icon_specs, output_dir):
    """
    Generate Contents.json file for Xcode AppIcon.appiconset.

    Args:
        icon_specs: List of icon specifications
        output_dir: Directory where Contents.json will be written
    """
    images = []

    for spec in icon_specs:
        image_entry = {
            "filename": generate_filename(spec),
            "idiom": spec['idiom'],
            "scale": spec['scale'],
            "size": spec['size']
        }
        images.append(image_entry)

    contents = {
        "images": images,
        "info": {
            "author": "xcode",
            "version": 1
        }
    }

    contents_path = output_dir / "Contents.json"
    with open(contents_path, 'w', encoding='utf-8') as f:
        json.dump(contents, f, indent=2)

    return contents_path


def generate_all_icons(output_dir, icon_specs):
    """
    Generate all app icons.

    Args:
        output_dir: Directory for output (AppIcon.appiconset)
        icon_specs: List of icon specifications to generate

    Returns:
        Number of icons generated
    """
    # Create output directory
    output_dir.mkdir(parents=True, exist_ok=True)

    # Generate each icon
    icons_generated = 0

    for spec in icon_specs:
        # Calculate pixel dimensions
        width, height = get_pixel_size(spec['size'], spec['scale'])

        # Generate filename
        filename = generate_filename(spec)
        output_path = output_dir / filename

        # Generate icon
        try:
            generate_icon(output_path, width, height)
            print(f"   ✅ {filename} ({width}x{height}px)")
            icons_generated += 1
        except Exception as e:
            print(f"   ❌ Failed to generate {filename}: {e}")

    return icons_generated


def main():
    """Main entry point for icon generation."""
    print("\n" + "="*60)
    print("  Summarum App Icon Generator")
    print("="*60 + "\n")

    # Paths
    svg_path = Path("logo/logo.svg")
    output_dir = Path("logo/AppIcon.appiconset")

    # Verify SVG exists
    if not svg_path.exists():
        print(f"❌ Error: SVG file not found at {svg_path}")
        print("   Please ensure logo/logo.svg exists.")
        return 1

    print(f"📄 Source: {svg_path}")
    print(f"📂 Output: {output_dir}/")
    print()

    # Clean output directory if it exists
    if output_dir.exists():
        print("🧹 Cleaning existing output directory...")
        shutil.rmtree(output_dir)

    # Generate icons
    print(f"🎨 Generating {len(ICON_SPECIFICATIONS)} icon sizes...\n")

    icons_generated = generate_all_icons(
        output_dir,
        ICON_SPECIFICATIONS
    )

    # Generate Contents.json
    print("\n📝 Generating Contents.json for Xcode...")
    contents_path = create_contents_json(ICON_SPECIFICATIONS, output_dir)
    print(f"   ✅ {contents_path}")

    # Summary
    print("\n" + "="*60)
    print(f"✨ Complete! Generated {icons_generated} app icons")
    print(f"📂 Location: {output_dir.absolute()}")
    print("\n📱 To use in Xcode:")
    print(f"   1. Open your Xcode project")
    print(f"   2. Select your app target")
    print(f"   3. Go to 'App Icons and Launch Screen'")
    print(f"   4. Drag {output_dir.name}/ into the App Icon source")
    print("="*60 + "\n")

    return 0


if __name__ == "__main__":
    exit(main())
