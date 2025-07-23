import pandas as pd
import sqlite3
from datetime import datetime

df = pd.read_csv("gamedata.csv")
df["timestamp"] = pd.to_datetime(df["timestamp"])

conn = sqlite3.connect("game_data.db")
df.to_sql("logs",conn ,if_exists="replace", index=False)

start_events = df[df["event"] == "game_started"]
end_events = df[df["event"] == "game_over"]
mid_events = df[~df["event"].isin(["game_started", "game_over"])]

points = mid_events.groupby("player_id")["score"].sum().reset_index()

sessions = pd.merge(start_events, end_events, on="player_id", suffixes=('_start', '_end'))
sessions["game_duration"] =(sessions["timestamp_end"] - sessions["timestamp_start"]).dt.total_seconds().astype(int)

results= pd.merge(sessions[["player_id" , "game_duration"]], points, on="player_id")
results["total_score"]=results["game_duration"] + results["score"]

results.to_sql("results", conn, if_exists="replace", index=False)

conn.close()
print("DONE")