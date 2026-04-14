#!/usr/bin/env python3
"""
Skrypt dodaje brakujące obrazki do plików kart MtG przez Scryfall API.
Uruchom: python3 fix_missing_images.py
"""
import os, re, time, json
import urllib.request, urllib.parse

BASE_DIR = "/home/franno3/workspace/mymtg/MtG/Karty"

# Karty bez obrazka
MISSING = [
    "Bezbarwne/Brute Suit.md",
    "Niebieskie/Serpentine Ambush.md",
    "Niebieskie/Wretched Throng.md",
    "Białe/Unholy Officiant.md",
    "Białe/Seven-Tail Mentor.md",
    "Czarne/Cleaving Reaper.md",
    "Zielone/Glorious Sunrise.md",
    "Zielone/Lambholt Harrier.md",
    "Zielone/Spore Crawler.md",
    "Zielone/Flourishing Hunter.md",
    "Zielone/Topiary Stomper.md",
    "Czerwone/High-Rise Sawjack.md",
    "Czerwone/Mounted Dreadknight.md",
    "Czerwone/Voldaren Stinger.md",
]

def fetch_image_url(card_name):
    url = f"https://api.scryfall.io/cards/named?exact={urllib.parse.quote(card_name)}"
    req = urllib.request.Request(url, headers={"User-Agent": "mymtg/1.0"})
    with urllib.request.urlopen(req, timeout=10) as r:
        data = json.loads(r.read())
    return data.get("image_uris", {}).get("normal", "")

fixed = 0
errors = []

for rel_path in MISSING:
    card_name = os.path.basename(rel_path).replace(".md", "")
    card_path = os.path.join(BASE_DIR, rel_path)

    if not os.path.exists(card_path):
        print(f"  POMINIĘTO (brak pliku): {card_name}")
        continue

    try:
        img_url = fetch_image_url(card_name)
        time.sleep(0.1)  # grzeczność wobec API

        if not img_url:
            errors.append(f"{card_name}: brak image_uris.normal w odpowiedzi")
            continue

        with open(card_path, "r", encoding="utf-8") as f:
            text = f.read()

        # Wstaw obrazek po nagłówku H1
        img_line = f"\n![{card_name}]({img_url})\n"
        new_text = re.sub(
            rf'(# {re.escape(card_name)}\n)',
            rf'\1{img_line}',
            text, count=1
        )

        if new_text != text:
            with open(card_path, "w", encoding="utf-8") as f:
                f.write(new_text)
            print(f"  OK  {card_name}")
            fixed += 1
        else:
            print(f"  ~   {card_name} (nie znaleziono miejsca wstawienia)")

    except Exception as e:
        errors.append(f"{card_name}: {e}")
        print(f"  ERR {card_name}: {e}")

print(f"\nZaktualizowano: {fixed}/{len(MISSING)} kart")
if errors:
    print("Błędy:")
    for e in errors:
        print(f"  - {e}")
