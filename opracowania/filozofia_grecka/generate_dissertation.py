#!/usr/bin/env python3
import os
import sys
import json
import time
import urllib.request
import re

BASE_DIR = "/Users/adamsnihur/Desktop/AG projects/opracowania/filozofia_grecka"
CHAPTERS_DIR = os.path.join(BASE_DIR, "chapters")
RAW_DIR = os.path.join(BASE_DIR, "chapters_raw")
os.makedirs(CHAPTERS_DIR, exist_ok=True)
os.makedirs(RAW_DIR, exist_ok=True)

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
GOOGLE_KEY = ENV.get("GOOGLE_API_KEY")

if not GOOGLE_KEY:
    print("ERROR: GOOGLE_API_KEY not found in .env file.", file=sys.stderr)
    sys.exit(1)

def query_llm_with_backoff(system_prompt: str, user_prompt: str, max_retries=5):
    """Query direct Gemini API with exponential backoff for rate limits."""
    for attempt in range(max_retries):
        try:
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
                    
        except Exception as e:
            wait_time = (2 ** attempt) * 5
            print(f"Error on attempt {attempt + 1}: {e}. Waiting {wait_time}s before retry...", file=sys.stderr)
            time.sleep(wait_time)
            
    raise Exception("Max retries exceeded. Model query failed.")

SYSTEM_PROMPT = """Jesteś wybitnym historykiem filozofii i profesorem akademickim piszącym monografię naukową (poziom doktorancki) o wpływie filozofii greckiej na cywilizację zachodnią.
Wytyczne dotyczące stylu:
1. Pisz w języku polskim, zachowując najwyższą staranność stylistyczną, precyzję pojęciową oraz głęboki akademicki ton.
2. Analizuj niuanse pojęciowe w sposób niezwykle szczegółowy i wyczerpujący. Unikaj powtórzeń, ale rozwijaj myśli, podając przykłady historyczne i analizując dzieła źródłowe.
3. Objętość: Generowany podrozdział musi być bardzo obszerny (celuj w 1500 - 2000 słów). Rozpisz się szeroko na zadany temat.
4. Nagłówki: Używaj odpowiednich nagłówków Markdown (np. ### lub ####) dla sekcji. Nie dodawaj nagłówków H1 (#), ponieważ pliki sekcji zostaną połączone pod jednym H1.
5. Pierwszy akapit: Nie dodawaj tagu <p class="chapter-start"> w sekcjach, ponieważ zostanie on dodany automatycznie na początku całego rozdziału podczas łączenia.
6. Listy: Każda lista w Markdown musi być bezwzględnie poprzedzona pustą linią, a jej elementy formatowane linijka po linijce.
7. Kod HTML (tabele, diagramy) nie może posiadać wcięć na początku linii.
8. Bezwzględnie NIE dodawaj na końcu pliku żadnych stopek w stylu "Aktywne Skille" ani "Reasoning Mythos Protocol". Zwróć wyłącznie treść podrozdziału w formacie Markdown."""

