# Aurebesh Font Pipeline

Converts a curated set of Aurebesh fonts from OTF to WOFF2 for web use, and publishes them as a GitHub release.

## Fonts included

| Font | Role | Source |
|---|---|---|
| AB Equinox | Display / headings | [AurekFonts](https://aurekfonts.github.io/?font=ABEquinox) |
| AurebeshAF Canon | Body / UI text | [AurekFonts](https://aurekfonts.github.io/?font=AurebeshAF) |
| AurebeshAF Legends | Body / UI text (Legends variant) | [AurekFonts](https://aurekfonts.github.io/?font=AurebeshAF) |
| Aurebesh Red Regular | Monospaced / code | [AurekFonts](https://aurekfonts.github.io/?font=AurebeshRed) |
| Aurebesh Red Bold | Monospaced / code (bold) | [AurekFonts](https://aurekfonts.github.io/?font=AurebeshRed) |

All original fonts are sourced from [AurekFonts](https://aurekfonts.github.io/), an archive of Star Wars universe fonts. Credits and licenses belong to their respective authors.

## Using the fonts

Download the latest WOFF2 files from the [Releases](../../releases/latest) page. No build step required.

## Releasing a new version

1. Add or update OTF files in `src/`
2. Commit and push to `main`
3. Tag the commit with a version number:
   ```bash
   git tag v1.0.0
   git push origin v1.0.0
   ```

The GitHub Actions workflow will convert the fonts and publish a release with the WOFF2 files attached automatically.

## Running locally

Requires Python 3 and the `fonttools` and `brotli` packages:

```bash
pip install fonttools brotli
python convert.py
```

Output is written to `dist/`.
