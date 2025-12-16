"""
Design System Variables for Summarum Website

This file centralizes all design tokens including colors, typography, spacing,
sizes, and other design-related values used throughout the site.
"""

# =============================================================================
# COLORS
# =============================================================================

# Brand Colors (extracted from logo)
BRAND_COLORS = {
    "orange": "#f4a261",
    "yellow": "#f9b94a",
    "coral": "#e76f6f",
}

# Background Colors
BACKGROUND_COLORS = {
    "primary": "#000000",      # black
    "secondary": "#111827",    # gray-900
    "tertiary": "#1f2937",     # gray-800
}

# Text Colors
TEXT_COLORS = {
    "primary": "#ffffff",      # white
    "secondary": "#d1d5db",    # gray-300
    "tertiary": "#9ca3af",     # gray-400
    "muted": "#374151",        # gray-700
    "dark": "#000000",         # black (for text on light backgrounds)
}

# Border Colors
BORDER_COLORS = {
    "primary": "#1f2937",      # gray-800
}

# Gradient Combinations
GRADIENTS = {
    "brand_primary": f"linear-gradient(to right, {BRAND_COLORS['orange']}, {BRAND_COLORS['yellow']}, {BRAND_COLORS['coral']})",
    "brand_secondary": f"linear-gradient(to right, {BRAND_COLORS['orange']}, {BRAND_COLORS['yellow']})",
    "brand_tertiary": f"linear-gradient(to right, {BRAND_COLORS['yellow']}, {BRAND_COLORS['coral']})",
    "brand_accent": f"linear-gradient(to right, {BRAND_COLORS['coral']}, {BRAND_COLORS['orange']})",
}

# =============================================================================
# TYPOGRAPHY
# =============================================================================

# Font Families
FONT_FAMILIES = {
    "sans": "ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif",
    "mono": "ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace",
}

# Font Sizes (in rem units for accessibility)
FONT_SIZES = {
    "xs": "0.75rem",      # 12px
    "sm": "0.875rem",     # 14px
    "base": "1rem",       # 16px
    "lg": "1.125rem",     # 18px
    "xl": "1.25rem",      # 20px
    "2xl": "1.5rem",      # 24px
    "3xl": "1.875rem",    # 30px
    "4xl": "2.25rem",     # 36px
    "5xl": "3rem",        # 48px
    "6xl": "3.75rem",     # 60px
}

# Font Weights
FONT_WEIGHTS = {
    "normal": "400",
    "medium": "500",
    "semibold": "600",
    "bold": "700",
}

# Line Heights
LINE_HEIGHTS = {
    "tight": "1.25",
    "normal": "1.5",
    "relaxed": "1.75",
}

# =============================================================================
# SPACING & SIZING
# =============================================================================

# Spacing Scale (in rem units)
SPACING = {
    "0": "0",
    "1": "0.25rem",    # 4px
    "2": "0.5rem",     # 8px
    "3": "0.75rem",    # 12px
    "4": "1rem",       # 16px
    "6": "1.5rem",     # 24px
    "8": "2rem",       # 32px
    "12": "3rem",      # 48px
    "16": "4rem",      # 64px
    "20": "5rem",      # 80px
}

# Icon Sizes
ICON_SIZES = {
    "sm": "1rem",      # 16px - w-4 h-4
    "md": "1.5rem",    # 24px - w-6 h-6
    "lg": "2rem",      # 32px - w-8 h-8
    "xl": "2.5rem",    # 40px - w-10 h-10
    "2xl": "3rem",     # 48px - w-12 h-12
    "3xl": "8rem",     # 128px - w-32 h-32
}

# Logo Sizes
LOGO_SIZES = {
    "nav": "2.5rem",   # 40px - h-10
    "footer": "2rem",  # 32px - h-8
    "hero": "8rem",    # 128px - h-32
}

# Container Max Widths
CONTAINER_MAX_WIDTHS = {
    "7xl": "80rem",    # 1280px - max-w-7xl
    "3xl": "48rem",    # 768px - max-w-3xl
}

# =============================================================================
# LAYOUT
# =============================================================================

# Navigation
NAVIGATION = {
    "height": "4rem",           # 64px - h-16
    "padding_x": "1rem",        # px-4
    "padding_x_md": "1.5rem",   # sm:px-6
    "padding_x_lg": "2rem",     # lg:px-8
}

# Sections
SECTION_PADDING = {
    "y": "5rem",        # 80px - py-20
    "x": "1rem",        # 16px - px-4
    "x_md": "1.5rem",   # 24px - sm:px-6
    "x_lg": "2rem",     # 32px - lg:px-8
}

