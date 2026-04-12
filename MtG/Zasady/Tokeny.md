---
tags:
  - zasada
numer_zasady: "111"
kategoria: Mechanika
---

# Tokeny (Żetony)

> [!note] Oficjalny numer
> Zasada **111** — Kompleksowe Zasady MtG

---

## Definicja

Token to permanenty stworzony przez efekt karty lub zdolności, który nie ma odpowiednika karty w bibliotece. Tokeny mogą reprezentować stwory, artefakty lub inne typy permanentów.

---

## Kluczowe zasady tokenów

1. **Tokeny nie są kartami** — nie mają wersji karty w talii, można je reprezentować żetonowym kafelkiem lub monety
2. **Token opuszczający pole bitwy przestaje istnieć** — nie trafia do cmentarza, egzylu ani ręki. Znika.
3. **Token ginie od stanu jak normalny stwór** — obrażenia, -X/-X, efekty destroy
4. **Tokeny mogą mieć zdolności** — jeśli efekt je tworzący tak mówi

---

## Token a State-Based Actions

Token z wytrzymałością ≤0 lub ze śmiertelną ilością obrażeń znika w SBA — tak jak normalny stwór, ale nie trafia na cmentarz (znika w próżni).

> **Wyjątek:** Efekty sprawdzające „whether a creature died" (np. Morbid Opportunist) — token który „zginął" (opuścił pole bitwy poprzez zniszczenie/SBA) spełnia warunek śmierci.

---

## Przykłady tokenów

| Token | Typowy opis | Tworząca karta |
|---|---|---|
| Goblin 1/1 red | 1/1 czerwony Goblin | [[Karty/Czerwone/Krenko, Mob Boss\|Krenko, Mob Boss]] |
| Soldier 1/1 white | 1/1 biały Żołnierz | Adeline, Thalia |
| Spirit 1/1 white flying | 1/1 biały Duch z Flying | Lingering Souls |
| Treasure | Artefakt: `{T}`, Sacrifice: add 1 any color mana | Dockside Extortionist |
| Food | Artefakt: `{2}`,`{T}`, Sacrifice: gain 3 life | Oko, Thief of Crowns |

---

## Przykłady

### Przykład 1 — token opuszczający pole bitwy
> **Sytuacja:** Masz 3 żetony 1/1 Goblin. Przeciwnik zagrywa Exile All Creatures.
> **Zastosowanie zasady:** Tokeny zostają wygnane — trafiają do egzylu, ale natychmiast przestają istnieć. Egzyl jest pusty (tokeny znikają).

### Przykład 2 — token a karta w cmentarzu
> **Sytuacja:** Twój token Goblin ginie w walce. Chcesz go przywrócić efektem Reanimation.
> **Zastosowanie zasady:** Token nie trafia na cmentarz — znika. Nie ma czego przywracać. Reanimation nie może dotyczyć tokenów.

### Przykład 3 — Divine Visitation transformuje tokeny
> **Sytuacja:** Masz Divine Visitation w grze. Grasz efekt tworzący 2 żetony 1/1 Goblin.
> **Zastosowanie zasady:** Divine Visitation to Replacement Effect — zamiast 1/1 Goblin tworzysz 4/4 Angel z Flying i Vigilance.

---

## Powiązane zasady

- [[Zasady/State-Based Actions]] — tokeny giną przez SBA tak jak normalne stwory
- [[Zasady/Replacement Effects]] — efekty mogące zastąpić typ tworzonego tokenu
- [[Zasady/Strefy Gry]] — tokeny nie mogą istnieć poza polem bitwy

---

## Częste błędy i nieporozumienia

- **Błąd:** "Mój token Goblin który zginął trafia na cmentarz — mogę go przywrócić."
  **Poprawnie:** Tokeny **nie trafiają na cmentarz** — przestają istnieć. Nie można ich reanimować.

- **Błąd:** "Token wygnany przez Swords to Plowshares zostaje w egzylu."
  **Poprawnie:** Token trafia do egzylu (spełniając warunek wygnania, gracz dostaje życie), ale natychmiast znika jako token.
