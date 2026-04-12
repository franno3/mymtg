---
tags:
  - zasada
numer_zasady: "506"
kategoria: Mechanika
---

# Faza Walki

> [!note] Oficjalny numer
> Zasada **506** — Kompleksowe Zasady MtG

---

## Definicja

Faza walki (Combat Phase) składa się z pięciu kroków: Beginning of Combat, Declare Attackers, Declare Blockers, Combat Damage, End of Combat.

---

## Struktura fazy walki

```
1. Beginning of Combat Step
   └─ Zdolności "at the beginning of combat" aktywują się
   └─ Oboje dostają priorytet

2. Declare Attackers Step
   └─ Aktywny gracz deklaruje atakujących (tapuje ich, chyba że mają Vigilance)
   └─ Zdolności "whenever X attacks" aktywują się
   └─ Oboje dostają priorytet

3. Declare Blockers Step
   └─ Nieatywny gracz deklaruje blokerów
   └─ Aktywny gracz ustala kolejność obrażeń dla każdego blokowanego stwora
   └─ Zdolności "whenever X blocks/becomes blocked" aktywują się
   └─ Oboje dostają priorytet

4. Combat Damage Step
   └─ Krok 1 (jeśli ktoś ma First/Double Strike): first strike damage
   └─ Krok 2: normal damage — wszyscy przydzielają obrażenia jednocześnie
   └─ State-Based Actions sprawdzane po każdym kroku

5. End of Combat Step
   └─ Zdolności "at end of combat" aktywują się
   └─ Atakujący i blokujący przestają być "atakującymi/blokującymi"
```

---

## Szczegóły ważnych kroków

### Declare Attackers
- Możesz atakować dowolnego gracza lub planeswalkerów
- Atakujące stwory tapują się (chyba że mają Vigilance lub specjalny efekt)
- Stwory z summoning sickness **nie mogą** atakować (chyba że mają Haste)

### Declare Blockers
- Każdy bloker może blokować tylko jeden atak, ale jeden atak może mieć wielu blokerów
- Stwory tapowane **nie mogą** blokować
- Blokować można stwory z Flying **tylko** posiadając Flying lub Reach
- Stwory z Menace wymagają co najmniej 2 blokerów

### Combat Damage
- Jeśli ktoś ma First Strike lub Double Strike — dwa kroki obrażeń
- Obrażenia od wszystkich atakujących/blokujących przydzielane **jednocześnie**
- Stwór blokujący przydziela obrażenia wg kolejności ustalonej przez atakującego gracza

---

## Powiązane zasady

- [[Zasady/Flying]] — blokowanie stworów latających
- [[Zasady/First Strike]] — dodatkowy krok obrażeń
- [[Zasady/Trample]] — obrażenia przechodzące przez blokera
- [[Zasady/Menace]] — wymóg liczby blokerów
- [[Zasady/Vigilance]] — atakowanie bez tapowania
- [[Zasady/Haste]] — atak w turze wejścia
- [[Zasady/Fazy Tury]] — faza walki w kontekście całej tury

---

## Częste błędy i nieporozumienia

- **Błąd:** "Mogę zagłosować na blokowanie w dowolnym momencie."
  **Poprawnie:** Blokować można **tylko** w kroku Declare Blockers — nie można zdecydować się na blok po tym jak atakujący zakończyli deklarowanie.

- **Błąd:** "Mogę zmienić blokerów po tym jak deklaruję atakujących."
  **Poprawnie:** Po zakończeniu kroku Declare Blockers blokerzy są przypisani — nie można ich zmienić (chyba że specjalny efekt na to pozwala).

- **Błąd:** "Stwory tapowane mogą blokować."
  **Poprawnie:** Tapowane stwory **nie mogą** być deklarowane jako blokujące.
