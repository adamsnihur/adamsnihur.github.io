# Lekcja 2.1: Krzywizna Riemanna, tensor Ricciego i tensor energii-pędu

<p class="chapter-start">W przeciwieństwie do symboli Christoffela, które zależą od wyboru układu współrzędnych i mogą zostać wyzerowane w lokalnym układzie inercjalnym, prawdziwa, fizyczna krzywizna czasoprzestrzeni ma charakter obiektywny. Miarą tej krzywizny jest tensor krzywizny Riemanna, opisujący zjawisko sił pływowych oraz dewiację linii geodezyjnych [^1].</p>

## Cel operacyjny lekcji
Po ukończeniu tej lekcji będziesz potrafił:
1. Zdefiniować tensor krzywizny Riemanna $R^\rho_{\ \sigma\mu\nu}$ poprzez komutator pochodnych kowariantnych.
2. Zbudować tensor Ricciego $R_{\mu\nu}$ oraz skalar krzywizny $R$.
3. Zdefiniować relatywistyczny tensor energii-pędu $T_{\mu\nu}$ dla płynu doskonałego i zinterpretować jego prawo zachowania $\nabla_\mu T^{\mu\nu} = 0$.

---

## 1. Tensor Krzywizny Riemanna i Dewiacja Geodezyjnych

Jeśli przeniesiemy równolegle wektor $V^\alpha$ wzdłuż zamkniętej pętli w zakrzywionej czasoprzestrzeni, wektor końcowy nie pokryje się z wyjściowym. Matematycznie zjawisko to wyraża komutator pochodnych kowariantnych:

$$[\nabla_\mu, \nabla_\nu] V^\rho = \nabla_\mu \nabla_\nu V^\rho - \nabla_\nu \nabla_\mu V^\rho = R^\rho_{\ \sigma\mu\nu} V^\sigma$$

Tensor Riemanna wyraża się poprzez symbole Christoffela i ich pochodne:

$$R^\rho_{\ \sigma\mu\nu} = \partial_\mu \Gamma^\rho_{\nu\sigma} - \partial_\nu \Gamma^\rho_{\mu\sigma} + \Gamma^\rho_{\mu\lambda} \Gamma^\lambda_{\nu\sigma} - \Gamma^\rho_{\nu\lambda} \Gamma^\lambda_{\mu\sigma}$$

W 4-wymiarowej czasoprzestrzeni tensor Riemanna posiada $4^4 = 256$ składowych, lecz dzięki tożsamościom algebraicznym (antysymetria po dwóch pierwszych i dwóch ostatnich indeksach, symetria przy zamianie par) liczba niezależnych składowych redukuje się do 20 [^1].

<div class="tree-container">
<div class="tree-node"><strong>Hierarchia Krzywizny Riemanna</strong>
<div class="tree-node">Tensor Riemanna $R^\rho_{\ \sigma\mu\nu}$ (20 niezależnych składowych - pełna geometria)</div>
<div class="tree-node">Ślad 1: Tensor Ricciego $R_{\mu\nu} = R^\lambda_{\ \mu\lambda\nu}$ (10 składowych symetrycznych)</div>
<div class="tree-node">Ślad 2: Skalar Ricciego $R = g^{\mu\nu} R_{\mu\nu}$ (1 niezmiennik skalarny)</div>
<div class="tree-node">Część bezśladowa: Tensor Weyla $C_{\rho\sigma\mu\nu}$ (10 składowych - pole grawitacyjne w próżni i fale)</div>
</div>
</div>

---

## 2. Tensor Energii-Pędu ($T_{\mu\nu}$)

W fizyce newtonowskiej źródłem pola grawitacyjnego jest wyłącznie gęstość masy spoczynkowej $\rho$. Zgodnie z zasadą równoważności masy i energii STW ($E = mc^2$), grawitować musi wszelka forma energii, pędu, ciśnienia i naprężeń. Opisuje je symetryczny tensor drugiego rzędu $T_{\mu\nu}$:

<div class="table-wrapper">
<table class="academic-table">
  <caption>Tabela 2.1: Struktura Fizyczna Tensora Energii-Pędu $T_{\mu\nu}$</caption>
  <thead>
    <tr>
      <th>Składowe</th>
      <th>Interpretacja Fizyczna</th>
      <th>Wymiar Fizyczny</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$T_{00}$</td>
      <td>Gęstość energii (w tym masa spoczynkowa $c^2 \rho$)</td>
      <td>$\text{J/m}^3 = \text{Pa}$</td>
    </tr>
    <tr>
      <td>$T_{0i} = T_{i0}$</td>
      <td>Gęstość pędu / strumień energii w kierunku $i$</td>
      <td>$\text{kg}/(\text{m}^2 \cdot \text{s})$</td>
    </tr>
    <tr>
      <td>$T_{ii}$</td>
      <td>Ciśnienie izotropowe $P$ w kierunku $i$</td>
      <td>$\text{N/m}^2 = \text{Pa}$</td>
    </tr>
    <tr>
      <td>$T_{ij}$ ($i \neq j$)</td>
      <td>Naprężenia ścinające (lepkość)</td>
      <td>$\text{N/m}^2 = \text{Pa}$</td>
    </tr>
  </tbody>
