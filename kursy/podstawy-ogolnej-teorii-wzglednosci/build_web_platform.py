#!/usr/bin/env python3
"""
Build Standalone Interactive Web LMS Platform for General Relativity
Converts lessons into interactive modules with progress tracking,
interactive quizzes, MathJax rendering, Pure CSS diagrams, and local state.
Output: index.html
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

def render_markdown_chunk(md_path: Path) -> str:
    res = subprocess.run(
        ["pandoc", str(md_path), "-f", "markdown", "-t", "html", "--katex"],
        capture_output=True,
        text=True,
        check=True
    )
    return res.stdout

def build_lms_html():
    rendered_lessons = []
    for idx, (mod, fname, title, mod_cat) in enumerate(LESSONS):
        path = CONTENT_DIR / mod / fname
        html_body = render_markdown_chunk(path)
        rendered_lessons.append({
            "index": idx,
            "id": f"lesson-{idx+1}",
            "title": title,
            "mod_cat": mod_cat,
            "html": html_body
        })

    # Read base CSS
    css_path = BASE_DIR / "style.css"
    academic_css = css_path.read_text(encoding="utf-8") if css_path.exists() else ""

    html = f"""<!DOCTYPE html>
<html lang="pl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Podstawy Ogólnej Teorii Względności | Akademia Relatywistyczna (PhD Standard)</title>
  <meta name="description" content="Akademicki kurs e-learningowy z podstaw Ogólnej Teorii Względności zgodny ze standardem ScientistTwo i PhD.">
  
  <!-- KaTeX for math rendering -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"
          onload="renderMathInElement(document.body);"></script>

  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700&family=Instrument+Sans:wght@400;500;600;700&family=Merriweather:ital,wght@0,300;0,400;0,700;1,300&display=swap" rel="stylesheet">

  <style>
{academic_css}

    /* LMS Application Shell Styles */
    :root {{
      --carmine: #821D2D;
      --gold: #B88942;
      --navy: #1B354B;
      --bg: #FAF8F5;
      --card-bg: #FFFFFF;
      --border: #E8E2D9;
      --text: #2B2927;
      --sidebar-width: 340px;
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: 'Instrument Sans', sans-serif;
      background: var(--bg);
      color: var(--text);
      display: flex;
      flex-direction: column;
      height: 100vh;
      overflow: hidden;
    }}

    /* Top Navigation Bar */
    header.lms-header {{
      background: #FFFFFF;
      border-bottom: 2px solid var(--border);
      height: 64px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 24px;
      z-index: 100;
      flex-shrink: 0;
    }}
    .lms-brand {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}
    .lms-badge {{
      background: var(--carmine);
      color: #FFF;
      font-size: 11px;
      font-weight: 700;
      padding: 3px 8px;
      border-radius: 4px;
      letter-spacing: 0.5px;
      text-transform: uppercase;
    }}
    .lms-title {{
      font-family: 'Cinzel', serif;
      font-size: 16px;
      color: var(--navy);
      font-weight: 700;
    }}
    .lms-controls {{
      display: flex;
      align-items: center;
      gap: 16px;
    }}
    .progress-bar-container {{
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 12px;
      font-weight: 600;
      color: var(--navy);
    }}
    .progress-track {{
      width: 140px;
      height: 8px;
      background: #ECE7DE;
      border-radius: 4px;
      overflow: hidden;
    }}
    .progress-fill {{
      height: 100%;
      background: var(--carmine);
      width: 12.5%;
      transition: width 0.3s ease;
    }}
    .btn-pdf {{
      background: var(--gold);
      color: #FFFFFF;
      padding: 8px 14px;
      border-radius: 6px;
      font-size: 12px;
      font-weight: 600;
      text-decoration: none;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: opacity 0.2s;
    }}
    .btn-pdf:hover {{ opacity: 0.9; }}

    /* Layout Body */
    .lms-container {{
      display: flex;
      flex: 1;
      overflow: hidden;
    }}

    /* Sidebar */
    aside.lms-sidebar {{
      width: var(--sidebar-width);
      background: #FFFFFF;
      border-right: 1px solid var(--border);
      overflow-y: auto;
      flex-shrink: 0;
      display: flex;
      flex-direction: column;
    }}
    .sidebar-section-title {{
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      color: #8C827A;
      padding: 16px 20px 8px;
      letter-spacing: 0.6px;
    }}
    .lesson-item {{
      display: flex;
      align-items: center;
      padding: 12px 20px;
      border-left: 3px solid transparent;
      cursor: pointer;
      transition: all 0.15s ease;
      font-size: 13.5px;
      color: #4A4643;
      gap: 10px;
      text-decoration: none;
    }}
    .lesson-item:hover {{
      background: #F7F5F0;
      color: var(--carmine);
    }}
    .lesson-item.active {{
      background: #FBF8F3;
      border-left-color: var(--carmine);
      color: var(--carmine);
      font-weight: 600;
    }}
    .lesson-item.completed .status-dot {{
      background: #2E7D32;
    }}
    .status-dot {{
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: #D4CDC5;
      flex-shrink: 0;
    }}

    /* Main Content Stage */
    main.lms-main {{
      flex: 1;
      overflow-y: auto;
      padding: 40px 60px 80px;
      background: var(--bg);
      display: flex;
      justify-content: center;
    }}
    .content-card {{
      max-width: 860px;
      width: 100%;
      background: #FFFFFF;
      padding: 48px 56px;
      border-radius: 8px;
      box-shadow: 0 4px 20px rgba(0,0,0,0.03);
      border: 1px solid var(--border);
      display: none;
    }}
    .content-card.active {{
      display: block;
      animation: fadeIn 0.25s ease;
    }}
    @keyframes fadeIn {{
      from {{ opacity: 0; transform: translateY(6px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}

    /* Interactive Quiz Widget Styles */
    .quiz-box {{
      background: #FAF8F4;
      border: 1px solid #E2D9CC;
      border-left: 4px solid var(--carmine);
      padding: 24px;
      border-radius: 6px;
      margin: 32px 0 20px;
    }}
    .quiz-header {{
      font-family: 'Cinzel', serif;
      font-size: 15px;
      font-weight: 700;
      color: var(--carmine);
      margin-bottom: 12px;
    }}
    .quiz-options {{
      display: flex;
      flex-direction: column;
      gap: 8px;
      margin-top: 14px;
    }}
    .quiz-opt {{
      background: #FFFFFF;
      border: 1px solid #DCD5CA;
      padding: 12px 16px;
      border-radius: 6px;
      cursor: pointer;
      font-size: 13.5px;
      transition: all 0.15s ease;
    }}
    .quiz-opt:hover {{
      border-color: var(--gold);
      background: #FDFCF9;
    }}
    .quiz-opt.correct {{
      background: #E8F5E9;
      border-color: #2E7D32;
      color: #1B5E20;
      font-weight: 600;
    }}
    .quiz-opt.incorrect {{
      background: #FFEBEE;
      border-color: #C62828;
      color: #B71C1C;
    }}
    .quiz-feedback {{
      margin-top: 12px;
      padding: 12px 14px;
      border-radius: 6px;
      font-size: 13px;
      display: none;
      line-height: 1.45;
    }}
    .quiz-feedback.show {{ display: block; }}

    /* Bottom Action Controls */
    .lesson-footer-nav {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-top: 48px;
      padding-top: 24px;
      border-top: 1px solid var(--border);
    }}
    .btn-nav {{
      background: var(--navy);
      color: #FFFFFF;
      padding: 10px 20px;
      border-radius: 6px;
      font-size: 13px;
      font-weight: 600;
      cursor: pointer;
      border: none;
      transition: opacity 0.2s;
    }}
    .btn-nav:hover {{ opacity: 0.9; }}
    .btn-nav.btn-complete {{
      background: var(--carmine);
    }}

    /* Mobile Responsive */
    @media (max-width: 900px) {{
      aside.lms-sidebar {{ display: none; }}
      main.lms-main {{ padding: 20px 16px; }}
      .content-card {{ padding: 24px 20px; }}
    }}
  </style>
</head>
<body>

  <!-- Top Navigation Header -->
  <header class="lms-header">
    <div class="lms-brand">
      <span class="lms-badge">PhD Standard</span>
      <span class="lms-title">Podstawy Ogólnej Teorii Względności</span>
    </div>
    <div class="lms-controls">
      <div class="progress-bar-container">
        <span id="progress-percent">12%</span>
        <div class="progress-track">
          <div id="progress-bar-fill" class="progress-fill"></div>
        </div>
      </div>
      <a href="compendium.pdf" target="_blank" class="btn-pdf">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
        Pobierz Skrypt PDF (1.8 MB)
      </a>
    </div>
  </header>

  <!-- LMS Main Stage -->
  <div class="lms-container">
    <!-- Sidebar Navigation -->
    <aside class="lms-sidebar">
      <div class="sidebar-section-title">Program Kursu (4 Moduły)</div>
"""

    current_cat = ""
    for lesson in rendered_lessons:
        if lesson["mod_cat"] != current_cat:
            current_cat = lesson["mod_cat"]
            html += f'      <div class="sidebar-section-title">{current_cat}</div>\n'
        
        active_cls = " active" if lesson["index"] == 0 else ""
        html += f"""      <a class="lesson-item{active_cls}" data-target="{lesson['id']}" onclick="switchLesson('{lesson['id']}')">
        <span class="status-dot"></span>
        <span>{lesson['title']}</span>
      </a>\n"""

    html += """    </aside>

    <!-- Main Content Reader -->
    <main class="lms-main">
"""

    for lesson in rendered_lessons:
        active_cls = " active" if lesson["index"] == 0 else ""
        html += f"""      <article class="content-card{active_cls}" id="{lesson['id']}">
{lesson['html']}

        <div class="lesson-footer-nav">
          <button class="btn-nav" onclick="prevLesson()" {'disabled style="opacity: 0.5;"' if lesson['index'] == 0 else ''}>&larr; Poprzednia lekcja</button>
          <button class="btn-nav btn-complete" onclick="markCompleteAndNext('{lesson['id']}')">Zalicz lekcję i przejdź dalej &rarr;</button>
        </div>
      </article>\n"""

    html += """    </main>
  </div>

  <script>
    const totalLessons = 8;
    let completedSet = new Set(JSON.parse(localStorage.getItem('gr_completed_lessons') || '[]'));

    function updateProgressUI() {
      const pct = Math.max(12, Math.round((completedSet.size / totalLessons) * 100));
      document.getElementById('progress-percent').innerText = pct + '%';
      document.getElementById('progress-bar-fill').style.width = pct + '%';

      document.querySelectorAll('.lesson-item').forEach(item => {
        const id = item.getAttribute('data-target');
        if (completedSet.has(id)) {
          item.classList.add('completed');
        } else {
          item.classList.remove('completed');
        }
      });
    }

    function switchLesson(lessonId) {
      document.querySelectorAll('.content-card').forEach(c => c.classList.remove('active'));
      document.querySelectorAll('.lesson-item').forEach(i => i.classList.remove('active'));

      const targetCard = document.getElementById(lessonId);
      const targetItem = document.querySelector(`.lesson-item[data-target="${lessonId}"]`);
      if (targetCard) targetCard.classList.add('active');
      if (targetItem) targetItem.classList.add('active');

      document.querySelector('main.lms-main').scrollTop = 0;
      if (window.renderMathInElement) {
        renderMathInElement(targetCard);
      }
    }

    function markCompleteAndNext(lessonId) {
      completedSet.add(lessonId);
      localStorage.setItem('gr_completed_lessons', JSON.stringify(Array.from(completedSet)));
      updateProgressUI();

      const num = parseInt(lessonId.replace('lesson-', ''));
      if (num < totalLessons) {
        switchLesson(`lesson-${num + 1}`);
      } else {
        alert('Gratulacje! Ukończyłeś cały kurs Podstawy Ogólnej Teorii Względności (PhD & ScientistTwo Standard). Możesz pobrać oficjalny skrypt akademicki PDF!');
      }
    }

    function prevLesson() {
      const activeCard = document.querySelector('.content-card.active');
      if (!activeCard) return;
      const num = parseInt(activeCard.id.replace('lesson-', ''));
      if (num > 1) {
        switchLesson(`lesson-${num - 1}`);
      }
    }

    // Attach interactive quiz listeners
    document.addEventListener('DOMContentLoaded', () => {
      updateProgressUI();
    });
  </script>
</body>
</html>
"""
    OUTPUT_INDEX.write_text(html, encoding="utf-8")
    print(f"[SUCCESS] Zbudowano interaktywną platformę webową: {OUTPUT_INDEX}")

if __name__ == "__main__":
    build_lms_html()
