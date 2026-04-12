---
tags:
  - zasada
numer_zasady: "614"
kategoria: Mechanika zaawansowana
---

# Replacement Effects (Efekty Zastępowania)

> [!note] Oficjalny numer
> Zasada **614** — Kompleksowe Zasady MtG

---

## Definicja

Replacement Effect to efekt, który **zastępuje** jedno zdarzenie innym, zanim to pierwsze nastąpi. Nie wchodzą na Stack, nie mogą być kontrowane — działają automatycznie.

---

## Jak rozpoznać Replacement Effect

Kluczowe słowa: **„instead"** (zamiast), **„as ... enters"**, **„skip"**.

> „If a creature would die, exile it instead."
> „As ~ enters the battlefield, ..."
> „Skip your draw step."

---

## Typy Replacement Effects

### ETB Replacement Effects
Modyfikują jak permanenty wchodzą na pole bitwy.
> **Przykład:** „~ enters with X +1/+1 counters" — to nie trigger, to Replacement Effect. Stwór wchodzi **już** z licznikami.

### Death Replacement Effects
Zastępują śmierć innym zdarzeniem.
> **Przykład:** Leyline of the Void — „If a card would go to the graveyard, exile it instead."

### Draw Replacement Effects
Zastępują dobieranie kart.
> **Przykład:** Replacement for draw — „Skip your draw step" (Sylvan Library).

### Damage Replacement Effects
Modyfikują jak obrażenia są zadawane.
> **Przykład:** Gisela, Blade of Goldnight — obrażenia zadawane tobie są zmniejszane o połowę (Replacement Effect na obrażeniach).

---

## Replacement vs Triggered Ability

| Cecha | Replacement Effect | Triggered Ability |
|---|---|---|
| Wchodzi na Stack? | Nie | Tak |
| Może być kontrowane? | Nie | Tak (Stifle) |
| Słowa kluczowe | „instead", „as", „skip" | „when", „whenever", „at" |
| Timing | Przed zdarzeniem | Po zdarzeniu |
| Może zapobiec zdarzeniu? | Tak (zastępuje całkowicie) | Nie (reaguje po fakcie) |

---

## Przykłady

### Przykład 1 — ETB z licznikami
> **Sytuacja:** Grasz Walking Ballista za `{4}` (X=2). Masz Hardened Scales w grze.
> **Zastosowanie zasady:** Walking Ballista normalnie wchodzi z 2 licznikami +1/+1. Hardened Scales: „If one or more +1/+1 counters would be placed... put that many plus one instead." → wchodzi z 3 licznikami.

### Przykład 2 — Death Replacement
> **Sytuacja:** Twój stwór miałby trafić na cmentarz. Masz Leyline of the Void.
> **Zastosowanie zasady:** Zamiast na cmentarz → karta trafia do egzylu. Efekty „on death" (Zulaport Cutthroat) nadal się aktywują — stwór nadal „zginął".

### Przykład 3 — Divine Visitation zastępuje tokeny
> **Sytuacja:** Efekt tworzy żetony 1/1 Soldier. Divine Visitation jest w grze.
> **Zastosowanie zasady:** Divine Visitation: „If one or more creature tokens would be created... create that many 4/4 white Angel tokens instead." Żadnych 1/1 Soldiers — same 4/4 Angels.

---

## Powiązane zasady

- [[Zasady/Stack i Priorytet]] — Replacement Effects NIE wchodzą na Stack
- [[Zasady/State-Based Actions]] — SBA nie są Replacement Effects
- [[Zasady/Tokeny]] — Divine Visitation jako przykład Replacement Effect przy tokenach

---

## Częste błędy i nieporozumienia

- **Błąd:** "Replacement Effect wchodzi na Stack — mogę go kontrować."
  **Poprawnie:** Replacement Effects **nie wchodzą na Stack** — działają automatycznie, nie można ich kontrować. Można kontrować tylko czary i triggered/activated abilities.

- **Błąd:** "Stwór który trafił do egzylu zamiast na cmentarz (Replacement Effect) — nie 'zginął'."
  **Poprawnie:** Zginął — opuścił pole bitwy. Efekty „on death" się aktywują. To gdzie trafia to osobna kwestia.
