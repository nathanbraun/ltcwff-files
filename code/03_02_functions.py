import pandas as pd
from os import path

# change this to the directory where the csv files that come with the book are
# stored
# on Windows it might be something like 'C:/mydir'

DATA_DIR = './data'

# load adp data
adp = pd.read_csv(path.join(DATA_DIR, 'adp_2017.csv'))  # adp data

# book picks up here:

adp[['adp', 'high', 'low', 'stdev', 'times_drafted']].mean()
adp.max()

# Axis
adp[['adp', 'low', 'high', 'stdev']].mean(axis=0)
adp[['adp', 'low', 'high', 'stdev']].mean(axis=1).head()

# Summary functions on boolean columns
pg = pd.read_csv(path.join(DATA_DIR, 'player_game_2017_sample.csv')) # not in book

# book picks up again here
pg['good_rb_game'] = (pg['pos'] == 'RB') & (pg['rush_yards'] >= 100)

pg['good_rb_game'].mean()
pg['good_rb_game'].sum()

(pg['pass_yards'] > 400).any()
(pg['rush_yards'] >= 0).all()

(pg[['rush_yards', 'rec_yards']] > 100).any(axis=1)

(pg[['rush_yards', 'rec_yards']] > 100).any(axis=1).sum()

(pg[['rush_yards', 'rec_yards']] > 100).all(axis=1).sum()

(pg[['rush_yards', 'rec_yards']] > 75).all(axis=1).sum()

# Other misc built-in summary functions
adp['position'].value_counts()

adp['position'].value_counts(normalize=True)

pd.crosstab(adp['team'], adp['position']).head()
