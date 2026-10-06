# Lekcja 4.1: Linearyzacja równań pola, fale grawitacyjne i detekcja LIGO

<p class="chapter-start">W 1916 roku, zaledwie rok po ogłoszeniu ostatecznych równań OTW, Albert Einstein odkrył falowe rozwiązania swoich równań w przybliżeniu słabego pola. Wykazał, że oscylacje mas wytwarzają poprzeczne fale odkształcenia geometrii czasoprzestrzeni rozchodzące się z prędkością światła $c$ [^1], [^5].</p>

## Cel operacyjny lekcji
Po ukończeniu tej lekcji będziesz potrafił:
1. Przeprowadzić linearyzację równań pola Einsteina wokół metryki Minkowskiego.
2. Zdefiniować cechowanie poprzeczno-bezśladowe (TT - Transverse-Traceless Gauge) i rozróżnić dwie polaryzacje fal grawitacyjnych ($h_+$ i $h_\times$).
3. Wyprowadzić wzór kwadrupolowy Einsteina na moc promieniowania grawitacyjnego.
4. Zinterpretować zasadę działania laserowych detektorów interferometrycznych (LIGO, Virgo).

---

## 1. Linearyzacja OTW (Słabe Pole)

Rozważmy małe perturbacje $h_{\mu\nu}$ na tle płaskiej czasoprzestrzeni Minkowskiego $\eta_{\mu\nu}$:

$$g_{\mu\nu} = \eta_{\mu\nu} + h_{\mu\nu}, \quad |h_{\mu\nu}| \ll 1$$

Definiując śladowo odwróconą perturbację $\bar{h}_{\mu\nu} \equiv h_{\mu\nu} - \frac{1}{2} \eta_{\mu\nu} h$ oraz narzucając cechowanie Lorentza $\partial^\mu \bar{h}_{\mu\nu} = 0$, zlinearyzowane równania Einsteina w próżni sprowadzają się do standardowego równania falowego d'Alemberta:

$$\Box \bar{h}_{\mu\nu} = \left(-\frac{1}{c^2} \frac{\partial^2}{\partial t^2} + \nabla^2\right) \bar{h}_{\mu\nu} = 0$$

Fale grawitacyjne rozchodzą się dokładnie z prędkością światła $c$.

---

## 2. Polaryzacje Fali: Cechowanie TT

W cechowaniu poprzeczno-bezśladowym (TT Gauge), dla fali propagującej się wzdłuż osi $z$, tensor odkształcenia posiada tylko dwa niezależne stopnie swobody:

$$h_{ij}^{\text{TT}}(t, z) = \begin{pmatrix} h_+(t - z/c) & h_\times(t - z/c) & 0 \\ h_\times(t - z/c) & -h_+(t - z/c) & 0 \\ 0 & 0 & 0 \end{pmatrix}$$

Fale grawitacyjne wywołują poprzeczne, kwadrupolowe odkształcenie odległości między cząstkami próbnymi:
- Polaryzacja $h_+$: ściskanie wzdłuż osi $x$ przy jednoczesnym rozciąganiu wzdłuż osi $y$.
- Polaryzacja $h_\times$: to samo odkształcenie obrócone o kąt $45^\circ$.

---

## 3. Wzór Kwadrupolowy Einsteina

Ponieważ całkowita masa i pęd układu są zachowane, promieniowanie grawitacyjne nie może mieć charakteru monopolowego ani dipolowego. Najniższym dozwolonym rzędem jest promieniowanie kwadrupolowe. Całkowita moc emitowana w postaci fal grawitacyjnych przez układ o masowym momencie kwadrupolowym $I_{ij}$ wynosi:

$$P_{\text{GW}} = \frac{G}{5 c^5} \sum_{i,j} \left\langle \dddot{I}_{ij} \dddot{I}_{ij} \right\rangle$$

Czynnik $c^5$ w mianowniku ($c^5 \approx 2.43 \times 10^{42}\text{ W}$) sprawia, że fale grawitacyjne emitowane przez zjawiska laboratoryjne są niewykrywalnie słabe. Znaczące amplitudy powstają jedynie podczas najbardziej gwałtownych zjawisk we Wszechświecie: koalescencji podwójnych układów czarnych dziur i gwiazd neutronowych.

![Relatywistyczny sygnał 'Chirp' koalescencji podwójnej czarnej dziury](images/fala_grawitacyjna_chirp.png)

---

## 4. Historyczna Detekcja GW150914 (LIGO)

14 września 2015 roku dwa bliźniacze interferometry Advanced LIGO w Hanford i Livingston zarejestrowały pierwszy bezpośredni sygnał fali grawitacyjnej - zdarzenie **GW150914** [^5].

