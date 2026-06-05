#!/usr/bin/env python3
import os
import sys
import json
import time
import urllib.request
import re

BASE_DIR = "/Users/adamsnihur/Desktop/AG projects/opracowania/filozofia_grecka"
CHAPTERS_DIR = os.path.join(BASE_DIR, "chapters")
os.makedirs(CHAPTERS_DIR, exist_ok=True)

# Load environment
def load_env(env_path="/Users/adamsnihur/Desktop/AG projects/.env"):
    env_vars = {}
    if os.path.exists(env_path):
        with open(env_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                parts = line.split("=", 1)
                if len(parts) == 2:
                    env_vars[parts[0].strip()] = parts[1].strip()
    return env_vars

ENV = load_env()
GOOGLE_KEY = None # Temporarily disabled to force OpenRouter fallback
OPENROUTER_KEY = ENV.get("OPENROUTER_API_KEY")

if not GOOGLE_KEY and not OPENROUTER_KEY:
    print("ERROR: API keys not found in .env file.", file=sys.stderr)
    sys.exit(1)

def query_llm_with_backoff(system_prompt: str, user_prompt: str, model="google/gemini-2.5-flash", max_retries=5):
    """Query LLM with exponential backoff for rate limits."""
    for attempt in range(max_retries):
        try:
            if GOOGLE_KEY:
                url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={GOOGLE_KEY}"
                headers = {"Content-Type": "application/json"}
                payload = {
                    "contents": [
                        {
                            "parts": [{"text": f"SYSTEM INSTRUCTIONS:\n{system_prompt}\n\nUSER PROMPT:\n{user_prompt}"}]
                        }
                    ],
                    "generationConfig": {
                        "temperature": 0.7
                    }
                }
                
                req = urllib.request.Request(
                    url,
                    data=json.dumps(payload).encode("utf-8"),
                    headers=headers,
                    method="POST"
                )
                
                with urllib.request.urlopen(req, timeout=60) as response:
                    res_data = json.loads(response.read().decode("utf-8"))
                    return res_data["candidates"][0]["content"]["parts"][0]["text"]
            else:
                # OpenRouter fallback
                url = "https://openrouter.ai/api/v1/chat/completions"
                headers = {
                    "Authorization": f"Bearer {OPENROUTER_KEY}",
                    "Content-Type": "application/json",
                    "HTTP-Referer": "https://github.com/adamsnihur/AGprojects",
                    "X-Title": "Antigravity Academic Writer"
                }
                payload = {
                    "model": model,
                    "messages": [
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_prompt}
                    ],
                    "temperature": 0.7
                }
                
                req = urllib.request.Request(
                    url, 
                    data=json.dumps(payload).encode("utf-8"), 
                    headers=headers, 
                    method="POST"
                )
                
                with urllib.request.urlopen(req, timeout=60) as response:
                    res_data = json.loads(response.read().decode("utf-8"))
                    return res_data["choices"][0]["message"]["content"]
                    
        except Exception as e:
            wait_time = (2 ** attempt) * 5
            print(f"Error on attempt {attempt + 1}: {e}. Waiting {wait_time}s before retry...", file=sys.stderr)
            time.sleep(wait_time)
            
    raise Exception("Max retries exceeded. Model query failed.")

# Definitions of chapters to write
SYSTEM_PROMPT = """Jesteś wybitnym historykiem filozofii i profesorem akademickim piszącym monografię naukową (poziom doktorancki) o wpływie filozofii greckiej na cywilizację zachodnią.
Wytyczne dotyczące stylu:
1. Pisz w języku polskim, zachowując najwyższą staranność stylistyczną, precyzję pojęciową oraz głęboki akademicki ton.
2. Unikaj potocyzmów, pustosłowia i uproszczeń. Analizuj niuanse pojęciowe (używaj greckich terminów jak logos, arche, eidos, hyle, physis, techne, nomos itp. w odpowiednim kontekście).
3. Objętość: Rozdział musi być bardzo obszerny (celuj w 1800 - 2500 słów). Rozwijaj argumentację w sposób pełny i wyczerpujący.
4. Pierwszy akapit każdego rozdziału musi zaczynać się od tagu HTML:
   <p class="chapter-start">Lliteratura... lub podobnie</p> (pierwsza litera duża, druga mała zduplikowana, aby poprawnie zadziałał drop cap w CSS).
5. Listy: Każda lista wypunktowana/numerowana w Markdown musi być bezwzględnie poprzedzona pustą linią, a jej elementy formatowane linijka po linijce.
6. Kod HTML (tabele, diagramy) nie może posiadać wcięć na początku linii.
7. Bezwzględnie NIE dodawaj na końcu pliku żadnych stopek w stylu "Aktywne Skille" ani "Reasoning Mythos Protocol". Zwróć wyłącznie treść rozdziału w formacie Markdown."""

