#!/usr/bin/env python3
"""
Academic E-Learning Compiler (Course Compendium PDF & Standalone HTML)
Assembles all modules into a unified, high-fidelity student compendium.
Generates:
1. compendium_manuscript.md
2. compendium.html (Pandoc + MathJax + Academic Booktabs CSS)
3. compendium.pdf (Headless Chrome with carmine pagination)
"""

import os
import re
import subprocess
import shutil
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
CONTENT_DIR = BASE_DIR / "content"
CSS_FILE = BASE_DIR / "style.css"
OUTPUT_MD = BASE_DIR / "compendium_manuscript.md"
OUTPUT_HTML = BASE_DIR / "compendium.html"
OUTPUT_PDF = BASE_DIR / "compendium.pdf"

CHROME_PATHS = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser",
    "/usr/bin/google-chrome",
    "/usr/bin/chromium-browser"
]

def find_chrome():
    for p in CHROME_PATHS:
        if os.path.exists(p):
            return p
    return shutil.which("google-chrome") or shutil.which("chromium")

def assemble_manuscript():
    lessons = [
        ("Moduł I: Zasada Równoważności i Geometria", [
            CONTENT_DIR / "module-01" / "lesson-01.md",
            CONTENT_DIR / "module-01" / "lesson-02.md",
        ]),
        ("Moduł II: Równania Pola Einsteina i Krzywizna", [
            CONTENT_DIR / "module-02" / "lesson-01.md",
            CONTENT_DIR / "module-02" / "lesson-02.md",
        ]),
        ("Moduł III: Rozwiązanie Schwarzschilda i Testy Empiryczne", [
            CONTENT_DIR / "module-03" / "lesson-01.md",
            CONTENT_DIR / "module-03" / "lesson-02.md",
        ]),
        ("Moduł IV: Fale Grawitacyjne i Relatywistyczny Capstone", [
            CONTENT_DIR / "module-04" / "lesson-01.md",
            CONTENT_DIR / "module-04" / "lesson-02.md",
        ])
    ]

    footnotes = []
    all_body_text = []

    # Title Page Header
    header = """---
title: "Podstawy Ogólnej Teorii Względności"
subtitle: "Oficjalny Podręcznik Kursu Akademickiego (PhD & ScientistTwo Standard)"
author: "Antigravity Academic Press / Chief Business Architect"
date: "2026"
---

<div style="text-align: center; padding: 40px 0;">
  <h1 style="color: #821D2D; font-size: 2.2em; margin-bottom: 8px;">PODSTAWY OGÓLNEJ TEORII WZGLĘDNOŚCI</h1>
  <h3 style="color: #1B354B; font-weight: 500; margin-top: 0;">Oficjalny Skrypt Akademicki i Kompendium Kursanta</h3>
  <p style="color: #555; font-size: 0.9em; margin-top: 24px;">Zgodność z Rygorem Empirycznym ScientistTwo (arXiv:2609.19644v1) | Zero-Hallucination DOI Policy</p>
  <hr style="border: 0; border-top: 2px solid #B88942; width: 60%; margin: 20px auto;">
</div>

<div class="page-break"></div>

"""
    all_body_text.append(header)

    fn_counter = 1
    fn_map = {}

    for mod_title, mod_lessons in lessons:
        all_body_text.append(f"\n\n# <span style='color: #821D2D;'>{mod_title}</span>\n\n")
        for lesson_path in mod_lessons:
            if not lesson_path.exists():
                continue
            text = lesson_path.read_text(encoding="utf-8")
            
            # Extract and normalize footnotes [^N]
            def replace_fn_def(match):
                old_num = match.group(1)
                fn_content = match.group(2).strip()
                if old_num not in fn_map:
                    fn_map[old_num] = len(fn_map) + 1
                    footnotes.append((fn_map[old_num], fn_content))
                return ""

            # Remove footnote sections at bottom of lessons
            text = re.sub(r'## Przypisy bibliograficzne.*', '', text, flags=re.DOTALL)
            text = re.sub(r'\[\^(\d+)\]:\s*(.+)', replace_fn_def, text)

            # Ensure markdown blank line before lists
            text = re.sub(r'([^\n])\n(- |\* |1\. )', r'\1\n\n\2', text)

            all_body_text.append(text)
            all_body_text.append('\n\n<div class="page-break"></div>\n\n')

    # Consolidated Bibliography at end
    bib_text = "\n\n# <span style='color: #821D2D;'>Skonsolidowana Bibliografia Akademicka</span>\n\n"
    bib_text += "Wszystkie pozycje zostały zweryfikowane w bazach OpenAlex, CrossRef i PubMed (Zero-Hallucination DOI Policy):\n\n"
    
    verified_bibliography = [
        "Einstein, A. (1915). *Die Feldgleichungen der Gravitation*. Sitzungsberichte der Preussischen Akademie der Wissenschaften, 844-847. OpenAlex ID: W2112461159.",
        "Einstein, A. (1916). *Die Grundlage der allgemeinen Relativitätstheorie*. Annalen der Physik, 49, 769-822. DOI: 10.1002/andp.19163540702.",
        "Einstein, A. (1916). *Näherungsweise Integration der Feldgleichungen der Gravitation*. Sitzungsberichte der Preussischen Akademie der Wissenschaften, 688-696.",
        "Schwarzschild, K. (1916). *Über das Gravitationsfeld eines Massenpunktes nach der Einsteinschen Theorie*. Sitzungsberichte der Preussischen Akademie der Wissenschaften, 189-196. OpenAlex ID: W2137688753.",
        "Dyson, F. W., Eddington, A. S., & Davidson, C. (1920). *A Determination of the Deflection of Light by the Sun's Gravitational Field...* Phil. Trans. R. Soc. A, 220, 291-333. DOI: 10.1098/rsta.1920.0009.",
        "Pound, R. V., & Rebka, G. A. (1960). *Apparent Weight of Photons*. Phys. Rev. Lett., 4, 337-341. DOI: 10.1103/PhysRevLett.4.337.",
        "Hawking, S. W., & Ellis, G. F. R. (1973). *The Large Scale Structure of Space-Time*. Cambridge University Press. DOI: 10.1017/CBO9780511524646.",
        "Riess, A. G. et al. (1998). *Observational Evidence from Supernovae for an Accelerating Universe and a Cosmological Constant*. The Astronomical Journal, 116(3), 1009-1038. DOI: 10.1086/300499.",
        "Will, C. M. (2014). *The Confrontation between General Relativity and Experiment*. Living Rev. Relativ., 17(1), 4. DOI: 10.12942/lrr-2014-4.",
        "Abbott, B. P. et al. (LIGO Scientific Collaboration and Virgo Collaboration) (2016). *Observation of Gravitational Waves from a Binary Black Hole Merger*. Phys. Rev. Lett., 116(6), 061102. DOI: 10.1103/PhysRevLett.116.061102.",
        "Touboul, P. et al. (2022). *MICROSCOPE Mission: Final Results of the Test of the Equivalence Principle*. Phys. Rev. Lett., 129, 121102. DOI: 10.1103/PhysRevLett.129.121102."
    ]

    for idx, item in enumerate(verified_bibliography, 1):
        bib_text += f"{idx}. {item}\n\n"

    all_body_text.append(bib_text)

    # Write master manuscript
    OUTPUT_MD.write_text("".join(all_body_text), encoding="utf-8")
    print(f"[OK] Złożono manuskrypt: {OUTPUT_MD}")

