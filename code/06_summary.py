import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from os import path

# change this to the directory where the csv files that come with the book are
# stored
# on Windows it might be something like 'C:/mydir'

DATA_DIR = '/Users/nathan/fantasybook/data'

###############
# distributions
###############

df = pd.read_csv(path.join(DATA_DIR, 'player_game_2017_sample.csv'))

# summary stats
df.loc[df['pos'] == 'RB', 'rush_yards'].quantile(.9)
df[['rush_yards', 'rec_yards']].describe()

# densitiy plots with python

# add fantasy points to data
df['std'] = (0.1*(df['rush_yards'] + df['rec_yards']) +
             0.04*df['pass_yards'] +
             -3*(df['rush_fumbles'] +df['rec_fumbles'] +
                 df['interceptions']) +
             6*(df['rush_tds'] + df['rec_tds']) + 4*df['pass_tds'])
df['ppr'] = df['std'] + 1*df['receptions']
df['half_ppr'] = df['std'] + 0.5*df['receptions']

# density plot of standard points

# all on one line
g = sns.FacetGrid(df).map(sns.kdeplot, 'std', shade=True)

# on seperate lines so it's clearer it's a two step process
g = (sns.FacetGrid(df)
     .map(sns.kdeplot, 'std', shade=True))

# density plot of standard points by position
g = (sns.FacetGrid(df, hue='pos')
     .map(sns.kdeplot, 'std', shade=True)
     .add_legend())

# density plot of standard points by position and week
g = (sns.FacetGrid(df, hue='pos', col='week', col_wrap=4, height=2)
     .map(sns.kdeplot, 'std', shade=True)
     .add_legend())

# now want it by scoring system

# thinking about seaborn: specify seperate columns for columns, hue (color),
# thing we're plotting (points)
# so we need points in one column, then another type for scoring type

df[['pos', 'std', 'ppr', 'half_ppr']].head()  # have this

def score_type_df(_df, scoring):
    _df = _df[['pos', scoring]]
    _df.columns = ['pos', 'pts']
    _df['scoring'] = scoring
    return _df

df_pts_long = pd.concat(
    [score_type_df(df, scoring) for scoring in ['std', 'ppr', 'half_ppr']])

# now can plot points by scoring system and position
g = (sns.FacetGrid(df_pts_long, col='pos', hue='scoring', col_wrap=2,
                   aspect=1.3)
     .map(sns.kdeplot, 'pts', shade=True)
     .add_legend())

#################################
# relationships between variables
#################################

# airyards vs yac
g = sns.relplot(x='caught_airyards', y='raw_yac', data=df)
g.fig.subplots_adjust(top=0.9)
g.fig.suptitle('Airyards vs YAC')

# airyards vs yac - colored yb position
g = sns.relplot(x='caught_airyards', y='raw_yac', hue='pos', data=df)
g.fig.subplots_adjust(top=0.9)
g.fig.suptitle('Airyards vs YAC - by Position')

# correlation
df.loc[df['pos'] == 'WR',
       ['rec_raw_airyards', 'targets', 'carries', 'ppr', 'std']].corr()

# scatter plot of 0.58 correlation
g = sns.relplot(x='rec_raw_airyards', y='ppr', data=df.query("pos == 'WR'"))

# scatter plot of 0.98 correlation
g = sns.relplot(x='std', y='ppr', data=df.query("pos == 'WR'"))

########################
# line plots with python
########################

# points by week and position
g = sns.relplot(x='week', y='std', kind='line', hue='pos', data=df)

df.loc[(df['pos'] == 'QB') & (df['week'] == 1),
       ['player_name', 'week', 'std']].head()

# max points by week and position
max_pts_by_pos_week = (df.groupby(['pos', 'week'], as_index=False)
                       ['std'].max())

g = sns.relplot(x='week', y='std', kind='line', hue='pos', style='pos',
                data=max_pts_by_pos_week, height=4, aspect=1.2)
g.fig.subplots_adjust(top=0.9)
g.fig.suptitle("Max Points by Week and Position")

# points by player and week
g = sns.relplot(x='week', y='std', kind='line', hue='player_name',
                col='player_name', height=2, aspect=1.2, col_wrap=3,
                legend=False, data=df.query("pos == 'QB'"))
g.fig.subplots_adjust(top=0.9)
g.fig.suptitle("Points by Week = QBs")

##############
# plot options
##############

# basic plot
g = (sns.FacetGrid(df_pts_long, col='pos', hue='scoring')
     .map(sns.kdeplot, 'pts', shade=True))

# wrapping columns
g = (sns.FacetGrid(df_pts_long, col='pos', hue='scoring', col_wrap=2)
     .map(sns.kdeplot, 'pts', shade=True)
     .fig.subplots_adjust(top=0.9) # adding a title
     .fig.suptitle('Fantasy Points by Position, Scoring System')
     .set_xlabels('Points') # modifying axis
     .set_ylabels('Density')
     .add_legend()  # adding legend
     .savefig('scoring_by_pos_type.png'))  # saving
