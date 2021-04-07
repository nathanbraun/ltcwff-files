import pandas as pd
from os import path
import sqlite3

###############################################
# loading csvs and putting them in a sqlite db
###############################################

# only need to run this section once

# handle directories
DATA_DIR = '/Users/nathan/fantasybook/data'
DATA_DIR =  './data/'

# create connection
conn = sqlite3.connect(path.join(DATA_DIR, 'fantasy.sqlite'))

# load csv data
player_game = pd.read_csv(path.join(DATA_DIR, 'game_data_sample.csv'))
player = pd.read_csv(path.join(DATA_DIR, 'game_data_player_sample.csv'))

game = pd.read_csv(path.join(DATA_DIR, 'game_2017_sample.csv'))
team = pd.read_csv(path.join(DATA_DIR, 'teams.csv'))

# and write it to sql
player_game.to_sql('player_game', conn, index=False, if_exists='replace')
player.to_sql('player', conn, index=False, if_exists='replace')

game.to_sql('game', conn, index=False, if_exists='replace')
team.to_sql('team', conn, index=False, if_exists='replace')

#########
# Queries
#########
conn = sqlite3.connect(path.join(DATA_DIR, 'fantasy.sqlite'))

# return entire player table
df = pd.read_sql(
    """
    SELECT *
    FROM player
    """, conn)
df.head()

# return specific columns from player table + rename on the fly
df = pd.read_sql(
    """
    SELECT player_id, player_name AS name, pos
    FROM player
    """, conn)
df.head()

###########
# filtering
###########

# basic filter, only rows where team is MIA
df = pd.read_sql(
    """
    SELECT player_id, player_name AS name, pos
    FROM player
    WHERE team = 'MIA'
    """, conn)
df.head()

# AND in filter
df = pd.read_sql(
    """
    SELECT player_id, player_name AS name, pos
    FROM player
    WHERE team = 'MIA' AND pos == 'WR'
    """, conn)
df.head()

# OR in filter
df = pd.read_sql(
    """
    SELECT player_id, player_name AS name, pos, team
    FROM player
    WHERE team = 'MIA' OR team == 'NE'
    """, conn)
df.head()

# IN in filter
df = pd.read_sql(
    """
    SELECT player_id, player_name AS name, pos, team
    FROM player
    WHERE team IN ('MIA', 'NE')
    """, conn)

# negation with NOT
df = pd.read_sql(
    """
    SELECT player_id, player_name AS name, pos, team
    FROM player
    WHERE team NOT IN ('MIA', 'NE')
    """, conn)

#########
# joining
#########

# no WHERE so fullcrossjoin
df = pd.read_sql(
    """
    SELECT
        player.player_name as name,
        player.pos,
        player.team,
        team.conference,
        team.division
    FROM player, team
    """, conn)
df.head(10)

# add in two team columns to make clearer
df = pd.read_sql(
    """
    SELECT
        player.player_name as name,
        player.pos,
        player.team as player_team,
        team.team as team_team,
        team.conference,
        team.division
    FROM player, team
    """, conn)
df.head(10)

# n of rows
df.shape

# works when we add WHERE to filter after crossjoin
df = pd.read_sql(
    """
    SELECT
        player.player_name as name,
        player.pos,
        player.team,
        team.conference,
        team.division
    FROM player, team
    WHERE player.team = team.team
    """, conn)
df.head()

# add in team column to make clearer how it works
df = pd.read_sql(
    """
    SELECT
        player.player_name as name,
        player.pos,
        player.team as player_team,
        team.team as team_team,
        team.conference,
        team.division
    FROM player, team
    WHERE player.team = team.team
    """, conn)
df.head()

# adding a third table
df = pd.read_sql(
    """
    SELECT
        player.player_name as name,
        player.pos,
        team.team,
        team.conference,
        team.division,
        player_game.*
    FROM player, team, player_game
    WHERE
        player.team = team.team AND
        player_game.player_id = player.player_id
    """, conn)
df.head()

# adding a third table - shorthand
df = pd.read_sql(
    """
    SELECT
        p.player_name as name,
        p.pos,
        t.team,
        t.conference,
        t.division,
        pg.*
    FROM player AS p, team AS t, player_game AS pg
    WHERE
        p.team = t.team AND
        pg.player_id = p.player_id
    """, conn)
df.head()

# adding an additional filter
df = pd.read_sql(
    """
    SELECT
        p.player_name as name,
        p.pos,
        t.team,
        t.conference,
        t.division,
        pg.*
    FROM player AS p, team AS t, player_game AS pg
    WHERE
        p.team = t.team AND
        pg.player_id = p.player_id AND
        p.pos == 'RB'
    """, conn)
df.head()

###########
# LIMIT/TOP
###########

# SELECT *
# FROM player
# LIMIT 5

# SELECT TOP 5 *
# FROM player

df = pd.read_sql(
    """
    SELECT DISTINCT season, week, date
    FROM game
    """, conn)
df.head()

# UNION
# SUBQUERIES
# LEFT, RIGHT, OUTER JOINS

# SELECT *
# FROM <left_table>
# LEFT JOIN <right_table> ON <left_table>.<common_column> = <right_table>.<common_column>

df = pd.read_sql(
    """
    SELECT a.*, b.rec_yards, b.rush_yards, b.rec_tds, b.rush_tds
    FROM
        (SELECT game.season, week, gameid, home as team, player_id, player_name
        FROM game, player
        WHERE game.home = player.team
        UNION
        SELECT game.season, week, gameid, away as team, player_id, player_name
        FROM game, player
        WHERE game.away = player.team) AS a
    LEFT JOIN player_game AS b ON a.gameid = b.gameid AND a.player_id = b.player_id
    """, conn)
df.loc[df['player_name'] == 'M.Sanu']

game = pd.read_sql(
    """
    SELECT *
    FROM game
    """
    , conn)

game.loc[[11, 0, 1, 2, 3]]

game.query("home == 'GB'")
