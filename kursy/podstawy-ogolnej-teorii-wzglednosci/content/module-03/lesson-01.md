# Lekcja 3.1: Metryka Schwarzschilda, horyzont zdarzeń i orbity ISCO

<p class="chapter-start">Z ledwie kilka miesięcy po publikacji równań pola przez Einsteina, niemiecki fizyk i astronom Karl Schwarzschild znalazł pierwsze ścisłe, analityczne rozwiązanie równań Einsteina w próżni. Opisuje ono czasoprzestrzeń wokół statycznego, sferycznie symetrycznego ciała o masie $M$ [^4].</p>

## Cel operacyjny lekcji
Po ukończeniu tej lekcji będziesz potrafił:
1. Zapisać metrykę Schwarzschilda i zinterpretować jej osobliwości (pozorną na horyzoncie zdarzeń oraz fizyczną w $r = 0$).
2. Zdefiniować promień Schwarzschilda $r_s = \frac{2GM}{c^2}$.
3. Wyprowadzić efektywny potencjał dla cząstek masywnych i wyznaczyć promień najciaśniejszej stabilnej orbity kołowej (ISCO).

---

## 1. Postać Metryki Schwarzschilda

W próżniowych warunkach sferycznej symetrii ($R_{\mu\nu} = 0$, $T_{\mu\nu} = 0$), we współrzędnych sferycznych $(t, r, \theta, \phi)$, interwał czasoprzestrzenny ma postać:

$$ds^2 = -\left(1 - \frac{2GM}{c^2 r}\right) c^2 dt^2 + \left(1 - \frac{2GM}{c^2 r}\right)^{-1} dr^2 + r^2 (d\theta^2 + \sin^2\theta d\phi^2)$$

Wprowadzając definicję **promienia Schwarzschilda**:
$$r_s \equiv \frac{2GM}{c^2}$$
metrykę można zapisać zwięźle jako:
$$ds^2 = -\left(1 - \frac{r_s}{r}\right) c^2 dt^2 + \left(1 - \frac{r_s}{r}\right)^{-1} dr^2 + r^2 d\Omega^2$$

Dla Ziemi $r_s \approx 8.87\text{ mm}$, dla Słońca $r_s \approx 2.95\text{ km}$.

---

## 2. Dwie Osobliwości: Horyzont Zdarzeń vs Osobliwość Centralna

W metryce Schwarzschilda pojawiają się dwa punkty osobliwe:
1. **$r = r_s$ (Horyzont zdarzeń):** Składowa $g_{00} \to 0$, a $g_{rr} \to \infty$. Jest to osobliwość współrzędnościowa (pozorna), wynikająca ze złego doboru współrzędnych. Niezmiennik krzywizny Kretschmanna:
   $$K = R^{\alpha\beta\gamma\delta} R_{\alpha\beta\gamma\delta} = \frac{48 G^2 M^2}{c^4 r^6}$$
   w punkcie $r = r_s$ przyjmuje skończoną wartość $K(r_s) = \frac{12}{r_s^4}$. Oznacza to, że obserwator swobodnie spadający nie napotyka w $r=r_s$ nieskończonych sił pływowych.
2. **$r = 0$ (Osobliwość centralna):** Niezmiennik Kretschmanna dąży do nieskończoności ($K \to \infty$). Jest to rzeczywista osobliwość fizyczna (geodezyjnie nieprzekraczalna), w której załamuje się klasyczna geometria czasoprzestrzeni.

---

## 3. Efektywny Potencjał i Orbity ISCO

Z równania geodezyjnych w płaszczyźnie równikowej ($\theta = \pi/2$) dla cząstki próbnej o masie $m$ i jednostkowym momencie pędu $L$ otrzymujemy równanie radialne energii:

$$\frac{1}{2} \left(\frac{dr}{d\tau}\right)^2 + V_{\text{eff}}(r) = \frac{E^2 - c^2}{2}$$

gdzie relatywistyczny potencjał efektywny wynosi:

$$V_{\text{eff}}(r) = -\frac{GM}{r} + \frac{L^2}{2r^2} - \frac{GM L^2}{c^2 r^3}$$

<div class="table-wrapper">
<table class="academic-table">
  <caption>Tabela 3.1: Składniki Potencjału Efektywnego i ich Rola Fizyczna</caption>
  <thead>
    <tr>
      <th>Człon Potencjału</th>
      <th>Pochodzenie</th>
      <th>Wpływ na dynamikę orbity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$-\frac{GM}{r}$</td>
      <td>Grawitacja newtonowska</td>
      <td>Przyciąganie grawitacyjne dla dużych promieni $r$</td>
    </tr>
    <tr>
      <td>$+\frac{L^2}{2r^2}$</td>
      <td>Bariera siły odśrodkowej</td>
      <td>Odpychanie odśrodkowe, stabilizuje orbity eliptyczne</td>
    </tr>
    <tr>
      <td>$-\frac{GM L^2}{c^2 r^3}$</td>
      <td>Poprawka relatywistyczna Einsteina</td>
      <td>Głęboka studnia przyciągająca dla małych $r$; niszczy stabilność orbit</td>
    </tr>
  </tbody>
