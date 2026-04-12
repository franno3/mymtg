---
tags:
  - zasada
numer_zasady: "106"
kategoria: Mechanika
---

# Mana i Koszt Many

> [!note] Oficjalny numer
> Zasada **106** — Kompleksowe Zasady MtG

---

## Definicja

Mana to zasób używany do grania kart i aktywowania zdolności. Kosztem many (mana cost) jest ilość many różnych kolorów wymagana do zagrania czaru lub aktywacji zdolności.

---

## Rodzaje many

| Symbol | Kolor | Źródło |
|---|---|---|
| `{W}` | Biała | Plains, białe lądy |
| `{U}` | Niebieska | Island, niebieskie lądy |
| `{B}` | Czarna | Swamp, czarne lądy |
| `{R}` | Czerwona | Mountain, czerwone lądy |
| `{G}` | Zielona | Forest, zielone lądy |
| `{C}` | Bezbarwna | Artefakty, specjalne lądy |
| `{X}` | Zmienna | Tyle ile chcesz |

---

## Mana cost vs CMC (Converted Mana Cost / Mana Value)

- **Mana cost** to dokładny koszt: `{2}{R}{R}`
- **CMC / Mana Value** to suma wszystkich symboli many: `{2}{R}{R}` = 4
- Bezbarwna mana `{C}` liczy się do CMC ale jest bezbarwna
- Dla `{X}` — X=0 przy obliczaniu CMC w bibliotece/ręce/cmentarzu

---

## Mana pool i floating mana

- Mana wytworzona przez lądy/zdolności trafia do **mana pool**
- Nieużyta mana **znika** na końcu każdego kroku/fazy (od czasu Mana Burn Rule zmiany)
- Można wytworzyć manę i zagrać czar w tym samym kroku

---

## Koszty specjalne

### Phyrexian Mana `{W/P}`
- Możesz zapłacić odpowiednim kolorem many **lub** 2 punktami życia
- Pozwala grać karty poza color identity (ale kosztem życia)

### Hybrid Mana `{R/W}`
- Możesz zapłacić jednym z dwóch wskazanych kolorów
- Color identity karty zawiera **oba** kolory

### Generic Mana `{2}`, `{1}`, `{3}`...
- Dowolny kolor many (lub bezbarwna)
- `{2}` = dwie dowolne many, niekoniecznie tego samego koloru

---

## Przykłady

### Przykład 1 — zapłata kosztu
> **Karta:** Goblin Guide `{R}`, CMC=1
> **Aby zagrać:** Tapujesz Mountain → generuje `{R}` → płacisz `{R}` → Goblin Guide wchodzi.

### Przykład 2 — Hybrid mana
> **Karta:** Dreadbore `{B/R}{B/R}`
> **Możliwe zapłaty:** `{B}{B}`, `{B}{R}`, `{R}{R}` — dowolna kombinacja czarnej i czerwonej.

---

## Powiązane zasady

- [[Zasady/Czarowanie i Granie Kart]] — jak koszty many są opłacane podczas grania czarów
- [[Zasady/Color Identity]] — jak symbole many wpływają na color identity w Commander

---

## Częste błędy i nieporozumienia

- **Błąd:** "Mana zostaje w mana pool między turami."
  **Poprawnie:** Mana znika na końcu każdego **kroku** (step). Wytworzona mana musi być użyta w tym samym kroku.

- **Błąd:** "X w koszcie many = 0 gdy karta jest na cmentarzu."
  **Poprawnie:** Tak — poza Stackiem wartość X wynosi 0 przy obliczaniu Mana Value.
