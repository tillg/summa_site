"""
Configuration for Summarum website
"""

from design_variables import (
    BRAND_COLORS,
    BACKGROUND_COLORS,
    TEXT_COLORS,
    BORDER_COLORS,
    FONT_SIZES,
    FONT_WEIGHTS,
    SPACING,
    ICON_SIZES,
    LOGO_SIZES,
    BORDER_RADIUS,
    SHADOWS,
    BUTTON_STYLES,
    FEATURE_CARD_STYLES,
    GRADIENTS,
    get_tailwind_config,
)

# Site metadata
SITE_NAME = "Summarum"
SITE_TAGLINE = "Your Financial Overview, Simplified"
SITE_DESCRIPTION = "Keep track of your wealth across multiple bank accounts, stock accounts and other value stores. Dead simple, no API integration, simple, manual updates."
DOMAIN = "summarum.app"

# Directories
CONTENT_DIR = "content"
TEMPLATE_DIR = "templates"
STATIC_DIR = "static"
OUTPUT_DIR = "docs"

# Contact
CONTACT_EMAIL = "till.gartner@gmail.com"

# App Store links (placeholders for now)
TESTFLIGHT_LINK = "#"  # TODO: Add TestFlight link when available
MACOS_DOWNLOAD_LINK = "#"  # TODO: Add macOS download link when available

# Analytics
UMAMI_WEBSITE_ID = ""  # TODO: Add Umami website ID after setup
UMAMI_SCRIPT_URL = ""  # TODO: Add Umami script URL after setup
