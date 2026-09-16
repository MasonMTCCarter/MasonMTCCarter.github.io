# Little Wonder Paper Co.

A cheerful, hand-crafted website for Little Wonder Paper Co. — creators of coloring books, printable pages, and early-learning activities for kids ages 3–7.

**Live site:** [littlewonderpaperco.works](https://www.littlewonderpaperco.works)

---

## About This Site

Little Wonder Paper Co. specializes in:
- 🎨 **Coloring books** — cheerful paperback books featuring friendly animal characters
- 📄 **Printable coloring pages** — 40+ ready-to-print designs in PDF format
- 📚 **Early-learning workbooks** — letter tracing, vocabulary, and matching activities

The website showcases our products, highlights featured artwork, and provides a free downloadable coloring page.

---

## Tech Stack

- **Hosting:** GitHub Pages (published from `main` branch)
- **Static site generator:** Jekyll
- **Plugins:** jekyll-seo-tag, jekyll-sitemap
- **Styling:** Custom CSS (no frameworks)
- **Scripts:** Minimal JavaScript (consent management only)

---

## Project Structure

```
.
├── index.html              # Homepage (single-page site)
├── _config.yml             # Jekyll configuration
├── styles.css              # All site styling
├── consent.js              # Pinterest tracking consent logic
├── robots.txt              # SEO: search engine directives
├── CNAME                   # Custom domain configuration
├── _layouts/               # Jekyll layouts (if used)
├── assets/                 # Images, favicons, PDFs, downloads
│   ├── logo-*.webp         # Logo variants (WebP format)
│   ├── *-*.webp            # Character artwork (optimized images)
│   ├── favicon.png         # Favicon
│   ├── apple-touch-icon.png
│   ├── social-preview.jpg  # OpenGraph preview image
│   └── downloads/          # Free PDF downloads
├── scripts/                # Additional scripts (if any)
└── pinterest-*.html        # Pinterest verification file
```

---

## Key Features

### 1. Automatic Sitemap Generation
The repository uses Jekyll's `jekyll-sitemap` plugin to automatically generate `/sitemap.xml` from all published pages. The sitemap includes:
- Static HTML pages
- Canonical URL: `https://www.littlewonderpaperco.works`

**To exclude a page from the sitemap:**
Add this to the page's YAML front matter:
```yaml
sitemap: false
```

**Important:** Do not create a static `sitemap.xml` file — it would override automatic generation.

### 2. Search Engine Optimization
- **Plugins:** jekyll-seo-tag automatically injects meta tags (title, description, Open Graph, etc.)
- **robots.txt:** References the canonical sitemap URL
- **Social preview:** Open Graph image (`/assets/social-preview.jpg`) for link sharing

### 3. Privacy-First Tracking
Pinterest tracking is optional:
- **Consent dialog:** Displayed on first visit (in `consent.js`)
- **User choice:** Visitors can accept or reject tracking
- **Default:** Fully functional without tracking

### 4. Content Security Policy (CSP)
The homepage includes a restrictive CSP header that:
- Disallows inline scripts (except explicitly declared)
- Permits Pinterest scripts only from required origins
- Limits form submissions to same-origin
- Blocks object embeds and plugins

---

## Development & Deployment

### Local Development

1. **Install Jekyll:**
   ```bash
   gem install jekyll bundler
   ```

2. **Install dependencies:**
   ```bash
   bundle install
   ```

3. **Build and preview:**
   ```bash
   bundle exec jekyll serve
   ```
   Visit `http://localhost:4000` to preview changes.

### Deployment

GitHub Pages automatically publishes the site whenever you push to the `main` branch:
- ✅ Merges to `main` trigger an automatic build
- ✅ Site is published at `https://www.littlewonderpaperco.works` (via CNAME)
- ✅ CI/CD workflow verifies the build

**Never** commit broken changes to `main` — test locally first.

---

## File Guidelines

### Images
- **Format:** WebP (modern, optimized for web)
- **Responsive:** Use `srcset` for multiple sizes
- **Lazy loading:** Add `loading="lazy"` to off-screen images
- **Location:** `/assets/`

### Downloads
- **Format:** PDF
- **Location:** `/assets/downloads/`
- **Naming:** Descriptive, include format (e.g., `free-capybara-astronaut-us-letter.pdf`)

### External Links
- **Payhip** (product store): `https://payhip.com/LittleWonderPaperCo`
- **Classful** (workbooks): `https://classful.com/littlewonderpaperco/`
- **Amazon** (paperback): Use affiliate links with disclosure

---

## Content Guidelines

### Product Disclosures
Products featuring AI-generated artwork include this disclosure:
> "AI artwork disclosure: The animal illustrations in this product were generated using artificial intelligence (AI) and assembled into the finished product by Little Wonder Paper Co."

### Affiliate Disclosure
Amazon affiliate links include:
> "As an Amazon Associate I earn from qualifying purchases."

---

## Editing Tips

### Adding a New Product
1. Add product details to the relevant section in `index.html`
2. Link to external storefronts (Payhip, Classful, Amazon)
3. Include product preview image in `/assets/`
4. Add affiliate/AI disclosures as needed

### Updating Navigation
Edit the `<nav>` in the site header — it links to section IDs (`#products`, `#artwork`, `#about`).

### Changing Site Metadata
Edit `_config.yml`:
```yaml
title: Little Wonder Paper Co.
description: High-quality printables, digital art, and paper goods.
url: "https://www.littlewonderpaperco.works"
```

---

## Browser Support
- Modern browsers (Chrome, Firefox, Safari, Edge)
- Mobile-responsive (tested on iOS and Android)
- No dependencies on JavaScript frameworks

---

## Maintenance

### Regular Tasks
- ✅ Verify sitemap updates when pages are added/removed
- ✅ Test external links (Payhip, Classful, Amazon) quarterly
- ✅ Review analytics for traffic patterns and user behavior
- ✅ Check that Pinterest tracking consent works correctly

### Updates & Security
- Keep Jekyll and plugins updated
- Monitor GitHub security advisories for dependencies
- Test changes locally before pushing to `main`

---

## Questions?

For site-related inquiries, contact **hello@littlewonderpaperco.works**

---

**Last updated:** 2026
