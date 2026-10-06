# Lekcja 3.2: Trzy klasyczne testy empiryczne Ogólnej Teorii Względności

<p class="chapter-start">N awet najbardziej elegancka teoria matematyczna musi poddać się bezwzględnemu werdyktowi eksperymentu. Sam Albert Einstein zaproponował w 1916 roku trzy fundamentalne sprawdziany empiryczne swojej teorii: relatywistyczną precesję peryhelium Merkurego, ugięcie promieni świetlnych w pobliżu masywnych ciał oraz grawitacyjne przesunięcie ku czerwieni promieniowania [^1], [^6].</p>

## Cel operacyjny lekcji
Po ukończeniu tej lekcji będziesz potrafił:
1. Wyprowadzić relatywistyczny kąt precesji peryhelium i obliczyć słynną wartość 43'' na stulecie dla planety Merkury.
2. Wyjaśnić różnicę pomiędzy newtonowskim a relatywistycznym kątem ugięcia światła ($\theta_{\text{GR}} = 2 \theta_{\text{Newton}}$) i zanalizować historyczny eksperyment Eddingtona z 1919 roku.
3. Przedstawić współczesne testy OTW w formalizmie PPN (Parametrized Post-Newtonian).

---

## 1. Test I: Relatywistyczna Precesja Peryhelium Merkurego

Astronomowie XIX wieku (Urbain Le Verrier, 1859 r.) zauważyli, że orbita Merkurego obraca się w przestrzeni szybciej, niż wynika to z newtonowskiego oddziaływania grawitacyjnego pozostałych planet. Całkowita obserwowana precesja wynosi około 574 sekund łuku na stulecie, z czego perturbacje planetarne (głównie Jowisza, Wenus i Ziemi) wyjaśniały 531 sekund łuku. Pozostawała niewyjaśniona anomalia wynosząca:

$$\Delta \phi_{\text{anomalia}} \approx 43'' \text{ na stulecie}$$

Z równania geodezyjnych w metryce Schwarzschilda kąt obrotu peryhelium na jeden pełny obieg wynosi:

$$\Delta \phi = \frac{6 \pi G M_\odot}{c^2 a (1 - e^2)}$$

Dla parametrów orbity Merkurego ($a \approx 5.791 \times 10^{10}\text{ m}$, $e \approx 0.20563$, okres $T \approx 87.97\text{ dni}$), po przeliczeniu na 100 lat ziemskich (ok. 415 obiegów), wzór Einsteina daje dokładnie:

$$\Delta \phi_{\text{Merkury}} \approx 42.98'' \text{ na stulecie}$$

Zgodność z danymi obserwacyjnymi bez wprowadzania jakichkolwiek parametrów dopasowywanych była pierwszym spektakularnym triumfem OTW.

---

## 2. Test II: Ugięcie Promieni Świetlnych przy Krawędzi Słońca

W podejściu newtonowskim korpuskularna teoria światła (Soldner, 1801 r.) przewidywała kąt ugięcia fotonu przelatującego w odległości $b$ od środka Słońca:

$$\theta_{\text{Newton}} = \frac{2 G M_\odot}{c^2 b}$$

Dla promienia muskającego krawędź Słońca ($b = R_\odot$): $\theta_{\text{Newton}} \approx 0.875''$.

W OTW ugięcie światła wynika zarówno z dylatacji czasowej ($g_{00}$), jak i krzywizny przestrzennej ($g_{rr}$). Oba wkłady są równe i sumują się, podwajając kąt ugięcia:

$$\theta_{\text{GR}} = \frac{4 G M_\odot}{c^2 b} = 2 \theta_{\text{Newton}}$$

Dla krawędzi tarczy słonecznej:

$$\theta_{\text{GR}} \approx 1.751''$$

![Ugięcie promieni świetlnych w polu grawitacyjnym Słońca](images/ugiecie_swiatla_porownanie.png)

Podczas całkowitego zaćmienia Słońca 29 maja 1919 roku brytyjska ekspedycja pod kierownictwem Arthura Eddingtona i Franka Dysona zmierzyła przesunięcie pozycji gwiazd tła widocznych w pobliżu korony słonecznej na Wyspie Książęcej (Principe) i w Sobral (Brazylia), uzyskując wyniki $1.98'' \pm 0.12''$ oraz $1.61'' \pm 0.30''$ [^2], co ostatecznie potwierdziło przewidywanie OTW i przyniosło Einsteinowi międzynarodową sławę.

---

## 3. Test III: Grawitacyjne Przesunięcie ku Czerwieni (Redshift)

Dwa identyczne zegary atomowe umieszczone w różnych punktach potencjału grawitacyjnego mierzą różny upływ czasu własnego. Relacja częstotliwości fotonu emitowanego w punkcie o potencjale $\Phi_1$ i odbieranego w $\Phi_2$ wynosi:

$$\frac{f_2}{f_1} = \sqrt{\frac{g_{00}(r_1)}{g_{00}(r_2)}} \approx 1 - \frac{\Phi_2 - \Phi_1}{c^2}$$

