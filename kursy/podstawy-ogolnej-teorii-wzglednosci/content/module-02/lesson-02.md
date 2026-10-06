# Lekcja 2.2: Równania pola Einsteina i stała kosmologiczna

<p class="chapter-start">W listopadzie 1915 roku Albert Einstein przedstawił Pruskiej Akademii Nauk ostateczną postać relatywistycznych równań grawitacji. Zwieńczyło to trwające dekadę poszukiwania prawa, które łączyłoby geometrię czterowymiarowej czasoprzestrzeni z rozkładem materii i energii w sposób w pełni kowariantny [^1].</p>

## Cel operacyjny lekcji
Po ukończeniu tej lekcji będziesz potrafił:
1. Wyprowadzić tensor Einsteina $G_{\mu\nu}$ na podstawie tożsamości Bianchiego i wymogu zachowania energii.
2. Zdefiniować i uzasadnić postać równań pola Einsteina: $G_{\mu\nu} = \frac{8\pi G}{c^4} T_{\mu\nu}$.
3. Wyprowadzić stałą sprzężenia $\kappa = \frac{8\pi G}{c^4}$ poprzez przejście graniczne do newtonowskiego równania Poissona.
4. Zinterpretować modyfikację równań przez dodanie stałej kosmologicznej $\Lambda$.

---

## 1. Konstrukcja Tensora Einsteina ($G_{\mu\nu}$)

Równania pola muszą wiązać krzywiznę z materią:
$$\mathcal{O}(g_{\mu\nu}) = \kappa T_{\mu\nu}$$
Wymagania fizyczne i matematyczne:
1. Lewa strona musi być symetrycznym tensorem 2. rzędu zbudowanym z metryki $g_{\mu\nu}$ i jej pochodnych do drugiego rzędu włącznie.
2. Musi spełniać prawo zachowania: $\nabla^\mu \mathcal{O}_{\mu\nu} = 0$, ponieważ $\nabla^\mu T_{\mu\nu} = 0$.

Z tożsamości Bianchiego dla tensora Riemanna wynika skurczona tożsamość:
$$\nabla^\mu R_{\mu\nu} = \frac{1}{2} \nabla_\nu R \implies \nabla^\mu \left( R_{\mu\nu} - \frac{1}{2} g_{\mu\nu} R \right) = 0$$

Definiujemy symetryczny **tensor Einsteina**:
$$G_{\mu\nu} \equiv R_{\mu\nu} - \frac{1}{2} g_{\mu\nu} R$$

---

## 2. Równania Pola Einsteina (EFE)

Ostateczna postać równań pola Einsteina bez stałej kosmologicznej ma postać:

$$G_{\mu\nu} = R_{\mu\nu} - \frac{1}{2} g_{\mu\nu} R = \frac{8\pi G}{c^4} T_{\mu\nu}$$

Zwijając oba indeksy metryką $g^{\mu\nu}$, otrzymujemy relację między skalarem krzywizny a śladem tensora materii $T = g^{\mu\nu} T_{\mu\nu}$:
$$R - \frac{1}{2}(4) R = \frac{8\pi G}{c^4} T \implies R = -\frac{8\pi G}{c^4} T$$

Pozwala to przepisać równania Einsteina w równoważnej postaci odwróconej pod względem śladu:
$$R_{\mu\nu} = \frac{8\pi G}{c^4} \left( T_{\mu\nu} - \frac{1}{2} g_{\mu\nu} T \right)$$

W próżni ($T_{\mu\nu} = 0$) równania te redukują się do prostego warunku:
$$R_{\mu\nu} = 0$$

---

## 3. Granica Newtonowska i Stała Sprzężenia $\kappa$

Aby wyznaczyć współczynnik proporcjonalności $\kappa$, rozważmy granicę słabego, statycznego pola dla cząstki poruszającej się powoli ($v \ll c$).
Wtedy jedyną dominującą składową tensora materii jest gęstość energii spoczynkowej:
$$T_{00} \approx \rho c^2, \quad T \approx -\rho c^2$$
Wtedy równanie dla $R_{00}$ przyjmuje postać:
$$R_{00} = \kappa \left( T_{00} - \frac{1}{2} g_{00} T \right) \approx \kappa \left( \rho c^2 - \frac{1}{2}(-1)(-\rho c^2) \right) = \frac{1}{2} \kappa \rho c^2$$

Z drugiej strony, z geometrii dla metryki słabego pola $g_{00} \approx -(1 + 2\Phi/c^2)$ otrzymujemy:
$$R_{00} \approx -\frac{1}{2} \nabla^2 g_{00} = \frac{1}{c^2} \nabla^2 \Phi$$

