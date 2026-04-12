---
tags:
  - zasada
numer_zasady: "603"
kategoria: Mechanika zaawansowana
---

# Triggered vs Activated Abilities

> [!note] Oficjalny numer
> Zasada **603** (Triggered), **602** (Activated) — Kompleksowe Zasady MtG

---

## Definicja

**Triggered Ability** — zdolność aktywująca się automatycznie gdy nastąpi określone zdarzenie (trigger).

**Activated Ability** — zdolność którą gracz **aktywuje** płacąc koszt.

---

## Jak je odróżnić

| Cecha | Triggered | Activated |
|---|---|---|
| Słowa kluczowe | „when", „whenever", „at" | Format: `[Koszt]: [Efekt]` |
| Aktywacja | Automatyczna | Wymaga decyzji gracza |
| Koszt | Brak (trigger to nie koszt) | Zawsze ma koszt (mana, tap, etc.) |
| Może być „Stifled"? | Tak (Stifle kontruje triggered) | Tak |

---

## Triggered Abilities

### Trigger — zdarzenie wywołujące
Gdy trigger nastąpi → zdolność wchodzi na Stack przy następnej okazji gdy gracz dostanie priorytet.

### Przykłady triggerów

```
"Whenever ~ attacks, ..."          → trigger: deklaracja ataku
"When ~ enters the battlefield, ..." → trigger: ETB
"At the beginning of your upkeep, ..." → trigger: krok upkeep
"Whenever a creature dies, ..."    → trigger: śmierć stwora
```

### ETB (Enters the Battlefield)
Najczęstszy typ triggera — zdolność aktywuje się gdy permanenty wchodzi na pole bitwy.
> **Przykład:** Solemn Simulacrum — „When ~ enters the battlefield, you may search your library for a basic land card..."

---

## Activated Abilities

### Format: `[Koszt]: [Efekt]`
Dwukropek oddziela koszt od efektu — zawsze.

### Przykłady kosztów
```
{T}: ...               → koszt: tapowanie
{2}{R}: ...            → koszt: 2 bezbarwne + 1 czerwona mana
{T}, Sacrifice ~: ... → koszt: tap + poświęcenie
{1}: ...               → koszt: 1 bezbarwna mana
```

### Ograniczenia Activated Abilities
- Zdolności z `{T}` lub `{Q}` — nie można aktywować ze summoning sickness (chyba że Haste)
- Zdolności manowe (Mana Abilities) — aktywowane w odpowiedzi bez wchodzenia na Stack
- Zdolności lojalnościowe planeswalkerów — raz na turę, tylko w Main Phase przy pustym Stack

---

## Przykłady porównawcze

### Przykład 1 — ETB Triggered vs Activated
> **Triggered:** Ravenous Chupacabra — „When ~ enters the battlefield, destroy target creature..."
> → Automatycznie po wejściu → wchodzi na Stack
>
> **Activated:** Visara the Dreadful — „{T}: Destroy target creature."
> → Musisz aktywować ręcznie → płacisz {T} → wchodzi na Stack

### Przykład 2 — Triggered w odpowiedzi
> **Sytuacja:** Wróg Stifle'uje twój ETB trigger Solemn Simulacrum.
> **Zastosowanie zasady:** Triggered Abilities wchodzą na Stack → można je kontrować przez Stifle. Stwór wchodzi normalnie, ale ETB trigger nie rozwiązuje się.

---

## Powiązane zasady

- [[Zasady/Stack i Priorytet]] — oba typy zdolności wchodzą na Stack
- [[Zasady/Haste]] — znosi ograniczenie summoning sickness dla Activated Abilities z `{T}`
- [[Zasady/Replacement Effects]] — NIE wchodzą na Stack (w odróżnieniu od Triggered)

---

## Częste błędy i nieporozumienia

- **Błąd:** "Triggered Ability rozwiązuje się natychmiast — nie można jej kontrować."
  **Poprawnie:** Triggered Abilities wchodzą na Stack i można na nie odpowiedzieć. Stifle kontruje triggered ability.

- **Błąd:** "Mana Abilities wchodzą na Stack."
  **Poprawnie:** Mana Abilities (zdolności generujące manę — tapowanie lądów) **nie wchodzą na Stack** — są specjalnym wyjątkiem. Nie można na nie odpowiedzieć.
