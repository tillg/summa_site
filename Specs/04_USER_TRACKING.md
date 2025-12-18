# User Tracking

## Requirements

I would like to know about my users:

- How many are viewing my site?
- From which countries/regions
- What device
- Are they returning?
- How long do they watch a site
- Did they click on my call to action button

**Solution:** Google Analytics 4 (GA4)

**Why GA4:**

- Industry standard and most widely used
- Free for standard usage
- Covers all tracking requirements automatically
- Easy integration (single script tag)
- No maintenance or self-hosting required

**Privacy Considerations:**

- IP anonymization enabled by default in GA4
- Configure shorter data retention period (2-6 months)
- May require cookie consent banner for EU users (GDPR)
- 25-40% of users with ad blockers won't be tracked (acceptable limitation)

---

## Implementation Plan

### Step 1: Create GA4 Property - Done

- Sign up for Google Analytics at analytics.google.com
- Create new GA4 property for summarum.app
- Get tracking ID (format: G-XXXXXXXXXX)
- Configure data retention period (recommend 2-6 months)
- Disable personalized advertising features for privacy

Did it, this is the Google tag snippet that was created:

```html
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-CYN3HPDLCG"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-CYN3HPDLCG');
</script>
```

### Step 2: Update Configuration - Done

### Step 3: Add Tracking Script to Template - Done

### Step 4: Add CTA Button Tracking - Done

### Step 5: Configuration - Done

**Implementation completed!**

All tracking code has been integrated:
- GA4 tracking script added to templates/base.html
- Event tracking added to CTA buttons in landing page
- Analytics always enabled for all builds
- Verified working correctly

To build and deploy, simply run: `python generate_site.py`

---

## Original Implementation Notes

### Step 3: Add Tracking Script to Template (Original Plan)

Insert GA4 tracking code in the `<head>` section of `templates/base.html`:

```html
{% if config.ENABLE_ANALYTICS and config.GOOGLE_ANALYTICS_ID %}
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id={{ config.GOOGLE_ANALYTICS_ID }}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', '{{ config.GOOGLE_ANALYTICS_ID }}', {
    'anonymize_ip': true,
    'cookie_flags': 'SameSite=None;Secure'
  });
</script>
{% endif %}
```

**What This Tracks Automatically:**

- Page views
- Geographic location (country/region)
- Device type and OS
- Session duration
- Returning vs. new visitors

### Step 4: Add CTA Button Tracking

Add event tracking to CTA buttons in your templates:

```html
<!-- App Store Download Button -->
<a href="[App Store URL]"
   class="cta-button"
   onclick="gtag('event', 'cta_click', {
     'event_category': 'engagement',
     'event_label': 'app_store_download'
   });">
  Download on App Store
</a>

<!-- TestFlight Link -->
<a href="[TestFlight URL]"
   class="cta-button"
   onclick="gtag('event', 'cta_click', {
     'event_category': 'engagement',
     'event_label': 'testflight_signup'
   });">
  Join TestFlight
</a>
```

### Step 5: Configuration

Final configuration in `config.py`:

```python
# Google Analytics
GOOGLE_ANALYTICS_ID = "G-CYN3HPDLCG"
ENABLE_ANALYTICS = True
```

Analytics are always enabled for simplicity. All builds will include tracking.

---

## Testing & Verification

### Local Testing

1. Build the site: `python generate_site.py`
2. Start development server: `python dev_server.py`
3. Open browser to `http://localhost:8000`
4. Open browser DevTools → Network tab
5. Verify `gtag/js` script loads successfully
6. Check browser console for any errors
7. Click CTA buttons and verify events fire in console (if debug mode enabled)

### Production Testing

After deploying to GitHub Pages:

1. Visit summarum.app
2. Open browser DevTools → Network tab
3. Verify `gtag/js` script loads successfully
4. Navigate to GA4 dashboard (may take 24-48 hours for first data)
5. Test CTA button clicks and verify events appear in Real-time reports
6. Check that geographic and device data is being collected

---

## Privacy Policy Update

**REQUIRED:** Update privacy policy to disclose analytics usage. Include:

- What data is collected (page views, location, device type, interactions)
- Purpose (understand user behavior, improve website)
- Third-party service (Google Analytics)
- Data retention period (2-6 months)
- User rights and opt-out options
- Link to Google's privacy policy

---

## Questions to Resolve

1. **Cookie Consent Banner**
   - Do we need a cookie consent banner for EU users?
   - If yes, implement before enabling GA4

2. **CTA Tracking Scope**
   - Which specific buttons/links should be tracked?
   - Current list: App Store button, TestFlight link
   - Any other interactions to track?

3. **Dashboard Access**
   - Who needs access to the GA4 dashboard?
   - Set up Google account permissions

4. **Data Retention**
   - Confirm data retention period (recommend 2-6 months)
   - Configure in GA4 property settings

---

## Implementation Checklist

- [ ] Answer open questions (cookie consent, CTA scope, dashboard access)
- [ ] Create GA4 property and get tracking ID
- [ ] Update `config.py` with GA4 ID and environment detection
- [ ] Add GA4 tracking script to `templates/base.html`
- [ ] Add event tracking to CTA buttons
- [ ] Update privacy policy with analytics disclosure
- [ ] Test locally (verify analytics disabled in dev)
- [ ] Deploy to GitHub Pages
- [ ] Verify tracking in production (check GA4 Real-time reports)
- [ ] Set up dashboard access for stakeholders

---

## Resources

- [GA4 Setup Guide](https://support.google.com/analytics/answer/9304153)
- [GA4 Event Tracking](https://developers.google.com/analytics/devguides/collection/ga4/events)
- [GDPR Compliance for GA4](https://support.google.com/analytics/answer/9019185)
