"""
Answers to the end of chapter exercises for Pandas chapter.

Questions with written (not code) answers are inside triple quotes.
"""
###############################################################################
# PANDAS BASICS
###############################################################################

#######
# 3.1.1
#######
import pandas as pd
from os import path

DATA_DIR = '/Users/nathan/fantasybook/data'
adp = pd.read_csv(path.join(DATA_DIR, 'adp_2017.csv'))

#######
# 3.1.2
#######
# works because data is sorted by adp already
adp50 = adp.head(50)

# this is better if don't want to assume data is sorted
adp50 = adp.sort_values('adp').head(50)

#######
# 3.1.3
#######
adp.sort_values('name', ascending=False, inplace=True)
adp.head()

# Note: if this didn't work when you printed it on a new line in the REPL you
# probably forgot the `inplace=True` argument.

#######
# 3.1.4
#######
type(adp.sort_values('adp'))  # it's a DataFfame

#######
# 3.1.5
#######
# a
adp_simple = adp[['name', 'position', 'adp']]

# b
adp_simple = adp_simple[['position', 'name', 'adp']]

# c
adp_simple['team'] = adp['team']

# d
adp.to_csv(path.join(DATA_DIR, 'adp.txt'), sep='|')

###############################################################################
# COLUMNS
###############################################################################

#######
# 3.2.1
#######
import pandas as pd
from os import path

DATA_DIR = '/Users/nathan/fantasybook/data'
pg = pd.read_csv(path.join(DATA_DIR, 'player_game_2017_sample.csv'))

#######
# 3.2.2
#######
pg['rec_pts_ppr'] = 0.1*pg['rec_yards'] + 6*pg['rec_tds'] + pg['receptions']
pg['rec_pts_ppr'].head()

#######
# 3.2.3
#######
pg['player_desc'] = pg['player_name'] + ' is the ' + pg['team'] + ' ' + pg['pos']
pg['player_desc'].head()

#######
# 3.2.4
#######
pg['is_possesion_rec'] = pg['caught_airyards'] > pg['raw_yac']
pg['is_possesion_rec'].head()

#######
# 3.2.5
#######
pg['len_last_name'] = (pg['player_name']
                       .apply(lambda x: len(x.split('.')[-1])))
pg['len_last_name'].head()

#######
# 3.2.6
#######
pg['gameid'] = pg['gameid'].astype(str)

#######
# 3.2.7
#######
# a
pg.columns = [x.replace('_', ' ') for x in pg.columns]
pg.head()

# b
pg.columns = [x.replace(' ', '_') for x in pg.columns]
pg.head()

#######
# 3.2.8
#######
# a
pg['rush_td_percentage'] = pg['rush_tds']/pg['carries']
pg['rush_td_percentage'].head()

# b
"""
`'rush_td_percentage'` is rushing tds divided by carries. Since you can't
divide by 0, rush td percentage is missing whenever carries are missing.
"""

# To replace all the missing values with `-99`:
pg['rush_td_percentage'].fillna(-99, inplace=True)
pg['rush_td_percentage'].head()

#######
# 3.2.9
#######
pg.drop('rush_td_percentage', axis=1, inplace=True)
pg.head()

# If you forget the `axis=1` Pandas will try to drop the *row* with the
# index value `'rush_td_percentage'`. Since that doesn't exist, it'll throw an
# error.

# Without the `inplace=True`, Pandas just returns a new copy of `pg` without the
# `'rush_td_percentage'` column. Nothing happens to the original `pg`, though we
# could reassign it if we wanted like this:

# alternative to inplace=True
# pg = pg.drop('rush_td_percentage', axis=1)

###############################################################################
# BUILT-IN FUNCTIONS
###############################################################################
#######
# 3.3.1
#######
import pandas as pd
from os import path

DATA_DIR = '/Users/nathan/fantasybook/data'
pg = pd.read_csv(path.join(DATA_DIR, 'player_game_2017_sample.csv'))

