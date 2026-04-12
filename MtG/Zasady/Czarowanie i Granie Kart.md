---
tags:
  - zasada
numer_zasady: "601"
kategoria: Mechanika
---

# Czarowanie i Granie Kart

> [!note] Oficjalny numer
> Zasada **601** — Kompleksowe Zasady MtG

---

## Definicja

Zagranie karty (playing a card) to proces przeniesienia karty do gry — dla czarów przez Stack, dla lądów bezpośrednio na pole bitwy.

---

## Typy kart i gdzie lądują

| Typ | Jak się gra | Gdzie ląduje |
|---|---|---|
| Instant | Na Stack w dowolnym momencie z priorytetem | Po rozwiązaniu: cmentarz |
| Sorcery | Na Stack w Main Phase przy pustym Stack | Po rozwiązaniu: cmentarz |
| Permanenty (Stwór, Artefakt, Enchant, Planeswalker, Land) | Permanenty na Stack (lądy nie) | Pole bitwy |
| Ląd | Gra się bezpośrednio, nie przez Stack | Pole bitwy |

---

## Kroki zagrania czaru

1. **Deklaracja** — ogłaszasz zamiar zagrania czaru, karta wędruje na Stack
2. **Wybór trybów/celów** — jeśli czar ma tryby lub wymaga celów — wybierasz teraz
3. **Określenie kosztów** — bazowy koszt ± modyfikatory (reducery, dodatkowe koszty)
4. **Aktywacja mana abilities** — tapujesz lądy, aktywujesz zdolności many
5. **Płacisz koszty** — manę i inne koszty
6. **Czar jest na Stacku** — gracze dostają priorytet do odpowiedzi

---

## Kiedy można grać czary

| Typ czaru | Kiedy |
|---|---|
| Instant | W dowolnym momencie gdy masz priorytet |
| Sorcery | Tylko w Main Phase (twojej), przy pustym Stack |
| Permanenty | Tylko w Main Phase (twojej), przy pustym Stack |
| Ląd | Tylko w Main Phase (twojej), przy pustym Stack, raz na turę |

---

## Flash

Karta z Flash może być grana jak Instant — w dowolnym momencie gdy masz priorytet, niezależnie od normalnych ograniczeń typu karty.

---

## Przykłady

### Przykład 1 — kolejność kroków
> **Sytuacja:** Chcesz zagrać Lightning Bolt `{R}` na stwora.
> **Kroki:** (1) Deklarujesz Bolt, wchodzi na Stack. (2) Wybierasz cel — stwór 2/2. (3) Koszt = `{R}`. (4) Tapujesz Mountain → `{R}`. (5) Płacisz `{R}`. Bolt na Stacku — przeciwnik może odpowiedzieć.

### Przykład 2 — instant w turze wroga
> **Sytuacja:** Tura wroga. Atakuje cię 3/3. Masz Giant Growth w ręce i 2/2.
> **Zastosowanie zasady:** Giant Growth jest instantem — możesz grać go w fazie walki (masz priorytet po declare blockers). Grasz Giant Growth na swoim 2/2 → staje się 5/5 → blokuje i zabija 3/3.

---

## Powiązane zasady

- [[Zasady/Stack i Priorytet]] — jak Stack działa po zagraniu czaru
- [[Zasady/Mana i Koszt Many]] — płacenie kosztu many
- [[Zasady/Fazy Tury]] — kiedy można grać różne typy kart

---

## Częste błędy i nieporozumienia

- **Błąd:** "Sorcery mogę zagrać w odpowiedzi na coś."
  **Poprawnie:** Sorcery można grać **tylko** w Main Phase przy pustym Stacku. Nie można nim odpowiadać na czary przeciwnika.

- **Błąd:** "Karta wchodzi do gry od razu jak ją gram."
  **Poprawnie:** Permanenty (poza lądami) wchodzą na Stack i muszą się „rozwiązać" zanim trafią na pole bitwy. Przeciwnik może odpowiedzieć zanim wejdą.
