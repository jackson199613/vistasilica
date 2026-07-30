# -*- coding: utf-8 -*-
# Vistasilica TDS data — from lab (v1.0 Preliminary, typical values pending validation)
# Source: Vistasilica-TDS-General.docx + VS-OE550 lab data
# IMPORTANT: These are TYPICAL / PRELIMINARY values based on industry reference data,
# NOT confirmed specifications. Must be labelled as such on the site.

DISCLAIMER = ("Typical values representative of the grade family. Values are for "
              "guidance; a grade-specific specification sheet is available on request.")

# property order + units + test methods (shared)
PROPS = [
    ("BET specific surface area", "m²/g", "ISO 9277 / DIN 66131"),
    ("Oil absorption (DOP)", "g/100g", "ISO 4652 / DIN 53617"),
    ("Particle size D50", "µm", "ISO 13320 (laser diffraction)"),
    ("Sieve residue (45 µm)", "%", "ISO 2591-1"),
    ("Bulk density (poured)", "g/L", "ISO 60"),
    ("Tapped density", "g/L", "ISO 697"),
    ("pH (5% aq. suspension)", "—", "ISO 6588"),
    ("Loss on drying (105 °C, 2 h)", "%", "ISO 787-2"),
    ("SiO₂ content (dry basis)", "%", "Gravimetric / XRF"),
    ("Loss on ignition (1000 °C)", "%", "ISO 6798"),
]

# grade: {page, name, track, use, focus, values[list matching PROPS], competitors}
GRADES = {
    "VS-C200": {
        "page": "feed-additives", "track": "Feed additives · Food powders",
        "name": "VS-C200 Carrier",
        "use": "Premix carrier, liquid-additive powdering, vitamin/trace-mineral blends",
        "focus": "High liquid absorption, carrier capacity, dispersion uniformity",
        "values": ["170 – 230", "240 – 290", "10 – 18", "≤ 0.10", "90 – 140", "140 – 210", "6.0 – 7.5", "4.0 – 7.0", "≥ 97.0", "≤ 6.0"],
    },
    "VS-F120": {
        "page": "food-powder", "track": "Feed additives · Food powders",
        "name": "VS-F120 Flow Aid",
        "use": "Anti-caking, flow aid for seasoning powders, dry blends",
        "focus": "Free-flow improvement, shelf stability, anti-bridging",
        "values": ["100 – 150", "180 – 230", "5 – 12", "≤ 0.05", "110 – 170", "170 – 250", "6.0 – 7.5", "4.0 – 6.0", "≥ 98.0", "≤ 5.0"],
    },
    "VS-A070": {
        "page": "oral-care", "track": "Oral care",
        "name": "VS-A070 Abrasive",
        "use": "Toothpaste abrasive, cleaning-type paste formulations",
        "focus": "Controlled RDA, cleaning efficiency, paste stability",
        "values": ["45 – 90", "90 – 140", "6 – 12", "≤ 0.05", "180 – 260", "280 – 400", "6.5 – 7.5", "4.0 – 6.0", "≥ 98.0", "≤ 5.0"],
    },
    "VS-T400": {
        "page": "oral-care", "track": "Oral care",
        "name": "VS-T400 Thickener",
        "use": "Toothpaste thickener, structure-building, thixotropy",
        "focus": "Thickening, paste structure, extrusion performance",
        "values": ["350 – 450", "260 – 310", "8 – 15", "≤ 0.10", "70 – 110", "110 – 170", "6.5 – 7.5", "5.0 – 8.0", "≥ 97.0", "≤ 7.0"],
    },
    "VS-WG180": {
        "page": "agro", "track": "Agrochemical",
        "name": "VS-WG180 WG Carrier",
        "use": "WP/WG inert carrier, SC anti-caking / rheology modifier",
        "focus": "Active loading, disintegration, suspension stability",
        "values": ["160 – 210", "200 – 250", "12 – 22", "≤ 0.15", "100 – 160", "150 – 230", "6.0 – 7.5", "4.0 – 7.0", "≥ 96.0", "≤ 7.0"],
    },
    "VS-OE550": {
        "page": "oil-refining", "track": "Edible oil refining",
        "name": "VS-OE550 Adsorbent",
        "use": "Silica adsorbent for degumming / soap & phosphatide removal / filter aid",
        "focus": "Phospholipid & soap adsorption, high surface area & pore volume, filtration",
        "values": ["400 – 600", "180 – 260", "8 – 18", "≤ 1.0", "350 – 500", "450 – 600", "4.0 – 6.5", "≤ 8.0", "≥ 98.0", "≤ 10.0"],
    },
    "VS-P200": {
        "page": "personal-care", "track": "Personal care",
        "name": "VS-P200 Personal Care",
        "use": "Color cosmetics, foundation, sun care, pressed powder",
        "focus": "Oil absorption, matte finish, skin feel, soft-focus effect",
        "values": ["180 – 240", "220 – 270", "3 – 8", "≤ 0.03", "100 – 150", "150 – 220", "6.5 – 7.5", "3.0 – 6.0", "≥ 98.5", "≤ 4.5"],
    },
}

# page -> list of grade keys (oral-care has two)
PAGE_GRADES = {}
for k, g in GRADES.items():
    PAGE_GRADES.setdefault(g["page"], []).append(k)

if __name__ == "__main__":
    print("Grades:", len(GRADES))
    for page, keys in PAGE_GRADES.items():
        print(f"  {page}: {', '.join(keys)}")
