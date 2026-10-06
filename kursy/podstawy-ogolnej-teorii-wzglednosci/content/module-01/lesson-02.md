# Lekcja 1.2: Równanie geodezyjnych i symbole Christoffela

<p class="chapter-start">G dy grawitacja zostaje utożsamiona z geometrią czasoprzestrzeni, pojęcie cząstki swobodnej zyskuje nowe, ścisłe znaczenie matematyczne. Ciało niepodlegające żadnym siłom nielokalnym nie porusza się po linii prostej w sensie euklidesowym, lecz podąża za najprostszą możliwą trajektorią w zakrzywionej czasoprzestrzeni czterowymiarowej - linią geodezyjną [^1].</p>

## Cel operacyjny lekcji
Po ukończeniu tej lekcji będziesz potrafił:
1. Zdefiniować tensor metryczny $g_{\mu\nu}$ oraz interwał czasoprzestrzenny $ds^2$.
2. Wyprowadzić i obliczyć symbole Christoffela $\Gamma^\mu_{\alpha\beta}$ dla zadanego tensora metrycznego.
3. Zapisać i zinterpretować równanie geodezyjnych jako uogólnienie pierwszej zasady dynamiki Newtona.

---

## 1. Tensor Metryczny i Geometria Riemanna

W czterowymiarowej czasoprzestrzeni o współrzędnych $x^\mu = (x^0, x^1, x^2, x^3) = (ct, x, y, z)$ odległość między dwoma nieskończenie bliskimi zdarzeniami opisuje interwał:

$$ds^2 = g_{\mu\nu} dx^\mu dx^\nu$$

gdzie $g_{\mu\nu}$ jest symetrycznym tensorem metrycznym drugiego rzędu ($g_{\mu\nu} = g_{\nu\mu}$), a sumowanie po powtarzających się indeksach greckich ($\mu, \nu \in \{0, 1, 2, 3\}$) wynika z konwencji sumacyjnej Einsteina.

- W płaskiej czasoprzestrzeni Minkowskiego (STW): $g_{\mu\nu} = \eta_{\mu\nu} = \text{diag}(-1, 1, 1, 1)$.
- W obecności mas i energii: $g_{\mu\nu}(x)$ staje się funkcją położenia w czasoprzestrzeni, wyznaczając jej lokalną krzywiznę.

---

## 2. Pochodna Kowariantna i Symbole Christoffela

Zwykła pochodna cząstkowa tensora $\partial_\alpha T^\mu$ nie przekształca się w sposób tensorowy przy ogólnych transformacjach współrzędnych, ponieważ bazy wektorów zmieniają się od punktu do punktu rozmaitości. Aby zachować kowariancję różniczkowania, wprowadza się pochodną kowariantną:

$$\nabla_\alpha V^\mu = \partial_\alpha V^\mu + \Gamma^\mu_{\alpha\beta} V^\beta$$

Wielkości $\Gamma^\mu_{\alpha\beta}$ noszą nazwę symboli Christoffela drugiego rodzaju (lub współczynników koneksji Levi-Civity). Z warunku metryczności ($\nabla_\alpha g_{\mu\nu} = 0$) oraz symetrii koneksji (brak torsji: $\Gamma^\mu_{\alpha\beta} = \Gamma^\mu_{\beta\alpha}$) wynika ich jednoznaczna postać:

$$\Gamma^\mu_{\alpha\beta} = \frac{1}{2} g^{\mu\sigma} \left( \partial_\alpha g_{\beta\sigma} + \partial_\beta g_{\alpha\sigma} - \partial_\sigma g_{\alpha\beta} \right)$$

gdzie $g^{\mu\sigma}$ jest tensorem metrycznym odwrotnym ($g^{\mu\sigma} g_{\sigma\nu} = \delta^\mu_\nu$).

<div class="flow-container">
<div class="flow-step">1. Postać tensora metrycznego $g_{\mu\nu}$</div>
<div class="flow-step">2. Wyznaczenie tensora odwrotnego $g^{\mu\nu}$</div>
<div class="flow-step">3. Obliczenie pochodnych cząstkowych $\partial_\sigma g_{\alpha\beta}$</div>
<div class="flow-step">4. Złożenie symboli Christoffela $\Gamma^\mu_{\alpha\beta}$</div>
</div>

---

## 3. Równanie Geodezyjnych

Linia geodezyjna to linia ekstremalnej długości (lub czasu własnego $\tau$) łącząca dwa zdarzenia w czasoprzestrzeni. Z zasady wariacyjnej $\delta \int ds = 0$ otrzymujemy równanie geodezyjnych:

$$\frac{d^2 x^\mu}{d\tau^2} + \Gamma^\mu_{\alpha\beta} \frac{dx^\alpha}{d\tau} \frac{dx^\beta}{d\tau} = 0$$

gdzie $\tau$ jest parametrem afinicznym (dla cząstek z masą: czasem własnym).

Zauważmy analogię z mechaniką newtonowską:
$$\frac{d^2 x^i}{dt^2} = - \Gamma^i_{\alpha\beta} \frac{dx^\alpha}{dt} \frac{dx^\beta}{dt}$$
Człon $\Gamma^i_{\alpha\beta} \frac{dx^\alpha}{dt} \frac{dx^\beta}{dt}$ odgrywa rolę pozornej siły grawitacyjnej wywołanej zakrzywieniem geometrii.

---

## 4. Przykład z rozwiązaniem (Worked Example)

### Zadanie:
Wyznacz symbole Christoffela dla płaszczyzny dwuwymiarowej we współrzędnych biegunowych $(r, \theta)$, gdzie interwał wynosi:
$$ds^2 = dr^2 + r^2 d\theta^2$$

