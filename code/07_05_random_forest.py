import pandas as pd
from pandas import DataFrame, Series
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from os import path

DATA_DIR = '/Users/nathan/fantasybook/data'
DATA_DIR = './data'

df = pd.read_csv(path.join(DATA_DIR, 'player_game_2017_sample.csv'))

xvars = ['carries', 'rush_yards', 'rush_fumbles', 'rush_tds', 'targets',
         'receptions', 'rec_yards', 'raw_yac', 'rec_fumbles', 'rec_tds',
         'ac_tds', 'rec_raw_airyards', 'caught_airyards', 'attempts',
         'completions', 'pass_yards', 'pass_raw_airyards', 'comp_airyards',
         'timeshit', 'interceptions', 'pass_tds', 'air_tds']
yvar = 'pos'

train, test = train_test_split(df, test_size=0.20)

model = RandomForestClassifier(n_estimators=100)
model.fit(train[xvars], train[yvar])

test['pos_hat'] = model.predict(test[xvars])
test['correct'] = (test['pos_hat'] == test['pos'])
test['correct'].mean()

model.predict_proba(test[xvars])

probs = DataFrame(model.predict_proba(test[xvars]),
                  index=test.index,
                  columns=model.classes_)
probs.head()

results = pd.concat([
    test[['player_id', 'player_name', 'pos', 'pos_hat', 'correct']],
    probs], axis=1)

results[['player_name', 'pos', 'correct', 'QB', 'RB', 'TE', 'WR']].head()

results.groupby('pos')[['correct', 'QB', 'RB', 'WR', 'TE']].mean()

# cross validation
model = RandomForestClassifier(n_estimators=100)
scores = cross_val_score(model, df[xvars], df[yvar], cv=10)

scores
scores.mean()

# feature importance
Series(model.feature_importances_, xvars).sort_values(ascending=False)
