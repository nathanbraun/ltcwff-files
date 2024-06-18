"""
Answers to the end of chapter exercises for Summary Stats and Visualization
chapter.
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from os import path

# change this to the directory where the csv files that come with the book are
# stored
# on Windows it might be something like 'C:/mydir'

# DATA_DIR = '/Users/nathan/fantasybook/data'
DATA_DIR = '/Users/nathanbraun/fantasymath/ltcwff-files/data'

pbp = pd.read_csv(path.join(DATA_DIR, 'play_data_sample.csv'))  # play by play data

###############################################################################
# 6.1a
###############################################################################
g = sns.displot(pbp, x='yards_gained', kind='kde', fill=True)
g.figure.subplots_adjust(top=0.9)
g.figure.suptitle('Distribution of Yards Gained Per Play, LTCWFF Sample')
g.savefig('./solutions-to-exercises/6-1a.png')

###############################################################################
# 6.1b
###############################################################################
g = sns.displot(pbp.query("down <= 3"), x='yards_gained', kind='kde',
                hue='down', fill=True)
g.figure.subplots_adjust(top=0.9)
g.figure.suptitle('Distribution of Yards Gained Per Play by Down, LTCWFF Sample')
g.savefig('./solutions-to-exercises/6-1b.png')

###############################################################################
# 6.1c
###############################################################################
g = sns.displot(pbp.query("down <= 3"), x='yards_gained', kind='kde',
                col='down', fill=True)
g.figure.subplots_adjust(top=0.8)
g.figure.suptitle('Distribution of Yards Gained Per Play by Down, LTCWFF Sample')
g.savefig('./solutions-to-exercises/6-1c.png')

###############################################################################
# 6.1d
###############################################################################
g = sns.displot(pbp.query("down <= 3"), x='yards_gained', kind='kde',
                row='posteam', col='down', fill=True)
g.figure.subplots_adjust(top=0.9)
g.figure.suptitle('Distribution of Yards Gained Per Play by Down, Team, LTCWFF Sample')
g.savefig('./solutions-to-exercises/6-1d.png')

###############################################################################
# 6.1e
###############################################################################
g = sns.displot(pbp.query("down <= 3"), x='yards_gained', col='down',
                row='posteam', hue='posteam', fill=True)
g.figure.subplots_adjust(top=0.9)
g.figure.suptitle('Distribution of Yards Gained Per Play by Down, Team, LTCWFF Sample')
g.savefig('./solutions-to-exercises/6-1e.png')

###############################################################################
# 6.2
###############################################################################
# relationships
pg = pd.read_csv(path.join(DATA_DIR, 'player_game_2017_sample.csv'))
g = sns.relplot(x='carries', y='rush_yards', hue='pos', data=pg)
g.figure.subplots_adjust(top=0.9)
g.figure.suptitle('Carries vs Rush Yards by Position, LTCWFF Sample')
g.savefig('./answers-to-exercises/6-2.png')

pg['ypc'] = pg['rush_yards']/pg['carries']

# easy way to check
pg.groupby('pos')['ypc'].mean()

# more advanced/not seen before, but Pandas often does what you might expect
pg.groupby('pos')['ypc'].describe()

g = sns.relplot(x='qtr', y='yards_gained', kind='line', hue='posteam', data=pbp)

g = sns.relplot(x='carries', y='rush_fumbles', data=pg)
g = sns.relplot(x='attempts', y='pass_raw_airyards', data=pg)
g = sns.relplot(x='pass_raw_airyards', y='interceptions', data=pg)
