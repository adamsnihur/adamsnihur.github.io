#!/usr/bin/env python3
"""
Master Compilation Pipeline for Academic Monograph:
'Portret Polaków Własny. Raport z badań DNA marki Polska'
"""

import os
import sys
import subprocess
import re
import tempfile
import time

BASE_DIR = "/Users/adamsnihur/Desktop/AG projects/opracowania/portret_polakow_wlasny"
CHAPTERS_DIR = os.path.join(BASE_DIR, "chapters")
CSS_FILE = os.path.join(BASE_DIR, "academic_monograph_style.css")
OUTPUT_MD = os.path.join(BASE_DIR, "Portret_Polakow_Wlasny_Raport_DNA_Marki_Polska.md")
OUTPUT_HTML = os.path.join(BASE_DIR, "Portret_Polakow_Wlasny_Raport_DNA_Marki_Polska.html")
OUTPUT_PDF = os.path.join(BASE_DIR, "Portret_Polakow_Wlasny_Raport_DNA_Marki_Polska.pdf")

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
    svg_shield = """<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
<!-- Outer geometric shield -->
<polygon points="50,4 96,24 96,76 50,96 4,76 4,24" fill="none" stroke="#821D2D" stroke-width="2"/>
<polygon points="50,9 91,27 91,73 50,91 9,73 9,27" fill="none" stroke="#B88942" stroke-width="1.2" stroke-dasharray="2,2"/>
<!-- Crown -->
<path d="M35,32 L40,22 L50,28 L60,22 L65,32 Z" fill="#B88942" stroke="#821D2D" stroke-width="1"/>
<circle cx="50" cy="21" r="1.5" fill="#B88942"/>
<!-- Stylized Eagle Head & Body -->
<path d="M48,34 Q50,30 53,34 L56,36 Q54,39 52,42 L52,58 L48,58 L48,42 Q46,39 44,36 Z" fill="#821D2D"/>
<path d="M53,35 L58,34 L54,37 Z" fill="#B88942"/>
<!-- Wings -->
<path d="M48,42 C36,36 24,42 16,56 C24,56 34,54 44,52 Z" fill="#821D2D"/>
<path d="M52,42 C64,36 76,42 84,56 C76,56 66,54 56,52 Z" fill="#821D2D"/>
<path d="M46,50 C38,48 28,52 20,64 C28,62 36,60 46,56 Z" fill="#B88942" opacity="0.85"/>
<path d="M54,50 C62,48 72,52 80,64 C72,62 64,60 54,56 Z" fill="#B88942" opacity="0.85"/>
<!-- Tail -->
<polygon points="50,60 42,76 50,72 58,76" fill="#821D2D"/>
<!-- Oak / Laurel branches -->
<path d="M12,50 Q10,32 22,25" fill="none" stroke="#B88942" stroke-width="1.5" stroke-linecap="round"/>
<path d="M88,50 Q90,32 78,25" fill="none" stroke="#B88942" stroke-width="1.5" stroke-linecap="round"/>
</svg>"""
    
    html = f"""<div class="title-page">
<div class="title-header">
<h1>Portret Polaków Własny</h1>
<div class="subtitle">Raport z badań DNA marki Polska. Studium tożsamościowe, socjologiczne i reputacyjne</div>
</div>
<div class="title-emblem">
{svg_shield}
</div>
<div class="title-metadata">
<p>Monografia Naukowa & Raport Strategiczny</p>
<p>Antigravity Research Press</p>
<p>Rok Pański 2026</p>
</div>
</div>"""
    return html

