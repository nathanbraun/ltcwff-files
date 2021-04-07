import pandas as pd
import numpy as np
from os import path

# change this to the directory where the csv files that come with the book are
# stored
# on Windows it might be something like 'C:/mydir'

DATA_DIR = '/Users/nathan/fantasybook/data'

# note: we're passing the index_col argument, which immediately setting the
# index to be the player_id column
adp = pd.read_csv(path.join(DATA_DIR, 'adp_2017.csv'), index_col='player_id')

# Filtering

tom_brady_id = 119
adp.loc[tom_brady_id]

my_player_ids = ([119, 1886, 925])

adp.loc[my_player_ids]
adp.loc[my_player_ids, ['name', 'adp', 'stdev']]
adp.loc[my_player_ids, 'name']

# Boolean Indexing
is_a_rb = adp['position'] == 'RB'

is_a_rb.head()

adp_rbs = adp.loc[is_a_rb]

adp_rbs[['name', 'adp', 'position']].head()
adp_wrs = adp.loc[adp['position'] == 'WR']

adp_wrs[['name', 'adp', 'position']].head()

is_a_te = adp['position'] == 'TE'

adp_not_te = adp.loc[~is_a_te]

adp_not_te[['name', 'adp', 'position']].head()

# Duplicates
adp.drop_duplicates(inplace=True)

adp.drop_duplicates('position')[['name', 'adp', 'position']]

adp.duplicated().head()

adp['position'].duplicated().head()

adp.drop_duplicates('position')
adp.loc[~adp['position'].duplicated()]

# Combining filtering with changing columns
pg = pd.read_csv(path.join(DATA_DIR, 'player_game_2017_sample.csv'))

pg['primary_yards'] = np.nan
pg.loc[pg['pos'] == 'QB', 'primary_yards'] = pg['pass_yards']
pg.loc[pg['pos'] == 'RB', 'primary_yards'] = pg['rush_yards']
pg.loc[pg['pos'] == 'WR', 'primary_yards'] = pg['rec_yards']

pg[['player_name', 'pos', 'pass_yards', 'rush_yards', 'rec_yards',
    'primary_yards']].sample(5)

# Query
pg.query("pos == 'RB'").head()

pg['is_a_rb'] = pg['pos'] == 'RB'

pg.query("is_a_rb").head()

pg.query("raw_yac.notnull()")[['gameid', 'player_id', 'raw_yac']].head()

# note: if getting an error on line above, try it with engine='python' like
# this
pg.query("raw_yac.notnull()", engine='python')[['gameid', 'player_id', 'raw_yac']].head()