#######
# 3.3.2
#######
pg['total_yards1'] = pg['rush_yards'] + pg['rec_yards'] + pg['pass_yards']

pg['total_yards2'] = pg[['rush_yards', 'rec_yards', 'pass_yards']].sum(axis=1)

(pg['total_yards1'] == pg['total_yards2']).all()

#######
# 3.3.3
#######

# a
pg[['rush_yards', 'rec_yards']].mean()

# rush_yards    14.909154
# rec_yards     32.761705

# b
((pg['pass_yards'] >= 300) & (pg['pass_tds'] >= 3)).sum()  # 15

# c
(((pg['pass_yards'] >= 300) & (pg['pass_tds'] >= 3)).sum()
 / (pg['pos'] == 'QB').sum())

# d
pg['rush_tds'].sum()  # 141

# e
pg['week'].value_counts()  #14, 8

###############################################################################
# FILTERING
###############################################################################
#######
# 3.4.1
#######
import pandas as pd
from os import path

DATA_DIR = '/Users/nathan/fantasybook/data'
adp = pd.read_csv(path.join(DATA_DIR, 'adp_2017.csv'))

#######
# 3.4.2
#######
# a
adp_cb1 = adp.loc[adp['team'] == 'DAL', ['name', 'position', 'adp']]
adp_cb1.head()

# b
adp_cb2 = adp.query("team == 'DAL'")[['name', 'position', 'adp']]
adp_cb2.head()

#######
# 3.4.3
#######
adp_nocb = adp.loc[adp['team'] != 'DAL', ['name', 'position', 'adp', 'team']]
adp_nocb.head()

#######
# 3.4.4
#######

# a
adp['last_name'] = adp['name'].apply(lambda x: x.split(' ')[1])
adp[['last_name', 'position']].duplicated().any()  # yes there are

adp[['last_name', 'position']].duplicated().sum()

# b
# flags ALL dups (not just 2nd) because passing keep=False
dups = adp[['last_name', 'position']].duplicated(keep=False)

adp_dups = adp.loc[dups]
adp_no_dups = adp.loc[~dups]

#######
# 3.4.5
#######
import numpy as np

adp['adp_description'] = np.nan
adp.loc[adp['adp'] < 40, 'adp_description'] = 'stud'
adp.loc[adp['adp'] > 120, 'adp_description'] = 'scrub'
adp[['adp', 'adp_description']].sample(5)


#######
# 3.4.6
#######
# a
adp_no_desc1 = adp.loc[adp['adp_description'].isnull()]

# b
adp_no_desc2 = adp.query("adp_description.isnull()")

###############################################################################
# GRANULARITY
###############################################################################
#######
# 3.5.1
#######
"""
Usually you can only shift your data from more (play by play) to less (game)
granular, which necessarily results in a loss of information. If I go from
knowing what Kareem Hunt rushed for on every particular play to just knowing
how many yards he rushed for *total*, that's a loss of information.
"""

#######
# 3.5.2
#######

# a
import pandas as pd
from os import path

DATA_DIR = '/Users/nathan/fantasybook/data'
pbp = pd.read_csv(path.join(DATA_DIR, 'play_data_sample.csv'))

# b
(pbp
.query("play_type == 'run'")
.groupby(['game_id', 'rusher_player_name'])['yards_gained'].sum())

# c
(pbp
.query("play_type == 'run'")
.groupby(['game_id', 'rusher_player_name'])['yards_gained'].mean())

# d
pbp['lte_0_yards'] = pbp['yards_gained'] <= 0

(pbp
.query("play_type == 'run'")
.groupby(['game_id', 'rusher_player_name'])['lte_0_yards'].mean())

#######
# 3.5.3
#######
pbp.groupby('game_id').count()
"""
Count counts the number of non missing (non `np.nan`) values. This is different
than `sum` which adds up the values in all of the columns. The only time
`count` and `sum` would return the same thing is if you had a column filled
with 1s without any missing values.
"""

