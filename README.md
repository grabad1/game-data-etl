# 🎮 Game Data ETL

A simple ETL project for a Data Engineering internship.

- Loads a CSV file with game events  
- Extracts start and end of sessions per player  
- Calculates total points and session duration  
- Saves data into a SQLite database (`logs` and `player_summary` tables)  

## How to run

1. Install dependencies:  
pip install panda

2. Run the script:
python etl_pipeline.py

3. Open the game_data.db database in a SQLite viewer to check the tables.
