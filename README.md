# P'Wayz Happy Binz

Static marketing website for P'Wayz Happy Binz, a residential trash bin cleaning service
serving Arcola, Missouri City, Manvel, Rosharon and Fresno, Texas.

Tagline: "We clean the funk out ya binz."

## Local preview

Run any static web server from the project root, for example:

```powershell
python -m http.server 4173
```

Then open `http://localhost:4173`.

## Deployment

The site auto-deploys to Netlify from the `main` branch of this repository.
The publish directory is the repository root and no build command is required.

Form submissions appear in the Netlify dashboard under **Forms → service-request**.

## Assets

- `logo.png` is the full logo with the tagline, background removed.
- `logo-nav.png` is the same logo with the tagline cropped off. It is the one
  used in the header and footer, because the tagline is unreadable at nav size.
- `trailer.jpg` is a real photo of the business's Jeep and wrapped trailer.
- There are no stock photos and no external image dependencies.
- Do not put flyer artwork on the site. Flyers are reference for copy and pricing only.

The logo wordmark is white, so any surface it sits on must stay dark. That is why
the header is purple rather than white.

## Cache busting

`styles.css` and `script.js` are referenced with a `?v=N` query string. Bump that
number in `index.html` and `thank-you.html` whenever either file changes, so
returning visitors do not get a stale copy.
