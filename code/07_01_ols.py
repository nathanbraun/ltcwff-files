import pandas as pd
import statsmodels.formula.api as smf
from os import path

DATA_DIR = '/Users/nathan/fantasybook/data'

###################
# linear regression
###################

# load
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

prob_of_td(75)
prob_of_td(25)
prob_of_td(5)

df['offensive_td_hat'] = results.predict(df)
df[['offensive_td', 'offensive_td_hat']].head()