# Cards/Panels
CARD_PADDING = {
    "default": "2rem",  # 32px - p-8
    "large": "3rem",    # 48px - p-12
}

# =============================================================================
# BORDERS & DECORATIONS
# =============================================================================

# Border Radius
BORDER_RADIUS = {
    "none": "0",
    "sm": "0.125rem",   # 2px
    "default": "0.25rem",   # 4px - rounded
    "md": "0.375rem",   # 6px
    "lg": "0.5rem",     # 8px - rounded-lg
    "xl": "0.75rem",    # 12px
    "full": "9999px",   # rounded-full
}

# Border Widths
BORDER_WIDTHS = {
    "default": "1px",
    "2": "2px",
}

# Shadow Styles
SHADOWS = {
    "sm": "0 1px 2px 0 rgba(0, 0, 0, 0.05)",
    "default": "0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px 0 rgba(0, 0, 0, 0.06)",
    "md": "0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
    "lg": "0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)",
    "xl": "0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04)",
}

# =============================================================================
# TRANSITIONS & ANIMATIONS
# =============================================================================

# Transition Durations
TRANSITION_DURATIONS = {
    "fast": "150ms",
    "normal": "200ms",
    "slow": "300ms",
}

# Transition Timing Functions
TRANSITION_TIMING = {
    "ease": "cubic-bezier(0.4, 0, 0.2, 1)",
    "ease_in": "cubic-bezier(0.4, 0, 1, 1)",
    "ease_out": "cubic-bezier(0, 0, 0.2, 1)",
    "ease_in_out": "cubic-bezier(0.4, 0, 0.2, 1)",
}

# Transform Scales (for hover effects)
TRANSFORM_SCALES = {
    "hover": "1.05",
}

# =============================================================================
# COMPONENT-SPECIFIC STYLES
# =============================================================================

# Buttons
BUTTON_STYLES = {
    "padding_x": "2rem",        # 32px - px-8
    "padding_y": "0.75rem",     # 12px - py-3
    "font_weight": FONT_WEIGHTS["semibold"],
    "border_radius": BORDER_RADIUS["lg"],
    "shadow": SHADOWS["lg"],
    "transition": f"all {TRANSITION_DURATIONS['normal']} {TRANSITION_TIMING['ease']}",
    "hover_scale": TRANSFORM_SCALES["hover"],
}

# Feature Cards
FEATURE_CARD_STYLES = {
    "padding": CARD_PADDING["default"],
    "border_radius": BORDER_RADIUS["lg"],
    "border_width": BORDER_WIDTHS["default"],
    "border_color": BORDER_COLORS["primary"],
    "background": BACKGROUND_COLORS["primary"],
    "icon_size": ICON_SIZES["2xl"],
    "icon_padding": "0.75rem",  # 12px - inside 3rem container
}

# Grid Layouts
GRID_LAYOUTS = {
    "features": {
        "columns": "1",           # Default mobile
        "columns_md": "3",        # Desktop
        "gap": "2rem",            # 32px - gap-8
    }
}

# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def get_css_variables():
    """
    Generate CSS custom properties from design variables.
    Returns a dictionary of CSS variable names and values.
    """
    css_vars = {}

    # Brand colors
    for name, color in BRAND_COLORS.items():
        css_vars[f"--color-brand-{name}"] = color

    # Background colors
    for name, color in BACKGROUND_COLORS.items():
        css_vars[f"--color-bg-{name}"] = color

    # Text colors
    for name, color in TEXT_COLORS.items():
        css_vars[f"--color-text-{name}"] = color

    # Border colors
    for name, color in BORDER_COLORS.items():
        css_vars[f"--color-border-{name}"] = color

    # Font sizes
    for name, size in FONT_SIZES.items():
        css_vars[f"--font-size-{name}"] = size

    # Spacing
    for name, size in SPACING.items():
        css_vars[f"--spacing-{name}"] = size

    # Border radius
    for name, radius in BORDER_RADIUS.items():
        css_vars[f"--radius-{name}"] = radius

    return css_vars


def get_tailwind_config():
    """
    Generate Tailwind CSS configuration object for extending theme.
    Returns a dictionary that can be serialized to JSON for Tailwind config.
    """
    return {
        "colors": {
            "brand-orange": BRAND_COLORS["orange"],
            "brand-yellow": BRAND_COLORS["yellow"],
            "brand-coral": BRAND_COLORS["coral"],
        },
        "fontFamily": {
            "sans": FONT_FAMILIES["sans"].split(", "),
            "mono": FONT_FAMILIES["mono"].split(", "),
        }
    }
