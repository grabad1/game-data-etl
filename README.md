# 🎮 Game Data ETL

Jednostavan ETL projekat za praksu Data Engineering pozicije.

- Učitava CSV fajl sa game eventovima
- Izdvaja početak i kraj sesije po igraču
- Računa ukupne poene i vreme trajanja igre
- Snima podatke u SQLite bazu (`logs` i `player_summary` tabele)

## Pokretanje

1. Instaliraj zavisnosti:
pip install pandas
Pokreni skriptu:

2. Pokreni:
python etl_pipeline.py
3. Otvori game_data.db bazu u SQLite vieweru da pogledaš tabele.