</table>
</div>

![Efektywny potencjał w geometrii Schwarzschilda i próg ISCO](images/orbity_schwarzschild_isco.png)

Stabilne orbity kołowe istnieją tylko tam, gdzie $\frac{dV_{\text{eff}}}{dr} = 0$ oraz $\frac{d^2 V_{\text{eff}}}{dr^2} > 0$.
Punkt przegięcia potencjału, wyznaczający **najciaśniejszą stabilną orbitę kołową (Innermost Stable Circular Orbit - ISCO)**, zachodzi dokładnie w:

$$r_{\text{ISCO}} = 6 \frac{GM}{c^2} = 3 r_s$$

Dla $r < r_{\text{ISCO}}$ materia z dysku akrecyjnego traci stabilność i nieuchronnie opada po spirali do wnętrza czarnej dziury.

---

## 4. Przykład z rozwiązaniem (Worked Example)

### Zadanie:
Wyznacz promień Schwarzschilda dla supermasywnej czarnej dziury Sagittarius A* w centrum Drogi Mlecznej o masie $M = 4.154 \times 10^6 M_\odot$.

### Rozwiązanie krok po kroku:
1. Obliczamy masę w kilogramach:
   $$M = 4.154 \times 10^6 \times 1.98847 \times 10^{30}\text{ kg} \approx 8.260 \times 10^{36}\text{ kg}$$
2. Stosujemy wzór na promień horyzontu $r_s = \frac{2GM}{c^2}$:
   $$r_s = \frac{2 \times (6.67430 \times 10^{-11}) \times (8.260 \times 10^{36})}{(2.99792 \times 10^8)^2} = \frac{1.1026 \times 10^{27}}{8.98755 \times 10^{16}} \approx 1.2268 \times 10^{10}\text{ m}$$
3. W jednostkach astronomicznych (AU, $1\text{ AU} \approx 1.496 \times 10^{11}\text{ m}$):
   $$r_s \approx 0.082\text{ AU} \approx 12.27\text{ mln km}$$
Promień horyzontu zdarzeń Sgr A* wynosi w przybliżeniu zaledwie 1/5 odległości Merkurego od Słońca.

---

## 5. Zadanie laboratoryjne dla kursanta (Hands-on Practice)

### Polecenie:
Wyznacz promień sfery fotonowej (promień, na którym fotony mogą poruszać się po niestabilnej orbicie kołowej) wokół czarnej dziury Schwarzschilda, analizując potencjał efektywny dla cząstek bezmasowych ($ds^2 = 0$).

### Wzorcowa odpowiedź (Model Answer):
Dla fotonu $ds^2 = 0$, więc równanie radialne przyjmuje postać:
$$\frac{1}{2}\left(\frac{dr}{d\lambda}\right)^2 + V_{\text{ph}}(r) = \frac{E^2}{2}, \quad V_{\text{ph}}(r) = \frac{L^2}{2r^2} \left(1 - \frac{2GM}{c^2 r}\right)$$
Warunek orbity kołowej $V'_{\text{ph}}(r) = 0$:
$$V'_{\text{ph}}(r) = -\frac{L^2}{r^3} \left(1 - \frac{2GM}{c^2 r}\right) + \frac{L^2}{2r^2} \left(\frac{2GM}{c^2 r^2}\right) = -\frac{L^2}{r^3} + \frac{3GM L^2}{c^2 r^4} = 0$$
Mnożąc przez $r^4 / L^2$:
$$-r + \frac{3GM}{c^2} = 0 \implies r_{\text{ph}} = \frac{3GM}{c^2} = 1.5 r_s$$
Sfera fotonowa znajduje się dokładnie w odległości $1.5$ promienia Schwarzschilda. Orbita ta jest niestabilna ($V''_{\text{ph}}(r_{\text{ph}}) < 0$).

---

## 6. Szybki sprawdzian wiedzy (Retrieval Check)

**Pytanie:** Co dzieje się z materią w dysku akrecyjnym czarnej dziury po przekroczeniu promienia $r_{\text{ISCO}} = 6GM/c^2$?
- **A)** Materia zwalnia i tworzy stabilny pierścień stacjonarny.
- **B)** Siły grawitacyjne równoważą się z siłami odśrodkowymi.
- **C)** Materia traci stabilność orbity kołowej i po dynamicznej trajektorii spiralnej wpada pod horyzont zdarzeń bez potrzeby dalszej utraty momentu pędu.

*Prawidłowa odpowiedź: C.*
*Wyjaśnienie dydaktyczne:* Poniżej promienia ISCO nie istnieją żadne stabilne orbity kołowe dla ciał masywnych. Wszelkie zaburzenie powoduje natychmiastowe zepchnięcie materii w kierunku horyzontu (tzw. plunging region).

---

## Przypisy bibliograficzne (DOI Verified)
[^4]: Schwarzschild, K. (1916). *Über das Gravitationsfeld eines Massenpunktes nach der Einsteinschen Theorie*. Sitzungsberichte der Preussischen Akademie der Wissenschaften, 189-196. OpenAlex ID: W2137688753.
