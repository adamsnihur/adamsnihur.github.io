# Lekcja 1.1: Ograniczenia mechaniki newtonowskiej i zasada równoważności

<p class="chapter-start">K lasyczna teoria grawitacji sformułowana przez Isaaca Newtona w 1687 roku opierała się na koncepcji siły działającej natychmiastowo na odległość w statycznej, trójwymiarowej przestrzeni euklidesowej. Choć model ten z niezwykłą precyzją opisywał ruch planet Układu Słonecznego przez ponad dwa stulecia, u progu XX wieku ujawnił fundamentalne sprzeczności fizyczne i teoretyczne z rodzącą się Szczególną Teorią Względności (STW) [^1].</p>

## Cel operacyjny lekcji
Po ukończeniu tej lekcji będziesz potrafił:
1. Zidentyfikować fundamentalne sprzeczności pomiędzy prawem powszechnego ciążenia Newtona a postulatem niezmienniczości prędkości światła.
2. Zdefiniować i rozróżnić słabą (WEP) oraz silną (SEP) zasadę równoważności.
3. Wykazać, w jaki sposób lokalna nierozróżnialność pola grawitacyjnego i przyspieszenia prowadzi do geometryzacji grawitacji.

---

## 1. Sprzeczność newtonowskiego ciążenia ze Szczególną Teorią Względności

Zgodnie z newtonowskim prawem powszechnego ciążenia siła grawitacyjna pomiędzy masami $M$ i $m$ wynosi:

$$\mathbf{F} = -G \frac{M m}{r^2} \hat{\mathbf{r}}$$

Równanie to zakłada nieskończoną prędkość propagacji oddziaływania: zmiana położenia masy $M$ wywołuje natychmiastową zmianę siły działającej na masę $m$, niezależnie od dzielącej je odległości $r$. Stoi to w bezpośredniej sprzeczności z podstawowym postulatem STW, zgodnie z którym żadna informacja ani oddziaływanie fizyczne nie może rozchodzić się z prędkością większą niż prędkość światła w próżni $c$ ($c \approx 299\,792\,458\text{ m/s}$) [^1].

<div class="tree-container">
<div class="tree-node"><strong>Kryzys grawitacji newtonowskiej</strong>
<div class="tree-node">Problem I: Nieskończona prędkość propagacji (sprzeczność z c)</div>
<div class="tree-node">Problem II: Niezmienniczość Galileusza zamiast Lorentza</div>
<div class="tree-node">Problem III: Anomalia precesji peryhelium Merkurego (43'' na stulecie)</div>
</div>
</div>

---

## 2. Zasada Równoważności: Słaba vs Silna

Kluczem do przezwyciężenia tego kryzysu stała się obserwacja, którą Albert Einstein nazwał "najszczęśliwszą myślą swojego życia" (1907 r.): obserwator spadający swobodnie w polu grawitacyjnym nie odczuwa własnego ciężaru.

<div class="table-wrapper">
<table class="academic-table">
  <caption>Tabela 1.1: Taksonomia Zasad Równoważności w Fizyce Relatywistycznej</caption>
  <thead>
    <tr>
      <th>Wariant Zasady</th>
      <th>Sformułowanie Fizyczne</th>
      <th>Rygor Empiryczny (Testy)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Słaba Zasada Równoważności (WEP)</strong></td>
      <td>Równość masy grawitacyjnej i bezwładnej: $m_g = m_i$. Wszystkie ciała spadają z tym samym przyspieszeniem w próżni.</td>
      <td>Eötvös, Dicke, Braginsky, misja satelitarna MICROSCOPE: $\eta < 10^{-15}$ [^2]</td>
    </tr>
    <tr>
      <td><strong>Einsteina Zasada Równoważności (EEP)</strong></td>
      <td>WEP + lokalna niezmienniczość Lorentza (LLI) + lokalna niezmienniczość pozycyjna (LPI). Wynik lokalnego eksperymentu nielaboratoryjnego nie zależy od prędkości układu ani miejsca w czasoprzestrzeni.</td>
      <td>Testy zegarów atomowych, pomiary stałych sprzężenia, eksperyment Pounda-Rebki [^3]</td>
    </tr>
    <tr>
      <td><strong>Silna Zasada Równoważności (SEP)</strong></td>
      <td>WEP stosuje się również do ciał posiadających znaczącą grawitacyjną energię własną (np. gwiazdy neutronowe, czarne dziury).</td>
      <td>Pomiary laserowe odległości Księżyca (LLR), układy pulsarów podwójnych [^6]</td>
    </tr>
  </tbody>
</table>
</div>

---

## 3. Eksperyment Myślowy: Winda Einsteina

Rozważmy zamkniętą kabinę windy w dwóch scenariuszach:
1. Kabina spoczywa na powierzchni Ziemi w jednorodnym polu grawitacyjnym o natężeniu $g$.
2. Kabina znajduje się w głębokiej przestrzeni kosmicznej z dala od mas, ale jest ciągnięta z przyspieszeniem $a = g$.

