#!/usr/bin/env python3
import os
import sys
import subprocess
import re

# Path configurations
BASE_DIR = "/Users/adamsnihur/Desktop/AG projects/opracowania/border_collie"
CHAPTERS_DIR = os.path.join(BASE_DIR, "chapters")
CSS_FILE = os.path.join(BASE_DIR, "academic_monograph_style.css")
OUTPUT_MD = os.path.join(BASE_DIR, "Historia_powstania_rasy_Border_Collie.md")
OUTPUT_HTML = os.path.join(BASE_DIR, "Historia_powstania_rasy_Border_Collie.html")
OUTPUT_PDF = os.path.join(BASE_DIR, "Historia_powstania_rasy_Border_Collie.pdf")

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
    html = f"""<div class="title-page">
<div class="title-header">
<h1>Historia powstania rasy Border Collie</h1>
<div class="subtitle">Studium historyczno-genetyczne nad ewolucją kynologii użytkowej</div>
</div>
<div class="illustration-container" style="max-width: 320px; margin: 20px auto;">
<img src="images/cover.png" alt="The Working Collie" style="width: 100%; height: auto; border: 2px solid #475569; border-radius: 6px; box-shadow: 0 6px 15px rgba(0,0,0,0.1);">
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
        
        # Check if bibliography or intro/conclusion
        if "Bibliografia" in title:
            html += f"""
<li class="toc-item">
<span class="toc-name"><a href="#{anchor}">{title}</a></span>
<span class="toc-dots"></span>
<span class="toc-page">Literatura</span>
</li>"""
        elif "Wstęp" in title or "Zakończenie" in title or "Podsumowanie" in title:
            html += f"""
<li class="toc-item">
<span class="toc-name"><a href="#{anchor}">{title}</a></span>
<span class="toc-dots"></span>
<span class="toc-page">Tekst główny</span>
</li>"""
        else:
            # Main chapters start from index 1 (excluding Introduction)
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
    """Programmatic fix: ensures all markdown lists (starting with *, -, or numbers)
    have a blank line before them for correct Pandoc parsing.
    """
    lines = content.split('\n')
    processed_lines = []
    for line in lines:
        if line.strip() and not line.strip().startswith(('#', '*', '-', '>')) and ' * **' in line:
            parts = line.split(' * **')
            if len(parts) > 1:
                new_line_block = [parts[0].strip(), ""]
                for part in parts[1:]:
                    new_line_block.append(f"* **{part.strip()}")
                processed_lines.extend(new_line_block)
                continue
        processed_lines.append(line)
        
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
    print("--- ROZPOCZĘCIE KOMPILACJI MONOGRAFII BORDER COLLIE ---")
    
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

    # Parse titles for TOC
    chapters_metadata = []
    for file in files:
        filepath = os.path.join(CHAPTERS_DIR, file)
        with open(filepath, 'r', encoding='utf-8') as f:
            first_line = f.readline().strip()
            match = re.match(r'^#\s+(?:\d+\.\s+)?(.+)$', first_line)
            if match:
                title = match.group(1)
            else:
                title = file.replace(".md", "").replace("chapter_", "").replace("_", " ").title()
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
                
                # Anchor mapping
                title = chapters_metadata[idx-1][0]
                anchor = re.sub(r'[^a-z0-9_-]', '', title.lower().replace(' ', '-'))
                
                # Format first H1 header with anchor
                if "Wstęp" in title or "Podsumowanie" in title or "Bibliografia" in title:
                    content = re.sub(
                        r'^#\s+.+$',
                        f'# <span id="{anchor}">{title}</span>',
                        content,
                        count=1,
                        flags=re.MULTILINE
                    )
                else:
                    merytoryczny_idx = idx - 1  # Chapter 1 is files[1] (Introduction is files[0])
                    content = re.sub(
                        r'^#\s+(?:\d+\.\s+)?(.+)$',
                        f'# <span id="{anchor}">Rozdział {merytoryczny_idx}: {title}</span>',
                        content,
                        count=1,
                        flags=re.MULTILINE
                    )
                
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
        "--metadata", "title=Historia powstania rasy Border Collie"
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
        "--footer-template=<div style='font-size: 10px; font-family: \"Montserrat\", sans-serif; width: 100%; text-align: center; color: #5B21B6;'><span class='pageNumber'></span></div>", # Purple page numbers
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