CHAPTERS_SPECS = [
    {
        "filename": "chapter_00_wstep.md",
        "title": "Wstęp",
        "prompt": """Napisz wstęp do monografii naukowej.
- Temat: Wpływ filozofii greckiej na dzieje zachodniej cywilizacji.
- Sformułuj hipotezę badawczą: grecka filozofia stanowi pierwotny i nadrzędny system operacyjny (conceptual operating system) zachodniej cywilizacji, który dostarczył podstawowych kategorii ontologicznych, epistemologicznych, etycznych i politycznych determinujących bieg historii Europy.
- Przedstaw strukturę monografii (12 rozdziałów tematycznych od Presokratyków do współczesnej recepcji oraz greckich korzeni nowożytnej nauki i polityki) oraz metodologię badawczą (metoda historyczno-filozoficzna, hermeneutyka tekstów źródłowych, historia idei).
- Celuj w około 1800 słów.
- Zacznij dokładnie tak:
<p class="chapter-start">Nniniejsza monografia stawia sobie za cel rekonstrukcję...</p>"""
    },
    {
        "filename": "chapter_01_od_mitu_do_logosu.md",
        "title": "Świt racjonalizmu: Od mitu do logosu",
        "prompt": """Napisz Rozdział 1 o narodzinach myślenia racjonalnego u Presokratyków.
- Omów szkołę milezyjską (Tales, Anaksymander, Anaksymenes) i ich poszukiwania materialnego i racjonalnego *arche* wszechświata (woda, apeiron, powietrze).
- Zderz dynamiczny wariabilizm Heraklita (panta rhei, logos, walka przeciwieństw) ze statycznym monizmem szkoły eleackiej (Parmenides – byt jest, niebytu nie ma, krytyka poznania zmysłowego).
- Przedstaw pitagorejski mistyczny matematyzm (liczba jako zasada rzeczywistości) oraz atomizm Demokryta i Leucypa (atomy i próżnia, mechanistyczne wyjaśnienie przyrody).
- Celuj w około 2200 słów.
- Umieść tabelę porównawczą koncepcji arche bez wcięć:
<table class="academic-table">
<thead>
<tr><th>Filozof / Szkoła</th><th>Koncepcja Arche</th><th>Istota teorii</th></tr>
</thead>
<tbody>
...
</tbody>
</table>
- Zacznij dokładnie tak:
<p class="chapter-start">Nnarodziny filozofii w greckich koloniach Azji Mniejszej...</p>"""
    },
    {
        "filename": "chapter_02_sokrates.md",
        "title": "Sokrates i przełom antropologiczny",
        "prompt": """Napisz Rozdział 2 o Sokratesie i antropologicznym zwrocie w filozofii.
- Wyjaśnij opozycję Sokratesa wobec relatywizmu i pragmatyzmu sofistów (Protagoras).
- Omów metodę elenktyczną (zbijanie błędnych przekonań) oraz metodę maieutyczną (położniczą – wydobywanie prawdy).
- Zanalizuj intelektualizm etyczny (tożsamość cnoty i wiedzy, zło jako błąd poznawczy/niewiedza) oraz koncepcję troski o duszę (*psyche*).
- Przedstaw konflikt Sokratesa z ateńską polis, jego proces, obronę oraz znaczenie jego śmierci. Wyjaśnij pojęcie *daimoniona* jako indywidualnego głosu sumienia stojącego ponad prawem stanowionym.
- Celuj w około 2000 słów.
- Użyj bloków cytatów (<blockquote>) z Platona opisujących obronę Sokratesa.
- Zacznij dokładnie tak:
<p class="chapter-start">Sokrates z Aten pozostaje w dziejach myśli europejskiej...</p>"""
    },
    {
        "filename": "chapter_03_platon.md",
        "title": "Platon: Świat idei i metafizyczny fundament Państwa",
        "prompt": """Napisz Rozdział 3 o Platonie.
- Zbadaj teorię idei (postulowanie obiektywnego, niematerialnego i wiecznego bytu) jako odpowiedź na spór Heraklita z Parmenidesem.
- Zinterpretuj alegorię jaskini (Państwo, księga VII) jako model epistemologiczny i ontologiczny.
- Analizuj platońską teorię poznania jako anamnezy (przypominania sobie idei przez duszę) oraz jego trójdzielną koncepcję duszy (rozumna, popędliwa, pożądliwa).
- Przedstaw platońską teorię państwa idealnego – strukturę klas społecznych (filozofowie, strażnicy, żywiciele) odpowiadającą częściom duszy, koncepcję sprawiedliwości oraz krytykę demokracji i tyranii.
- Celuj w około 2500 słów.
- Dodaj tabelę analogii duszy i państwa u Platona bez wcięć:
<table class="academic-table">
<thead>
<tr><th>Część duszy</th><th>Cnota kardynalna</th><th>Klasa w Państwie</th></tr>
</thead>
<tbody>
...
</tbody>
</table>
- Zacznij dokładnie tak:
<p class="chapter-start">Pplatoński idealizm stanowi bez wątpienia punkt zwrotny...</p>"""
    },
    {
        "filename": "chapter_04_arystoteles.md",
        "title": "Arystoteles: Systematyzacja wiedzy, logika i teleologia",
        "prompt": """Napisz Rozdział 4 o Arystotelesie.
- Przedstaw jego krytykę platońskiej teorii idei (zarzut "dwojenia bytów").
- Wyjaśnij hylemorfizm (byt jako synteza materii i formy) oraz pojęcia aktu i możności.
- Omów teorię czterech przyczyn (materialna, formalna, sprawcza, celowa) oraz teleologiczną wizję kosmosu z Pierwszym Poruszycielem jako czystym aktem i celem wszechrzeczy.
- Przedstaw logiczne analizy Arystotelesa (sylogistyka, kategorie) oraz etykę złotego środka (mesotes) i koncepcję człowieka jako zoon politikon.
- Celuj w około 2500 słów.
- Dodaj tabelę porównawczą Platona i Arystotelesa bez wcięć przy użyciu `<table class="academic-table">`.
- Zacznij dokładnie tak:
<p class="chapter-start">Aarystoteles ze Stagiry, najwybitniejszy uczeń Platona...</p>"""
    },
    {
        "filename": "chapter_05_hellenizm.md",
        "title": "Hellenizm i troska o duszę: Stoicyzm, epikureizm, sceptycyzm",
        "prompt": """Napisz Rozdział 5 o filozofii epoki hellenistycznej.
- Omów stoicyzm (Zeno z Kition, Chryzyp, Seneka, Epiktet, Marek Aureliusz) – fizyka materialistyczna (pneumatyczna), dychotomia kontroli, zgoda z losem (amor fati), kosmopolityzm i cnota jako jedyne dobro.
- Przedstaw epikureizm (Epikur) – atomizm fizyczny, unikanie cierpienia (aponia) i niepokoju (ataraksja), czwórmian leczniczy (tetrapharmakos) i rola przyjaźni.
- Zanalizuj sceptycyzm (Pyrron z Elidy, Sekstus Empiryk) – powstrzymanie się od wydawania sądów (epoche) jako droga do spokoju ducha (ataraksja).
- Wykaż, jak filozofie te ukształtowały rzymską elitę i nowożytną moralność na Zachodzie.
- Celuj w około 2200 słów.
- Zacznij dokładnie tak:
<p class="chapter-start">Wwraz z upadkiem klasycznej greckiej polis...</p>"""
    },
    {
        "filename": "chapter_06_ateny_i_jerozolima.md",
        "title": "Spotkanie Aten z Jerozolimą: Filozofia grecka a wczesne chrześcijaństwo i patrystyka",
        "prompt": """Napisz Rozdział 6 o syntezie myśli greckiej z chrześcijaństwem.
- Przeanalizuj wkład Filona z Aleksandrii w syntezę judaizmu i platonizmu za pomocą metody alegorycznej i pojęcia *Logosu*.
- Omów recepcję pojęcia *Logosu* w Ewangelii wg św. Jana oraz we wczesnej patrystyce (Klemens Aleksandryjski, Orygenes – filozofia jako "wychowawca do Chrystusa").
- Zanalizuj opór wobec filozofii (Tertulian: "Co mają Ateny do Jerozolimy?").
- Przedstaw szczegółowo neoplatonizm św. Augustyna – koncepcję Boga jako najwyższego Bytu, Prawdy i Dobra, teorię iluminacji, psychologiczną interpretację Trójcy Świętej, koncepcję czasu jako wymiaru duszy oraz historiozofię Państwa Bożego.
- Celuj w około 2500 słów.
- Zacznij dokładnie tak:
<p class="chapter-start">Ssłynne pytanie Tertuliana: "Co mają Ateny do Jerozolimy?"...</p>"""
    },
    {
        "filename": "chapter_07_scholastyka.md",
        "title": "Scholastyka średniowieczna: Synteza tomistyczna i spór o uniwersalia",
        "prompt": """Napisz Rozdział 7 o średniowiecznym arystotelizmie i scholastyce.
- Przedstaw spór o uniwersalia (powszechniki) – realizm skrajny (Wilhelm z Champeaux), realizm umiarkowany (Abelard, Tomasz), konceptualizm i nominalizm (Wilhelm Ockham i jego brzytwa).
- Analizuj wielką syntezę tomistyczną św. Tomasza z Akwinu – chrześcijańską adaptację Arystotelesa, rozróżnienie między istotą (essentia) a istnieniem (existentia), relację rozumu i wiary (rozum jako przedsionek wiary), oraz pięć dróg rozumowego dowodzenia istnienia Boga (quinque viae).
- Pokaż, jak ta synteza stała się oficjalną nauką Kościoła rzymskokatolickiego.
- Celuj w około 2500 słów.
- Dodaj tabelę porównawczą stanowisk w sporze o uniwersalia bez wcięć przy użyciu `<table class="academic-table">`.
- Zacznij dokładnie tak:
<p class="chapter-start">Sśredniowiecze, wbrew dawnym uproszczonym opiniom...</p>"""
    },
    {
        "filename": "chapter_08_renesans.md",
        "title": "Renesansowy powrót do źródeł: Humanizm i neoplatonizm florencki",
        "prompt": """Napisz Rozdział 8 o renesansowym renesansie platonizmu.
- Omów rewolucję intelektualną związaną z hasłem *ad fontes* (do źródeł) i ponownym odkryciem tekstów greckich po upadku Konstantynopola (1453).
- Przedstaw historię Akademii Florenckiej, rolę Kosmy Medyceusza oraz przekłady i komentarze Marsilio Ficina (platonizm, hermetyzm).
- Zanalizuj antropologiczne manifesty renesansu, zwłaszcza Giovanniego Pico della Mirandola *Mowę o godności człowieka* (wolność woli człowieka jako istoty umieszczonej w centrum kosmosu).
- Przedstaw chrześcijański humanizm Erazma z Rotterdamu i Thomasa More'a oraz ich inspiracje etyką grecką.
- Celuj w około 2000 słów.
- Zacznij dokładnie tak:
<p class="chapter-start">Rrenesansowy postulat ad fontes ("do źródeł")...</p>"""
    },
    {
        "filename": "chapter_09_nowozytnosc.md",
        "title": "Nowożytny racjonalizm i empiryzm jako spadkobiercy greckich pytań",
        "prompt": """Napisz Rozdział 9 o nowożytnej recepcji filozofii greckiej.
- Wykaż, że nowożytny racjonalizm kontynuuje platońską koncepcję poznania – przeanalizuj Kartezjusza (idee wrodzone, dualizm res cogitans i res extensa) oraz Spinozę (monizm substancjalny nawiązujący do Parmenidesa i panteistycznego fizykalizmu stoików).
- Zderz to z empiryzmem brytyjskim (Locke, Hume) i jego zakorzenieniem w arystotelesowskiej koncepcji tabula rasa i epikurejskim sensualizmie.
- Analizuj syntezę Immanuela Kanta – formy aprioryczne zmysłowości i kategorie intelektu jako nowożytne przekształcenie platońskich idei i arystotelesowskich kategorii.
- Celuj w około 2500 słów.
- Zacznij dokładnie tak:
<p class="chapter-start">Nnowożytny przełom epistemologiczny, zapoczątkowany przez...</p>"""
    },
    {
        "filename": "chapter_10_xix_xx_wiek.md",
        "title": "Filozofia grecka w XIX i XX wieku: Hegel, Nietzsche i kryzys metafizyki",
        "prompt": """Napisz Rozdział 10 o recepcji myśli greckiej w XIX i XX wieku.
- Analizuj idealizm absolutny G.W.F. Hegla – jego koncepcję dialektyki Ducha jako rozwinięcie heraklitejskiej walki przeciwieństw i syntezy.
- Zbadaj głęboką dekonstrukcję tradycji sokratejsko-platońskiej u Fryderyka Nietzschego – dychotomia apolińskość vs dionizyjskość, oskarżenie Sokratesa o uśmiercenie greckiej tragedii i instynktu życiowego, oraz powrót do filozofii przedsokratycznej.
- Omów egzystencjalizm i fenomenologię XX wieku, w szczególności projekt Martina Heideggera polegający na przezwyciężeniu zapomnienia bytu (Seinsvergessenheit) poprzez powrót do pytań wczesnych Greków (Parmenidesa, Heraklita).
- Celuj w około 2200 słów.
- Zacznij dokładnie tak:
<p class="chapter-start">Wwiek dziewiętnasty i dwudziesty przyniosły...</p>"""
    },
    {
        "filename": "chapter_11_korzenie_nauki.md",
        "title": "Greckie korzenie nauki nowożytnej i współczesnej",
        "prompt": """Napisz Rozdział 11 o greckiej genezie nauki.
- Analizuj narodziny koncepcji racjonalnej kosmologii (świat jako kosmos – uporządkowana całość podlegająca powszechnym prawom).
- Przedstaw platońsko-pitagorejski postulat, że księga przyrody napisana jest językiem matematyki (wpływ na Galileusza, Keplera, Newtona).
- Zbadaj powrót nowożytnego mechanicyzmu (Gassendi, Boyle) do atomizmu Demokryta i Epikura.
- Omów, jak arystotelesowski empiryzm i taksonomia stworzyły podwaliny pod nowożytną biologię i nauki przyrodnicze.
- Celuj w około 2200 słów.
- Zacznij dokładnie tak:
<p class="chapter-start">Wwspółczesna nauka, mimo swoich skomplikowanych metod...</p>"""
    },
    {
        "filename": "chapter_12_polityka_prawo_etyka.md",
        "title": "Demokracja, prawo i etyka publiczna: Antyczny fundament zachodniej polityki",
        "prompt": """Napisz Rozdział 12 o wpływie greckiej myśli politycznej i etycznej.
- Zbadaj narodziny i funkcjonowanie ateńskiej demokracji bezpośredniej (*isonomia*, *isegoria*) oraz jej wpływ na nowożytne teorie republikańskie i demokratyczne (Rousseau).
- Zanalizuj arystotelesowską koncepcję rządów prawa (praworządność – prawa powinny rządzić, a nie ludzie) oraz pojęcie dobra wspólnego.
- Omów koncepcję prawa naturalnego (ius naturale) u stoików, jej rozwój przez Cycerona, oraz recepcję w nowożytnym prawie międzynarodowym (Grocjusz) i w Deklaracjach Praw Człowieka.
- Celuj w około 2200 słów.
- Zacznij dokładnie tak:
<p class="chapter-start">Zzachodni model polityczny opiera się na fundamencie...</p>"""
    },
    {
        "filename": "chapter_13_zakonczenie.md",
        "title": "Zakończenie",
        "prompt": """Napisz zakończenie monografii naukowej.
- Dokonaj syntetycznego i głębokiego podsumowania drogi rozwojowej, jaką odbyła myśl grecka w zachodniej kulturze.
- Potwierdź hipotezę o filozofii greckiej jako 'systemie operacyjnym' Zachodu.
- Odnieś się do współczesnego kryzysu tożsamości zachodniej cywilizacji w kontekście posthumanizmu, sztucznej inteligencji i sekularyzacji, wskazując na konieczność powrotu do greckich pytań o byt, prawdę (*aletheia*), dobro (*agathon*) i piękno (*kalon*).
- Celuj w około 1800 słów.
- Zacznij dokładnie tak:
<p class="chapter-start">Pprzemierzając dzieje zachodniej myśli...</p>"""
    },
    {
        "filename": "chapter_14_bibliografia.md",
        "title": "Bibliografia",
        "prompt": """Napisz bibliografię monografii naukowej.
- Przedstaw listę co najmniej 25 kluczowych, klasycznych i współczesnych dzieł naukowych (np. Werner Jaeger - Paideia, Giovanni Reale - Historia filozofii starożytnej, Władysław Tatarkiewicz - Historia filozofii, W.K.C. Guthrie - A History of Greek Philosophy, Diels-Kranz - Fragmente der Vorsokratiker, wydania krytyczne dzieł Platona i Arystotelesa w Bibliotece Klasyków Filozofii PWN, oraz monografie współczesne z zakresu recepcji filozofii greckiej).
- Wszystkie pozycje bibliograficzne muszą posiadać rzeczywiste numery DOI lub oficjalne dane wydawnicze (Zasada **Zero-Hallucination DOI Policy**). Przykłady realnych DOI dla klasyków: Jaeger Paideia (Oxford University Press), Reale (KUL), itp. Zweryfikuj ich istnienie.
- Formatuj bibliografię elegancko, stosując odpowiednie puste linie między wpisami.
- Zacznij dokładnie tak:
# Bibliografia

oraz poniżej umieść listę pozycji."""
    }
]

