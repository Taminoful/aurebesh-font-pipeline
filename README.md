# Aurebesh Font Pipeline

Converts commercially-free Star Wars Aurebesh fonts from OTF/TTF to WOFF2 for web use, and publishes them as a GitHub release.

All fonts are sourced from [AurekFonts](https://aurekfonts.github.io/), an archive of Star Wars universe fonts. Credits and licenses belong to their respective authors. See [LICENSE](LICENSE) for details.

## Downloading the fonts

Grab the latest WOFF2 files from the [Releases](../../releases/latest) page. No build step required.

Each release includes:
- Individual WOFF2 files for every font
- Family zip bundles for multi-variant fonts
- `all-fonts.zip` containing every WOFF2 in one download

## Fonts included

All 65 fonts are free for personal and commercial use.

### Aurebesh

| Bundle | Variants | Source |
|---|---|---|
| `AurebeshAF.zip` | Canon, CanonTech, Legends, LegendsTech | [AurebeshAF](https://aurekfonts.github.io/?font=AurebeshAF) |
| `Aurebesh-PixelSagas.zip` | Regular, Bold, Italic, Bold Italic, + Condensed variants | [Aurebesh (Pixel Sagas)](https://aurekfonts.github.io/?font=AurebeshPixelSagas) |
| `Aurebesh-Cantina.zip` | Regular, Bold, Italic, Bold Italic | [Aurebesh Cantina](https://aurekfonts.github.io/?font=AurebeshCantina) |
| `Auraboo.zip` | Regular | [Auraboo](https://aurekfonts.github.io/?font=Auraboo) |
| `NewAurabesh.zip` | Regular | [New Aurabesh](https://aurekfonts.github.io/?font=NewAurabesh) |
| Individual | AB Equinox, Aurebesh (AURABESH), Aurebesh Droid, Aurebesh English, Aurebesh Bloops AF, Aurebesh LU, Aurebesh (Pixel Sagas 2000), DroidobeshDepot, ImperialBroadcast87, SGAurebesh | Various |

### Mandalorian

| Bundle | Variants | Source |
|---|---|---|
| `MandoAF.zip` | Regular, Classic | [Mando AF](https://aurekfonts.github.io/?font=MandoAF) |
| Individual | Mando AlbansBane | [AurekFonts](https://aurekfonts.github.io/) |

### Other scripts

| Bundle | Variants | Source |
|---|---|---|
| `Aurek-Besh.zip` | Regular, Narrow | [Aurek-Besh](https://aurekfonts.github.io/?font=AurekBesh) |
| `Aurek-Besh-Hand.zip` | Hand | [Aurek-Besh Hand](https://aurekfonts.github.io/?font=AurekBeshHand) |
| `KyberCrystalDisplay.zip` | Aurebesh, Alphabet | [Kyber Crystal Display](https://aurekfonts.github.io/?font=KCDAurebesh) |
| `Protobesh.zip` | Coremaic, Square | [Protobesh](https://aurekfonts.github.io/?font=Protobesh) |
| `ProtobeshAF.zip` | Regular | [Protobesh AF](https://aurekfonts.github.io/?font=ProtobeshAF) |
| `Goongan-AF.zip` | Alphabet, Syllabics | [Goongan AF](https://aurekfonts.github.io/?font=GoonganAFAlpha) |
| `Ur-Kittat.zip` | Regular, LU variant | [Ur-Kittat](https://aurekfonts.github.io/?font=UrKittat) |
| `OldTongue.zip` | Old Tongue, Old Tongue Yavin | [AurekFonts](https://aurekfonts.github.io/) |
| `SkyLuke.zip` | Regular | [SkyLuke](https://aurekfonts.github.io/?font=SkyLuke) |
| `UbeseBoushh.zip` | Regular | [Ubese Boushh](https://aurekfonts.github.io/?font=UbeseBoushh) |
| Individual | Ithorian AF, Kitisakkullian, Lapti Nek AF, Life Day AF, Maulobesh, MB450, Naboo AF, Nirvanabesh, Outer Rim AF, Prime Jedi, Remember Kamino, S-Foil, Sith AF, Skyhook, TF Gunray, Umbara AF, Umbaran ST, Veers Numeric | Various |

## Converting your own fonts locally

You can use this pipeline to convert any OTF or TTF font to WOFF2 yourself.

### Requirements

- Python 3
- `fonttools` and `brotli` packages

```bash
pip install fonttools brotli
```

### Convert your fonts

Drop your OTF/TTF files into the `src/` folder and run:

```bash
python convert.py
```

Converted WOFF2 files and family bundles are written to `dist/`.

### Use in CSS

```css
@font-face {
  font-family: 'YourFont';
  src: url('YourFont.woff2') format('woff2');
  font-weight: normal;
  font-style: normal;
}
```

## Releasing a new version

1. Add or update font files in `src/`
2. Commit and push to `main`
3. Tag the commit with a version number:
   ```bash
   git tag v1.1.0
   git push origin v1.1.0
   ```

The GitHub Actions workflow will convert the fonts and publish a release with all WOFF2 files and bundles attached automatically.
