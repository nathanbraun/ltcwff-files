from os import path
import pandas as pd

# change this to the directory where the csv files that come with the book are
# stored
# on Windows it might be something like 'C:/mydir'

DATA_DIR = '/Users/nathan/fantasybook/data'

adp = pd.read_csv(path.join(DATA_DIR, 'adp_2017.csv'))  # adp data

##############
# Loading data
##############
adp = pd.read_csv(path.join(DATA_DIR, 'adp_2017.csv'))  # adp data

type(adp)

##################################
# DataFrame methods and attributes
##################################
adp.head()

adp.columns

adp.shape

#################################
# Working with subsets of columns
#################################
# A single column
adp['name'].head()

type(adp['name'])

adp['name'].to_frame().head()
type(adp['name'].to_frame().head())

# Multiple columns
adp[['name', 'position', 'adp']].head()

type(adp[['name', 'position', 'adp']])

# adp['name', 'position', 'adp'].head()  # commented out because it throws an error

##########
# Indexing
##########
adp[['name', 'position', 'adp']].head()

adp.set_index('player_id').head()

# Copies and the inplace argument
adp.head()  # note: player_id not the index, even though we just set it

adp.set_index('player_id', inplace=True)
adp.head()  # now player_id is index

# alternate to using inplace, reassign adp
# reload adp with default 0, 1, ... index
adp = pd.read_csv(path.join(DATA_DIR, 'adp_2017.csv'))  # adp data
adp = adp.set_index('player_id')
adp.head()  # now player_id is index

adp.reset_index().head()

#############################
# Indexes keep things aligned
#############################
adp_rbs = adp.loc[adp['position'] == 'RB', ['name', 'position', 'team']]
adp_rbs.head()

adp_rbs.sort_values('name', inplace=True)
adp_rbs.head()

# assigning a new column
adp_rbs['times_drafted'] = adp['times_drafted']
adp_rbs.head()

# has the same index as adp_rbs and adp['adp']
adp['adp'].head()

#################
# Outputting data
#################
adp_rbs.to_csv(path.join(DATA_DIR, 'adp_rb.csv'))

adp_rbs.to_csv(path.join(DATA_DIR, 'adp_rb_no_index.csv'), index=False)

