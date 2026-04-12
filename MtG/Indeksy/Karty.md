# Indeks Kart

Używaj tagów lub przeglądaj wg koloru:

## Wg koloru
- [[Karty/Białe/|Białe (W)]]
- [[Karty/Niebieskie/|Niebieskie (U)]]
- [[Karty/Czarne/|Czarne (B)]]
- [[Karty/Czerwone/|Czerwone (R)]]
- [[Karty/Zielone/|Zielone (G)]]
- [[Karty/Wielokolorowe/|Wielokolorowe]]
- [[Karty/Bezbarwne/|Bezbarwne / Artefakty]]

## Wg typu
`#stwór` | `#instant` | `#czar` | `#artefakt` | `#enchantment` | `#planeswalker` | `#ląd`

## Wyszukiwanie zaawansowane

Użyj widoku **Dataview** (jeśli plugin aktywny):
```dataview
TABLE koszt_many, typ, edycja
FROM #karta
SORT file.name ASC
```
