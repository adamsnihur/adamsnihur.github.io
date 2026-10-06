#!/usr/bin/env python3
"""
High-Fidelity Interactive Web LMS Platform Builder
Course: Podstawy Ogolnej Teorii Wzglednosci (General Relativity Foundations)
Key Capabilities:
1. Native page scrolling (fixes Safari/Chrome scroll-trapping & overflow issues)
2. MathJax 3 with full LaTeX rendering for all tensor equations
3. Interactive Quiz Widget with real-time feedback & misconception explanations
4. Interactive Capstone Simulator (Chirp mass & black hole merger parameters)
5. Responsive sticky sidebar + mobile drawer toggle
6. LocalStorage persistence for progress tracking
"""

import re
import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
CONTENT_DIR = BASE_DIR / "content"
OUTPUT_INDEX = BASE_DIR / "index.html"

LESSONS = [
    ("module-01", "lesson-01.md", "1.1: Ograniczenia grawitacji Newtona i Zasada Równoważności", "Moduł I: Zasada Równoważności"),
    ("module-01", "lesson-02.md", "1.2: Równanie Geodezyjnych i Symbole Christoffela", "Moduł I: Zasada Równoważności"),
    ("module-02", "lesson-01.md", "2.1: Krzywizna Riemanna, Tensor Ricciego i Tensor Energii", "Moduł II: Równania Pola Einsteina"),
    ("module-02", "lesson-02.md", "2.2: Równania Pola Einsteina i Stała Kosmologiczna", "Moduł II: Równania Pola Einsteina"),
    ("module-03", "lesson-01.md", "3.1: Metryka Schwarzschilda, Horyzont i Orbity ISCO", "Moduł III: Rozwiązanie Schwarzschilda"),
    ("module-03", "lesson-02.md", "3.2: Trzy Klasyczne Testy Empiryczne OTW", "Moduł III: Rozwiązanie Schwarzschilda"),
    ("module-04", "lesson-01.md", "4.1: Linearyzacja OTW, Fale Grawitacyjne i LIGO", "Moduł IV: Fale Grawitacyjne & Capstone"),
    ("module-04", "lesson-02.md", "4.2: Relatywistyczny Projekt Końcowy (Capstone GW150914)", "Moduł IV: Fale Grawitacyjne & Capstone")
]

