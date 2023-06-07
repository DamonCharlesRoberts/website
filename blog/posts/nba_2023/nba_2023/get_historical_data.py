# Title: Get nba score data

# Notes:
    #* Description: 
        #** py script to collect data on nba scores
    #* Updated: 
        #** 2023-03-02
        #** dcr

# import packages
import duckdb as db
import pandas as pd
from nba_api.stats.endpoints import scoreboard

dates = pd.date_range(start='2021-10-19', end='2023-03-02').strftime('%Y-%m-%d').tolist()

scores = pd.DataFrame()
for date in dates:
    score = scoreboard.Scoreboard(game_date = date, day_offset = 0)
    score_df = score.get_data_frames()[0]
    scores = pd.concat([scores, score_df])

db.connect("data/scorecard.db")

db.sql('''
    CREATE OR REPLACE TABLE scorecard AS SELECT * FROM scores
''')