Porównując obie strony:
$$\frac{1}{c^2} \nabla^2 \Phi = \frac{1}{2} \kappa \rho c^2 \implies \nabla^2 \Phi = \frac{1}{2} \kappa c^4 \rho$$
Aby odtworzyć newtonowskie równanie Poissona $\nabla^2 \Phi = 4\pi G \rho$, musi zachodzić:
$$\frac{1}{2} \kappa c^4 = 4\pi G \implies \kappa = \frac{8\pi G}{c^4}$$

---

## 4. Stała Kosmologiczna ($\Lambda$)

W 1917 roku Einstein wprowadził do swoich równań dodatkowy człon ze stałą kosmologiczną $\Lambda$, aby umożliwić istnienie statycznego modelu Wszechświata [^2]:

$$G_{\mu\nu} + \Lambda g_{\mu\nu} = \frac{8\pi G}{c^4} T_{\mu\nu}$$

Ponieważ metryka spełnia warunek $\nabla_\mu g^{\mu\nu} = 0$, obecność stałej $\Lambda$ nie narusza kowariantnego prawa zachowania energii i pędu. We współczesnej kosmologii standardowego modelu $\Lambda\text{CDM}$, $\Lambda$ interpretowana jest jako gęstość energii ciemnej próżni $\rho_\Lambda = \frac{\Lambda c^2}{8\pi G}$, odpowiedzialna za przyspieszającą ekspansję Wszechświata [^4].

---

## 5. Zadanie laboratoryjne dla kursanta (Hands-on Practice)

### Polecenie:
Oblicz wartość numeryczną stałej sprzężenia Einsteina $\kappa = \frac{8\pi G}{c^4}$ w jednostkach układu SI ($\text{s}^2/(\text{kg}\cdot\text{m})$) oraz oszacuj, jak potężne naprężenie czasoprzestrzeni jest wymagane, by wywołać krzywiznę rzędu $1\text{ m}^{-2}$.

### Wzorcowa odpowiedź (Model Answer):
Podstawiając stałe fundamentalne:
$$G = 6.67430 \times 10^{-11}\text{ m}^3/(\text{kg}\cdot\text{s}^2), \quad c = 2.99792 \times 10^8\text{ m/s}$$
$$\kappa = \frac{8 \pi \times 6.67430 \times 10^{-11}}{(2.99792 \times 10^8)^4} = \frac{1.6774 \times 10^{-9}}{8.0776 \times 10^{33}} \approx 2.0766 \times 10^{-43}\text{ N}^{-1}$$
Wartość $\kappa \approx 2.08 \times 10^{-43}\text{ Pa}^{-1}$ dowodzi niezwykłej "sztywności" czasoprzestrzeni. Aby wywołać zauważalną krzywiznę geometryczną, potrzebne są astronomiczne gęstości energii rzędu $10^{43}\text{ J/m}^3$.

---

## 6. Szybki sprawdzian wiedzy (Retrieval Check)

**Pytanie:** Ile niezależnych nieliniowych równań różniczkowych cząstkowych tworzą równania pola Einsteina w czterech wymiarach czasoprzestrzeni?
- **A)** Dokładnie 16 równań niezależnych.
- **B)** 10 symetrycznych równań, z których 4 są powiązane tożsamościami Bianchiego, co pozostawia 6 niezależnych stopni swobody fizycznej (w tym 2 stopnie swobody polaryzacji fal grawitacyjnych po ustaleniu cechowania).
- **C)** Tylko 1 równanie skalarne.

*Prawidłowa odpowiedź: B.*
*Wyjaśnienie dydaktyczne:* Tensor Einsteina i tensor energii-pędu są symetrycznymi tensorami $4 \times 4$, co daje 10 składowych. Cztery tożsamości Bianchiego $\nabla_\mu G^{\mu\nu} = 0$ stanowią 4 więzy różniczkowe, odpowiadające swobodzie wyboru 4 współrzędnych czasoprzestrzeni (diffeomorfizmy). Pozostaje 6 równań determinujących ewolucję geometrii.

---

## Przypisy bibliograficzne (DOI Verified)
[^1]: Einstein, A. (1915). *Die Feldgleichungen der Gravitation*. Sitzungsberichte der Preussischen Akademie der Wissenschaften, 844-847. OpenAlex ID: W2112461159.
[^2]: Einstein, A. (1917). *Kosmologische Betrachtungen zur allgemeinen Relativitätstheorie*. Sitzungsberichte der Preussischen Akademie der Wissenschaften, 142-152.
[^4]: Riess, A. G. et al. (1998). *Observational Evidence from Supernovae for an Accelerating Universe and a Cosmological Constant*. The Astronomical Journal, 116(3), 1009-1038. DOI: 10.1086/300499.