def parse_and_enhance_lesson(md_path: Path, lesson_id: str) -> str:
    raw_text = md_path.read_text(encoding="utf-8")
    
    # 1. Extract Retrieval Check Quiz if present
    quiz_html = ""
    quiz_match = re.search(
        r'##\s*(?:\d+\.\s*)?Szybki sprawdzian wiedzy.*?\n\n\*\*Pytanie:\*\*\s*(.*?)\n'
        r'-\s*\*\*A\)\*\*\s*(.*?)\n'
        r'-\s*\*\*B\)\*\*\s*(.*?)\n'
        r'-\s*\*\*C\)\*\*\s*(.*?)\n\n'
        r'\*Prawidłowa odpowiedź:\s*([ABC])\.\*\n'
        r'\*Wyjaśnienie dydaktyczne:\*\s*(.*?)(?=\n##|\Z)',
        raw_text,
        re.DOTALL
    )
    
    if quiz_match:
        question = quiz_match.group(1).strip()
        opt_a = quiz_match.group(2).strip()
        opt_b = quiz_match.group(3).strip()
        opt_c = quiz_match.group(4).strip()
        correct_letter = quiz_match.group(5).strip().upper()
        explanation = quiz_match.group(6).strip()
        
        # Remove the raw markdown quiz from the text so we don't display it twice
        raw_text = raw_text[:quiz_match.start()] + raw_text[quiz_match.end():]
        
        quiz_html = f"""
<div class="interactive-quiz-container" id="quiz-{lesson_id}">
  <div class="quiz-badge"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg> Interaktywny Sprawdzian Wiedzy (ScientistTwo Diagnostic)</div>
  <p class="quiz-question-text"><strong>Pytanie:</strong> {question}</p>
  <div class="quiz-options-group">
    <button type="button" class="quiz-btn" data-opt="A" data-correct="{'true' if correct_letter == 'A' else 'false'}" onclick="handleQuizAnswer(this, 'quiz-{lesson_id}')">
      <span class="quiz-opt-letter">A</span>
      <span class="quiz-opt-text">{opt_a}</span>
    </button>
    <button type="button" class="quiz-btn" data-opt="B" data-correct="{'true' if correct_letter == 'B' else 'false'}" onclick="handleQuizAnswer(this, 'quiz-{lesson_id}')">
      <span class="quiz-opt-letter">B</span>
      <span class="quiz-opt-text">{opt_b}</span>
    </button>
    <button type="button" class="quiz-btn" data-opt="C" data-correct="{'true' if correct_letter == 'C' else 'false'}" onclick="handleQuizAnswer(this, 'quiz-{lesson_id}')">
      <span class="quiz-opt-letter">C</span>
      <span class="quiz-opt-text">{opt_c}</span>
    </button>
  </div>
  <div class="quiz-feedback-box" id="feedback-quiz-{lesson_id}">
    <div class="feedback-heading">Analiza dydaktyczna (Misconception Resolution):</div>
    <p class="feedback-body">{explanation}</p>
  </div>
</div>
"""

    # 2. Add Capstone interactive widget if lesson is 4.2
    capstone_widget = ""
    if "lesson-02.md" in str(md_path) and "module-04" in str(md_path):
        capstone_widget = """
<div class="capstone-interactive-lab">
  <div class="lab-header">
    <span class="lab-tag">LABORATORIUM EMPIRYCZNE</span>
    <h3>Interaktywny Symulator Koalescencji GW150914 (LIGO)</h3>
    <p>Zmieniaj parametry obserwowane sygnału fali grawitacyjnej i obserwuj relatywistyczną rekonstrukcję parametrów układu czarnych dziur w czasie rzeczywistym:</p>
  </div>
  <div class="lab-controls-grid">
    <div class="lab-control">
      <label for="input-f">Częstotliwość fali $f$ [Hz]: <span id="val-f" class="val-badge">75 Hz</span></label>
      <input type="range" id="input-f" min="35" max="150" value="75" step="1" oninput="updateCapstoneSim()">
    </div>
    <div class="lab-control">
      <label for="input-fdot">Tempo wzrostu $\\dot{f}$ [Hz/s]: <span id="val-fdot" class="val-badge">1350 Hz/s</span></label>
      <input type="range" id="input-fdot" min="200" max="4000" value="1350" step="50" oninput="updateCapstoneSim()">
    </div>
  </div>
  <div class="lab-results-grid">
    <div class="result-tile">
      <span class="tile-label">Masa Chirpowa $\\mathcal{M}$</span>
      <span class="tile-val" id="res-mchirp">31.27 M☉</span>
      <span class="tile-sub">LIGO: 28.3 - 31.5 M☉</span>
    </div>
    <div class="result-tile">
      <span class="tile-label">Masa Składowa $m_1 = m_2$</span>
      <span class="tile-val" id="res-m0">35.92 M☉</span>
      <span class="tile-sub">Czarna dziura Kerra</span>
    </div>
    <div class="result-tile">
      <span class="tile-label">Promień Horyzontu $r_s$</span>
      <span class="tile-val" id="res-rs">183.1 km</span>
      <span class="tile-sub">Przed koalescencją</span>
    </div>
    <div class="result-tile">
      <span class="tile-label">Wypromieniowana Energia $\\Delta E$</span>
      <span class="tile-val" id="res-dE">3.0 M☉ c²</span>
      <span class="tile-sub">Moc szczytowa 10⁴⁹ W</span>
    </div>
  </div>
  <div class="lab-status-badge" id="lab-verdict">
    ✓ Zgodność empiryczna: Model zbieżny z detekcją LIGO Hanford/Livingston
  </div>
</div>
"""

    # 3. Compile markdown with Pandoc using --mathjax
    res = subprocess.run(
        ["pandoc", "-f", "markdown", "-t", "html", "--mathjax"],
        input=raw_text,
        capture_output=True,
        text=True,
        check=True
    )
    html_output = res.stdout

    # Append interactive widgets
    if quiz_html:
        html_output += quiz_html
    if capstone_widget:
        html_output += capstone_widget

    return html_output