# Outline of all sections to generate
SECTIONS = [
    # WSTĘP
    {
        "chapter": "chapter_00_wstep.md",
        "title": "Wstęp",
        "section_id": "00_1",
        "prompt": "Napisz Podrozdział 1 Wstępu: 'Cel badawczy i status metodologiczny monografii'. Przedstaw hipotezę badawczą: filozofia grecka jako 'system operacyjny' zachodniej cywilizacji, który ukształtował ramy myślowe Europy. Omów cel badawczy monografii, analizując jak greckie kategorie (byt, logos, physis) ufundowały zachodnią naukę, politykę i teologię."
    },
    {
        "chapter": "chapter_00_wstep.md",
        "title": "Wstęp",
        "section_id": "00_2",
        "prompt": "Napisz Podrozdział 2 Wstępu: 'Stan badań nad recepcją antyku w historiografii filozoficznej'. Przeanalizuj kluczowe stanowiska badawcze od G.W.F. Hegla, przez Wernera Jaegera (koncepcja paidei), aż po współczesne analizy Pierre'a Hadota (filozofia jako sztuka życia) oraz Leo Straussa."
    },
    {
        "chapter": "chapter_00_wstep.md",
        "title": "Wstęp",
        "section_id": "00_3",
        "prompt": "Napisz Podrozdział 3 Wstępu: 'Zarys metodologiczny i struktura pracy'. Opisz zastosowanie metody historyczno-filozoficznej, hermeneutyki tekstów źródłowych oraz historii idei w analizie procesów recepcyjnych. Omów strukturę monografii."
    },
    # ROZDZIAŁ 1
    {
        "chapter": "chapter_01_od_mitu_do_logosu.md",
        "title": "Świt racjonalizmu: Od mitu do logosu",
        "section_id": "01_1",
        "prompt": "Napisz Podrozdział 1.1: 'Kosmologia szkoły milezyjskiej'. Analizuj Talesa, Anaksymandra i Anaksymenesa. Omów przejście od mitologii (Homer, Hezjod) do logosu. Przedstaw szczegółowo poszukiwanie racjonalnego, materialnego *arche* kosmosu (woda, apeiron, powietrze) oraz koncepcję hlozoizmu."
    },
    {
        "chapter": "chapter_01_od_mitu_do_logosu.md",
        "title": "Świt racjonalizmu: Od mitu do logosu",
        "section_id": "01_2",
        "prompt": "Napisz Podrozdział 1.2: 'Wariabilizm i dialektyka Heraklita z Efezu'. Analizuj postulat powszechnego stawania się (panta rhei), rolę ognia jako arche, oraz koncepcję kosmicznego Logos jako zasady porządkującej walkę i jedność przeciwieństw."
    },
    {
        "chapter": "chapter_01_od_mitu_do_logosu.md",
        "title": "Świt racjonalizmu: Od mitu do logosu",
        "section_id": "01_3",
        "prompt": "Napisz Podrozdział 1.3: 'Ontologia szkoły eleackiej'. Zbadaj Parmenidesa i jego monizm bytowy ('byt jest, niebytu nie ma'). Analizuj krytykę poznania zmysłowego na rzecz poznania rozumowego. Omów paradoksy Zenona z Elei jako formalne dowody przeciwko ruchowi i wielości."
    },
    {
        "chapter": "chapter_01_od_mitu_do_logosu.md",
        "title": "Świt racjonalizmu: Od mitu do logosu",
        "section_id": "01_4",
        "prompt": "Napisz Podrozdział 1.4: 'Matematyzacja i atomizm: Pitagoras i Demokryt'. Omów pitagorejską koncepcję liczby jako zasady wszechświata oraz atomizm Demokryta i Leucypa (atomy, próżnia, mechanicyzm). Dodaj tabelę porównawczą arche milezyjczyków, Heraklita, Parmenidesa i Demokryta przy użyciu `<table class=\"academic-table\">`."
    },
    # ROZDZIAŁ 2
    {
        "chapter": "chapter_02_sokrates.md",
        "title": "Sokrates i przełom antropologiczny",
        "section_id": "02_1",
        "prompt": "Napisz Podrozdział 2.1: 'Sofistyczny relatywizm jako tło przełomu antropologicznego'. Przeanalizuj działalność sofistów (Protagoras – człowiek miarą wszechrzeczy, Gorgiasz – nihilizm poznawczy) i ich wkład w rozwój retoryki, humanizmu i relatywizmu etycznego."
    },
    {
        "chapter": "chapter_02_sokrates.md",
        "title": "Sokrates i przełom antropologiczny",
        "section_id": "02_2",
        "prompt": "Napisz Podrozdział 2.2: 'Metoda sokratejska: Elenktyka i maieutyka'. Zbadaj mechanizm dialektyczny Sokratesa. Wyjaśnij metodę elenktyczną (zbijanie fałszywych przekonań) i maieutyczną (położniczą) jako rewolucję w epistemologii i dialogu."
    },
    {
        "chapter": "chapter_02_sokrates.md",
        "title": "Sokrates i przełom antropologiczny",
        "section_id": "02_3",
        "prompt": "Napisz Podrozdział 2.3: 'Intelektualizm etyczny Sokratesa'. Przeanalizuj tożsamość wiedzy i cnoty (*arete*), koncepcję cnoty jako dobra bezwzględnego oraz troskę o duszę (*psyche*) jako centrum ludzkiej podmiotowości."
    },
    {
        "chapter": "chapter_02_sokrates.md",
        "title": "Sokrates i przełom antropologiczny",
        "section_id": "02_4",
        "prompt": "Napisz Podrozdział 2.4: 'Proces Sokratesa i dziedzictwo Daimoniona'. Zanalizuj polityczne i moralne tło skazania Sokratesa, jego odmowę ucieczki z więzienia (posłuszeństwo wobec praw polis) oraz koncepcję *daimoniona* jako głosu wewnętrznego sumienia. Użyj cytatów z *Obrony Sokratesa* Platona przy użyciu `<blockquote>`."
    },
    # ROZDZIAŁ 3
    {
        "chapter": "chapter_03_platon.md",
        "title": "Platon: Świat idei i metafizyczny fundament Państwa",
        "section_id": "03_1",
        "prompt": "Napisz Podrozdział 3.1: 'Teoria Idei i dualizm metafizyczny Platona'. Przeanalizuj podział na świat zmysłowy (*horatos topos*) i intelligibilny (*noetos topos*). Szczegółowo zinterpretuj alegorię jaskini z *Państwa* (Księga VII)."
    },
    {
        "chapter": "chapter_03_platon.md",
        "title": "Platon: Świat idei i metafizyczny fundament Państwa",
        "section_id": "03_2",
        "prompt": "Napisz Podrozdział 3.2: 'Epistemologia platońska: Anamneza i stopnie poznania'. Omów teorię poznania jako przypominania sobie idei (*anamnesis*), metaforę linii podzielonej oraz rolę dialektyki i miłości (*eros*) w drodze do Absolutu."
    },
    {
        "chapter": "chapter_03_platon.md",
        "title": "Platon: Świat idei i metafizyczny fundament Państwa",
        "section_id": "03_3",
        "prompt": "Napisz Podrozdział 3.3: 'Teoria duszy i jej eschatologia'. Zanalizuj trójdzielną koncepcję duszy (rozumna, popędliwa, pożądliwa) i jej cnoty kardynalne. Omów dowody na nieśmiertelność duszy z *Fedona* i mit o Erze z *Państwa*."
    },
    {
        "chapter": "chapter_03_platon.md",
        "title": "Platon: Świat idei i metafizyczny fundament Państwa",
        "section_id": "03_4",
        "prompt": "Napisz Podrozdział 3.4: 'Projekt ustrojowy w Państwie i Prawach'. Zbadaj platońską koncepcję państwa idealnego – strukturę klas społecznych (filozofowie, wojownicy, rzemieślnicy), ideę sprawiedliwości oraz krytykę demokracji i tyranii. Dodaj tabelę analogii duszy i państwa przy użyciu `<table class=\"academic-table\">`."
    },
    # ROZDZIAŁ 4
    {
        "chapter": "chapter_04_arystoteles.md",
        "title": "Arystoteles: Systematyzacja wiedzy, logika i teleologia",
        "section_id": "04_1",
        "prompt": "Napisz Podrozdział 4.1: 'Krytyka Platona i sformułowanie hylemorfizmu'. Przeanalizuj krytykę teorii idei ('trzeci człowiek', 'dwojenie bytów'). Omów hylemorfizm (byt jako kompozycja materii, *hyle*, i formy, *morphe*) oraz parę pojęciową aktu (*energeia*) i możności (*dynamis*)."
    },
    {
        "chapter": "chapter_04_arystoteles.md",
        "title": "Arystoteles: Systematyzacja wiedzy, logika i teleologia",
        "section_id": "04_2",
        "prompt": "Napisz Podrozdział 4.2: 'Cztery przyczyny i teleologia kosmiczna'. Zbadaj teorię przyczyn (materialna, formalna, sprawcza, celowa). Przeanalizuj kosmologiczną koncepcję Pierwszego Poruszyciela jako czystego aktu i ostatecznego celu wszechświata."
    },
    {
        "chapter": "chapter_04_arystoteles.md",
        "title": "Arystoteles: Systematyzacja wiedzy, logika i teleologia",
        "section_id": "04_3",
        "prompt": "Napisz Podrozdział 4.3: 'Logika jako organon nauki'. Przeanalizuj sylogistykę, teorię kategorii i metodologię naukową Arystotelesa, stanowiące fundament dedukcji i klasyfikacji zachodniej."
    },
    {
        "chapter": "chapter_04_arystoteles.md",
        "title": "Arystoteles: Systematyzacja wiedzy, logika i teleologia",
        "section_id": "04_4",
        "prompt": "Napisz Podrozdział 4.4: 'Etyka cnót i człowiek jako zoon politikon'. Omów etykę złotego środka (*mesotes*), podział na cnoty etyczne i dianoetyczne, szczęście (*eudaimonia*) oraz koncepcję człowieka jako istoty społeczno-politycznej. Dodaj tabelę porównawczą metafizyki Platona i Arystotelesa przy użyciu `<table class=\"academic-table\">`."
    },
    # ROZDZIAŁ 5
    {
        "chapter": "chapter_05_hellenizm.md",
        "title": "Hellenizm i troska o duszę: Stoicyzm, epikureizm, sceptycyzm",
        "section_id": "05_1",
        "prompt": "Napisz Podrozdział 5.1: 'Stoicyzm i etyka kosmicznego determinizmu'. Omów fizykę (pneuma, kosmiczny ogień), fatalizm, dychotomię kontroli (Epiktet), kosmopolityzm, oraz cnotę jako jedyne i samowystarczalne dobro (Seneka, Marek Aureliusz)."
    },
    {
        "chapter": "chapter_05_hellenizm.md",
        "title": "Hellenizm i troska o duszę: Stoicyzm, epikureizm, sceptycyzm",
        "section_id": "05_2",
        "prompt": "Napisz Podrozdział 5.2: 'Epikureizm i hedonizm umiarkowany'. Zbadaj atomistyczną fizykę Epikura, koncepcję braku cierpienia (*aponia*) i niepokoju (*ataraksja*), oraz czwórmian leczniczy (*tetrapharmakos*). Omów rolę ogrodu i przyjaźni."
    },
    {
        "chapter": "chapter_05_hellenizm.md",
        "title": "Hellenizm i troska o duszę: Stoicyzm, epikureizm, sceptycyzm",
        "section_id": "05_3",
        "prompt": "Napisz Podrozdział 5.3: 'Sceptycyzm pyrroński i zawieszenie sądu'. Analizuj Pyrrona i Sekstusa Empiryka. Omów zawieszenie sądów (*epoche*) jako jedyną drogę do ataraksji oraz krytykę dogmatyzmu innych szkół."
    },
    {
        "chapter": "chapter_05_hellenizm.md",
        "title": "Hellenizm i troska o duszę: Stoicyzm, epikureizm, sceptycyzm",
        "section_id": "05_4",
        "prompt": "Napisz Podrozdział 5.4: 'Wpływ etyki hellenistycznej na Rzym i chrześcijaństwo'. Pokaż jak stoicyzm wpłynął na rzymskie elity (Cyceron, Seneka) oraz wczesnochrześcijańską etykę i ascezę."
    },
    # ROZDZIAŁ 6
    {
        "chapter": "chapter_06_ateny_i_jerozolima.md",
        "title": "Spotkanie Aten z Jerozolimą: Filozofia grecka a wczesne chrześcijaństwo i patrystyka",
        "section_id": "06_1",
        "prompt": "Napisz Podrozdział 6.1: 'Filon z Aleksandrii i metoda alegoryczna'. Analizuj syntezę judaizmu i platonizmu, interpretację Pisma Świętego oraz koncepcję *Logosu* jako pośrednika między transcendentnym Bogiem a światem."
    },
    {
        "chapter": "chapter_06_ateny_i_jerozolima.md",
        "title": "Spotkanie Aten z Jerozolimą: Filozofia grecka a wczesne chrześcijaństwo i patrystyka",
        "section_id": "06_2",
        "prompt": "Napisz Podrozdział 6.2: 'Logos w Nowym Testamencie i apologetyce chrześcijańskiej'. Przeanalizuj Prolog Ewangelii wg św. Jana i chrystologiczną reinterpretację Logosu (wcielenie). Omów koncepcję *Logosu spermatikos* u Justyna Męczennika."
    },
    {
        "chapter": "chapter_06_ateny_i_jerozolima.md",
        "title": "Spotkanie Aten z Jerozolimą: Filozofia grecka a wczesne chrześcijaństwo i patrystyka",
        "section_id": "06_3",
        "prompt": "Napisz Podrozdział 6.3: 'Spór o hellenizację: Aleksandryjczycy vs Tertulian'. Przedstaw stanowisko Klemensa Aleksandryjskiego i Orygenesa (filozofia jako przygotowanie do Ewangelii) w opozycji do radykalizmu Tertuliana ('Co mają Ateny do Jerozolimy?')."
    },
    {
        "chapter": "chapter_06_ateny_i_jerozolima.md",
        "title": "Spotkanie Aten z Jerozolimą: Filozofia grecka a wczesne chrześcijaństwo i patrystyka",
        "section_id": "06_4",
        "prompt": "Napisz Podrozdział 6.4: 'Wielka synteza św. Augustyna'. Zbadaj neoplatońskie inspiracje Augustyna (Plotyn), koncepcję Boga jako Bytu, Prawdy i Dobra, teorię iluminacji (*illuminatio*), psychologiczny model Trójcy, teorię czasu oraz historiozofię w *De Civitate Dei*."
    },
    # ROZDZIAŁ 7
    {
        "chapter": "chapter_07_scholastyka.md",
        "title": "Scholastyka średniowieczna: Synteza tomistyczna i spór o uniwersalia",
        "section_id": "07_1",
        "prompt": "Napisz Podrozdział 7.1: 'Spór o uniwersalia w filozofii średniowiecznej'. Przeanalizuj stanowiska: realizm skrajny, realizm umiarkowany, konceptualizm i nominalizm (Wilhelm Ockham i jego brzytwa). Pokaż ich metafizyczne konsekwencje."
    },
    {
        "chapter": "chapter_07_scholastyka.md",
        "title": "Scholastyka średniowieczna: Synteza tomistyczna i spór o uniwersalia",
        "section_id": "07_2",
        "prompt": "Napisz Podrozdział 7.2: 'Tomistyczna synteza arystotelizmu'. Zbadaj św. Tomasza z Akwinu i jego adaptację Arystotelesa. Omów podział na wiarę i rozum, oraz dystynkcję między istotą (*essentia*) a istnieniem (*existentia*)."
    },
    {
        "chapter": "chapter_07_scholastyka.md",
        "title": "Scholastyka średniowieczna: Synteza tomistyczna i spór o uniwersalia",
        "section_id": "07_3",
        "prompt": "Napisz Podrozdział 7.3: 'Pięć dróg św. Tomasza do Boga'. Przeanalizuj logiczną i kosmologiczną strukturę *quinque viae*, wykazując ich bezpośrednie zakorzenienie w fizyce i teleologii Arystotelesa (ruch, przyczyna, cel)."
    },
    {
        "chapter": "chapter_07_scholastyka.md",
        "title": "Scholastyka średniowieczna: Synteza tomistyczna i spór o uniwersalia",
        "section_id": "07_4",
        "prompt": "Napisz Podrozdział 7.4: 'Wpływ scholastyki na kulturę intelektualną Zachodu'. Zanalizuj narodziny uniwersytetów, rozwój disputatio i racjonalną metodę badania dogmatów. Dodaj tabelę porównawczą stanowisk w sporze o uniwersalia bez wcięć przy użyciu `<table class=\"academic-table\">`."
    },
    # ROZDZIAŁ 8
    {
        "chapter": "chapter_08_renesans.md",
        "title": "Renesansowy powrót do źródeł: Humanizm i neoplatonizm florencki",
        "section_id": "08_1",
        "prompt": "Napisz Podrozdział 8.1: 'Postulat ad fontes i Akademia Florencka'. Analizuj odkrycie tekstów greckich (upadek Konstantynopola), rolę Kosmy Medyceusza oraz przekłady i chrześcijański platonizm Marsilio Ficina."
    },
    {
        "chapter": "chapter_08_renesans.md",
        "title": "Renesansowy powrót do źródeł: Humanizm i neoplatonizm florencki",
        "section_id": "08_2",
        "prompt": "Napisz Podrozdział 8.2: 'Antropologia Giovanniego Pico della Mirandola'. Przeanalizuj *Mowę o godności człowieka* jako manifest renesansowego neoplatonizmu i koncepcję wolnej woli człowieka jako istoty twórczej."
    },
    {
        "chapter": "chapter_08_renesans.md",
        "title": "Renesansowy powrót do źródeł: Humanizm i neoplatonizm florencki",
        "section_id": "08_3",
        "prompt": "Napisz Podrozdział 8.3: 'Renesansowy arystotelizm i szkoła padewska'. Omów arystotelizm renesansowy (Pomponazzi, Zabarella) w opozycji do platonizmu florenckiego, jego badania nad duszą oraz autonomię nauk przyrodniczych."
    },
    {
        "chapter": "chapter_08_renesans.md",
        "title": "Renesansowy powrót do źródeł: Humanizm i neoplatonizm florencki",
        "section_id": "08_4",
        "prompt": "Napisz Podrozdział 8.4: 'Erazm z Rotterdamu i humanizm chrześcijański'. Pokaż, jak idee tolerancji, edukacji i filologii greckiej Nowego Testamentu Erazma ufundowały nowożytny humanizm europejski."
    },
    # ROZDZIAŁ 9
    {
        "chapter": "chapter_09_nowozytnosc.md",
        "title": "Nowożytny racjonalizm i empiryzm jako spadkobiercy greckich pytań",
        "section_id": "09_1",
        "prompt": "Napisz Podrozdział 9.1: 'Kartezjusz i platoński natywizm'. Analizuj racjonalizm Kartezjusza, wątpienie metodologiczne, koncepcję idei wrodzonych (nawiązanie do Platona) oraz dualizm psychofizyczny."
    },
    {
        "chapter": "chapter_09_nowozytnosc.md",
        "title": "Nowożytny racjonalizm i empiryzm jako spadkobiercy greckich pytań",
        "section_id": "09_2",
        "prompt": "Napisz Podrozdział 9.2: 'Monizm i substancja: Spinoza i Leibniz'. Przeanalizuj panteistyczny monizm Spinozy (nawiązania do Parmenidesa i stoików) oraz pluralistyczną monadologię Leibniza w odniesieniu do greckiej metafizyki."
    },
    {
        "chapter": "chapter_09_nowozytnosc.md",
        "title": "Nowożytny racjonalizm i empiryzm jako spadkobiercy greckich pytań",
        "section_id": "09_3",
        "prompt": "Napisz Podrozdział 9.3: 'Empiryzm brytyjski: Locke i Hume'. Zbadaj koncepcję *tabula rasa* Johna Locke'a (arystotelesowskie korzenie) oraz sceptycyzm Davida Hume'a (wpływ sceptyków antycznych i epikurejskiego sensualizmu)."
    },
    {
        "chapter": "chapter_09_nowozytnosc.md",
        "title": "Nowożytny racjonalizm i empiryzm jako spadkobiercy greckich pytań",
        "section_id": "09_4",
        "prompt": "Napisz Podrozdział 9.4: 'Synteza transcendentalna Immanuela Kanta'. Analizuj rewolucję kopernikańską Kanta, formy aprioryczne i kategorie rozsądku jako syntezę platońskiego natywizmu i arystotelesowskiej systematyzacji naukowej."
    },
    # ROZDZIAŁ 10
    {
        "chapter": "chapter_10_xix_xx_wiek.md",
        "title": "Filozofia grecka w XIX i XX wieku: Hegel, Nietzsche i kryzys metafizyki",
        "section_id": "10_1",
        "prompt": "Napisz Podrozdział 10.1: 'Idealizm absolutny Hegla i dialektyka'. Analizuj system Hegla, koncepcję stawania się i dialektyki Ducha jako historyczne rozwinięcie dynamicznej kosmologii Heraklita."
    },
    {
        "chapter": "chapter_10_xix_xx_wiek.md",
        "title": "Filozofia grecka w XIX i XX wieku: Hegel, Nietzsche i kryzys metafizyki",
        "section_id": "10_2",
        "prompt": "Napisz Podrozdział 10.2: 'Nietzsche i krytyka sokratyzmu'. Analizuj dychotomię Apollina i Dionizosa w *Narodzinach tragedii*, oskarżenie Sokratesa o racjonalizację i degenerację kultury, oraz koncepcję woli mocy jako powrót do Presokratyków."
    },
    {
        "chapter": "chapter_10_xix_xx_wiek.md",
        "title": "Filozofia grecka w XIX i XX wieku: Hegel, Nietzsche i kryzys metafizyki",
        "section_id": "10_3",
        "prompt": "Napisz Podrozdział 10.3: 'Martin Heidegger i przezwyciężenie zapomnienia bytu'. Analizuj krytykę metafizyki zachodniej jako zapomnienia bytu (*Seinsvergessenheit*) od Platona. Zbadaj jego powrót do Parmenidesa i Heraklita oraz koncepcję prawdy jako nieukrytości (*aletheia*)."
    },
    {
        "chapter": "chapter_10_xix_xx_wiek.md",
        "title": "Filozofia grecka w XIX i XX wieku: Hegel, Nietzsche i kryzys metafizyki",
        "section_id": "10_4",
        "prompt": "Napisz Podrozdział 10.4: 'Fenomenologia i hermeneutyka XX wieku'. Pokaż recepcję myśli greckiej u Edmunda Husserla, Jean-Paula Sartre'a oraz w hermeneutyce Hansa-Georga Gadamera (dialog i tradycja)."
    },
    # ROZDZIAŁ 11
    {
        "chapter": "chapter_11_korzenie_nauki.md",
        "title": "Greckie korzenie nauki nowożytnej i współczesnej",
        "section_id": "11_1",
        "prompt": "Napisz Podrozdział 11.1: 'Matematyzacja przyrody: Platon i Pitagorejczycy'. Zbadaj platońsko-pitagorejską wiarę w geometryczną i matematyczną strukturę wszechświata i jej wpływ na narodziny fizyki nowożytnej (Galileusz, Kepler, Newton)."
    },
    {
        "chapter": "chapter_11_korzenie_nauki.md",
        "title": "Greckie korzenie nauki nowożytnej i współczesnej",
        "section_id": "11_2",
        "prompt": "Napisz Podrozdział 11.2: 'Atomizm antyczny a fizyka współczesna'. Analizuj odrodzenie atomizmu Demokryta u Gassendiego, Boyle'a i Daltona. Pokaż, jak idea niepodzielnych cząstek w próżni ukształtowała mechanicyzm nowożytny i współczesną fizykę cząstek elementarnych."
    },
    {
        "chapter": "chapter_11_korzenie_nauki.md",
        "title": "Greckie korzenie nauki nowożytnej i współczesnej",
        "section_id": "11_3",
        "prompt": "Napisz Podrozdział 11.3: 'Metoda empiryczna Arystotelesa i taksonomia'. Zbadaj, jak klasyfikacja biologiczna Arystotelesa, jego obserwacja zjawisk przyrodniczych i systematyzacja wiedzy stworzyły podwaliny pod nowożytne nauki przyrodnicze."
    },
    {
        "chapter": "chapter_11_korzenie_nauki.md",
        "title": "Greckie korzenie nauki nowożytnej i współczesnej",
        "section_id": "11_4",
        "prompt": "Napisz Podrozdział 11.4: 'Koncepcje przestrzeni i czasu w nowożytnej fizyce'. Omów greckie koncepcje próżni (*kenon*), miejsca (*topos*) i przestrzeni (*chora* u Platona w *Timajosie*) oraz ich recepcję w fizyce relatywistycznej i kwantowej."
    },
    # ROZDZIAŁ 12
    {
        "chapter": "chapter_12_polityka_prawo_etyka.md",
        "title": "Demokracja, prawo i etyka publiczna: Antyczny fundament zachodniej polityki",
        "section_id": "12_1",
        "prompt": "Napisz Podrozdział 12.1: 'Ateńska demokracja bezpośrednia i jej dziedzictwo'. Analizuj pojęcia równego prawa głosu (*isegoria*) i równości wobec prawa (*isonomia*) w Atenach, ich krytykę u Platona i Arystotelesa, oraz wpływ na współczesny konstytucjonalizm i republikanizm."
    },
    {
        "chapter": "chapter_12_polityka_prawo_etyka.md",
        "title": "Demokracja, prawo i etyka publiczna: Antyczny fundament zachodniej polityki",
        "section_id": "12_2",
        "prompt": "Napisz Podrozdział 12.2: 'Rządy prawa u Arystotelesa'. Analizuj postulat z *Polityki*, że państwem powinny rządzić sprawiedliwe prawa, a nie arbitralna wola ludzi (nomokracja). Zbadaj koncepcję dobra wspólnego jako celu państwa."
    },
    {
        "chapter": "chapter_12_polityka_prawo_etyka.md",
        "title": "Demokracja, prawo i etyka publiczna: Antyczny fundament zachodniej polityki",
        "section_id": "12_3",
        "prompt": "Napisz Podrozdział 12.3: 'Stoicka koncepcja prawa naturalnego'. Zbadaj narodziny uniwersalnego prawa naturalnego (*lex naturalis*) u stoików, jego recepcję u Cycerona, oraz fundamentalną rolę w narodzinach nowożytnej teorii praw człowieka i prawa międzynarodowego (Grocjusz)."
    },
    {
        "chapter": "chapter_12_polityka_prawo_etyka.md",
        "title": "Demokracja, prawo i etyka publiczna: Antyczny fundament zachodniej polityki",
        "section_id": "12_4",
        "prompt": "Napisz Podrozdział 12.4: 'Współczesny renesans etyki cnót'. Przeanalizuj neotradycjonalistyczny powrót do arystotelesowskiej etyki cnót u Alasdaira MacIntyre'a (*After Virtue*) oraz Marthy Nussbaum, jako alternatywy dla deontologyzmu i utylitaryzmu."
    },
    # ZAKOŃCZENIE
    {
        "chapter": "chapter_13_zakonczenie.md",
        "title": "Zakończenie",
        "section_id": "13_1",
        "prompt": "Napisz Podrozdział 13.1 Zakończenia: 'Synteza historyczna recepcji'. Dokonaj całościowego, głębokiego podsumowania drogi rozwojowej recepcji myśli greckiej, od patrystyki do XX wieku. Wykaż trwałość greckich fundamentów w tożsamości kulturowej i intelektualnej Zachodu."
    },
    {
        "chapter": "chapter_13_zakonczenie.md",
        "title": "Zakończenie",
        "section_id": "13_2",
        "prompt": "Napisz Podrozdział 13.2 Zakończenia: 'Greckie kategorie wobec wyzwań ponowoczesności'. Zbadaj wyzwania współczesnej technologii, sztucznej inteligencji, transhumanizmu i posthumanizmu, analizując je przez pryzmat greckich kategorii *techne* (technika) oraz *physis* (natura)."
    },
    {
        "chapter": "chapter_13_zakonczenie.md",
        "title": "Zakończenie",
        "section_id": "13_3",
        "prompt": "Napisz Podrozdział 13.3 Zakończenia: 'Powrót do źródeł jako warunek humanistycznego renesansu'. Sformułuj wnioski końcowe postulujące, że zachowanie zachodniej tożsamości wymaga nieustannego dialogu z greckim dziedzictwem, które pozostaje żywym źródłem pytań o byt, dobro (*agathon*), prawdę (*aletheia*) i piękno (*kalon*)."
    }
]

