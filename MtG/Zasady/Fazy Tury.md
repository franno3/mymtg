---
tags:
  - zasada
numer_zasady: "500"
kategoria: Mechanika
---

# Fazy Tury

> [!note] Oficjalny numer
> Zasada **500** — Kompleksowe Zasady MtG

---

## Definicja

Każda tura składa się z pięciu faz, które następują po sobie w określonej kolejności: Beginning Phase, Pre-combat Main Phase, Combat Phase, Post-combat Main Phase, Ending Phase.

---

## Struktura tury

```
┌─────────────────────────────────────────────────┐
│  BEGINNING PHASE (Faza Początku)                │
│    └─ Untap Step       — odtapuj wszystko       │
│    └─ Upkeep Step      — zdolności upkeep       │
│    └─ Draw Step        — dobierz kartę          │
├─────────────────────────────────────────────────┤
│  PRE-COMBAT MAIN PHASE (Główna 1)               │
│    └─ Zagraj lądy, zaklęcia, aktywuj zdolności  │
├─────────────────────────────────────────────────┤
│  COMBAT PHASE (Faza Walki)                      │
│    └─ Beginning of Combat                       │
│    └─ Declare Attackers                         │
│    └─ Declare Blockers                          │
│    └─ Combat Damage                             │
│    └─ End of Combat                             │
├─────────────────────────────────────────────────┤
│  POST-COMBAT MAIN PHASE (Główna 2)              │
│    └─ Zagraj lądy (jeśli nie zagrałeś), czary  │
├─────────────────────────────────────────────────┤
│  ENDING PHASE (Faza Końca)                      │
│    └─ End Step  — zdolności "at end of turn"    │
│    └─ Cleanup   — odrzuć do 7 kart, usuń rany  │
└─────────────────────────────────────────────────┘
```

---

## Wyjaśnienie każdej fazy

### Untap Step
- Odtapowyjesz wszystkie swoje permanenty
- Nikt nie dostaje priorytetu (nie można grać czarów)

### Upkeep Step
- Aktywują się zdolności mówiące „na początku twojego upkeep"
- Gracze dostają priorytet — można grać instants i aktywować zdolności

### Draw Step
- Dobierasz 1 kartę (pierwszy gracz w turze 1 nie dobiera)
- Aktywują się zdolności „na początku twojego draw step"

### Pre-combat Main Phase
- Możesz zagrać jeden ląd
- Możesz grać sorceries, instants, permanenty, aktywować zdolności
- Stwory wystawione tutaj mają summoning sickness — nie mogą atakować (chyba że mają Haste)

### Combat Phase
- Szczegóły w: [[Zasady/Faza Walki]]

### Post-combat Main Phase
- Identyczna z Pre-combat, ale stwory wystawione tu **nie mogą** atakować w tej turze (minęła faza walki)
- Dobry moment na zagranie kart po zobaczeniu jak skończyła się walka

### End Step
- Zdolności „at the beginning of the end step" aktywują się
- Ważny moment dla triggerów Commander decków (np. Thalisse)

### Cleanup Step
- Odrzucasz karty do 7 (hand size) jeśli masz za dużo
- Wszystkie obrażenia na stworach zostają usunięte
- Większość efektów „until end of turn" wygasa

---

## Powiązane zasady

- [[Zasady/Faza Walki]] — szczegóły fazy walki
- [[Zasady/Stack i Priorytet]] — kiedy gracze dostają priorytet do grania kart
- [[Zasady/Haste]] — znosi ograniczenie ataku w turze wejścia

---

## Częste błędy i nieporozumienia

- **Błąd:** "Mogę zagrać ląd w dowolnym momencie tury."
  **Poprawnie:** Ląd możesz zagrać tylko raz na turę, tylko w Main Phase (twojej), gdy Stack jest pusty.

- **Błąd:** "Stwory wyczyszczają obrażenia na końcu każdej fazy."
  **Poprawnie:** Obrażenia są usuwane tylko w **Cleanup Step** — na końcu tury. W trakcie tury kumulują się.