def generate_all_chapters():
    print("=== STARTING SEQUENTIAL CHAPTER GENERATION ===")
    for idx, spec in enumerate(CHAPTERS_SPECS):
        filename = spec["filename"]
        filepath = os.path.join(CHAPTERS_DIR, filename)
        
        # Check if already generated to support resuming
        if os.path.exists(filepath) and os.path.getsize(filepath) > 1000:
            print(f"[{idx+1}/{len(CHAPTERS_SPECS)}] Chapter {filename} already exists. Skipping.")
            continue
            
        print(f"[{idx+1}/{len(CHAPTERS_SPECS)}] Generating {filename} ({spec['title']})...")
        user_prompt = f"Rozdział: {spec['title']}\nWytyczne:\n{spec['prompt']}"
        
        try:
            content = query_llm_with_backoff(SYSTEM_PROMPT, user_prompt)
            # Write to file
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"[{idx+1}/{len(CHAPTERS_SPECS)}] Successfully saved {filename}.")
        except Exception as e:
            print(f"FATAL ERROR generating {filename}: {e}", file=sys.stderr)
            sys.exit(1)
            
        # Wait between calls to avoid rate limits
        print("Sleeping 10s to manage API rate limit...")
        time.sleep(10)
        
    print("=== ALL CHAPTERS GENERATED SUCCESSFULLY ===")

if __name__ == "__main__":
    generate_all_chapters()