#######
# 3.5.4
#######
pbp.groupby(['posteam', 'game_id'])['turnover', 'first_down'].mean()

# Pats (31.25%) and Chiefs vs LA (6.85%).

#######
# 3.5.5
#######
"""
Stacking is when you change the granularity in your data, but shift information
from rows to columns (or vis versa) so it doesn't result in any loss on
information.

An example would be going from the player-game level to the player level. If we
stacked it, we'd go from rows being:

     player_name  week  pass_tds
214     T.Taylor    10       0.0
339       M.Ryan    14       1.0
220     T.Taylor    11       1.0
70       T.Brady    15       1.0
1192    C.Newton     1       2.0

To:

                 pass_tds       ...
week                   1    2   ...    12   13   14   15   16   17
player_name                     ...
A.Smith               4.0  1.0  ...   1.0  4.0  1.0  2.0  1.0  NaN
B.Bortles             1.0  1.0  ...   0.0  2.0  2.0  3.0  3.0  0.0
B.Hundley             NaN  NaN  ...   3.0  0.0  3.0  NaN  0.0  1.0
B.Roethlisberger      2.0  2.0  ...   5.0  2.0  2.0  3.0  2.0  NaN
C.Newton              2.0  0.0  ...   0.0  2.0  1.0  4.0  0.0  1.0
"""

###############################################################################
# COMBINING DATAFRAMES
###############################################################################
#######
# 3.6.1
#######
# a
import pandas as pd
from os import path

DATA_DIR = '/Users/nathan/fantasybook/data'
df_touch = pd.read_csv(path.join(DATA_DIR, 'problems/combine1', 'touch.csv'))
df_yard = pd.read_csv(path.join(DATA_DIR, 'problems/combine1', 'yard.csv'))
df_td = pd.read_csv(path.join(DATA_DIR, 'problems/combine1', 'td.csv'))

# b
df_comb1 = pd.merge(df_touch, df_yard)
df_comb1 = pd.merge(df_comb1, df_td, how='left')

df_comb1[['rush_tds', 'rec_tds']] = df_comb1[['rush_tds', 'rec_tds']].fillna(0)


# c
df_comb2 = pd.concat([df_touch.set_index('id'), df_yard.set_index('id'),
                      df_td.set_index('id')], axis=1)
df_comb2[['rush_tds', 'rec_tds']] = df_comb2[['rush_tds', 'rec_tds']].fillna(0)

# d
"""
Which is better is somewhat subjective, but I generally prefer `concat` when
combining three or more DataFrames because you can do it all in one step.

Note `merge` gives a little more fine grained control over how you merge (left,
or outer) vs `concat`, which just gives you inner vs outer.

Note also we have to set the index equal id before concating.
"""

########
# 3.6.2a
########
import pandas as pd
from os import path

DATA_DIR = '/Users/nathan/fantasybook/data'
qb = pd.read_csv(path.join(DATA_DIR, 'problems/combine2', 'qb.csv'))
rb = pd.read_csv(path.join(DATA_DIR, 'problems/combine2', 'rb.csv'))
wr = pd.read_csv(path.join(DATA_DIR, 'problems/combine2', 'wr.csv'))
te = pd.read_csv(path.join(DATA_DIR, 'problems/combine2', 'te.csv'))

# b
df = pd.concat([qb, rb, wr, te])

#######
# 3.6.3
#######
# a
import pandas as pd
from os import path

DATA_DIR = '/Users/nathan/fantasybook/data'
adp = pd.read_csv(path.join(DATA_DIR, 'adp_2017.csv'))

# b
for pos in ['QB', 'RB', 'WR', 'TE', 'PK', 'DEF']:
    (adp
     .query(f"position == '{pos}'")
     .to_csv(path.join(DATA_DIR, f'adp_{pos}.csv'), index=False))


# c
df = pd.concat([pd.read_csv(path.join(DATA_DIR, f'adp_{pos}.csv'))
    for pos in ['QB', 'RB', 'WR', 'TE', 'PK', 'DEF']], ignore_index=True)

