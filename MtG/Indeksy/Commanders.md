# Indeks Dowódców (Commanders)

Dowódcą może być: **legendarny stwór** lub **planeswalker z dopiskiem "can be your commander"**.

---

## Filtr wg color identity

### Mono-kolorowi
```dataview
TABLE color_identity, podtyp, koszt_many AS "CMC"
FROM #karta AND #dowódca AND #mono
SORT color_identity ASC
```

### Dwukolorowi (Guild)
```dataview
TABLE color_identity, podtyp, koszt_many AS "CMC"
FROM #karta AND #dowódca AND #guild
SORT color_identity ASC
```

### Trzykolorowi (Shard / Wedge)
```dataview
TABLE color_identity, podtyp, koszt_many AS "CMC"
FROM #karta AND #dowódca AND #shard
SORT color_identity ASC
```

### Czterokolorowi i pięciokolorowi
```dataview
TABLE color_identity, podtyp, koszt_many AS "CMC"
FROM #karta AND #dowódca AND #multi
SORT color_identity ASC
```

---

## Wszyscy dowódcy w bazie

```dataview
TABLE color_identity, podtyp, koszt_many AS "Koszt", edycja
FROM #karta AND #dowódca
SORT color_identity ASC
```

---

## Partnerzy

```dataview
TABLE color_identity, koszt_many AS "Koszt"
FROM #karta AND #dowódca AND #partner
SORT file.name ASC
```

---

## Jak oznaczyć kartę jako dowódcę?

Dodaj do frontmatter karty:
```yaml
tags:
  - karta
  - dowódca          # oznacza że może być Commander
  - mono             # lub: guild | shard | wedge | multi | bezbarwny
color_identity: "R"  # np. R, UG, WBR, WUBRG
moze_byc_dowodca: true
```
