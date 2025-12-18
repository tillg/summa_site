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

# App Links
TESTFLIGHT_LINK = ""  # Add TestFlight URL here
MACOS_DOWNLOAD_LINK = ""  # Add macOS download URL here

# Google Analytics
GOOGLE_ANALYTICS_ID = "G-CYN3HPDLCG"
ENABLE_ANALYTICS = True
