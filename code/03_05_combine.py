import pandas as pd
from os import path

# change this to the directory where the csv files that come with the book are
# stored
# on Windows it might be something like 'C:/mydir'

DATA_DIR = '/Users/nathan/fantasybook/data'

pg = pd.read_csv(path.join(DATA_DIR, 'player_game_2017_sample.csv'))  # player-game
games = pd.read_csv(path.join(DATA_DIR, 'game_2017_sample.csv'))  # game info
player = pd.read_csv(path.join(DATA_DIR, 'player_2017_sample.csv')) # player info

# player game data
pg_qbs = (pg.query("pos == 'QB'")
          [['player_name', 'team', 'week', 'gameid', 'pass_yards', 'pass_tds']]
          .head())

# game table
games.head()

# Merge Question 1. What columns are you joining on?
pd.merge(pg, games[['gameid', 'home', 'away']], on='gameid').head()

rush_df = pg[['gameid', 'player_id', 'rush_yards', 'rush_tds']]
rec_df = pg[['gameid', 'player_id', 'rec_yards', 'rec_tds']]

combined = pd.merge(rush_df, rec_df, on=['player_id', 'gameid'])
combined.head()

# Merge Question 2. Are you doing a 1:1, 1:many (or many:1), or many:many
# join?player.head()

player['player_id'].duplicated().any()

combined['player_id'].duplicated().any()

pd.merge(combined, player).head()

# pd.merge(combined, player, validate='1:1')  # this will fail since it's 1:m

# Merge Question 3. What are you doing with unmatched observations?
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

comb_left.head()

comb_outer = pd.merge(rush_df, rec_df, how='outer', indicator=True)
comb_outer.shape

comb_outer['_merge'].value_counts()

# More on pd.merge
# left_on and right_on
rush_df = pg.loc[pg['rush_yards'] > 0,
                 ['gameid', 'player_id', 'rush_yards', 'rush_tds']]
rush_df.columns = ['gameid', 'rusher_id', 'rush_yards', 'rush_tds']

rec_df = pg.loc[pg['rec_yards'] > 0,
          ['gameid', 'player_id', 'rec_yards', 'rec_tds']]
rec_df.columns = ['gameid', 'receiver_id', 'rec_yards', 'rec_tds']

pd.merge(rush_df, rec_df, left_on=['gameid', 'rusher_id'],
    right_on=['gameid', 'receiver_id']).head()

# merging on index
max_rush_df = (rush_df
               .groupby('rusher_id')
               .agg(max_rush_yards = ('rush_yards', 'max'),
                    max_rush_tds =  ('rush_tds', 'max')))

max_rush_df.head()

pd.merge(rush_df, max_rush_df, left_on='rusher_id', right_index=True).head()

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

#### Combining DataFrames Vertically
adp = pd.read_csv(path.join(DATA_DIR, 'adp_2017.csv'))  # adp data

qbs = adp.loc[adp['position'] == 'QB']
rbs = adp.loc[adp['position'] == 'RB']

qbs.shape
rbs.shape

pd.concat([qbs, rbs]).shape

qbs_reset = qbs.reset_index(drop=True)
rbs_reset = rbs.reset_index(drop=True)

qbs_reset.head()

pd.concat([qbs_reset, rbs_reset]).sort_index().head()

pd.concat([qbs_reset, rbs_reset], ignore_index=True).sort_index().head()
