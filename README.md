# Little Wonder Paper Co.

GitHub Pages publishes this site from the root of `main`.

## Sitemap

GitHub Pages runs `jekyll-sitemap` on every publication. It generates `/sitemap.xml` from the published pages, including static HTML, using the canonical `https://www.littlewonderpaperco.works` origin. Adding or removing a page updates the sitemap in the same build; no separate URL list needs maintenance.

For a Jekyll page that should not appear in the sitemap, set `sitemap: false` in its YAML front matter. Keep drafts unpublished. Do not add a static `sitemap.xml`, which would override automatic generation.

`robots.txt` references the requested apex-domain sitemap URL, which follows the site's existing redirect to the canonical www host.