</table>
</div>

Dla płynu doskonałego (ideal fluid) poruszającego się z czteroprędkością $u^\mu$ tensor energii-pędu ma postać:
$$T_{\mu\nu} = (\rho + P/c^2) u_\mu u_\nu + P g_{\mu\nu}$$

Fundamentalnym prawem fizyki jest lokalne zachowanie energii i pędu, wyrażone przez znikanie dywergencji kowariantnej:
$$\nabla_\mu T^{\mu\nu} = 0$$

---

## 3. Przykład z rozwiązaniem (Worked Example)

### Zadanie:
Dla sfery dwuwymiarowej o promieniu $r_0$ opisanej metryką $ds^2 = r_0^2 (d\theta^2 + \sin^2\theta d\phi^2)$, wyznacz skalar krzywizny Ricciego $R$.

### Rozwiązanie krok po kroku:
1. Obliczając niezerowe symbole Christoffela otrzymujemy:
   $$\Gamma^\theta_{\phi\phi} = -\sin\theta\cos\theta, \quad \Gamma^\phi_{\theta\phi} = \Gamma^\phi_{\phi\theta} = \cot\theta$$
2. Jedyną niezależną składową tensora Riemanna jest:
   $$R^\theta_{\ \phi\theta\phi} = \partial_\theta \Gamma^\theta_{\phi\phi} - \partial_\phi \Gamma^\theta_{\theta\phi} + \Gamma^\theta_{\theta\lambda}\Gamma^\lambda_{\phi\phi} - \Gamma^\theta_{\phi\lambda}\Gamma^\lambda_{\theta\phi} = -\cos^2\theta + \sin^2\theta - (-\sin\theta\cos\theta \cot\theta) = \sin^2\theta$$
3. Składowe tensora Ricciego $R_{\mu\nu} = R^\lambda_{\ \mu\lambda\nu}$:
   $$R_{\theta\theta} = 1, \quad R_{\phi\phi} = \sin^2\theta$$
4. Skalar krzywizny Ricciego:
   $$R = g^{\mu\nu} R_{\mu\nu} = g^{\theta\theta} R_{\theta\theta} + g^{\phi\phi} R_{\phi\phi} = \frac{1}{r_0^2} (1) + \frac{1}{r_0^2 \sin^2\theta} (\sin^2\theta) = \frac{2}{r_0^2}$$
Krzywizna jest stała i dodatnia, co potwierdza geometrię standardowej sfery o promieniu $r_0$.

---

## 4. Zadanie laboratoryjne dla kursanta (Hands-on Practice)

### Polecenie:
Wyjaśnij fizyczną rolę tensora Weyla $C_{\rho\sigma\mu\nu}$ w obszarach próżniowych otaczających gwiazdę ($T_{\mu\nu} = 0$). Dlaczego próżnia wokół Słońca jest zakrzywiona, skoro tensor Ricciego znika w próżni ($R_{\mu\nu} = 0$)?

### Wzorcowa odpowiedź (Model Answer):
W próżni równania Einsteina implikują $R_{\mu\nu} = 0$ oraz $R = 0$. Jednak tensor krzywizny Riemanna dekomponuje się na część Ricciego oraz część bezśladową - tensor Weyla:
$$R_{\rho\sigma\mu\nu} = C_{\rho\sigma\mu\nu} + \text{człony zależne od } R_{\mu\nu}$$
W próżni tensor Weyla nie znika ($C_{\rho\sigma\mu\nu} \neq 0$). To właśnie tensor Weyla koduje siły pływowe rozciągające ciała, fale grawitacyjne oraz zakrzywienie czasoprzestrzeni wokół odległych mas (jak Słońce czy czarne dziury).

---

## 5. Szybki sprawdzian wiedzy (Retrieval Check)

**Pytanie:** Co oznacza tożsamość Bianchiego $\nabla_\mu G^{\mu\nu} = 0$ w kontekście tensora energii-pędu $T^{\mu\nu}$?
- **A)** Że energia i pęd mogą być bez ograniczeń niszczone w obecności czarnych dziur.
- **B)** Że z samej struktury geometrii różniczkowej wynika automatyczne, lokalne zachowanie energii i pędu materii $\nabla_\mu T^{\mu\nu} = 0$.
- **C)** Że stała grawitacji $G$ maleje wraz z rozszerzaniem się Wszechświata.

*Prawidłowa odpowiedź: B.*
*Wyjaśnienie dydaktyczne:* Zróżniczkowana tożsamość Bianchiego gwarantuje, że tensor Einsteina $G_{\mu\nu} = R_{\mu\nu} - \frac{1}{2} R g_{\mu\nu}$ ma bezwzględnie tożsamościowo zerową dywergencję kowariantną. Po związaniu go z tensorem materii równaniem $G_{\mu\nu} = \kappa T_{\mu\nu}$, lokalne prawo zachowania energii i pędu materii staje się bezpośrednią konsekwencją geometrii czasoprzestrzeni.

---

## Przypisy bibliograficzne (DOI Verified)
[^1]: Hawking, S. W., & Ellis, G. F. R. (1973). *The Large Scale Structure of Space-Time*. Cambridge University Press. DOI: 10.1017/CBO9780511524646.
