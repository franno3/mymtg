---
tags:
  - zasada
numer_zasady: "903.4"
kategoria: Mechanika
---

# Color Identity

> [!note] Oficjalny numer
> Zasada **903.4** — Kompleksowe Zasady MtG (sekcja Commander)

---

## Definicja

Color identity karty to zbiór wszystkich symboli many (`{W}`, `{U}`, `{B}`, `{R}`, `{G}`) które pojawiają się:
1. W koszcie many karty (mana cost)
2. W tekście reguł karty (rules text)
3. Na każdej stronie karty dwustronnej (DFC)

---

## Wyjaśnienie prostym językiem

Color identity decyduje jakich kart możesz użyć w Commander decku. Talia może zawierać **tylko** karty których color identity mieści się w color identity twojego dowódcy.

**Kolor karty ≠ color identity karty** — to dwie różne rzeczy.

---

## Przykłady

### Przykład 1 — tekst karty rozszerza color identity
> **Karta:** Karlov of the Ghost Council ({W}{B})  
> **Tekst:** `{2}{W}{B}: Exile target creature...`  
> **Color identity:** W, B (koszt many i tekst zgadzają się → WB)

### Przykład 2 — zdolność modalna
> **Karta:** Firesong and Sunspeaker ({4}{R}{W})  
> **Color identity:** R, W

### Przykład 3 — karta z mana ability innego koloru
> **Karta:** Bounty Agent ({1}{W}) z tekstem `{G}{W}: ...`  
> **Color identity:** G, W — choć karta jest biała, ma zielony symbol w tekście!

### Przykład 4 — karta bezbarwna z kolorowym tekstem
> **Karta:** Transguild Courier ({4}) — bezbarwna  
> **Color identity:** bezbarwna — brak symboli many *(reminder text w nawiasach nie liczy się)*

### Przykład 5 — co NIE liczy się do color identity
> - Tekst w nawiasach `(reminder text)` — nie liczy się
> - Flavor text — nie liczy się  
> - Nazwa koloru pisana słowem (np. "red") — nie liczy się, tylko symbol many

---

## Powiązane zasady

- [[Zasady/Commander.md|Format Commander]] — gdzie color identity jest kluczowa
- [[Formaty/Commander]] — zasady budowania talii

---

## Karty ilustrujące tę zasadę

![Atraxa, Praetors' Voice](https://cards.scryfall.io/normal/front/d/0/d0d33d52-3d28-4635-b985-51e126289259.jpg)

- Sidar Kondo of Jamuraa — Partner, WG color identity
- Thrasios, Triton Hero — Partner, UG color identity

---

## Częste błędy i nieporozumienia

- **Błąd:** "Karta bezbarwna może wejść do każdej talii Commander."  
  **Poprawnie:** Tak, karty bezbarwne (bez symboli many) mogą być w każdej talii — Sol Ring, Wastes, artefakty bezbarwne.

- **Błąd:** "Mogę grać Forest w moim mono-czerwonym Commander decku."  
  **Poprawnie:** Nie — Forest ma zieloną color identity i nie może wejść do czerwonej talii. Używaj Wastes lub Mountain.

- **Błąd:** "Reminder text liczy się do color identity."  
  **Poprawnie:** Nie — `(This spell can't be countered.)` czy `(You can cast this only during...)` to reminder text w nawiasach — ignorowany przy color identity.

- **Błąd:** "Mogę użyć karty z Phyrexian mana {G/P} w mono-czarnej talii."  
  **Poprawnie:** Nie — {G/P} zawiera symbol zielonej many → color identity: G. Karta nie może wejść do mono-czarnej talii.