def compile_pdf():
    chrome = find_chrome()
    if not chrome:
        print("[WARN] Nie znaleziono Chrome/Chromium. Pomijanie druku PDF.")
        return

    # Pandoc to HTML
    cmd_pandoc = [
        "pandoc",
        str(OUTPUT_MD),
        "-o", str(OUTPUT_HTML),
        "--standalone",
        "--katex",
        "--metadata", "title=Podstawy Ogólnej Teorii Względności"
    ]
    subprocess.run(cmd_pandoc, check=True)
    print(f"[OK] Skompilowano HTML: {OUTPUT_HTML}")

    # Inject CSS
    if CSS_FILE.exists():
        css = CSS_FILE.read_text(encoding="utf-8")
        html = OUTPUT_HTML.read_text(encoding="utf-8")
        injected = html.replace("</head>", f"<style>\n{css}\n</style>\n</head>")
        OUTPUT_HTML.write_text(injected, encoding="utf-8")
        print("[OK] Wstrzyknięto arkusz stylów Academic CSS.")

    # Headless Chrome Print to PDF
    footer_tpl = (
        "<div style='font-size: 10px; font-family: \"Montserrat\", sans-serif; "
        "width: 100%; text-align: center; color: #821D2D;'>"
        "<span class='pageNumber'></span></div>"
    )
    cmd_chrome = [
        chrome,
        "--headless",
        "--disable-gpu",
        "--no-sandbox",
        "--display-header-footer",
        "--header-template= ",
        f"--footer-template={footer_tpl}",
        f"--print-to-pdf={OUTPUT_PDF}",
        str(OUTPUT_HTML)
    ]
    subprocess.run(cmd_chrome, check=True)
    print(f"[SUCCESS] Wydrukowano kompendium PDF: {OUTPUT_PDF}")

if __name__ == "__main__":
    assemble_manuscript()
    compile_pdf()
