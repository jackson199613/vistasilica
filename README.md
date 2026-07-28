# Vistasilica — Website

Official site for Vistasilica, a Vista brand for cross-track silica ingredient solutions. Pure static site (HTML / CSS / JS), no build step, deployable directly to Netlify. English.

## Structure

```
/
├── index.html              Home
├── contact.html            Contact (inquiry form + regional contacts)
├── solutions/              Six solutions (overview + 6 detail pages + dual nav)
├── resources/              Selector / Download Center / Quality / Whitepapers+FAQ / Sample request
├── company/                About / Global Presence / Customer Proof / News
├── legal/                  Privacy / Cookie / Compliance (GDPR) / Terms
├── css/style.css           Global styles (design tokens + components)
├── js/main.js              Nav / FAQ / forms / interactions
├── assets/img/             Logo and assets
├── robots.txt              Allows standard + AI crawlers (good for GEO)
├── sitemap.xml             Sitemap
└── netlify.toml            Netlify config (caching / security headers)
```

> `_build/` holds the Python page generators — for maintenance only, not required for deployment. Keep or delete.

## Deployment (GitHub → Netlify)

1. **Save to a GitHub repo**
   ```bash
   git init
   git add .
   git commit -m "Vistasilica site"
   git branch -M main
   git remote add origin https://github.com/<you>/vistachem.git
   git push -u origin main
   ```

2. **Connect the repo on Netlify**
   - Netlify → Add new site → Import an existing project
   - Choose GitHub, authorize and pick the repo
   - Leave Build command empty; set Publish directory to `.`
   - Deploy site

3. **Add the domain vistasilica.com**
   - Netlify → Domain settings → Add custom domain → `vistasilica.com`
   - Configure DNS as prompted; Netlify issues SSL (HTTPS) automatically

4. **Updates**: push to `main` and Netlify redeploys automatically.

## To wire up later (placeholders ready)

- Forms: currently demo submissions. Add Netlify Forms (add the `netlify` attribute to each `<form>`) or a third-party form / CRM.
- Analytics: drop in Google Analytics / Search Console tags.
- Live chat: a WhatsApp float is in place; swap in a live-chat script if needed.
- Real imagery: replace placeholders for factory photos, exhibition photos, customer logos, etc.
