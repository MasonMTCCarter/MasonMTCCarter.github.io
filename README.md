# Little Wonder Paper Co.

GitHub Pages publishes this site from the root of `main`.

## Sitemap

The repository enables GitHub Pages' supported `jekyll-sitemap` plugin. It generates `/sitemap.xml` from the published pages, including static HTML, using the canonical `https://www.littlewonderpaperco.works` origin. Adding or removing a page updates the sitemap in the same build; no separate URL list needs maintenance. The repository verification workflow builds the site and checks the generated sitemap and `robots.txt` reference.

For a Jekyll page that should not appear in the sitemap, set `sitemap: false` in its YAML front matter. Keep drafts unpublished. Do not add a static `sitemap.xml`, which would override automatic generation.

`robots.txt` references the canonical `https://www.littlewonderpaperco.works/sitemap.xml` URL.

## Third-party scripts

Payhip purchases use ordinary HTTPS links rather than a third-party checkout
script. Pinterest tracking is loaded only after visitors explicitly accept it.
The homepage includes a restrictive Content Security Policy that limits script
execution and Pinterest network access to the required origins.