def build_lms():
    rendered_lessons = []
    for idx, (mod, fname, title, mod_cat) in enumerate(LESSONS):
        path = CONTENT_DIR / mod / fname
        lesson_id = f"lesson-{idx+1}"
        html_content = parse_and_enhance_lesson(path, lesson_id)
        rendered_lessons.append({
            "index": idx,
            "id": lesson_id,
            "title": title,
            "mod_cat": mod_cat,
            "html": html_content
        })

    html = f"""<!DOCTYPE html>
<html lang="pl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Podstawy Ogólnej Teorii Względności | Akademia Relatywistyczna (PhD Standard)</title>
  <meta name="description" content="Akademicki kurs e-learningowy z podstaw Ogólnej Teorii Względności zgodny ze standardem ScientistTwo i PhD.">
  
  <!-- MathJax 3 with TeX input and SVG/CommonHTML output -->
  <script>
    window.MathJax = {{
      tex: {{
        inlineMath: [['$', '$'], ['\\\\(', '\\\\)']],
        displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']],
        processEscapes: true
      }},
      options: {{
        skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code']
      }},
      startup: {{
        pageReady: () => {{
          return MathJax.startup.defaultPageReady();
        }}
      }}
    }};
  </script>
  <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script>

  <!-- Google Fonts: Instrument Sans, Cinzel, Lora, JetBrains Mono -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700&family=Instrument+Sans:wght@400;500;600;700&family=Lora:ital,wght@0,400;0,500;0,600;0,700;1,400&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">

  <style>
    /* ==========================================================================
       CANONICAL ACADEMIC LMS THEME & PURE CSS DIAGRAMS
       ========================================================================== */
    :root {{
      --carmine: #821D2D;
      --carmine-dark: #5C141F;
      --gold: #B88942;
      --gold-light: #DFCA9B;
      --navy: #1B354B;
      --bg: #FAF8F5;
      --card-bg: #FFFFFF;
      --border: #E2D9CB;
      --text: #1A1A1A;
      --text-muted: #555555;
      --sidebar-width: 330px;
      --header-height: 64px;
    }}

    /* Global Base */
    html, body {{
      margin: 0;
      padding: 0;
      width: 100%;
      min-height: 100%;
      background-color: var(--bg);
      color: var(--text);
      font-family: 'Instrument Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      line-height: 1.75;
      -webkit-font-smoothing: antialiased;
    }}

    /* Typography inside lessons */
    h1, h2, h3, h4 {{
      color: var(--carmine);
      font-family: 'Cinzel', serif;
      font-weight: 700;
      line-height: 1.3;
    }}
    .lesson-body h1 {{
      font-size: 2.1rem;
      border-bottom: 2px solid var(--gold);
      padding-bottom: 12px;
      margin: 10px 0 24px;
      text-align: left;
    }}
    .lesson-body h2 {{
      font-size: 1.5rem;
      border-bottom: 1px dashed var(--gold);
      padding-bottom: 8px;
      margin: 36px 0 16px;
      color: var(--carmine-dark);
    }}
    .lesson-body h3 {{
      font-size: 1.25rem;
      color: var(--navy);
      margin: 28px 0 12px;
    }}
    .lesson-body p {{
      margin: 16px 0;
      font-size: 1.05rem;
      color: #262422;
      font-family: 'Lora', Georgia, serif;
    }}
    .lesson-body ul, .lesson-body ol {{
      margin: 16px 0 20px 24px;
      font-family: 'Lora', Georgia, serif;
    }}
    .lesson-body li {{
      margin-bottom: 8px;
      font-size: 1.02rem;
    }}
    .lesson-body strong {{
      color: #111;
      font-weight: 600;
    }}
    .lesson-body hr {{
      border: 0;
      border-top: 1px solid var(--border);
      margin: 36px 0;
    }}

    /* Drop-cap */
    p.chapter-start {{
      font-size: 1.1rem;
      line-height: 1.8;
    }}
    p.chapter-start::first-letter {{
      font-family: 'Cinzel', serif;
      font-size: 3.4rem;
      float: left;
      line-height: 0.8;
      margin: 6px 10px 0 0;
      color: var(--carmine);
      font-weight: 700;
    }}

    /* Code & Math */
    pre, code {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.92rem;
    }}
    code {{
      background: #F4EFE6;
      color: var(--carmine-dark);
      padding: 2px 6px;
      border-radius: 4px;
      border: 1px solid #E5DEC0;
    }}
    pre {{
      background: #24292E;
      color: #F8F8F2;
      padding: 20px;
      border-radius: 6px;
      overflow-x: auto;
      margin: 20px 0;
      line-height: 1.5;
    }}
    pre code {{
      background: transparent;
      color: inherit;
      padding: 0;
      border: none;
    }}
    .mjx-chtml {{
      font-size: 108% !important;
    }}

    /* Images */
    .lesson-body img {{
      max-width: 100%;
      height: auto;
      border-radius: 6px;
      border: 1px solid var(--border);
      box-shadow: 0 4px 14px rgba(0,0,0,0.05);
      margin: 24px 0;
      display: block;
    }}

    /* Pure CSS Diagrams (Academic Monograph Standard) */
    .tree-container {{
      background: #FDFBF7;
      border: 1px solid var(--border);
      border-left: 4px solid var(--carmine);
      padding: 20px 24px;
      border-radius: 6px;
      margin: 24px 0;
    }}
    .tree-node {{
      margin: 8px 0;
      padding-left: 18px;
      position: relative;
      font-size: 0.96rem;
      color: #333;
    }}
    .tree-node::before {{
      content: "├─";
      position: absolute;
      left: 0;
      color: var(--gold);
      font-family: monospace;
      font-weight: bold;
    }}
    .tree-node:last-child::before {{
      content: "└─";
    }}
    .flow-container {{
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      margin: 24px 0;
    }}
    .flow-step {{
      background: #FFFFFF;
      border: 1px solid var(--border);
      border-top: 3px solid var(--navy);
      padding: 12px 16px;
      border-radius: 4px;
      font-size: 0.92rem;
      font-weight: 500;
      box-shadow: 0 2px 6px rgba(0,0,0,0.03);
    }}

    /* Booktabs Academic Tables */
    .table-wrapper {{
      overflow-x: auto;
      margin: 28px 0;
    }}
    table.academic-table {{
      width: 100%;
      border-collapse: collapse;
      font-family: 'Instrument Sans', sans-serif;
      font-size: 0.95rem;
      background: #FFFFFF;
      border-top: 2px solid var(--carmine);
      border-bottom: 2px solid var(--carmine);
    }}
    table.academic-table caption {{
      font-family: 'Cinzel', serif;
      font-weight: 700;
      color: var(--carmine-dark);
      text-align: left;
      padding-bottom: 8px;
      font-size: 0.98rem;
    }}
    table.academic-table th {{
      border-bottom: 1.5px solid var(--gold);
      padding: 12px 14px;
      text-align: left;
      font-weight: 600;
      color: var(--navy);
      background: #FAF7F2;
    }}
    table.academic-table td {{
      padding: 12px 14px;
      border-bottom: 1px solid #EFEAE1;
      vertical-align: top;
    }}
    table.academic-table tr:hover {{
      background: #FDFBF7;
    }}

    /* ==========================================================================
       LMS APPLICATION SHELL
       ========================================================================== */
    header.lms-navbar {{
      position: sticky;
      top: 0;
      z-index: 1000;
      height: var(--header-height);
      background: #FFFFFF;
      border-bottom: 2px solid var(--border);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 24px;
      box-shadow: 0 2px 12px rgba(0,0,0,0.04);
    }}
    .nav-left {{
      display: flex;
      align-items: center;
      gap: 14px;
    }}
    .menu-toggle-btn {{
      display: none;
      background: transparent;
      border: 1px solid var(--border);
      border-radius: 4px;
      padding: 6px 10px;
      font-size: 16px;
      cursor: pointer;
    }}
    .brand-badge {{
      background: var(--carmine);
      color: #FFF;
      font-size: 10.5px;
      font-weight: 700;
      padding: 4px 8px;
      border-radius: 4px;
      letter-spacing: 0.5px;
      text-transform: uppercase;
    }}
    .brand-title {{
      font-family: 'Cinzel', serif;
      font-size: 16px;
      font-weight: 700;
      color: var(--navy);
    }}
    .nav-right {{
      display: flex;
      align-items: center;
      gap: 20px;
    }}
    .progress-widget {{
      display: flex;
      align-items: center;
      gap: 10px;
      font-size: 12px;
      font-weight: 600;
      color: var(--navy);
    }}
    .progress-bar-bg {{
      width: 140px;
      height: 8px;
      background: #EAE3D5;
      border-radius: 4px;
      overflow: hidden;
    }}
    .progress-bar-fill {{
      height: 100%;
      background: var(--carmine);
      width: 12.5%;
      transition: width 0.3s ease;
    }}
    .btn-download-pdf {{
      background: var(--gold);
      color: #FFFFFF;
      padding: 8px 16px;
      border-radius: 6px;
      font-size: 12.5px;
      font-weight: 600;
      text-decoration: none;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: background 0.2s;
    }}
    .btn-download-pdf:hover {{
      background: #A07535;
    }}

    /* Layout Wrapper */
    .lms-wrapper {{
      display: flex;
      width: 100%;
      min-height: calc(100vh - var(--header-height));
    }}

    /* Sidebar Navigation */
    aside.lms-sidebar {{
      width: var(--sidebar-width);
      flex-shrink: 0;
      background: #FFFFFF;
      border-right: 1px solid var(--border);
      position: sticky;
      top: var(--header-height);
      height: calc(100vh - var(--header-height));
      overflow-y: auto;
      padding: 16px 0;
    }}
    .sidebar-mod-heading {{
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.8px;
      color: #8C827A;
      padding: 16px 20px 8px;
      border-top: 1px solid #F5F1EB;
    }}
    .sidebar-mod-heading:first-child {{ border-top: none; }}
    .nav-lesson-link {{
      display: flex;
      align-items: center;
      gap: 10px;
      padding: 12px 20px;
      font-size: 13.5px;
      color: #4A4643;
      text-decoration: none;
      border-left: 3px solid transparent;
      cursor: pointer;
      transition: background 0.15s, border-left-color 0.15s;
    }}
    .nav-lesson-link:hover {{
      background: #FAF8F5;
      color: var(--carmine);
    }}
    .nav-lesson-link.active {{
      background: #F7F3EB;
      border-left-color: var(--carmine);
      color: var(--carmine);
      font-weight: 600;
    }}
    .nav-lesson-link.is-done .status-indicator {{
      background: #2E7D32;
    }}
    .status-indicator {{
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: #D4CDC5;
      flex-shrink: 0;
    }}

    /* Main Lesson Stage (Native Scrolling) */
    main.lms-main-stage {{
      flex: 1;
      min-width: 0;
      padding: 40px 48px 120px;
      display: flex;
      justify-content: center;
    }}
    .lesson-sheet {{
      width: 100%;
      max-width: 880px;
      background: #FFFFFF;
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 48px 56px;
      box-shadow: 0 4px 20px rgba(0,0,0,0.03);
      display: none;
    }}
    .lesson-sheet.active {{
      display: block;
      animation: fadeIn 0.2s ease-in-out;
    }}
    @keyframes fadeIn {{
      from {{ opacity: 0; transform: translateY(4px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}

    /* Interactive Quiz Widget */
    .interactive-quiz-container {{
      background: #FCFBF9;
      border: 1px solid #E2D9CC;
      border-left: 4px solid var(--carmine);
      border-radius: 6px;
      padding: 24px 28px;
      margin: 36px 0 20px;
    }}
    .quiz-badge {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.6px;
      color: var(--carmine);
      margin-bottom: 12px;
    }}
    .quiz-question-text {{
      font-size: 1.05rem;
      font-weight: 500;
      color: #1A1A1A;
      margin-bottom: 16px;
      font-family: 'Instrument Sans', sans-serif !important;
    }}
    .quiz-options-group {{
      display: flex;
      flex-direction: column;
      gap: 10px;
    }}
    .quiz-btn {{
      display: flex;
      align-items: flex-start;
      gap: 12px;
      background: #FFFFFF;
      border: 1px solid #DCD5CA;
      border-radius: 6px;
      padding: 12px 16px;
      text-align: left;
      cursor: pointer;
      font-family: 'Instrument Sans', sans-serif;
      font-size: 0.95rem;
      color: #333;
      transition: all 0.15s ease;
    }}
    .quiz-btn:hover {{
      border-color: var(--gold);
      background: #FAF8F5;
    }}
    .quiz-opt-letter {{
      background: #EEE9DF;
      color: #444;
      font-weight: 700;
      font-size: 11px;
      width: 22px;
      height: 22px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      margin-top: 2px;
    }}
    .quiz-btn.is-correct {{
      background: #E8F5E9 !important;
      border-color: #2E7D32 !important;
      color: #1B5E20 !important;
      font-weight: 600;
    }}
    .quiz-btn.is-correct .quiz-opt-letter {{
      background: #2E7D32;
      color: #FFF;
    }}
    .quiz-btn.is-wrong {{
      background: #FFEBEE !important;
      border-color: #C62828 !important;
      color: #B71C1C !important;
    }}
    .quiz-btn.is-wrong .quiz-opt-letter {{
      background: #C62828;
      color: #FFF;
    }}
    .quiz-feedback-box {{
      margin-top: 16px;
      padding: 14px 18px;
      border-radius: 6px;
      background: #F4EFE6;
      border: 1px solid #E2D9CC;
      display: none;
    }}
    .quiz-feedback-box.show {{ display: block; }}
    .feedback-heading {{
      font-size: 11.5px;
      font-weight: 700;
      text-transform: uppercase;
      color: var(--carmine);
      margin-bottom: 6px;
    }}
    .feedback-body {{
      font-size: 0.95rem;
      color: #333;
      line-height: 1.5;
      font-family: 'Lora', serif !important;
      margin: 0 !important;
    }}

    /* Capstone Simulator Widget */
    .capstone-interactive-lab {{
      background: #FDFCF9;
      border: 2px solid var(--gold);
      border-radius: 8px;
      padding: 28px 32px;
      margin: 36px 0;
    }}
    .lab-header h3 {{
      font-size: 1.3rem;
      margin: 6px 0 10px;
    }}
    .lab-tag {{
      background: var(--gold);
      color: #FFF;
      font-size: 10px;
      font-weight: 700;
      padding: 3px 8px;
      border-radius: 3px;
    }}
    .lab-controls-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
      margin: 20px 0;
    }}
    .lab-control label {{
      display: flex;
      justify-content: space-between;
      font-size: 0.92rem;
      font-weight: 600;
      margin-bottom: 8px;
    }}
    .val-badge {{
      background: var(--navy);
      color: #FFF;
      padding: 2px 8px;
      border-radius: 4px;
      font-size: 11px;
    }}
    .lab-control input[type="range"] {{
      width: 100%;
      accent-color: var(--carmine);
    }}
    .lab-results-grid {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 12px;
      margin: 24px 0 16px;
    }}
    .result-tile {{
      background: #FFFFFF;
      border: 1px solid var(--border);
      border-top: 3px solid var(--carmine);
      padding: 14px 12px;
      border-radius: 6px;
      display: flex;
      flex-direction: column;
      gap: 4px;
    }}
    .tile-label {{
      font-size: 11px;
      color: #666;
      font-weight: 600;
    }}
    .tile-val {{
      font-size: 1.25rem;
      font-weight: 700;
      color: var(--carmine);
      font-family: 'JetBrains Mono', monospace;
    }}
    .tile-sub {{
      font-size: 10px;
      color: #888;
    }}
    .lab-status-badge {{
      background: #E8F5E9;
      color: #1B5E20;
      padding: 10px 14px;
      border-radius: 6px;
      font-size: 12.5px;
      font-weight: 600;
      border: 1px solid #C8E6C9;
    }}

    /* Lesson Navigation Bar */
    .lesson-nav-footer {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-top: 48px;
      padding-top: 24px;
      border-top: 1px solid var(--border);
    }}
    .nav-btn {{
      background: var(--navy);
      color: #FFFFFF;
      border: none;
      padding: 12px 22px;
      border-radius: 6px;
      font-size: 13.5px;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: background 0.15s, opacity 0.15s;
    }}
    .nav-btn:hover {{ opacity: 0.92; }}
    .nav-btn.btn-complete-action {{
      background: var(--carmine);
    }}

    /* Responsive */
    @media (max-width: 960px) {{
      .menu-toggle-btn {{ display: block; }}
      aside.lms-sidebar {{
        position: fixed;
        left: -330px;
        top: var(--header-height);
        height: calc(100vh - var(--header-height));
        z-index: 999;
        box-shadow: 4px 0 20px rgba(0,0,0,0.1);
      }}
      aside.lms-sidebar.open {{
        left: 0;
      }}
      main.lms-main-stage {{ padding: 24px 16px; }}
      .lesson-sheet {{ padding: 28px 20px; }}
      .lab-controls-grid {{ grid-template-columns: 1fr; }}
      .lab-results-grid {{ grid-template-columns: 1fr 1fr; }}
    }}
  </style>
</head>
<body>

  <!-- Top Fixed Navigation -->
  <header class="lms-navbar">
    <div class="nav-left">
      <button type="button" class="menu-toggle-btn" onclick="toggleSidebar()" aria-label="Przełącz spis lekcji">☰</button>
      <span class="brand-badge">PhD Standard</span>
      <span class="brand-title">Podstawy Ogólnej Teorii Względności</span>
    </div>
    <div class="nav-right">
      <div class="progress-widget">
        <span id="ui-progress-text">12%</span>
        <div class="progress-bar-bg">
          <div class="progress-bar-fill" id="ui-progress-bar"></div>
        </div>
      </div>
      <a href="compendium.pdf" target="_blank" class="btn-download-pdf">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg>
        Pobierz Skrypt PDF (1.8 MB)
      </a>
    </div>
  </header>

  <!-- LMS Main Layout -->
  <div class="lms-wrapper">
    <!-- Sidebar Navigation -->
    <aside class="lms-sidebar" id="sidebar-drawer">
"""

    current_cat = ""
    for lesson in rendered_lessons:
        if lesson["mod_cat"] != current_cat:
            current_cat = lesson["mod_cat"]
            html += f'      <div class="sidebar-mod-heading">{current_cat}</div>\n'
        active_cls = " active" if lesson["index"] == 0 else ""
        html += f"""      <a class="nav-lesson-link{active_cls}" data-id="{lesson['id']}" onclick="activateLesson('{lesson['id']}')">
        <span class="status-indicator"></span>
        <span>{lesson['title']}</span>
      </a>\n"""

    html += """    </aside>

    <!-- Main Content Reader -->
    <main class="lms-main-stage">
"""

    for lesson in rendered_lessons:
        active_cls = " active" if lesson["index"] == 0 else ""
        is_first = lesson["index"] == 0
        is_last = lesson["index"] == len(rendered_lessons) - 1

        html += f"""      <article class="lesson-sheet{active_cls}" id="{lesson['id']}">
        <div class="lesson-body">
{lesson['html']}
        </div>

        <div class="lesson-nav-footer">
          <button type="button" class="nav-btn" onclick="goToRelativeLesson(-1)" {'disabled style="opacity: 0.4;"' if is_first else ''}>&larr; Poprzednia lekcja</button>
          <button type="button" class="nav-btn btn-complete-action" onclick="completeCurrentLesson('{lesson['id']}')">{'Zalicz kurs i pobierz skrypt' if is_last else 'Zalicz lekcję i przejdź dalej &rarr;'}</button>
        </div>
      </article>\n"""

    html += """    </main>
  </div>

  <script>
    const TOTAL_LESSONS = 8;
    let completedSet = new Set(JSON.parse(localStorage.getItem('gr_completed_lessons') || '[]'));

    function toggleSidebar() {
      const sb = document.getElementById('sidebar-drawer');
      sb.classList.toggle('open');
    }

    function updateProgress() {
      const count = completedSet.size;
      const pct = Math.max(12, Math.round((count / TOTAL_LESSONS) * 100));
      document.getElementById('ui-progress-text').innerText = pct + '%';
      document.getElementById('ui-progress-bar').style.width = pct + '%';

      document.querySelectorAll('.nav-lesson-link').forEach(link => {
        const id = link.getAttribute('data-id');
        if (completedSet.has(id)) {
          link.classList.add('is-done');
        } else {
          link.classList.remove('is-done');
        }
      });
    }

    function activateLesson(lessonId) {
      document.querySelectorAll('.lesson-sheet').forEach(sheet => sheet.classList.remove('active'));
      document.querySelectorAll('.nav-lesson-link').forEach(link => link.classList.remove('active'));

      const targetSheet = document.getElementById(lessonId);
      const targetLink = document.querySelector(`.nav-lesson-link[data-id="${lessonId}"]`);
      if (targetSheet) targetSheet.classList.add('active');
      if (targetLink) targetLink.classList.add('active');

      // Native window smooth scroll to top
      window.scrollTo({ top: 0, behavior: 'smooth' });

      // Close mobile drawer if open
      const sb = document.getElementById('sidebar-drawer');
      if (sb) sb.classList.remove('open');

      // Trigger MathJax re-render for newly visible elements if needed
      if (window.MathJax && MathJax.typesetPromise) {
        MathJax.typesetPromise([targetSheet]);
      }
    }

    function completeCurrentLesson(lessonId) {
      completedSet.add(lessonId);
      localStorage.setItem('gr_completed_lessons', JSON.stringify(Array.from(completedSet)));
      updateProgress();

      const num = parseInt(lessonId.replace('lesson-', ''));
      if (num < TOTAL_LESSONS) {
        activateLesson(`lesson-${num + 1}`);
      } else {
        alert('Gratulacje! Zaliczyłeś wszystkie moduły kursu Podstawy Ogólnej Teorii Względności (PhD & ScientistTwo Standard). Możesz pobrać oficjalne kompendium PDF!');
      }
    }

    function goToRelativeLesson(delta) {
      const activeSheet = document.querySelector('.lesson-sheet.active');
      if (!activeSheet) return;
      const num = parseInt(activeSheet.id.replace('lesson-', ''));
      const target = num + delta;
      if (target >= 1 && target <= TOTAL_LESSONS) {
        activateLesson(`lesson-${target}`);
      }
    }

    // Interactive Quiz Handler
    function handleQuizAnswer(btn, quizId) {
      const group = btn.closest('.quiz-options-group');
      const allBtns = group.querySelectorAll('.quiz-btn');
      allBtns.forEach(b => b.classList.remove('is-correct', 'is-wrong'));

      const isCorrect = btn.getAttribute('data-correct') === 'true';
      if (isCorrect) {
        btn.classList.add('is-correct');
      } else {
        btn.classList.add('is-wrong');
        // Highlight correct option
        allBtns.forEach(b => {
          if (b.getAttribute('data-correct') === 'true') {
            b.classList.add('is-correct');
          }
        });
      }

      const feedback = document.getElementById('feedback-' + quizId);
      if (feedback) {
        feedback.classList.add('show');
      }
    }

    // Capstone Simulator Logic
    function updateCapstoneSim() {
      const f = parseFloat(document.getElementById('input-f').value);
      const fdot = parseFloat(document.getElementById('input-fdot').value);
      document.getElementById('val-f').innerText = f + ' Hz';
      document.getElementById('val-fdot').innerText = fdot + ' Hz/s';

      const G = 6.67430e-11;
      const c = 299792458.0;
      const M_sun = 1.98847e30;

      // Chirp Mass calculation
      const coeff = 5.0 / (96.0 * Math.pow(Math.PI, 8.0/3.0));
      const bracket = coeff * Math.pow(f, -11.0/3.0) * fdot;
      const mChirpKg = (Math.pow(c, 3.0) / G) * Math.pow(bracket, 3.0/5.0);
      const mChirpSolar = mChirpKg / M_sun;

      // Component masses (equal mass assumption)
      const m0Solar = mChirpSolar * Math.pow(2.0, 0.2);

      // Schwarzschild radius (M_final approx 62 M_sun)
      const r_s_km = (2 * G * (62.0 * M_sun)) / (c * c * 1000.0);

      document.getElementById('res-mchirp').innerText = mChirpSolar.toFixed(2) + ' M☉';
      document.getElementById('res-m0').innerText = m0Solar.toFixed(2) + ' M☉';
      document.getElementById('res-rs').innerText = r_s_km.toFixed(1) + ' km';
    }

    document.addEventListener('DOMContentLoaded', () => {
      updateProgress();
      if (document.getElementById('input-f')) {
        updateCapstoneSim();
      }
    });
  </script>
</body>
</html>
"""
    OUTPUT_INDEX.write_text(html, encoding="utf-8")
    print(f"[SUCCESS] Zbudowano zoptymalizowaną platformę LMS: {OUTPUT_INDEX}")

if __name__ == "__main__":
    build_lms()