### Rozwiązanie krok po kroku:
1. **Współrzędne:** $x^1 = r$, $x^2 = \theta$.
2. **Macierz metryki i jej odwrotność:**
   $$g_{\mu\nu} = \begin{pmatrix} 1 & 0 \\ 0 & r^2 \end{pmatrix}, \quad g^{\mu\nu} = \begin{pmatrix} 1 & 0 \\ 0 & \frac{1}{r^2} \end{pmatrix}$$
3. **Pochodne cząstkowe metryki:** Jedyną niezerową pochodną jest $\partial_1 g_{22} = \frac{\partial (r^2)}{\partial r} = 2r$.
4. **Symbole Christoffela:**
   - Dla $\mu = 1$ ($r$):
     $$\Gamma^1_{22} = \frac{1}{2} g^{11} (-\partial_1 g_{22}) = \frac{1}{2} (1) (-2r) = -r$$
   - Dla $\mu = 2$ ($\theta$):
     $$\Gamma^2_{12} = \Gamma^2_{21} = \frac{1}{2} g^{22} (\partial_1 g_{22}) = \frac{1}{2} \left(\frac{1}{r^2}\right) (2r) = \frac{1}{r}$$
   - Wszystkie pozostałe składowe wynoszą 0.
5. **Równania geodezyjnych we współrzędnych biegunowych:**
   $$\frac{d^2 r}{d\tau^2} - r \left(\frac{d\theta}{d\tau}\right)^2 = 0$$
   $$\frac{d^2 \theta}{d\tau^2} + \frac{2}{r} \frac{dr}{d\tau} \frac{d\theta}{d\tau} = 0$$
   Pierwsze równanie odtwarza newtonowskie przyspieszenie dośrodkowe $r \dot{\theta}^2$, a drugie zachowanie momentu pędu ($\frac{d}{d\tau}(r^2 \dot{\theta}) = 0$).

---

## 5. Zadanie laboratoryjne dla kursanta (Hands-on Practice)

### Polecenie:
W granicy słabego pola grawitacyjnego i małych prędkości ($v \ll c$, $dx^i/d\tau \ll dx^0/d\tau$), wykaż, że składowa $\Gamma^i_{00}$ tensora metrycznego przyjmuje postać:
$$\Gamma^i_{00} \approx \frac{1}{2} \delta^{ik} \partial_k h_{00}$$
gdzie $g_{00} = -(1 + 2\Phi/c^2)$, a $\Phi$ jest newtonowskim potencjałem grawitacyjnym, oraz udowodnij, że równanie geodezyjnych odtwarza prawo dynamiki Newtona $\frac{d^2 \mathbf{x}}{dt^2} = -\nabla \Phi$.

### Wzorcowa odpowiedź (Model Answer):
W granicy nieliniowej dla $v \ll c$, jedynym dominującym członem w równaniu geodezyjnych jest $\alpha = \beta = 0$:
$$\frac{d^2 x^i}{d\tau^2} + \Gamma^i_{00} \left(\frac{dx^0}{d\tau}\right)^2 = 0$$
Ponieważ $dx^0/d\tau \approx c dt/dt = c$, mamy:
$$\frac{d^2 x^i}{dt^2} \approx - c^2 \Gamma^i_{00}$$
Obliczając symbol Christoffela dla metryki statycznej ($\partial_0 g = 0$):
$$\Gamma^i_{00} = \frac{1}{2} g^{ik} (2\partial_0 g_{0k} - \partial_k g_{00}) \approx -\frac{1}{2} \partial_i g_{00} = -\frac{1}{2} \partial_i \left(-\left(1 + \frac{2\Phi}{c^2}\right)\right) = \frac{1}{c^2} \partial_i \Phi$$
Podstawiając do przyspieszenia:
$$\frac{d^2 x^i}{dt^2} \approx - c^2 \left(\frac{1}{c^2} \partial_i \Phi\right) = -\partial_i \Phi \implies \frac{d^2 \mathbf{x}}{dt^2} = -\nabla \Phi$$
Dowodzi to, że mechanika newtonowska jest asymptotyczną granicą słabego pola i małych prędkości w OTW.

---

## 6. Szybki sprawdzian wiedzy (Retrieval Check)

**Pytanie:** Co oznacza geometrycznie zerowanie się wszystkich symboli Christoffela $\Gamma^\mu_{\alpha\beta} = 0$ w pewnym punkcie czasoprzestrzeni?
- **A)** Że czasoprzestrzeń jest w tym punkcie globalnie euklidesowa.
- **B)** Że istnieje lokalny układ inercjalny (spadający swobodnie), w którym pierwsze pochodne metryki znikają w tym punkcie.
- **C)** Że gęstość materii w całym wszechświecie wynosi zero.

*Prawidłowa odpowiedź: B.*
*Wyjaśnienie dydaktyczne:* Zgodnie z zasadą równoważności, w dowolnym punkcie rozmaitości można zawsze dobrać lokalne współrzędne geodezyjne (LIF - Local Inertial Frame), w których $g_{\mu\nu} = \eta_{\mu\nu}$ oraz $\partial_\sigma g_{\mu\nu} = 0$, co zeruje symbole Christoffela w tym jednym punkcie. Nie oznacza to jednak, że krzywizna Riemanna (zależna od drugich pochodnych) jest zerowa!

---

## Przypisy bibliograficzne (DOI Verified)
[^1]: Einstein, A. (1916). *Die Grundlage der allgemeinen Relativitätstheorie*. Annalen der Physik, 49, 769-822. DOI: 10.1002/andp.19163540702.
