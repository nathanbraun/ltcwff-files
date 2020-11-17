"""
Answers to the end of chapter exercises for SQL chapter.

Note: this assumes you've already created/populated the SQL database as
outlined in the book and ./code/04_sql.py.
"""
import pandas as pd
from os import path
import sqlite3

DATA_DIR = '/Users/nathan/fantasybook/data'

conn = sqlite3.connect(path.join(DATA_DIR, 'fantasy.sqlite'))

###############################################################################
# 4.1
###############################################################################
# a
df = pd.read_sql(
    """
    SELECT
        game.season, week, player_name, player_game.team, attempts,
        completions, pass_yards as yards, pass_tds as tds, interceptions
    FROM player_game, team, game
    WHERE
        player_game.team = team.team AND
        game.gameid = player_game.gameid AND
        team.conference = 'AFC' AND
        player_game.pos = 'QB'
    """, conn)

# b
df = pd.read_sql(
    """
    SELECT
        g.season, week, p.player_name, t.team, attempts, completions,
        pass_yards AS yards, pass_tds AS tds, interceptions
    FROM player_game AS pg, team AS t, game AS g, player AS p
    WHERE
        pg.player_id = p.player_id AND
        g.gameid = pg.gameid AND
        t.team = p.team AND
        t.conference = 'AFC' AND
        p.pos = 'QB'
    """, conn)

###############################################################################
# 4.2
###############################################################################
df = pd.read_sql(
    """
    SELECT g.*, th.mascot as home_mascot, ta.mascot as away_mascot
    FROM game AS g, team AS th, team AS ta
    WHERE
        g.home = th.team AND
        g.away = ta.team
    """, conn)