def generate_toc(chapters_metadata):
    html = """<div class="toc-container">
<h2>Spis Treści</h2>
<ul class="toc-list">"""
    for idx, (title, filename) in enumerate(chapters_metadata, 1):
        anchor = re.sub(r'[^a-z0-9_-]', '', title.lower().replace(' ', '-'))
        title_lower = title.lower()
        if "bibliografia" in title_lower:
            html += f"""
<li class="toc-item">
<span class="toc-name"><a href="#{anchor}">{title}</a></span>
<span class="toc-dots"></span>
<span class="toc-page">Aparatura Źródłowa</span>
</li>"""
        elif "wstęp" in title_lower or "wstep" in title_lower:
            html += f"""
<li class="toc-item">
<span class="toc-name"><a href="#{anchor}">{title}</a></span>
<span class="toc-dots"></span>
<span class="toc-page">Wprowadzenie</span>
</li>"""
        else:
            merytoryczny_idx = idx - 1
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
    lines = content.split('\n')
    fixed_lines = []
    for idx, line in enumerate(lines):
        is_list_item = re.match(r'^\s*([*+-]|\d+\.)\s+', line)
        if is_list_item and idx > 0:
            prev_line = lines[idx-1]
            prev_is_list = re.match(r'^\s*([*+-]|\d+\.)\s+', prev_line)
            prev_is_empty = prev_line.strip() == ""
            prev_is_header = prev_line.strip().startswith('#')
            if not prev_is_empty and not prev_is_list and not prev_is_header:
                fixed_lines.append("")
        fixed_lines.append(line)
    return '\n'.join(fixed_lines)

