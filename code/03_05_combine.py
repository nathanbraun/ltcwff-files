import pandas as pd
import numpy as np
from os import path

# change this to the directory where the csv files that come with the book are
# stored
# on Windows it might be something like 'C:/mydir'

DATA_DIR = '/Users/nathan/fantasybook/data'

pg = pd.read_csv(path.join(DATA_DIR, 'player_game_2017_sample.csv'))  # player-game
games = pd.read_csv(path.join(DATA_DIR, 'game_2017_sample.csv'))  # game info

# things to care about while merging:
# 1. The columns you're joining on.
pd.merge(pg, games[['gameid', 'home', 'away']]).head()

rush_df = pg[['gameid', 'player_id', 'rush_yards', 'rush_tds']]
rec_df = pg[['gameid', 'player_id', 'rec_yards', 'rec_tds']]

combined = pd.merge(rush_df, rec_df, on=['player_id', 'gameid'])
combined.head()

# 2. Whether you're doing a one-to-one, one-to-many, or many-to-many merge
player = pd.read_csv(path.join(DATA_DIR, 'player_2017_sample.csv')) # player info

player['player_id'].duplicated().any()

pg['player_id'].duplicated().any()

pd.merge(combined, player).head()

# pd.merge(combined, player, validate='1:1')  # this will fail since it's 1:m

# 3. What you do with unmatched observations
rush_df = pg.loc[pg['rush_yards'] > 0,
       ['gameid', 'player_id', 'rush_yards', 'rush_tds']]

rec_df = pg.loc[pg['rec_yards'] > 0,
          ['gameid', 'player_id', 'rec_yards', 'rec_tds']]

rush_df.shape
rec_df.shape

comb_inner = pd.merge(rush_df, rec_df)
comb_inner.shape

comb_left = pd.merge(rush_df, rec_df, how='left')
comb_left.shape

comb_outer = pd.merge(rush_df, rec_df, how='outer', indicator=True)
comb_outer.shape

comb_outer['_merge'].value_counts()

# More on pd.merge
# left_on and right_on
rush_df = pg.loc[pg['rush_yards'] > 0,
                 ['gameid', 'player_id', 'rush_yards', 'rush_tds']]
rush_df.columns = ['gameid', 'rb_id', 'rush_yards', 'rush_tds']

pd.merge(rush_df, rec_df, left_on=['gameid', 'rb_id'],
    right_on=['gameid', 'player_id']).head()

# merging on index
max_rush_df = rush_df.groupby('rb_id')[['rush_yards', 'rush_tds']].max()
max_rush_df.head()

max_rush_df.columns = [f'max_{x}' for x in max_rush_df.columns]
max_rush_df.columns

pd.merge(rush_df, max_rush_df, left_on='rb_id', right_index=True).head()

#############
# pd.concat()
#############
rush_df = (pg.loc[pg['rush_yards'] > 0,
                  ['gameid', 'player_id', 'rush_yards', 'rush_tds']]
           .set_index(['gameid', 'player_id']))

rec_df = (pg.loc[pg['rec_yards'] > 0,
                 ['gameid', 'player_id', 'rec_yards', 'rec_tds']]
          .set_index(['gameid', 'player_id']))

pd.concat([rush_df, rec_df], axis=1).head()

pass_df = (pg.loc[pg['pass_yards'] > 0,
                  ['gameid', 'player_id', 'pass_yards', 'pass_tds']]
           .set_index(['gameid', 'player_id']))

pd.concat([rush_df, rec_df, pass_df], axis=1).head()

adp = pd.read_csv(path.join(DATA_DIR, 'adp_2017.csv'))  # adp data

qbs = adp.loc[adp['position'] == 'QB']
rbs = adp.loc[adp['position'] == 'RB']

qbs.shape
rbs.shape

pd.concat([qbs, rbs]).shape
