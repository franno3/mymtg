---
tags:
  - zasada
numer_zasady: "405"
kategoria: Mechanika
---

# Stack i Priorytet

> [!note] Oficjalny numer
> Zasada **405** — Kompleksowe Zasady MtG (Stack), **116** (Priority)

---

## Definicja

**Stack** to strefa gry, na której lądują czary i zdolności zanim zostaną rozwiązane. Każdy czar lub zdolność wchodzi na Stack i pozostaje tam aż nie zostanie rozwiązana lub kontrowana.

**Priorytet** to prawo do zagrania czarów lub aktywowania zdolności. Gracze dostają priorytet po sobie, zawsze zaczynając od aktywnego gracza.

---

## Jak działa Stack

```
Stack działa na zasadzie LIFO (Last In, First Out):
ostatni dodany element rozwiązuje się pierwszy.

Gracz A zagrywa Bolt → Stack: [Bolt]
Gracz B reaguje Counterspell → Stack: [Bolt, Counterspell]
Nikt nic nie dodaje → Counterspell rozwiązuje się → Bolt kontrowany
Stack: []
```

---

## Przepływ priorytetu

1. Aktywny gracz dostaje priorytet
2. Może zagrać czar, aktywować zdolność lub pass priority
3. Jeśli pass → nieaktywny gracz dostaje priorytet
4. Jeśli **oboje** pass z pustym Stackiem → przechodzi do następnego kroku/fazy
5. Jeśli **oboje** pass z czymś na Stacku → górny element rozwiązuje się
6. Po rozwiązaniu — aktywny gracz dostaje priorytet ponownie

---

## Kiedy można grać instants i zdolności

- W **dowolnym** momencie gdy masz priorytet
- Na Stack można odpowiadać innymi instantami i zdolnościami
- Sorcery, permanenty, lądy — **tylko** w Main Phase przy pustym Stacku i twoim priorytecie

---

## Przykłady

### Przykład 1 — odpowiedź na removal
> **Sytuacja:** Przeciwnik zagrywa Doom Blade na twój stwór. Masz Counterspell.
> **Zastosowanie zasady:** Doom Blade wchodzi na Stack → dostajesz priorytet → grasz Counterspell → Stack: [Doom Blade, Counterspell] → Counterspell rozwiązuje się i kontruje Doom Blade → stwór bezpieczny.

### Przykład 2 — odpowiedź na removal instantem
> **Sytuacja:** Przeciwnik zagrywa Lightning Bolt na twój 2/2. Masz Giant Growth (+3/+3).
> **Zastosowanie zasady:** Bolt na Stack → grasz Giant Growth → twój 2/2 staje się 5/5 → Bolt rozwiązuje się i zadaje 3 dmg → twój 5/5 przeżywa (ma 3 rany, 5 wytrzymałości).

### Przykład 3 — wiele triggerów na Stacku
> **Sytuacja:** Twoja karta trafia do cmentarza. Masz Zulaport Cutthroat i Blood Artist — oba triggerują "whenever a creature dies".
> **Zastosowanie zasady:** Oboje właściciel układa oba triggery na Stack w wybranej kolejności. Każdy rozwiązuje się osobno.

---

## Powiązane zasady

- [[Zasady/Triggered vs Activated Abilities]] — zdolności wchodzące na Stack
- [[Zasady/Czarowanie i Granie Kart]] — jak czary wchodzą na Stack
- [[Zasady/Replacement Effects]] — efekty które NIE wchodzą na Stack

---

## Częste błędy i nieporozumienia

- **Błąd:** "Mogę zagrać instant w dowolnym momencie nawet podczas untap."
  **Poprawnie:** Instants można grać tylko gdy masz **priorytet**. Untap i Cleanup Step normalnie nie dają priorytetu.

- **Błąd:** "Gdy zagrałem czar — przeciwnik nie może nic zrobić."
  **Poprawnie:** Po zagraniu czaru przeciwnik dostaje priorytet i może odpowiedzieć instantem lub zdolnością.

- **Błąd:** "Triggered ability rozwiązuje się natychmiast."
  **Poprawnie:** Triggery wchodzą na Stack i czekają na rozwiązanie — aktywny gracz dostaje priorytet po pojawieniu się triggera i może odpowiedzieć.
