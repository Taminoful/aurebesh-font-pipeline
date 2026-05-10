#!/usr/bin/env python3
"""Convert all OTF/TTF files in src/ to WOFF2 in dist/, then bundle by family and create an all-fonts zip."""
import glob
import os
import zipfile
from fontTools.ttLib import TTFont

os.makedirs("dist", exist_ok=True)

FAMILIES = {
    # Bundles matching source distribution
    "AurebeshAF":          ["AurebeshAF-Canon", "AurebeshAF-CanonTech", "AurebeshAF-Legends", "AurebeshAF-LegendsTech"],
    "Aurebesh-Cantina":    ["Aurebesh Cantina", "Aurebesh Cantina Bold", "Aurebesh Cantina Italic", "Aurebesh Cantina Bold Italic"],
    "Aurebesh-PixelSagas": ["Aurebesh", "Aurebesh Bold", "Aurebesh Italic", "Aurebesh Bold Italic",
                            "Aurebesh Condensed", "Aurebesh Condensed Bold", "Aurebesh Condensed Italic", "Aurebesh Condensed Bold Italic"],
    "Aurek-Besh":          ["Aurek-Besh", "Aurek-Besh Narrow"],
    "Aurek-Besh-Hand":     ["Aurek-Besh Hand"],
    "MandoAF":             ["MandoAF-Regular", "MandoAF-Classic"],
    "Protobesh":           ["Protobesh-Coremaic", "Protobesh-Square"],
    "KyberCrystalDisplay": ["KyberCrystalDisplay-Aurebesh", "KyberCrystalDisplay-Alphabet"],
    "Auraboo":             ["Auraboo"],
    "NewAurabesh":         ["newaure"],
    "SkyLuke":             ["SkyLuke"],
    "UbeseBoushh":         ["ubese-boushh-beta"],
    # Extra bundles where it makes sense
    "Goongan-AF":          ["Goongan_AF_Alphabet-Regular", "Goongan_AF_Syllabics-Regular"],
    "Ur-Kittat":           ["Ur-Kittat", "UrKittatLU"],
    "OldTongue":           ["OldTongue_Yavin", "old-tongue"],
    "ProtobeshAF":         ["ProtobeshAF"],
}

# Build a reverse lookup: stem -> family name
stem_to_family = {}
for family, stems in FAMILIES.items():
    for stem in stems:
        stem_to_family[stem] = family

# Convert all fonts
sources = sorted(glob.glob("src/*.otf") + glob.glob("src/*.ttf"))
failed = []
converted = []

for src_path in sources:
    stem = os.path.splitext(os.path.basename(src_path))[0]
    woff2_name = stem + ".woff2"
    dest_path = os.path.join("dist", woff2_name)
    try:
        font = TTFont(src_path)
        font.flavor = "woff2"
        font.save(dest_path)
        print(f"OK  {src_path} -> {dest_path}")
        converted.append((stem, dest_path))
    except Exception as e:
        print(f"ERR {src_path}: {e}")
        failed.append(src_path)

# Bundle family zips
family_files = {family: [] for family in FAMILIES}
for stem, woff2_path in converted:
    if stem in stem_to_family:
        family_files[stem_to_family[stem]].append(woff2_path)

for family, files in family_files.items():
    if not files:
        continue
    zip_path = os.path.join("dist", f"{family}.zip")
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for f in files:
            zf.write(f, os.path.basename(f))
    print(f"Bundled {family}.zip ({len(files)} files)")

# All-fonts zip
all_zip_path = os.path.join("dist", "all-fonts.zip")
with zipfile.ZipFile(all_zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
    for _, woff2_path in converted:
        zf.write(woff2_path, os.path.basename(woff2_path))
print(f"Bundled all-fonts.zip ({len(converted)} files)")

print(f"\n{len(converted)}/{len(sources)} converted.")
if failed:
    print("Failed:")
    for f in failed:
        print(f"  {f}")