def generate_dissertation():
    print("=== STARTING MASSIVE DISSERTATION GENERATION (52 SECTIONS) ===")
    
    # We generate raw sections and merge them at the end.
    for idx, sec in enumerate(SECTIONS):
        sec_file = f"sec_{sec['section_id']}.md"
        sec_path = os.path.join(RAW_DIR, sec_file)
        
        # Resuming check
        if os.path.exists(sec_path) and os.path.getsize(sec_path) > 1000:
            print(f"[{idx+1}/{len(SECTIONS)}] Section {sec_file} already exists. Skipping.")
            continue
            
        print(f"[{idx+1}/{len(SECTIONS)}] Querying API for: {sec['title']} -> {sec_file}...")
        user_prompt = f"Rozdział: {sec['title']}\nPodrozdział do napisania:\n{sec['prompt']}"
        
        try:
            content = query_llm_with_backoff(SYSTEM_PROMPT, user_prompt)
            # Write to raw section file
            with open(sec_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"[{idx+1}/{len(SECTIONS)}] Saved section {sec_file}.")
        except Exception as e:
            print(f"FATAL ERROR generating section {sec_file}: {e}", file=sys.stderr)
            sys.exit(1)
            
        # Standard sequential sleep to manage rate limit
        print("Sleeping 12s to manage API rate limit...")
        time.sleep(12)
        
    print("\n=== CONSOLIDATING RAW SECTIONS INTO CHAPTER FILES ===")
    # Group sections by chapter
    chapters_map = {}
    for sec in SECTIONS:
        chap = sec["chapter"]
        if chap not in chapters_map:
            chapters_map[chap] = []
        chapters_map[chap].append(sec)
        
    for chap, secs in chapters_map.items():
        chap_path = os.path.join(CHAPTERS_DIR, chap)
        print(f"Building chapter file: {chap}...")
        
        # Read the title of the chapter from the first section
        chap_title = secs[0]["title"]
        
        with open(chap_path, "w", encoding="utf-8") as out:
            # First line must be the H1 title of the chapter
            out.write(f"# {chap_title}\n\n")
            
            # For first paragraph drop cap formatting
            # The first section's content should start with a drop cap
            # We'll merge section contents
            for s_idx, sec in enumerate(secs):
                sec_file = f"sec_{sec['section_id']}.md"
                sec_path = os.path.join(RAW_DIR, sec_file)
                
                if not os.path.exists(sec_path):
                    print(f"WARNING: Raw section file {sec_file} not found. Skipping.", file=sys.stderr)
                    continue
                    
                with open(sec_path, "r", encoding="utf-8") as f:
                    content = f.read().strip()
                
                # If first section of the chapter, format the first paragraph with drop cap
                if s_idx == 0 and not chap.startswith("chapter_14"): # Chapter 14 is bibliography, no drop cap needed
                    # Find first paragraph and inject <p class="chapter-start">
                    # Usually, the model returns standard text. Let's find first letter and word
                    # Remove any initial headers if returned by model
                    content = re.sub(r'^#+.*$', '', content, flags=re.MULTILINE).strip()
                    paragraphs = content.split('\n\n')
                    if paragraphs:
                        first_p = paragraphs[0].strip()
                        # Format first letter
                        # e.g., "Narodziny..." -> "Nnarodziny..." -> "<p class="chapter-start">Nnarodziny...</p>"
                        if first_p and not first_p.startswith('<p'):
                            # Find first alphabetic character
                            match = re.search(r'([a-zA-ZąćęłńóśźżĄĆĘŁŃÓŚŹŻ])', first_p)
                            if match:
                                start_char = match.group(1)
                                start_idx = match.start()
                                char_lower = start_char.lower()
                                rest_of_p = first_p[start_idx+1:]
                                formatted_first_p = f'<p class="chapter-start">{start_char}{char_lower}{rest_of_p}</p>'
                                paragraphs[0] = formatted_first_p
                        content = '\n\n'.join(paragraphs)
                
                out.write(content)
                out.write("\n\n")
                
    # Copy bibliography (chapter 14) which is already complete and doesn't need raw sections
    # or it is generated as part of the list? We can keep the one we just wrote!
    print("=== DISSERTATION CHAPTERS RE-BUILT SUCCESSFULLY ===")

if __name__ == "__main__":
    generate_dissertation()
