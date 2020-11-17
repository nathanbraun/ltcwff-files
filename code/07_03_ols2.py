import pandas as pd
import math
import statsmodels.formula.api as smf
from os import path

DATA_DIR = '/Users/nathan/fantasybook/data'

df = pd.read_csv(path.join(DATA_DIR, 'play_data_sample.csv'))
df = df.loc[(df['play_type'] == 'run') | (df['play_type'] == 'pass')]
df['offensive_td'] = ((df['touchdown'] == 1) & (df['yards_gained'] > 0))

model = smf.ols(formula=
        """
        wpa ~ offensive_td + turnover + first_down
        """, data=df)
results = model.fit()
results.summary2()

df.groupby('first_down')['yards_gained'].mean()

# adding yards_gained
model = smf.ols(formula=
        """
        wpa ~ offensive_td + turnover + first_down + yards_gained
        """, data=df)
results = model.fit()
results.summary2()

# fixed effects
pd.get_dummies(df['down']).head()

#############
# intractions
#############
df['turnover'] = df['turnover'].astype(int)
df['is_4'] = (df['qtr'] == 4).astype(int)

model = smf.ols(formula=
        """
        wpa ~ offensive_td + turnover + turnover:is_4 + yards_gained + first_down
        """, data=df)
results = model.fit()
results.summary2()
