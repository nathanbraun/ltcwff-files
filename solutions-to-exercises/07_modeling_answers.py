"""
Answers to the end of chapter exercises for Modeling chapter.
"""
import pandas as pd
import random
from pandas import DataFrame, Series
import statsmodels.formula.api as smf
from os import path

DATA_DIR = '/Users/nathan/fantasybook/data'

###############################################################################
# problem 7.1
###############################################################################

###################
# from 07_01_ols.py
###################
df = pd.read_csv(path.join(DATA_DIR, 'play_data_sample.csv'))

# process
df = df.loc[(df['play_type'] == 'run') | (df['play_type'] == 'pass')]
df['offensive_td'] = ((df['touchdown'] == 1) & (df['yards_gained'] > 0))
df['offensive_td'] = df['offensive_td'].astype(int)
df['yardline_100_sq'] = df['yardline_100'] ** 2

df[['offensive_td', 'yardline_100', 'yardline_100_sq']].head()

# run regression
model = smf.ols(formula='offensive_td ~ yardline_100 + yardline_100_sq', data=df)
results = model.fit()

results.summary2()

def prob_of_td(yds):
    b0, b1, b2 = results.params
    return (b0 + b1*yds + b2*(yds**2))

df['offensive_td_hat'] = results.predict(df)

#########################
# answers to question 7.1
#########################
# a
df['offensive_td_hat_alt'] = df['yardline_100'].apply(prob_of_td)

df[['offensive_td_hat', 'offensive_td_hat_alt']].head()
(results.predict(df) == df['offensive_td_hat_alt']).all()


# b
model_b = smf.ols(
    formula='offensive_td ~ yardline_100 + yardline_100_sq +ydstogo', data=df)
results_b = model_b.fit()
results_b.summary2()

# c
model_c = smf.ols(formula='offensive_td ~ yardline_100 + yardline_100_sq + C(down)', data=df)
results_c = model_c.fit()
results_c.summary2()

# d
df['is2'] = df['down'] == 2
df['is3'] = df['down'] == 3
df['is4'] = df['down'] == 4

model_d = smf.ols(formula='offensive_td ~ yardline_100 + yardline_100_sq + is2 + is3 + is4', data=df)
results_d = model_d.fit()
results_d.summary2()

###############################################################################
# problem 7.2
###############################################################################

# a
def run_sim_get_pvalue():
    coin = ['H', 'T']

    # make empty DataFrame
    df = DataFrame(index=range(100))

    # now fill it with a "guess"
    df['guess'] = [random.choice(coin) for _ in range(100)]

    # and flip
    df['result'] = [random.choice(coin) for _ in range(100)]

    # did we get it right or not?
    df['right'] = (df['guess'] == df['result']).astype(int)

    model = smf.ols(formula='right ~ C(guess)', data=df)
    results = model.fit()

    return results.pvalues['C(guess)[T.T]']

# b
sims_1k = Series([run_sim_get_pvalue() for _ in range(1000)])
sims_1k.mean()  # 0.5083

# c
def runs_till_threshold(i, p=0.05):
    pvalue = run_sim_get_pvalue()
    if pvalue < p:
        return i
    else:
        return runs_till_threshold(i+1, p)

sim_time_till_sig_100 = Series([runs_till_threshold(1) for _ in range(100)])

# d

# According to Wikipedia, the mean and median of the Geometric distribution are
# 1/p and -1/log_2(1-p). Since we're working with a p of 0.05, that'd give us:

from math import log
p = 0.05
g_mean = 1/p  # 20
g_median = -1/log(1-p, 2)  # 13.51

g_mean, g_median

sim_time_till_sig_100.mean()
sim_time_till_sig_100.median()

###############################################################################
# problem 7.3
###############################################################################

df = pd.read_csv(path.join(DATA_DIR, 'play_data_sample.csv'))
df = df.loc[(df['play_type'] == 'run') | (df['play_type'] == 'pass')]
df['offensive_td'] = ((df['touchdown'] == 1) & (df['yards_gained'] > 0))

# a
model_a = smf.ols(formula=
    """
    wpa ~ offensive_td + interception + yards_gained + fumble
    """, data=df)
results_a = model_a.fit()
results_a.summary2()

# b
model_b = smf.ols(formula=
    """
    wpa ~ offensive_td + interception + yards_gained + fumble_lost
    """, data=df)
results_b = model_b.fit()
results_b.summary2()

###############################################################################
# problem 7.4
###############################################################################
"""
Because ADP is also in the regression, b2 can be interpreted as "the impact of
being a rookie on average fantasy points, *controlling for draft position*."

If you think ADP is generally efficient, and players go where they're supposed
to, you might think the b2 is close to 0 and statistically insignificant. On
the other hand, if you're more dubius about the crowd, you might expect them to
under (b2 > 0) or over value (b2 < 0) rookies.
"""

###############################################################################
# problem 7.5
###############################################################################
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score

df = pd.read_csv(path.join(DATA_DIR, 'player_game_2017_sample.csv'))

xvars = ['carries', 'rush_yards', 'rush_fumbles', 'rush_tds', 'targets',
         'receptions', 'rec_yards', 'raw_yac', 'rec_fumbles', 'rec_tds',
         'ac_tds', 'rec_raw_airyards', 'caught_airyards', 'attempts',
         'completions', 'pass_yards', 'pass_raw_airyards', 'comp_airyards',
         'timeshit', 'interceptions', 'pass_tds', 'air_tds']
yvar = 'pos'

df_mean = df.groupby('player_id')[xvars].mean()
df_mean['pos'] = df.groupby('player_id')[yvar].first()

model_a = RandomForestClassifier(n_estimators=100)
scores_a = cross_val_score(model_a, df_mean[xvars], df_mean[yvar], cv=10)

scores_a.mean()  # 0.8525 for me, better than player-game level

# b) now try using multiple aggregations, how about mean, median, min and max
# that's the benefit of random forest, can dump a ton of variables in and let
# it sort out what works

df_med = df.groupby('player_id')[xvars].median()
df_max = df.groupby('player_id')[xvars].max()
df_min = df.groupby('player_id')[xvars].min()
df_mean = df.groupby('player_id')[xvars].mean()

df_med.columns = [f'{x}_med' for x in df_med.columns]
df_max.columns = [f'{x}_max' for x in df_max.columns]
df_min.columns = [f'{x}_min' for x in df_min.columns]
df_mean.columns = [f'{x}_mean' for x in df_mean.columns]

df_mult = pd.concat([df_med, df_mean, df_min, df_max], axis=1)
xvars_mult = list(df_mult.columns)

df_mult['pos'] = df.groupby('player_id')[yvar].first()

model_b = RandomForestClassifier(n_estimators=100)
scores_b = cross_val_score(model_b, df_mult[xvars_mult], df_mult[yvar], cv=10)

scores_b.mean()  # 0.8699, which is a bit better than the mean only model

