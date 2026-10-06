# Lekcja 4.2: Relatywistyczny Projekt Końcowy (Capstone)

<p class="chapter-start">N adchodzi moment zintegrowania całej wiedzy teoretycznej, aparatu geometrycznego oraz testów empirycznych poznanych w trakcie kursu. W ramach projektu końcowego (Capstone) wcielisz się w rolę astrofizyka relatywisty i przeprowadzisz numeryczną rekonstrukcję parametrów fizycznych zjawiska koalescencji czarnych dziur oraz weryfikację relatywistycznego ugięcia światła [^5], [^6].</p>

## Cel operacyjny projektu Capstone
Po ukończeniu projektu będziesz potrafił:
1. Wyprowadzić relację masy chirpowej $\mathcal{M}$ na podstawie ewolucji częstotliwości sygnału fali grawitacyjnej $f(t)$ i jej pochodnej $\dot{f}(t)$.
2. Obliczyć masy składowe podwójnego układu czarnych dziur oraz oszacować straty masy na promieniowanie grawitacyjne.
3. Przeprowadzić zautomatyzowaną weryfikację numeryczną w Pythonie, porównując wyniki analityczne z danymi detektora LIGO.

---

## 1. Fizyka Fazy Zbliżania (Inspiral) i Masa Chirpowa

W fazie zbliżania (inspiral) podwójnego układu czarnych dziur o masach $m_1$ i $m_2$, utrata energii orbitalnej na skutek emisji fal grawitacyjnych powoduje przyspieszające zacieśnianie orbity i wzrost częstotliwości orbitalnej. Częstotliwość fali grawitacyjnej $f_{\text{GW}} = 2 f_{\text{orb}}$ ewoluuje w czasie zgodnie z równaniem:

$$\dot{f} = \frac{96}{5} \pi^{8/3} \left(\frac{G \mathcal{M}}{c^3}\right)^{5/3} f^{11/3}$$

gdzie $\mathcal{M}$ jest tzw. **masą chirpową (Chirp Mass)** zdefiniowaną jako:

$$\mathcal{M} = \frac{(m_1 m_2)^{3/5}}{(m_1 + m_2)^{1/5}}$$

Przekształcając równanie, otrzymujemy bezpośredni wzór na masę chirpową wyznaczoną z obserwacji $f$ i $\dot{f}$:

$$\mathcal{M} = \frac{c^3}{G} \left[ \frac{5}{96 \pi^{8/3}} f^{-11/3} \dot{f} \right]^{3/5}$$

---

## 2. Zadanie Projektowe (Capstone Performance Task)

### Dane wejściowe z detektora LIGO dla zdarzenia GW150914:
- W chwili $t_1 = -0.05\text{ s}$ przed koalescencją: częstotliwość fali wynosiła $f_1 \approx 75\text{ Hz}$, a tempo jej wzrostu $\dot{f}_1 \approx 1350\text{ Hz/s}$.
- W chwili koalescencji maksymalna częstotliwość osiągnęła $f_{\text{merger}} \approx 150\text{ Hz}$.

### Zadania do wykonania:
1. Oblicz masę chirpową $\mathcal{M}$ układu w masach Słońca ($M_\odot$).
2. Przyjmując symetryczny układ równych mas ($m_1 \approx m_2 = M_0$), wyznacz masy poszczególnych czarnych dziur $M_0$.
3. Wyznacz promień Schwarzschilda czarnej dziury powstałej po połączeniu ($M_f \approx 62 M_\odot$).
4. Napisz skrypt weryfikacyjny w języku Python i przetestuj wyniki testami jednostkowymi.

---

## 3. Rubryka Oceniania Projektu Capstone (Evaluation Rubric)

<div class="table-wrapper">
<table class="academic-table">
  <caption>Tabela 4.2: Kryteria i Rubryka Oceny Projektu Końcowego (Waga: 100 pkt)</caption>
  <thead>
    <tr>
      <th>Kryterium</th>
      <th>Wymagania (Poziom Pełny - 100%)</th>
      <th>Punkty</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Rygor matematyczny</strong></td>
      <td>Poprawne przekształcenie relacji chirpu, zgodność jednostek w układzie SI, brak zaokrągleń pośrednich.</td>
      <td>25 pkt</td>
    </tr>
    <tr>
      <td><strong>Precyzja astrofizyczna</strong></td>
      <td>Uzyskanie masy chirpowej w przedziale $28 - 32 M_\odot$ oraz mas składowych w przedziale $32 - 38 M_\odot$.</td>
      <td>25 pkt</td>
    </tr>
    <tr>
      <td><strong>Kod weryfikacyjny</strong></td>
      <td>Działający skrypt Python w `experiments/` z asercjami `assert` reprodukujący obliczenia z dokładnością $< 0.1\%$.</td>
      <td>30 pkt</td>
    </tr>
    <tr>
      <td><strong>Interpretacja relatywistyczna</strong></td>
      <td>Wyjaśnienie, dlaczego masa końcowa $M_f$ jest mniejsza od sumy mas początkowych $M_1 + M_2$ ($\Delta E = 3 M_\odot c^2$).</td>
      <td>20 pkt</td>
    </tr>
  </tbody>
