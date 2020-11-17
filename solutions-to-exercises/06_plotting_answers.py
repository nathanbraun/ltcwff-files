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

DATA_DIR = '/Users/nathan/fantasybook/data'

pbp = pd.read_csv(path.join(DATA_DIR, 'play_data_sample.csv'))  # play by play data

###############################################################################
# 6.1a
###############################################################################
g = (sns.FacetGrid(pbp)
     .map(sns.kdeplot, 'yards_gained', shade=True))
g.fig.subplots_adjust(top=0.9)
g.fig.suptitle('Distribution of Yards Gained Per Play, LTCWFF Sample')
g.savefig('./answers-to-exercises/6-1a.png')

###############################################################################
# 6.1b
###############################################################################
g = (sns.FacetGrid(pbp.query("down <= 3"), hue='down')
     .map(sns.kdeplot, 'yards_gained', shade=True))
g.add_legend()
g.fig.subplots_adjust(top=0.9)
g.fig.suptitle('Distribution of Yards Gained Per Play by Down, LTCWFF Sample')
g.savefig('./answers-to-exercises/6-1b.png')

###############################################################################
# 6.1c
###############################################################################
g = (sns.FacetGrid(pbp.query("down <= 3"), col='down')
     .map(sns.kdeplot, 'yards_gained', shade=True))
g.fig.subplots_adjust(top=0.8)
g.fig.suptitle('Distribution of Yards Gained Per Play by Down, LTCWFF Sample')
g.savefig('./answers-to-exercises/6-1c.png')

###############################################################################
# 6.1d
###############################################################################
g = (sns.FacetGrid(pbp.query("down <= 3"), col='down', row='posteam')
     .map(sns.kdeplot, 'yards_gained', shade=True))
g.fig.subplots_adjust(top=0.9)
g.fig.suptitle('Distribution of Yards Gained Per Play by Down, Team, LTCWFF Sample')
g.savefig('./answers-to-exercises/6-1d.png')

###############################################################################
# 6.1e
###############################################################################
g = (sns.FacetGrid(pbp.query("down <= 3"), col='down', row='posteam',
                   hue='posteam')
     .map(sns.kdeplot, 'yards_gained', shade=True))
g.fig.subplots_adjust(top=0.9)
g.fig.suptitle('Distribution of Yards Gained Per Play by Down, Team, LTCWFF Sample')
g.savefig('./answers-to-exercises/6-1e.png')


###############################################################################
# 6.2
###############################################################################
# relationships
pg = pd.read_csv(path.join(DATA_DIR, 'player_game_2017_sample.csv'))
g = sns.relplot(x='carries', y='rush_yards', hue='pos', data=pg)
g.fig.subplots_adjust(top=0.9)
g.fig.suptitle('Carries vs Rush Yards by Position, LTCWFF Sample')
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
