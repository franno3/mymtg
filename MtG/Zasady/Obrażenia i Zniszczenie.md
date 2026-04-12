---
tags:
  - zasada
numer_zasady: "120"
kategoria: Mechanika
---

# Obrażenia i Zniszczenie

> [!note] Oficjalny numer
> Zasada **120** — Kompleksowe Zasady MtG

---

## Definicja

**Obrażenia** (damage) to ilość szkody zadanej stworzeniu lub graczowi. Stwory giną gdy ich obrażenia są większe lub równe wytrzymałości. Gracze giną gdy życie spada do 0 lub poniżej.

**Zniszczenie** (destroy) to osobny mechanizm — karta z napisem „zniszcz" wysyła permanenty na cmentarz bezpośrednio, bez obrażeń.

---

## Obrażenia vs Zniszczenie — różnica

| Mechanizm | Przykłady | Chroni Indestructible? | Chroni Regeneration? |
|---|---|---|---|
| Obrażenia bojowe | atak, blok | Tak (potrzeba lethal damage) | Tak (regeneracja resetuje) |
| Obrażenia od efektu | Lightning Bolt, Pyroclasm | Tak | Tak |
| Zniszczenie (destroy) | Doom Blade, Wrath of God | Tak | Tak |
| Exile | Path to Exile, Swords to Plowshares | Nie | Nie |
| -X/-X do 0 toughness | Fatal Push efekty | Nie | Nie |

---

## Jak stwory giną od obrażeń

1. Stwór otrzymuje obrażenia (bojowe lub od efektów)
2. Po każdym kroku/fazy sprawdzane są **State-Based Actions**
3. Jeśli obrażenia ≥ wytrzymałość → stwór jest „ze śmiertelną ilością obrażeń" → ginie
4. Obrażenia znikają z kart w Cleanup Step

---

## Obrażenia kumulują się

Obrażenia na stworze kumulują się **przez całą turę** i znikają dopiero w Cleanup Step.

> **Przykład:** Twój 2/4 atakuje i zablokuje go 1/1 (2 obrażenia). Później w tej turze kolejny efekt zadaje mu 2 obrażenia. Łącznie 4 obrażenia = 4/4 wytrzymałości → ginie w następnym sprawdzeniu SBA.

---

## Źródła obrażeń

- **Obrażenia bojowe** — z walki (faza walki)
- **Obrażenia od zdolności** — Lightning Bolt (`{R}`), efekty ETB, triggered abilities
- **Obrażenia ciągłe** — efekty trwające (np. „zadaj 1 obrażenie wszystkim stworom")

---

## Przykłady

### Przykład 1 — obrażenia bojowe i State-Based Actions
> **Sytuacja:** Twój 3/3 walczy z 2/2. Oboje przydzielają obrażenia jednocześnie.
> **Zastosowanie zasady:** Twój 3/3 dostaje 2 obrażenia (3 wytrzymałość → przeżywa). Jego 2/2 dostaje 3 obrażenia (2 wytrzymałość ≤ 3 → ginie w SBA).

### Przykład 2 — obrażenia nie niszczą Indestructible bezpośrednio
> **Sytuacja:** Twój 5/5 atakuje 3/3 Indestructible.
> **Zastosowanie zasady:** 3/3 Indestructible dostaje 5 obrażeń — ale nie ginie. Jednak twój 5/5 ginie od 3 obrażeń zwrotnych. Indestructible przeżywa z 5 ranami (wyczyszczonymi w Cleanup Step).

---

## Powiązane zasady

- [[Zasady/State-Based Actions]] — kiedy stwory faktycznie giną
- [[Zasady/Indestructible]] — chroni przed zniszczeniem, nie przed wszystkimi efektami
- [[Zasady/Deathtouch]] — każda ilość obrażeń od Deathtouch jest lethal
- [[Zasady/Lifelink]] — obrażenia z Lifelink regenerują życie

---

## Częste błędy i nieporozumienia

- **Błąd:** "Stwory giną natychmiast po otrzymaniu śmiertelnych obrażeń."
  **Poprawnie:** Stwory giną dopiero gdy sprawdzane są State-Based Actions — na końcu każdego kroku/fazy. Nie ma to znaczenia w walce, ale ma znaczenie dla zdolności podczas tury.

- **Błąd:** "Destroy i damage to to samo."
  **Poprawnie:** To dwa osobne mechanizmy. Damage kumuluje się i może być zapobiegany przez prevention effects. Destroy wysyła na cmentarz bezpośrednio. Indestructible chroni przed oboma.
