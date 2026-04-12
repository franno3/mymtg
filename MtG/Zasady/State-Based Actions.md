---
tags:
  - zasada
numer_zasady: "704"
kategoria: Mechanika zaawansowana
---

# State-Based Actions (Akcje Oparte na Stanie)

> [!note] Oficjalny numer
> Zasada **704** — Kompleksowe Zasady MtG

---

## Definicja

State-Based Actions (SBA) to zasady sprawdzane automatycznie, w tle, **zanim jakikolwiek gracz dostanie priorytet**. Nie wchodzą na Stack — są sprawdzane natychmiast i powtarzane aż żadna nie będzie miała zastosowania.

---

## Kiedy SBA są sprawdzane

- Na początku każdego kroku i fazy
- Zanim aktywny gracz dostanie priorytet
- **Zawsze przed** pierwszym priorytetem po jakimkolwiek zdarzeniu

---

## Lista kluczowych State-Based Actions

### Śmierć stwora
- Stwór z wytrzymałością ≤ 0 → trafia na cmentarz
- Stwór ze śmiertelną ilością obrażeń (≥ wytrzymałość) → trafia na cmentarz
- Stwór z Deathtouch damage → trafia na cmentarz
- **Wyjątek:** Stwory Indestructible nie giną od obrażeń ani efektów „destroy"

### Śmierć gracza
- Gracz z 0 lub mniej punktami życia → przegrywa
- Gracz z 10+ poison counters → przegrywa
- Gracz który musi dobrać z pustej biblioteki → przegrywa

### Anulowanie liczników
- Permanenty z parami +1/+1 i -1/-1 → pary znikają

### Legendarność
- Jeśli kontrolujesz dwa permanenty o tej samej nazwie Legendary → musisz poświęcić jeden z nich (Legendary Rule)

### Tokeny poza polem bitwy
- Tokeny w strefie innej niż pole bitwy → znikają

### Aura bez celu
- Aura przywiązana do permanentu który zniknął → trafia na cmentarz

### Planeswalker z 0 loyalty
- Planeswalker z 0 loyalty counters → trafia na cmentarz

---

## Przykłady

### Przykład 1 — gracz ginie z 0 życia
> **Sytuacja:** Lightning Bolt (3 dmg) redukuje życie gracza do 0.
> **Zastosowanie zasady:** Zanim ktokolwiek dostanie priorytet → SBA sprawdzają życie gracza → 0 ≤ 0 → gracz przegrywa.

### Przykład 2 — Legendary Rule
> **Sytuacja:** Kontrolujesz Sol Ring. Efekt sprawia że dostajesz drugi Sol Ring.

> **Zastosowanie zasady:** Nie dotyczy! Sol Ring nie jest Legendary. Ale gdyby to był [[Karty/Czerwone/Krenko, Mob Boss|Krenko, Mob Boss]] — musisz poświęcić jednego z dwóch Krenko po SBA.

### Przykład 3 — wiele SBA jednocześnie
> **Sytuacja:** Po ataku: twój 2/2 ma 3 obrażenia (4/4 biło) i 4/4 ma 2 obrażenia (twój 2/2 bił).
> **Zastosowanie zasady:** SBA: twój 2/2 ginie (3 ≥ 2 wytrzymałości). Ich 4/4 przeżywa (2 < 4 wytrzymałości). Oboje sprawdzane jednocześnie.

---

## Powiązane zasady

- [[Zasady/Obrażenia i Zniszczenie]] — kiedy stwory giną
- [[Zasady/Liczniki (Counters)]] — anulowanie par +1/+1 i -1/-1 to SBA
- [[Zasady/Tokeny]] — tokeny poza polem bitwy to SBA

---

## Częste błędy i nieporozumienia

- **Błąd:** "Stwór ginie natychmiast gdy dostanie śmiertelne obrażenia."
  **Poprawnie:** Stwór ginie przy **następnym** sprawdzeniu SBA — nie w połowie aktywowanej zdolności czy czaru.

- **Błąd:** "Gracz może odpowiedzieć na SBA."
  **Poprawnie:** SBA są sprawdzane **przed** oddaniem priorytetu. Nie można na nie odpowiedzieć.
