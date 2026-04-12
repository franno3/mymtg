# Indeks Decklist

## Wg formatu

### Standard
```dataview
LIST
FROM #decklist AND #standard
SORT data_aktualizacji DESC
```

### Modern
```dataview
LIST
FROM #decklist AND #modern
SORT data_aktualizacji DESC
```

### Commander / EDH
```dataview
TABLE commander, color_identity, archetyp, poziom_mocy AS "Moc", status
FROM #decklist AND #commander
SORT poziom_mocy DESC
```

### Pioneer
```dataview
LIST
FROM #decklist AND #pioneer
```

### Pauper
```dataview
LIST
FROM #decklist AND #pauper
```

---

## Wszystkie talie

```dataview
TABLE format, archetyp, kolory, status, data_aktualizacji AS "Aktualizacja"
FROM #decklist
SORT data_aktualizacji DESC
```