Foton uciekający z głębi studni grawitacyjnej traci energię na rzecz pola, co objawia się wydłużeniem fali (przesunięciem w stronę czerwieni). Zjawisko to zostało laboratoryjnie potwierdzone z precyzją poniżej 1% w 1960 r. w eksperymencie Pounda-Rebki [^3].

---

## 4. Współczesny Status: Formalizm PPN i Zegary Satelitarne

Współcześnie OTW jest testowana w ramach formalizmu PPN (Parametrized Post-Newtonian). Parametr $\gamma$ mierzy wkład krzywizny przestrzennej do metryki ($\gamma = 1$ w OTW, $\gamma = 0$ w teorii Newtona). Pomiary opóźnienia sygnałów radiowych sondy Cassini (tzw. efekt Shapiro) w 2003 roku wyznaczyły [^6]:

$$\gamma - 1 = (2.1 \pm 2.3) \times 10^{-5}$$

co stanowi zgodność z OTW na poziomie 0.002%. Efekty OTW są również na bieżąco uwzględniane w systemie nawigacji satelitarnej GPS (zegary satelitów wyprzedzają zegary naziemne o ok. $38\,\mu\text{s}$ na dobę z powodu relatywistycznego przesunięcia częstotliwości).

---

## 5. Zadanie laboratoryjne dla kursanta (Hands-on Practice)

### Polecenie:
Wyjaśnij, dlaczego newtonowskie obliczenie kąta ugięcia światła ($\theta = 2GM/c^2 R$) pomija dokładnie połowę rzeczywistego relatywistycznego ugięcia. Odwołaj się do składowych tensora metrycznego Schwarzschilda $g_{00}$ i $g_{rr}$.

### Wzorcowa odpowiedź (Model Answer):
W ujęciu newtonowskim przestrzeń jest płaska, a grawitacja jest traktowana jako siła przyciągająca foton posiadający efektywną masę pędu $E/c^2$. W języku OTW odpowiada to uwzględnieniu wyłącznie zakrzywienia składowej czasowej metryki $g_{00} = -(1 - 2GM/c^2 r)$.
W pełnej OTW przestrzeń również jest zakrzywiona, co koduje składowa radialna $g_{rr} = (1 - 2GM/c^2 r)^{-1}$. Ruch fotonu po zerowej linii geodezyjnej ($ds^2 = 0$) odczuwa zarówno dylatację czasu ($dt$), jak i kontrakcję długości radialnej ($dr$). Każdy z tych dwóch członów wnosi dokładnie $2GM/c^2 R$ do kąta ugięcia, co w sumie daje pełną wartość $\theta_{\text{GR}} = 4GM/c^2 R$.

---

## 6. Szybki sprawdzian wiedzy (Retrieval Check)

**Pytanie:** O ile mikrosekund na dobę spieszą się zegary na satelitach GPS względem zegarów na powierzchni Ziemi w wyniku wypadkowej dylatacji grawitacyjnej (OTW) i dylatacji kinematycznej (STW)?
- **A)** Zegary spóźniają się o 1 sekundę na dobę.
- **B)** Wypadkowo spieszą się o około $+38\,\mu\text{s}$ na dobę (OTW: $+45\,\mu\text{s}$ na dobę z powodu wyższego potencjału, STW: $-7\,\mu\text{s}$ na dobę z powodu prędkości orbitalnej).
- **C)** Efekt jest całkowicie zerowy, ponieważ STW i OTW idealnie się znoszą.

*Prawidłowa odpowiedź: B.*
*Wyjaśnienie dydaktyczne:* Zegary na orbicie GPS (wysokość ok. 20 200 km) znajdują się w słabszym polu grawitacyjnym, co powoduje, że spieszą się o ok. $+45.9\,\mu\text{s}$ na dobę (efekt OTW). Jednocześnie poruszają się z prędkością orbitalną ok. 3.9 km/s, co opóźnia je o ok. $-7.2\,\mu\text{s}$ na dobę (efekt STW). Wypadkowa wynosi ok. $+38.7\,\mu\text{s}$ na dobę. Brak korekty relatywistycznej generowałby błąd nawigacji rzędu 11 km na dobę!

---

## Przypisy bibliograficzne (DOI Verified)
[^1]: Einstein, A. (1916). *Die Grundlage der allgemeinen Relativitätstheorie*. Annalen der Physik, 49, 769-822. DOI: 10.1002/andp.19163540702.
[^2]: Dyson, F. W., Eddington, A. S., & Davidson, C. (1920). *A Determination of the Deflection of Light by the Sun's Gravitational Field...* Phil. Trans. R. Soc. A, 220, 291-333. DOI: 10.1098/rsta.1920.0009.
[^3]: Pound, R. V., & Rebka, G. A. (1960). *Apparent Weight of Photons*. Phys. Rev. Lett., 4, 337-341. DOI: 10.1103/PhysRevLett.4.337.
[^6]: Will, C. M. (2014). *The Confrontation between General Relativity and Experiment*. Living Rev. Relativ., 17(1), 4. DOI: 10.12942/lrr-2014-4.
