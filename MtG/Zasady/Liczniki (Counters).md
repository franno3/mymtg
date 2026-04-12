---
tags:
  - zasada
numer_zasady: "122"
kategoria: Mechanika
---

# Liczniki (Counters)

> [!note] Oficjalny numer
> Zasada **122** — Kompleksowe Zasady MtG

---

## Definicja

Licznik (counter) to znacznik umieszczany na karcie, permanencie lub graczu, który modyfikuje jego właściwości lub jest używany do śledzenia stanu.

---

## Typy liczników

### Liczniki +1/+1 i -1/-1
Najczęstsze — modyfikują siłę i wytrzymałość stwora.

> **Ważna zasada:** Jeśli stwór ma zarówno liczniki +1/+1 jak i -1/-1, **anulują się** wzajemnie (state-based action). Jeden +1/+1 i jeden -1/-1 = oba znikają.

### Liczniki lojalnościowe (Loyalty counters)
Planeswalkerzy zaczynają z X loyalty (podane w prawym dolnym rogu). Zdolności + dodają, zdolności − odejmują.

### Inne typy liczników

| Typ | Zastosowanie |
|---|---|
| `+1/+1` | Wzmocnienie stwora (Hardened Scales, Scrounging Bandar) |
| `-1/-1` | Osłabienie stwora (Infect, Wither, Hapatra) |
| Poison | Gracz z 10 poison counterami przegrywa |
| Charge | Śledzenie stanu artefaktu/enchantu (Everflowing Chalice) |
| Time | Suspend — odliczanie tur |
| Age, Lore, Level | Specyficzne dla kart |

---

## Liczniki na graczach

- **Poison counters** — zdobywasz je od kart z Infect/Poisonous. Przy 10 przegrywasz grę.
- **Experience counters** — mechanika Commander 2015 — śledzą postęp dowódcy
- **Energy counters** — waluta energii z Kaladesh

---

## Przykłady

### Przykład 1 — +1/+1 counter i rozmiar stwora
> **Sytuacja:** Masz 2/2 z 3 licznikami +1/+1.
> **Zastosowanie zasady:** Stwór jest faktycznie 5/5 (2+3 / 2+3). Liczniki są trwałe — nie znikają na końcu tury.

### Przykład 2 — anulowanie +1/+1 i -1/-1
> **Sytuacja:** Twój 3/3 ma 2 liczniki +1/+1 i 1 licznik -1/-1.
> **Zastosowanie zasady:** SBA: 1 parę +1/+1 i -1/-1 anuluje → zostaje 1 licznik +1/+1. Stwór jest 4/4.

### Przykład 3 — liczniki nie giną przy opuszczaniu pola bitwy
> **Sytuacja:** Twój stwór z 3 licznikami +1/+1 wraca do ręki, potem wchodzi ponownie.
> **Zastosowanie zasady:** Przy powrocie na pole bitwy to „nowy" permanenty — traci wszystkie liczniki. Permanenty nie „pamiętają" poprzednich liczników.

---

## Powiązane zasady

- [[Zasady/State-Based Actions]] — anulowanie +1/+1 i -1/-1 to SBA
- [[Zasady/Replacement Effects]] — Hardened Scales zastępuje dodawanie 1 licznika przez dodanie 2

---

## Częste błędy i nieporozumienia

- **Błąd:** "Liczniki +1/+1 znikają na końcu tury."
  **Poprawnie:** Liczniki są trwałe. Znikają tylko jeśli efekt wyraźnie je usuwa lub permanenty opuści pole bitwy.

- **Błąd:** "Stwór 1/1 z jednym licznikiem -1/-1 po prostu ma 0/0 i ginie."
  **Poprawnie:** Tak — stwór z wytrzymałością ≤0 ginie przez SBA. Ale jeśli ma też +1/+1 counter, pary się anulują.
