# Rubryka Oceny Projektu Końcowego (Capstone Rubric)

## Zadanie: Numeryczna rekonstrukcja parametrów GW150914

### Kryteria ewaluacji:

1. **Rygor analityczny (25 pkt):**
   - Poprawne przekształcenie relacji częstotliwości i pochodnej do wzoru na masę chirpową.
   - Prawidłowe zastosowanie konwersji jednostek układu SI do mas Słońca ($M_\odot$).

2. **Poprawność fizyczna (25 pkt):**
   - Uzyskanie masy chirpowej w granicach $28 - 32 M_\odot$.
   - Poprawne wyznaczenie mas składowych dla modelu symetrycznego ($m_1 = m_2 \approx 34 - 36 M_\odot$).
   - Prawidłowe obliczenie promienia horyzontu czarnej dziury Kerra po koalescencji ($M_f \approx 62 M_\odot \implies r_s \approx 183\text{ km}$).

3. **Kod weryfikacyjny (30 pkt):**
   - Samodzielny skrypt w Pythonie (np. `experiments/capstone_reconstruction.py`).
   - Brak błędów wykonania, obecność asercji `assert` weryfikujących zgodność numeryczną.

4. **Interpretacja bilansu energii (20 pkt):**
   - Wyjaśnienie mechanizmu promieniowania 3 mas Słońca w postaci fal grawitacyjnych zgodnie z $E = mc^2$.