Żaden eksperyment mechaniczny ani optyczny przeprowadzony **wewnątrz** małej, lokalnej kabiny nie pozwala rozróżnić tych dwóch sytuacji. Wynika stąd bezpośredni wniosek: skoro przyspieszenie układu odniesienia wywołuje efekty nieodróżnialne od grawitacji, to pole grawitacyjne nie jest polem sił w tradycyjnym sensie, lecz przejawem geometrii układu.

---

## 4. Przykład z rozwiązaniem (Worked Example)

### Zadanie:
Wykaż, że z zasady równoważności wynika konieczność zakrzywienia toru promienia świetlnego w polu grawitacyjnym oraz wyznacz przybliżone ugięcie wiązki światła przebywającej kabinę windy o szerokości $L$ poruszającej się z przyspieszeniem $g$.

### Rozwiązanie krok po kroku:
1. **Czas przelotu fotonu:** Foton porusza się w poprzek kabiny z prędkością $c$, zatem czas przelotu wynosi:
   $$\Delta t = \frac{L}{c}$$
2. **Pionowe przemieszczenie kabiny:** W czasie $\Delta t$ kabina przyspieszająca z przyspieszeniem $g$ pokonuje pionowy dystans:
   $$\Delta y = \frac{1}{2} g (\Delta t)^2 = \frac{1}{2} g \left(\frac{L}{c}\right)^2$$
3. **Kąt ugięcia toru:** Kąt ugięcia wiązki światła zarejestrowany na przeciwległej ścianie wynosi:
   $$\theta \approx \frac{v_y}{c} = \frac{g \Delta t}{c} = \frac{g L}{c^2}$$
4. **Wniosek relatywistyczny:** Zgodnie z zasadą równoważności, ten sam efekt ugięcia musi wystąpić w spoczywającej kabinie znajdującej się w polu grawitacyjnym. Oznacza to, że promień światła ulega ugięciu w polu grawitacyjnym, mimo że foton nie posiada masy spoczynkowej ($m_0 = 0$).

---

## 5. Zadanie laboratoryjne dla kursanta (Hands-on Practice)

### Polecenie:
Wykorzystując wyprowadzony wzór na grawitacyjną dylatację czasu wynikającą z zasady równoważności:
$$\frac{\Delta f}{f} = \frac{g h}{c^2}$$
oblicz względną zmianę częstotliwości fotonów promieniowania gamma ($^{57}\text{Fe}$, $E = 14.4\text{ keV}$) w historycznym eksperymencie Pounda-Rebki przeprowadzonym na wieży Jefferson Physical Laboratory na Uniwersytecie Harvarda ($h = 22.5\text{ m}$, $g = 9.80665\text{ m/s}^2$).

### Wzorcowa odpowiedź (Model Answer):
Podstawiając wartości do wzoru:
$$\frac{\Delta f}{f} = \frac{9.80665\text{ m/s}^2 \times 22.5\text{ m}}{(299\,792\,458\text{ m/s})^2} = \frac{220.65}{8.98755 \times 10^{16}} \approx 2.455 \times 10^{-15}$$
Wynik ten został zweryfikowany z dokładnością do 1% w 1960 roku przez Roberta Pounda i Glena Rebkę [^3], potwierdzając, że czas płynie wolniej na niższych potencjałach grawitacyjnych.

---

## 6. Szybki sprawdzian wiedzy (Retrieval Check)

**Pytanie:** Dlaczego foton ulega zakrzywieniu w polu grawitacyjnym, skoro jego masa spoczynkowa wynosi zero?
- **A)** Ponieważ foton posiada ładunek elektryczny oddziałujący z jądrami atomowymi.
- **B)** Ponieważ grawitacja nie jest siłą zależną od masy spoczynkowej, lecz zakrzywieniem czasoprzestrzeni, po której fotony poruszają się wzdłuż zerowych linii geodezyjnych.
- **C)** Ponieważ ciśnienie promieniowania słonecznego odpycha cząstki światła.

*Prawidłowa odpowiedź: B.*
*Wyjaśnienie dydaktyczne:* W OTW cząstki bezmasowe poruszają się po liniach geodezyjnych czasoprzestrzeni ($ds^2 = 0$). To geometria czasoprzestrzeni jest zakrzywiona przez masę i energię, a nie trajektoria zakrzywiana przez newtonowską siłę przyciągania masowego. Odpowiedzi A i C są fizycznie fałszywe.

---

## Przypisy bibliograficzne (DOI Verified)
[^1]: Einstein, A. (1915). *Die Feldgleichungen der Gravitation*. Sitzungsberichte der Preussischen Akademie der Wissenschaften.
[^2]: Touboul, P. et al. (2022). *MICROSCOPE Mission: Final Results of the Test of the Equivalence Principle*. Phys. Rev. Lett., 129, 121102. DOI: 10.1103/PhysRevLett.129.121102.
[^3]: Pound, R. V., & Rebka, G. A. (1960). *Apparent Weight of Photons*. Phys. Rev. Lett., 4, 337-341. DOI: 10.1103/PhysRevLett.4.337.
