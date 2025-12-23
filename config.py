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
SITE_TAGLINE = "Your Data, your Way"
SITE_DESCRIPTION = "Track any number you care about - from bank balances and stock portfolios to car mileage and personal metrics - in one place."
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
