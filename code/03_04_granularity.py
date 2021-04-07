import pandas as pd
from os import path

# change this to the directory where the csv files that come with the book are
# stored
# on Windows it might be something like 'C:/mydir'

DATA_DIR = '/Users/nathan/fantasybook/data'

pbp = pd.read_csv(path.join(DATA_DIR, 'play_data_sample.csv'))  # play by play data

# Granularity

# Grouping
pbp.groupby('game_id').sum()

sum_cols = ['yards_gained', 'rush_attempt', 'pass_attempt', 'shotgun']
pbp.groupby('game_id').sum()[sum_cols]

pbp.groupby('game_id').agg({'yards_gained': 'sum', 'play_id':
    'count', 'interception': 'sum', 'touchdown': 'sum'})

pbp.groupby('game_id').agg(
    yards_gained = ('yards_gained', 'sum'),
    nplays = ('play_id', 'count'),
    interception = ('interception', 'sum'),
    touchdown = ('touchdown', 'sum'))

yards_per_team_game = (pbp
                       .groupby(['game_id', 'posteam'])
                       .agg(
                           ave_yards_per_play = ('yards_gained', 'mean'),
                           total_yards = ('yards_gained', 'sum')))

yards_per_team_game

# A note on multilevel indexing
yards_per_team_game.loc[[(2018101412, 'NE'), (2018111900, 'LA')]]

# Stacking and unstacking data
pg = pd.read_csv(path.join(DATA_DIR, 'player_game_2017_sample.csv'))

qbs = pg.loc[pg['pos'] == 'QB', ['player_name', 'week', 'pass_tds']]
qbs.sample(5)

qbs_reshaped = qbs.set_index(['player_name', 'week']).unstack()
qbs_reshaped.head()

total_tds = qbs_reshaped.sum(axis=1).head()

qbs_reshaped.max(axis=0).head()  # note: axis=0 not nec since it's the default

qbs_reshaped_undo = qbs_reshaped.stack()
qbs_reshaped_undo.head()
