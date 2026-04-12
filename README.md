# 🎴 myMtG PL

> **Polska baza wiedzy Magic: The Gathering** publikowana jako nowoczesna wiki z wykorzystaniem Quartz 4

Osobista kolekcja notatek o kartach, dekach, zasadach i mechanikach MTG, przekształcona w przeszukiwalną stronę internetową z pełnym wsparciem dla linków wewnętrznych, tagów i grafów połączeń.

🌐 **[mtg.calmcat.blog](https://mtg.calmcat.blog)** — zobacz live

---

## ✨ Cechy projektu

### 📚 Zawartość
- **Karty** — szczegółowe opisy ~200+ kart z obrazkami, tłumaczeniami i interakcjami
- **Decklists** — gotowe i testowe talie Commander/60-card
- **Zasady** — kompleksowe zasady gry
- **Edycje** — informacje o setkach kart
- **Formaty** — Standard, Modern, Commander i inne

### 🎨 Technologia
- **[Quartz 4](https://quartz.jzhao.xyz)** — statyczny generator z Obsidian-compatible Markdown
- **Obsidian-flavored links** — `[[Nazwa Karty]]` automatycznie linkowane
- **Dark/Light mode** — elegancka kolorystyka dostosowana do MTG
- **Graf połączeń** — wizualizacja relacji między kartami i taliami
- **Instant search** — FlexSearch z podglądem
- **SPA routing** — płynne przejścia między stronami

---

## 🚀 Instalacja i uruchomienie

### Wymagania
```bash
node >= 22
npm >= 10.9.2
```

### Pierwsze uruchomienie
```bash
# Klonowanie repo
git clone https://github.com/franno3/mymtg.git
cd mymtg

# Instalacja zależności
npm install

# Build i serwowanie lokalnie
npx quartz build --serve

# Strona dostępna pod http://localhost:8080
```

### Komendy
```bash
# Build produkcyjny (output → public/)
npx quartz build

# Serwowanie z hot-reload
npx quartz build --serve

# Formatowanie kodu
npm run format

# Sprawdzenie typów
npm run check
```

---

## 📂 Struktura projektu

```
mymtg/
├── MtG/                    # Wszystkie treści wiki
│   ├── Karty/              # Opisy kart (sortowane po kolorze)
│   │   ├── Białe/
│   │   ├── Niebieskie/
│   │   ├── Czarne/
│   │   ├── Czerwone/
│   │   ├── Zielone/
│   │   ├── Bezbarwne/
│   │   └── Wielokolorowe/
│   ├── Decklists/          # Gotowe talie
│   ├── Edycje/             # Setki kart
│   ├── Formaty/            # Opisy formatów
│   ├── Zasady/             # Kompleksowe zasady
│   ├── Indeksy/            # Strony nawigacyjne
│   ├── Szablony/           # Szablony notatek
│   └── index.md            # Strona główna wiki
├── quartz/                 # Engine Quartz
├── quartz.config.ts        # Konfiguracja motywu, pluginów
├── quartz.layout.ts        # Layout strony
└── package.json
```

---

## 📝 Format notatek

Każda karta używa YAML frontmatter + Markdown:

```markdown
---
tags:
  - karta
  - biały
  - stwór
kolor:
  - biały
typ: Stwór
podtyp: Legendary Human Knight
koszt_many: "{1}{W}{W}"
rzadkość: Rare
---

# Adeline, Resplendent Cathar

![Adeline](https://cards.scryfall.io/normal/front/...)

> [!info] Statystyki
> **Koszt many:** `{1}{W}{W}`
> **Typ:** Legendarny Stwór — Human Knight

## Tekst karty
...

## Zasady i interakcje
- Siła rośnie z każdym stworzeniem
- [[Blade of Selves]] — synergy!
```

Linki w stylu Obsidian (`[[Nazwa]]`) automatycznie działają.

---

## 🎨 Konfiguracja motywu

Kolory dostosowane do estetyki MTG (patrz `quartz.config.ts`):

```typescript
colors: {
  lightMode: {
    secondary: "#284b63",   // Niebieski MTG
    tertiary: "#84a59d",    // Zieleń MTG
    // ...
  }
}
```

---

## 🔧 Deployment

### GitHub Pages / Cloudflare Pages
```bash
# Build
npx quartz build

# Deploy folder `public/` na dowolny static hosting
```

### Automatyczny deploy
Projekt korzysta z Quartz sync — każdy push na `main` automatycznie buduje i publikuje stronę.

---

## 🛠️ Customizacja

### Dodanie nowej karty
1. Stwórz plik w `MtG/Karty/[Kolor]/Nazwa.md`
2. Użyj szablonu z `MtG/Szablony/Szablon Karty.md`
3. Wypełnij frontmatter + opisy
4. Build → karta pojawi się w grafie i wyszukiwarce

### Zmiana motywu
Edytuj `quartz.config.ts` → sekcja `theme`

---

## 📊 Statystyki

- **~200+ kart** z pełnymi opisami
- **6 kategorii kolorów** (białe, niebieskie, czarne, czerwone, zielone, bezbarwne/multicolor)
- **Integracja Scryfall** — obrazy kart z oficjalnego API
- **Responsywny design** — działa na mobile/desktop

---

## 🔗 Integracje

### Scryfall API
Obrazy kart automatycznie linkowane do Scryfall:
```markdown
![Nazwa](https://cards.scryfall.io/normal/front/...)
```

### Obsidian (opcjonalnie)
Możesz edytować folder `MtG/` w Obsidian — wszystkie linki i tagi będą działać.

---

## 📜 Licencja

**MIT License** — kod strony open source.

### Zastrzeżenia prawne
- **Obrazy kart** — własność Wizards of the Coast
- Projekt niekomercyjny, zgodny z [WotC Fan Content Policy](https://company.wizards.com/en/legal/fancontentpolicy)
- Dane z [Scryfall API](https://scryfall.com/docs/api) (użytek niekomercyjny dozwolony)

---

## 🤝 Współpraca

Pull requesty mile widziane! Jeśli masz:
- Nowe karty do dodania
- Poprawki w tłumaczeniach
- Ulepszenia layoutu

Otwórz issue lub PR.

---

## 📚 Przydatne linki

- [Quartz Documentation](https://quartz.jzhao.xyz)
- [Scryfall](https://scryfall.com)
- [MTG Comprehensive Rules](https://magic.wizards.com/en/rules)
- [EDHREC](https://edhrec.com) — statystyki Commander

---

**Zbudowano z ❤️ dla społeczności MTG PL**
