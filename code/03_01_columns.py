import pandas as pd
from os import path

# change this to the directory where the csv files that come with the book are
# stored
# on Windows it might be something like 'C:/mydir'

DATA_DIR = '/Users/nathan/fantasybook/data'

# load data
pg = pd.read_csv(path.join(DATA_DIR, 'player_game_2017_sample.csv'))

pg['pts_pr_pass_td'] = 4
pg[['gameid', 'player_id', 'pts_pr_pass_td']].head()

pg['pts_pr_pass_td'] = 6
pg[['gameid', 'player_id', 'pts_pr_pass_td']].head()

# Math and number columns
pg['rushing_pts'] = (
    pg['rush_yards']*0.1 + pg['rush_tds']*6 + pg['rush_fumbles']*-3)

pg[['player_name', 'gameid', 'rushing_pts']].head()

import numpy as np  # note: normally you'd import this at the top of the file

pg['distance_traveled'] = np.abs(pg['rush_yards'])

pg['ln_rush_yds'] = np.log(pg['rush_yards'])

# note on sample method

pg['points_per_fg'] = 3

pg[['player_name', 'gameid', 'points_per_fg']].sample(5)

# String Columns
pg['player_name'].str.upper().sample(5)

pg['player_name'].str.replace('.', ' ').sample(5)

(pg['player_name'] + ', ' + pg['pos'] + ' - ' + pg['team']).sample(5)

pg['player_name'].str.replace('.', ' ').str.lower().sample(5)

# Bool columns
pg['is_a_rb'] = (pg['pos'] == 'RB')
pg[['player_name', 'is_a_rb']].sample(5)

pg['is_a_rb_or_wr'] = (pg['pos'] == 'RB') | (pg['pos'] == 'WR')
pg['good_rb_game'] = (pg['pos'] == 'RB') & (pg['rush_yards'] >= 100)
pg['is_not_a_rb_or_wr'] = ~((pg['pos'] == 'RB') | (pg['pos'] == 'WR'))

(pg[['rush_yards', 'rec_yards']] > 100).sample(5)

# Applying functions to columns
def is_skill(pos):
  """
  Takes some string named pos ('QB', 'K', 'RT' etc) and checks
  whether it's a skill position (RB, WR, TE).
  """
  return pos in ['RB', 'WR', 'TE']

pg['is_skill'] = pg['pos'].apply(is_skill)

pg[['player_name', 'is_skill']].sample(5)

pg['is_skill_alternate'] = pg['pos'].apply(lambda x: x in ['RB', 'WR', 'TE'])

# Dropping Columns
pg.drop('is_skill_alternate', axis=1, inplace=True)

# Renaming Columns
pg.columns = [x.upper() for x in pg.columns]

pg.head()

pg.columns = [x.lower() for x in pg.columns]

pg.rename(columns={'interceptions': 'ints'}, inplace=True)

# Missing data
pbp = pd.read_csv(path.join(DATA_DIR, 'play_data_sample.csv'))

pbp['yards_after_catch'].isnull().head()

pbp['yards_after_catch'].notnull().head()

pbp['yards_after_catch'].fillna(-99).head()

# Changing column types
pg['gameid'].head()

gameid = '2017090700'

year = gameid[0:4]
month = gameid[4:6]
day = gameid[6:8]

year
month
day

# pg['month'] = pg['gameid'].str[4:6]  # commented out since it gives an error

pg['month'] = pg['gameid'].astype(str).str[4:6]
pg[['month', 'gameid']].head()

pg['month'].astype(int).head()

pg.dtypes.head()