CLEAN_TITLES = {
    "chapter_00_wstep.md": "Wstęp. Ramy Metodologiczne i Epistemologiczne Badań DNA Marki Narodowej",
    "chapter_01_korzenie_historyczne.md": "Historyczno-Kulturowe Źródła Tożsamości: Sarmatyzm vs. Romantyzm",
    "chapter_02_trauma_i_przesniona_rewolucja.md": "Trauma Dziejowa, Przemoc Strukturalna i „Prześniona Rewolucja”",
    "chapter_03_psychologia_spoleczna.md": "Psychologia Społeczna Polaków: Deficyt Zaufania, Amoralny Familizm i Zaradność",
    "chapter_04_struktura_wartosci.md": "Struktura Wartości, Aspiracje i Pęknięcia Społeczno-Pokoleniowe",
    "chapter_05_dna_gospodarcze.md": "Polskie DNA Gospodarcze: Etos Pracy, Innowacyjność i Odporność Operacyjna",
    "chapter_06_lustro_swiata.md": "Lustro Świata: Dysonans Między Auto-Percepcją a Postrzeganiem Międzynarodowym",
    "chapter_07_semiotyka_i_kultura.md": "Semiotyka, Kody Wizualne i Popkultura jako Nośniki Marki",
    "chapter_08_architektura_archetypow.md": "Architektura Archetypowa: Narodziny „Pragmatycznego Pioniera”",
    "chapter_09_filary_strategiczne.md": "Filary Strategiczne i Platforma Reputacyjna Marki Polska",
    "chapter_10_dyplomacja_publiczna.md": "Dyplomacja Publiczna, Zarządzanie Reputacją i Soft Power",
    "chapter_11_zakonczenie.md": "Zakończenie: Manifest Nowej Narracji Polski XXI Wieku",
    "chapter_12_bibliografia.md": "Bibliografia i Źródła Akademickie"
}

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
    
    files = sorted([f for f in os.listdir(CHAPTERS_DIR) if f.startswith("chapter_") and f.endswith(".md")])
    if not files:
        print("BŁĄD: Brak plików rozdziałów w katalogu chapters/.", file=sys.stderr)
        sys.exit(1)
        
    print(f"Wykryto {len(files)} plików do połączenia.")
    
    chapters_metadata = []
    for file in files:
        title = CLEAN_TITLES.get(file, file.replace(".md", "").replace("chapter_", "").replace("_", " ").title())
        chapters_metadata.append((title, file))
        
    print(f"Tworzenie pliku master Markdown: {OUTPUT_MD}")
    with open(OUTPUT_MD, 'w', encoding='utf-8') as master:
        master.write(generate_title_page())
        master.write("\n\n")
        master.write('<div style="page-break-after: always;"></div>\n\n')
        
        master.write(generate_toc(chapters_metadata))
        master.write("\n\n")
        master.write('<div style="page-break-after: always;"></div>\n\n')
        
        for idx, file in enumerate(files, 1):
            filepath = os.path.join(CHAPTERS_DIR, file)
            print(f"Scalanie: {file}...")
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
            content = re.sub(r'🎯\s*Aktywne\s*Skille:.*$', '', content, flags=re.MULTILINE)
            content = re.sub(r'\[Reasoning Mythos Protocol: Active\]', '', content)
            content = re.sub(r'\n---\s*\n###\s*(Przypisy|Literatura|Bibliografia)\s*\n', '\n\n', content, flags=re.IGNORECASE)
            content = content.strip()
            
            content = fix_markdown_lists(content)
            content = content.replace('–', '-').replace('—', '-')
            
            chapter_prefix = re.sub(r'[^a-zA-Z0-9]', '_', file.replace('.md', ''))
            content = re.sub(r'\[\^([^\]]+)\]', f'[^{chapter_prefix}_\\1]', content)
            
            title = chapters_metadata[idx-1][0]
            anchor = re.sub(r'[^a-z0-9_-]', '', title.lower().replace(' ', '-'))
            title_lower = title.lower()
            
            if "wstęp" in title_lower or "wstep" in title_lower or "zakończenie" in title_lower or "zakonczenie" in title_lower or "bibliografia" in title_lower:
                header_text = f'# <span id="{anchor}">{title}</span>'
            else:
                merytoryczny_idx = idx - 1
                header_text = f'# <span id="{anchor}">Rozdział {merytoryczny_idx}: {title}</span>'
                
            has_h1 = re.search(r'^#\s+.+$', content, flags=re.MULTILINE)
            if has_h1:
                content = re.sub(r'^#\s+.+$', header_text, content, count=1, flags=re.MULTILINE)
            else:
                content = header_text + "\n\n" + content
                
            master.write(content)
            master.write("\n\n")
            
            if idx < len(files):
                master.write('<div style="page-break-after: always;"></div>\n\n')
                
    print(f"Kompilacja Markdown do HTML: {OUTPUT_HTML}")
    cmd_pandoc = [
        "pandoc",
        OUTPUT_MD,
        "-o", OUTPUT_HTML,
        "--standalone",
        "--metadata", "title=Portret Polaków Własny. Raport z badań DNA marki Polska"
    ]
    subprocess.run(cmd_pandoc, check=True)
    
    with open(OUTPUT_HTML, 'r', encoding='utf-8') as f:
        html_content = f.read()
        
    with open(CSS_FILE, 'r', encoding='utf-8') as f:
        css_content = f.read()
        
    injected_html = html_content.replace('</head>', f'<style>\n{css_content}\n</style>\n</head>')
    
    with open(OUTPUT_HTML, 'w', encoding='utf-8') as f:
        f.write(injected_html)
    print("Pomyślnie zintegrowano style CSS w pliku HTML.")
    
    # Render PDF via Chrome Headless
    print("Renderowanie PDF via Chrome Headless...")
    user_data_dir = os.path.join(tempfile.gettempdir(), "chrome_monograph_profile_render")
    os.makedirs(user_data_dir, exist_ok=True)
    
    footer_template = "<div style='font-size: 10px; font-family: \"Montserrat\", sans-serif; width: 100%; text-align: center; color: #821D2D; letter-spacing: 1px;'><span class='pageNumber'></span></div>"
    
    cmd_chrome = [
        chrome_path,
        "--headless",
        "--disable-gpu",
        "--no-sandbox",
        f"--user-data-dir={user_data_dir}",
        "--display-header-footer",
        "--header-template= ",
        f"--footer-template={footer_template}",
        f"--print-to-pdf={OUTPUT_PDF}",
        OUTPUT_HTML
    ]
    
    # Run with timeout to prevent hanging after writing PDF
    proc = subprocess.Popen(cmd_chrome, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    for _ in range(30):
        time.sleep(1)
        if os.path.exists(OUTPUT_PDF) and os.path.getsize(OUTPUT_PDF) > 100000:
            time.sleep(2)
            try:
                proc.terminate()
            except Exception:
                pass
            break
            
    if os.path.exists(OUTPUT_PDF) and os.path.getsize(OUTPUT_PDF) > 0:
        pdf_mb = os.path.getsize(OUTPUT_PDF) / (1024 * 1024)
        print(f"SUKCES! Monografia wygenerowana do PDF: {OUTPUT_PDF} ({pdf_mb:.2f} MB)")
    else:
        print("BŁĄD generowania PDF!", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    compile_monograph()