<div class="table-wrapper">
<table class="academic-table">
  <caption>Tabela 4.1: Parametry Astrofizyczne Pierwszej Detekcji Fali Grawitacyjnej GW150914</caption>
  <thead>
    <tr>
      <th>Parametr Źródła</th>
      <th>Wartość Obserwowana</th>
      <th>Interpretacja Fizyczna</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Masa początkowa 1 ($M_1$)</td>
      <td>$36_{-4}^{+5} M_\odot$</td>
      <td>Ciężka czarna dziura gwiezdna</td>
    </tr>
    <tr>
      <td>Masa początkowa 2 ($M_2$)</td>
      <td>$29_{-4}^{+4} M_\odot$</td>
      <td>Druga czarna dziura gwiezdna</td>
    </tr>
    <tr>
      <td>Masa końcowa ($M_f$)</td>
      <td>$62_{-4}^{+4} M_\odot$</td>
      <td>Rotująca czarna dziura Kerra</td>
    </tr>
    <tr>
      <td>Wypromieniowana energia ($\Delta E_{\text{GW}}$)</td>
      <td>$3.0_{-0.5}^{+0.5} M_\odot c^2$</td>
      <td>Czysta energia wyemitowana w ułamku sekundy w postaci fal</td>
    </tr>
    <tr>
      <td>Maksymalna amplituda na Ziemi ($h$)</td>
      <td>$\sim 1.0 \times 10^{-21}$</td>
      <td>Względna zmiana długości ramienia interferometru: $\Delta L \approx 4 \times 10^{-18}\text{ m}$</td>
    </tr>
  </tbody>
</table>
</div>

---

## 5. Przykład z rozwiązaniem (Worked Example)

### Zadanie:
Dla interferometru LIGO o długości ramion $L = 4\text{ km}$, oblicz bezwzględne przemieszczenie zwierciadeł $\Delta L$ wywołane falą grawitacyjną o amplitudzie $h = 10^{-21}$. Porównaj wynik z rozmiarem protonu ($r_p \approx 0.84 \times 10^{-15}\text{ m}$).

### Rozwiązanie krok po kroku:
1. Zależność między amplitudą odkształcenia a długością ramienia:
   $$\frac{\Delta L}{L} \approx h \implies \Delta L = h \times L$$
2. Podstawiając wartości:
   $$\Delta L = 10^{-21} \times 4000\text{ m} = 4 \times 10^{-18}\text{ m}$$
3. Stosunek do promienia protonu:
   $$\frac{\Delta L}{r_p} = \frac{4 \times 10^{-18}\text{ m}}{0.84 \times 10^{-15}\text{ m}} \approx \frac{1}{210}$$
LIGO mierzy odkształcenie przestrzeni z precyzją stanowiącą ułamek jednej tysięcznej średnicy pojedynczego protonu na dystansie 4 kilometrów.

---

## 6. Szybki sprawdzian wiedzy (Retrieval Check)

**Pytanie:** Dlaczego idealnie sferyczna, pulsująca promieniowo gwiazda nie może emitować fal grawitacyjnych?
- **A)** Ponieważ jej gęstość jest zbyt niska.
- **B)** Zgodnie z twierdzeniem Birkhoffa i wzorem kwadrupolowym, promieniowanie grawitacyjne wymaga niezerowej trzeciej pochodnej masowego momentu kwadrupolowego; pulsacje sferyczne posiadają symetrię monopolową, która nie emituje fal.
- **C)** Ponieważ fale grawitacyjne są pochłaniane przez fotosferę gwiazdy.

*Prawidłowa odpowiedź: B.*
*Wyjaśnienie dydaktyczne:* Zgodnie z prawem zachowania energii i twierdzeniem Birkhoffa, każde pole sferycznie symetryczne w próżni jest ściśle statyczne (metryka Schwarzschilda). Brak zmiennego kwadrupolowego momentu pędu wyklucza emisję promieniowania falowego.

---

## Przypisy bibliograficzne (DOI Verified)
[^1]: Einstein, A. (1916). *Näherungsweise Integration der Feldgleichungen der Gravitation*. Sitzungsberichte der Preussischen Akademie der Wissenschaften, 688-696.
[^5]: Abbott, B. P. et al. (LIGO Scientific Collaboration and Virgo Collaboration) (2016). *Observation of Gravitational Waves from a Binary Black Hole Merger*. Phys. Rev. Lett., 116(6), 061102. DOI: 10.1103/PhysRevLett.116.061102.
