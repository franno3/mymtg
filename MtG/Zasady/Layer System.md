---
tags:
  - zasada
numer_zasady: "613"
kategoria: Mechanika zaawansowana
---

# Layer System (System Warstw)

> [!note] Oficjalny numer
> Zasada **613** — Kompleksowe Zasady MtG

---

## Definicja

System Warstw określa kolejność w jakiej efekty ciągłe (continuous effects) są aplikowane do permanentów. Gdy wiele efektów modyfikuje tę samą kartę, Layer System ustala który efekt działa na bazie którego.

---

## 7 Warstw (w kolejności stosowania)

| Warstwa | Co modyfikuje | Przykłady |
|---|---|---|
| **1** | Efekty kopiowania (Copy effects) | Clone, Spark Double |
| **2** | Efekty kontroli (Control-changing) | Threaten, Act of Treason |
| **3** | Efekty typu i podtypu (Text-changing) | Xenograft, Conspiracy |
| **4** | Efekty modyfikujące tekst karty | Sleight of Mind |
| **5** | Efekty zmieniające typ (Type-changing) | Humility |
| **6** | Efekty zdolności (Add/Remove abilities) | Ethereal Armor, Lignify |
| **7** | Efekty mocy/wytrzymałości (P/T) | Giant Growth, Glorious Anthem |

---

## Sublayers warstwy 7

Warstwa 7 (P/T) ma dalszy podział:
- **7a** — wartości bazowe z tekstu karty
- **7b** — efekty ustawiające P/T na konkretną wartość (`becomes X/X`)
- **7c** — efekty modyfikujące o stały bonus (`+2/+2`)
- **7d** — liczniki +1/+1 i -1/-1
- **7e** — efekty przełączające P/T (power/toughness switching)

---

## Dlaczego kolejność warstw ma znaczenie

Efekty są zawsze aplikowane w kolejności **1→7**, niezależnie od tego kiedy weszły do gry (wyjątek: zależności — patrz niżej).

### Przykład — Humility + Lord efekt

> **Sytuacja:** Humility jest w grze (stwory tracą wszystkie zdolności i stają się 1/1). Grasz Goblin Chieftain (Gobliny mają +1/+1 i Haste).
>
> **Warstwa 5:** Humility nie zmienia podtypu Goblin.
> **Warstwa 6:** Humility usuwa wszystkie zdolności → Goblin Chieftain traci swój Lord efekt → Gobliny NIE dostają +1/+1.
> **Warstwa 7c:** Goblin Chieftain Lord efekt nie działa (już usunięty w warstwie 6).
>
> **Wynik:** Gobliny są 1/1 bez zdolności. Chieftain jest 1/1 bez zdolności.

---

## Zależności (Dependencies)

Wyjątek od reguły 1→7: jeśli zastosowanie efektu A zmienia to jak efekt B jest stosowany — A jest stosowany przed B, niezależnie od kolejności warstw.

---

## Praktyczne przykłady

### Przykład 1 — +1/+1 z Countera vs Humility
> **Sytuacja:** Masz 1/1 z 3 licznikami +1/+1 (warstwa 7d). Wróg zagrywa Humility (wszystkie stwory 1/1, tracą zdolności — warstwy 6 i 7b).
>
> **Warstwa 6:** Tracą zdolności.
> **Warstwa 7b:** Humility ustawia P/T na 1/1.
> **Warstwa 7d:** Liczniki +1/+1 dodają +3/+3 → 4/4.
>
> **Wynik:** Stwór jest 4/4 bez zdolności. Liczniki są w warstwie 7d — PÓŹNIEJSZEJ niż 7b Humility.

### Przykład 2 — kolejność wejścia nie ma znaczenia (zazwyczaj)
> **Sytuacja:** Glorious Anthem (+1/+1 dla wszystkich Białych, warstwa 7c) i Opalescence (enchants stają się stworami, warstwa 5) w grze.
>
> Niezależnie od kolejności ich zagrania — Warstwa 5 zawsze przed 7c.

---

## Powiązane zasady

- [[Zasady/Replacement Effects]] — nie mylić z Layer System; Replacement Effects zastępują zdarzenia
- [[Zasady/Liczniki (Counters)]] — liczniki +1/+1 działają w warstwie 7d

---

## Częste błędy i nieporozumienia

- **Błąd:** "Ostatnio zagrany efekt wygrywa."
  **Poprawnie:** Efekty są aplikowane wg warstw **1→7**, nie wg kolejności zagrania. Wyjątek: gdy dwa efekty są w tej samej sublayer — wtedy późniejszy nadpisuje wcześniejszy.

- **Błąd:** "Layer System dotyczy tylko Sorcery i Instantów."
  **Poprawnie:** Layer System dotyczy **efektów ciągłych** — enchantów, efektów permanentów, aur, emblematów. Jednorazowe efekty (rozwiązane czary) nie są objęte.
