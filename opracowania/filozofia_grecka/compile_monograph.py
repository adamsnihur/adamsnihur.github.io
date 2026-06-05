#!/usr/bin/env python3
import os
import sys
import subprocess
import re

# Path configurations
BASE_DIR = "/Users/adamsnihur/Desktop/AG projects/opracowania/filozofia_grecka"
CHAPTERS_DIR = os.path.join(BASE_DIR, "chapters")
CSS_FILE = os.path.join(BASE_DIR, "academic_monograph_style.css")
OUTPUT_MD = os.path.join(BASE_DIR, "Wplyw_filozofii_greckiej_na_dzieje_zachodniej_cywilizacji.md")
OUTPUT_HTML = os.path.join(BASE_DIR, "Wplyw_filozofii_greckiej_na_dzieje_zachodniej_cywilizacji.html")
OUTPUT_PDF = os.path.join(BASE_DIR, "Wplyw_filozofii_greckiej_na_dzieje_zachodniej_cywilizacji.pdf")

# Chrome path candidates on macOS
CHROME_PATH_OPTIONS = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser",
    "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge"
]

def find_chrome():
    for path in CHROME_PATH_OPTIONS:
        if os.path.exists(path):
            return path
    return None

def check_pandoc():
    try:
        subprocess.run(["pandoc", "--version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def generate_title_page():
    # Returns HTML for the title page with custom Greek Temple / Olive branches emblem
    svg_shield = """<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
<!-- Outer geometric shield -->
<polygon points="50,5 95,25 95,75 50,95 5,75 5,25" fill="none" stroke="#1A303A" stroke-width="2"/>
<polygon points="50,10 90,28 90,72 50,90 10,72 10,28" fill="none" stroke="#B58A3D" stroke-width="1" stroke-dasharray="2,2"/>
<!-- Temple Pediment (triangle) -->
<polygon points="25,35 75,35 50,23" fill="#1A303A"/>
<!-- Architrave and frieze -->
<rect x="23" y="36" width="54" height="4" fill="#B58A3D"/>
<rect x="25" y="41" width="50" height="2" fill="#1A303A"/>
<!-- Columns -->
<rect x="28" y="44" width="6" height="26" fill="#1A303A"/>
<rect x="40" y="44" width="6" height="26" fill="#1A303A"/>
<rect x="54" y="44" width="6" height="26" fill="#1A303A"/>
<rect x="66" y="44" width="6" height="26" fill="#1A303A"/>
<!-- Stylobate (3 steps base) -->
<rect x="20" y="70" width="60" height="3" fill="#1A303A"/>
<rect x="18" y="73" width="64" height="3" fill="#B58A3D"/>
<rect x="15" y="76" width="70" height="4" fill="#1A303A"/>
<!-- Olive branch details in corners -->
<path d="M12,50 Q10,35 20,28" fill="none" stroke="#B58A3D" stroke-width="1.5" stroke-linecap="round"/>
<path d="M88,50 Q90,35 80,28" fill="none" stroke="#B58A3D" stroke-width="1.5" stroke-linecap="round"/>
</svg>"""
    
    html = f"""<div class="title-page">
<div class="title-header">
<h1>Wpływ filozofii greckiej na dzieje zachodniej cywilizacji</h1>
<div class="subtitle">Studium historyczno-filozoficzne nad fundamentami myśli europejskiej</div>
</div>
<div class="title-emblem">
{svg_shield}
</div>
<div class="title-metadata">
<p>Monografia Dysertacyjna</p>
<p>Antigravity Research Press</p>
<p>Rok Pański 2026</p>
</div>
</div>"""
    return html

def generate_toc(chapters):
    # Returns HTML for the Table of Contents
    html = """<div class="toc-container">
<h2>Spis Treści</h2>
<ul class="toc-list">"""
    for idx, (title, filename) in enumerate(chapters, 1):
        anchor = re.sub(r'[^a-z0-9_-]', '', title.lower().replace(' ', '-'))
        title_lower = title.lower()
        # Bibliografię i Wstęp/Zakończenie formatujemy odpowiednio
        if "bibliografia" in title_lower:
            html += f"""
<li class="toc-item">
<span class="toc-name"><a href="#{anchor}">{title}</a></span>
<span class="toc-dots"></span>
<span class="toc-page">Literatura</span>
</li>"""
        elif "wstęp" in title_lower or "wstep" in title_lower or "zakończenie" in title_lower or "zakonczenie" in title_lower:
            html += f"""
<li class="toc-item">
<span class="toc-name"><a href="#{anchor}">{title}</a></span>
<span class="toc-dots"></span>
<span class="toc-page">Tekst główny</span>
</li>"""
        else:
            # Ustalamy prawidłowy indeks rozdziału (np. Rozdział 1 dla pierwszego merytorycznego)
            # Wstęp ma indeks 0, więc merytoryczne rozdziały od indeksu 1
            # chapters to (title, filename)
            # let's count merytoryczne
            merytoryczny_idx = idx - 1 # Wstęp jest pierwszy (idx=1)
            html += f"""
<li class="toc-item">
<span class="toc-name"><a href="#{anchor}">Rozdział {merytoryczny_idx}: {title}</a></span>
<span class="toc-dots"></span>
<span class="toc-page">Rozdział {merytoryczny_idx}</span>
</li>"""
    html += """
</ul>
</div>"""
    return html

def fix_markdown_lists(content):
    """Programmatic fix: ensures all markdown lists (starting with *, -, or numbers)
    have a blank line before them for correct Pandoc parsing.
    Also handles inline list items separated by asterisks and converts them to actual lines.
    """
    # 1. Transform inline lists separated by '*' inside paragraphs to proper newlines if they look like:
    # "Jego argumentacja opierała się na kilku filarach: * Wystarczalność... * Źródło..."
    # We look for patterns where text is followed by multiple * items on the same line.
    lines = content.split('\n')
    processed_lines = []
    for line in lines:
        if line.strip() and not line.strip().startswith(('#', '*', '-', '>')) and ' * **' in line:
            # Replace inline ' * **' with newlines to form proper list items
            # but keep the introductory text on its own line
            parts = line.split(' * **')
            if len(parts) > 1:
                new_line_block = [parts[0].strip(), ""]
                for part in parts[1:]:
                    new_line_block.append(f"* **{part.strip()}")
                processed_lines.extend(new_line_block)
                continue
        processed_lines.append(line)
        
    # 2. Ensure blank line before list starts
    fixed_lines = []
    for idx, line in enumerate(processed_lines):
        is_list_item = re.match(r'^\s*([*+-]|\d+\.)\s+', line)
        if is_list_item and idx > 0:
            prev_line = processed_lines[idx-1]
            prev_is_list_item = re.match(r'^\s*([*+-]|\d+\.)\s+', prev_line)
            prev_is_empty = prev_line.strip() == ""
            prev_is_header = prev_line.strip().startswith('#')
            
            if not prev_is_empty and not prev_is_list_item and not prev_is_header:
                fixed_lines.append("")  # Inject blank line before list
        fixed_lines.append(line)
    return '\n'.join(fixed_lines)

def compile_monograph():
    print("--- ROZPOCZĘCIE KOMPILACJI MONOGRAFII ---")
    
    if not check_pandoc():
        print("BŁĄD: Pandoc nie jest zainstalowany lub nie ma go w ścieżce PATH.", file=sys.stderr)
        sys.exit(1)
        
    chrome_path = find_chrome()
    if not chrome_path:
        print("BŁĄD: Nie znaleziono Google Chrome ani żadnej kompatybilnej przeglądarki na macOS.", file=sys.stderr)
        sys.exit(1)
        
    print(f"Znaleziono przeglądarkę: {chrome_path}")

    # Check chapters directory
    if not os.path.exists(CHAPTERS_DIR):
        print(f"BŁĄD: Katalog z rozdziałami nie istnieje: {CHAPTERS_DIR}", file=sys.stderr)
        sys.exit(1)
        
    files = sorted([f for f in os.listdir(CHAPTERS_DIR) if f.startswith("chapter_") and f.endswith(".md")])
    if not files:
        print("BŁĄD: Brak plików rozdziałów w katalogu chapters/.", file=sys.stderr)
        sys.exit(1)
        
    print(f"Wykryto {len(files)} plików do połączenia.")

    # Map filenames to clean titles to prevent duplicate numbering
    CLEAN_TITLES = {
        "chapter_00_wstep.md": "Wstęp. Filozofia grecka jako system operacyjny cywilizacji zachodniej",
        "chapter_01_od_mitu_do_logosu.md": "Od mitu do logosu",
        "chapter_02_sokrates.md": "Sokrates",
        "chapter_03_platon.md": "Platon",
        "chapter_04_arystoteles.md": "Arystoteles",
        "chapter_05_hellenizm.md": "Hellenizm",
        "chapter_06_ateny_i_jerozolima.md": "Ateny i Jerozolima",
        "chapter_07_scholastyka.md": "Scholastyka i wielkie syntezy średniowiecza",
        "chapter_08_renesans.md": "Renesans",
        "chapter_09_nowozytnosc.md": "Nowożytność",
        "chapter_10_xix_xx_wiek.md": "Wiek XIX i XX",
        "chapter_11_korzenie_nauki.md": "Korzenie nauki",
        "chapter_12_polityka_prawo_etyka.md": "Polityka, prawo, etyka",
        "chapter_13_zakonczenie.md": "Zakończenie",
        "chapter_14_bibliografia.md": "Bibliografia"
    }

    # Parse titles for TOC
    chapters_metadata = []
    for file in files:
        title = CLEAN_TITLES.get(file, file.replace(".md", "").replace("chapter_", "").replace("_", " ").title())
        chapters_metadata.append((title, file))

    # Generate Master Markdown
    print(f"Tworzenie pliku master Markdown: {OUTPUT_MD}")
    with open(OUTPUT_MD, 'w', encoding='utf-8') as master:
        # Title page
        master.write(generate_title_page())
        master.write("\n\n")
        master.write('<div style="page-break-after: always;"></div>\n\n')
        
        # Table of Contents
        master.write(generate_toc(chapters_metadata))
        master.write("\n\n")
        master.write('<div style="page-break-after: always;"></div>\n\n')
        
        # Chapters
        for idx, file in enumerate(files, 1):
            filepath = os.path.join(CHAPTERS_DIR, file)
            print(f"Scalanie: {file}...")
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
                # Check for agent footers and strip them
                content = re.sub(r'🎯\s*Aktywne\s*Skille:.*$', '', content, flags=re.MULTILINE)
                content = re.sub(r'\[Reasoning Mythos Protocol: Active\]', '', content)
                content = content.strip()
                
                # Fix list formatting programmatically
                content = fix_markdown_lists(content)
                
                # Sanitize dashes systematically to standard hyphens
                content = content.replace('–', '-').replace('—', '-')
                
                # Prefix footnotes to prevent collisions between chapters
                chapter_prefix = re.sub(r'[^a-zA-Z0-9]', '_', file.replace('.md', ''))
                content = re.sub(r'\[\^([^\]]+)\]', f'[^{chapter_prefix}_\\1]', content)
                
                # Anchor mapping
                title = chapters_metadata[idx-1][0]
                anchor = re.sub(r'[^a-z0-9_-]', '', title.lower().replace(' ', '-'))
                title_lower = title.lower()
                
                # Format first H1 header with anchor
                if "wstęp" in title_lower or "wstep" in title_lower or "zakończenie" in title_lower or "zakonczenie" in title_lower or "bibliografia" in title_lower:
                    header_text = f'# <span id="{anchor}">{title}</span>'
                else:
                    merytoryczny_idx = idx - 1 # Wstęp jest idx=1, więc Rozdział 1 ma idx=2
                    header_text = f'# <span id="{anchor}">Rozdział {merytoryczny_idx}: {title}</span>'
                
                # If there's an existing H1 header, replace it, otherwise prepend it
                has_h1 = re.search(r'^#\s+.+$', content, flags=re.MULTILINE)
                if has_h1:
                    content = re.sub(
                        r'^#\s+.+$',
                        header_text,
                        content,
                        count=1,
                        flags=re.MULTILINE
                    )
                else:
                    content = header_text + "\n\n" + content
                
                master.write(content)
                master.write("\n\n")
                
                # Add page break between chapters
                if idx < len(files):
                    master.write('<div style="page-break-after: always;"></div>\n\n')

    # Compile Markdown to HTML via Pandoc
    print(f"Kompilacja Markdown do HTML: {OUTPUT_HTML}")
    cmd_pandoc = [
        "pandoc",
        OUTPUT_MD,
        "-o", OUTPUT_HTML,
        "--standalone",
        "--metadata", "title=Wpływ filozofii greckiej na dzieje zachodniej cywilizacji"
    ]
    
    try:
        subprocess.run(cmd_pandoc, check=True)
    except subprocess.CalledProcessError as e:
        print(f"BŁĄD Pandoca podczas kompilacji do HTML: {e}", file=sys.stderr)
        sys.exit(1)

    # Inject CSS link in HTML head
    with open(OUTPUT_HTML, 'r', encoding='utf-8') as f:
        html_content = f.read()

    css_link = f'\n<link rel="stylesheet" href="academic_monograph_style.css">\n'
    html_content = html_content.replace('</head>', f'{css_link}</head>')

    with open(OUTPUT_HTML, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print("Poprawnie połączono style CSS z plikiem HTML.")

    # Generate PDF via Headless Chrome with elegant page numbers
    print(f"Kompilacja HTML do PDF za pomocą bezgłowej przeglądarki...")
    cmd_chrome = [
        chrome_path,
        "--headless",
        "--disable-gpu",
        "--no-sandbox",
        "--display-header-footer",
        "--header-template= ", # hides default date and title
        "--footer-template=<div style='font-size: 10px; font-family: \"Montserrat\", sans-serif; width: 100%; text-align: center; color: #8C2D19;'><span class='pageNumber'></span></div>", # terracotta page numbers
        f"--print-to-pdf={OUTPUT_PDF}",
        OUTPUT_HTML
    ]

    try:
        subprocess.run(cmd_chrome, check=True)
        print(f"SUKCES! Monografia została pomyślnie wygenerowana: {OUTPUT_PDF}")
    except subprocess.CalledProcessError as e:
        print(f"BŁĄD Chrome podczas generowania PDF: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    compile_monograph()