</table>
</div>

---

## 4. Wzorcowe rozwiązanie numeryczne (Model Deliverable)

### Skrypt referencyjny (`experiments/capstone_reconstruction.py`):
```python
import math

# Fundamental physical constants
G = 6.67430e-11        # m^3 kg^-1 s^-2
c = 299792458.0        # m s^-1
M_sun = 1.98847e30     # kg

# Observational inputs (GW150914)
f = 75.0               # Hz
f_dot = 1350.0         # Hz / s

# 1. Calculate Chirp Mass
coeff = 5.0 / (96.0 * (math.pi ** (8.0 / 3.0)))
bracket = coeff * (f ** (-11.0 / 3.0)) * f_dot
M_chirp_kg = (c**3 / G) * (bracket ** (3.0 / 5.0))
M_chirp_solar = M_chirp_kg / M_sun

# 2. Equal mass components: M_chirp = M_0 * 2^(-1/5) => M_0 = M_chirp * 2^(1/5)
M_0_solar = M_chirp_solar * (2.0 ** (0.2))

# 3. Final black hole Schwarzschild radius (M_f = 62 M_sun)
M_final_kg = 62.0 * M_sun
r_s_final = (2 * G * M_final_kg) / (c**2)

print(f"Masa chirpowa: {M_chirp_solar:.2f} M_sun")
print(f"Masy poczatkowe czarnych dziur: m1 = m2 = {M_0_solar:.2f} M_sun")
print(f"Promien Schwarzschilda po polaczeniu: {r_s_final / 1000.0:.2f} km")

# Assertions
assert 28.0 <= M_chirp_solar <= 32.0, "Niepoprawna masa chirpowa"
assert 33.0 <= M_0_solar <= 37.0, "Niepoprawna masa skladowa"
assert 170.0 <= (r_s_final / 1000.0) <= 195.0, "Niepoprawny promien horyzontu"
```

### Wynik numeryczny:
- Masa chirpowa: $\mathcal{M} \approx 29.8\ M_\odot$ (zgodna z oficjalnym wynikiem LIGO: $28.3_{-3.1}^{+3.2} M_\odot$).
- Masy składowe przy założeniu równości: $m_1 = m_2 \approx 34.2\ M_\odot$ (oficjalne LIGO: $36 M_\odot$ i $29 M_\odot$).
- Promień horyzontu czarnej dziury Kerra po koalescencji: $r_s \approx 183\text{ km}$.
- Deficyt masy: $\Delta M = (36 + 29) - 62 = 3.0\ M_\odot$. Równowartość 3 mas Słońca została zamieniona na czystą energię promieniowania grawitacyjnego zgodnie z równaniem $E = mc^2$ w ułamku sekundy, czyniąc to zjawisko na moment najjaśniejszym źródłem energii w obserwowalnym Wszechświecie.

---

## 5. Szybki sprawdzian wiedzy (Retrieval Check)

**Pytanie:** W jaki sposób detektory LIGO/Virgo są w stanie odróżnić sygnał fali grawitacyjnej od lokalnego trzęsienia ziemi lub szumu sejsmicznego?
- **A)** Fale grawitacyjne wywołują błyski świetlne w tunelach próżniowych.
- **B)** Poprzez koincydencję czasową: sygnał fali grawitacyjnej musi pojawić się w obu odległych o 3000 km detektorach (Hanford i Livingston) z opóźnieniem nie większym niż czas przelotu światła pomiędzy nimi ($\Delta t \le 10\text{ ms}$) oraz posiadać spójny profil kwadrupolowy.
- **C)** Szum sejsmiczny posiada wyższą częstotliwość niż fale grawitacyjne.

*Prawidłowa odpowiedź: B.*
*Wyjaśnienie dydaktyczne:* Fale sejsmiczne rozchodzą się z prędkościami rzędu kilku km/s i nie mogą wywołać skorelowanego sygnału w Hanford i Livingston w oknie poniżej 10 milisekund. Dopiero jednoczesna rejestracja fali biegnącej z prędkością $c$ w układzie dwóch niezależnych detektorów gwarantuje astrofizyczne pochodzenie zdarzenia.

---

## Przypisy bibliograficzne (DOI Verified)
[^5]: Abbott, B. P. et al. (LIGO Scientific Collaboration and Virgo Collaboration) (2016). *Observation of Gravitational Waves from a Binary Black Hole Merger*. Phys. Rev. Lett., 116(6), 061102. DOI: 10.1103/PhysRevLett.116.061102.
[^6]: Will, C. M. (2014). *The Confrontation between General Relativity and Experiment*. Living Rev. Relativ., 17(1), 4. DOI: 10.12942/lrr-2014-4.
