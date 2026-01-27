# DEPRECATED - Summarum Website

> **This repository has been deprecated and split into separate repos.**

## New Repositories

| Repository | Purpose | URL |
|------------|---------|-----|
| **tills-static-site-generator** | Generator code & templates | https://github.com/tillg/tills-static-site-generator |
| **summarum.app** | Content for summarum.app | https://github.com/tillg/summarum.app |
| **frechen.bayern** | Content for frechen.bayern | https://github.com/tillg/frechen.bayern |

## Why the split?

The original `summa_site` repo contained both the static site generator and the content for summarum.app. This has been refactored into:

1. **A reusable generator** that can power multiple sites
2. **Separate content repos** for each site, with their own configs and themes

This allows:
- Multiple sites to share the same generator code
- Independent content updates without touching generator code
- Different themes (dark for summarum.app, white for frechen.bayern)
- Cleaner CI/CD with GitHub Actions

## Migration

If you have local changes or forks:

1. Generator code (`generate_site.py`, `dev_server.py`, `templates/`) → moved to `tills-static-site-generator`
2. Content (`content/`, `static/`, `config.py`) → moved to `summarum.app`

---

*This repo is archived for historical reference only. Please use the new repositories above.*
