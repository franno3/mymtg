---
tags:
  - zasada
numer_zasady: "400"
kategoria: Mechanika
---

# Strefy Gry

> [!note] Oficjalny numer
> Zasada **400** — Kompleksowe Zasady MtG

---

## Definicja

Strefy gry (game zones) to miejsca, w których mogą znajdować się karty. Każda strefa ma inne zasady dotyczące dostępu, widoczności i tego co można z niej robić.

---

## Lista stref

| Strefa | Angielska nazwa | Widoczność | Dostęp |
|---|---|---|---|
| Biblioteka | Library | Zakryta | Właściciel |
| Ręka | Hand | Zakryta (tylko właściciel) | Właściciel |
| Pole bitwy | Battlefield | Otwarta | Wszyscy |
| Cmentarz | Graveyard | Otwarta | Wszyscy |
| Stack | Stack | Otwarta | Wszyscy |
| Egzyl | Exile | Otwarta (zazwyczaj) | Zależnie od efektu |
| Komenda | Command Zone | Otwarta | Zależnie od formatu |

---

## Opis każdej strefy

### Biblioteka (Library)
- Zakryta talia kart
- Normalnie nie możesz zmieniać kolejności kart w bibliotecewielu
- Dobierasz z wierzchniej karty, chyba że efekt mówi inaczej
- Przeszukiwanie biblioteki (search/tutor) zawsze kończy się przetasowaniem

### Ręka (Hand)
- Karty widoczne tylko dla właściciela
- Normalny limit ręki: 7 kart (na koniec tury, Cleanup Step)
- Niektóre efekty pozwalają przeciwnikowi widzieć twoją rękę

### Pole bitwy (Battlefield)
- Współdzielona strefa dla wszystkich permanentów
- Stwory, artefakty, enchanty, lądy, planeswalkerzy — wszystko co jest „w grze"
- Nowy permanent wchodząc na pole bitwy uruchamia efekty ETB (enters the battlefield)

### Cmentarz (Graveyard)
- Zakopane czary i permanenty
- Otwarta strefa — wszyscy widzą twoją kartę na cmentarzu
- Kolejność kart na cmentarzu jest zachowywana (ma znaczenie dla niektórych kart)

### Stack
- Czary i zdolności czekające na rozwiązanie
- Działa LIFO (ostatni wchodzi, pierwszy wychodzi)
- Szczegóły: [[Zasady/Stack i Priorytet]]

### Egzyl (Exile)
- „Limbo" — karty wygnane z gry
- Domyślnie permanentnie (chyba że karta mówi inaczej — np. Suspend, Flashback)
- Niektóre efekty „exilują i zwracają" jako sposób na reset stwora

### Strefa Komendy (Command Zone)
- Specyficzna dla formatu Commander
- Dowódca (Commander) zaczyna i może wracać tu z każdej strefy
- Emblematy planeswalkerów też tu trafiają

---

## Powiązane zasady

- [[Zasady/Stack i Priorytet]] — Stack jako strefa gry
- [[Zasady/Replacement Effects]] — efekty modyfikujące przejścia między strefami
- [[Zasady/Tokeny]] — tokeny przestają istnieć gdy opuszczają pole bitwy

---

## Częste błędy i nieporozumienia

- **Błąd:** "Karta na cmentarzu jest 'poza grą' — nikt jej nie widzi."
  **Poprawnie:** Cmentarz jest **otwartą** strefą — wszyscy gracze mogą w dowolnej chwili przejrzeć dowolny cmentarz.

- **Błąd:** "Egzyl jest permanentny — karty wygnane nigdy nie wracają."
  **Poprawnie:** Wiele efektów egzyluje tymczasowo (Suspend, Detention Sphere, Banishing Light) lub pozwala grać z egzylu (Flashback, Foretell).

- **Błąd:** "Token wygnany z pola bitwy trafia do egzylu i zostaje tam."
  **Poprawnie:** Tokeny znikają gdy opuszczają pole bitwy — nie mogą istnieć w żadnej innej strefie. Wygnany token przestaje istnieć w momencie dotarcia do egzylu.
