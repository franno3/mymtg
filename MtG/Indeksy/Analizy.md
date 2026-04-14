# Indeks Analiz

## Wg typu

### Analiza talii
```dataview
TABLE temat, format, data AS "Data"
FROM #analiza AND #talia
SORT data DESC
```

### Analiza karty
```dataview
TABLE temat, format, data AS "Data"
FROM #analiza AND #karta
SORT data DESC
```

### Analiza metagame
```dataview
TABLE temat, format, data AS "Data"
FROM #analiza AND #metagame
SORT data DESC
```

### Inne
```dataview
TABLE temat, format, data AS "Data"
FROM #analiza AND !#talia AND !#karta AND !#metagame
SORT data DESC
```

---

## Wszystkie analizy

```dataview
TABLE temat, typ, format, data AS "Data"
FROM #analiza
SORT data DESC
```
