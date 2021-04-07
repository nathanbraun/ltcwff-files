##############
# basic python
# v0.0.7
##############

##########################
# how to read this chapter
##########################
1 + 1

##########
# comments
##########

# print the result of 1 + 1
print(1 + 1)

###########
# variables
###########

pts_per_passing_td = 4

pts_per_passing_td
3*pts_per_passing_td

pts_per_passing_td = pts_per_passing_td - 3

pts_per_passing_td

####################
# types of variables
####################

over_under = 48  # int
wind_speed = 22.8  # float

starting_qb = 'Tom Brady'
starting_rb = "Le'Veon Bell"

type(starting_qb)

type(over_under)

team_name = f'{starting_qb}, {starting_rb}, & co.'
team_name

# string methods
'he could go all the way'.upper()

'Chad Johnson'.replace('Johnson', 'Ochocinco')

####################################
# How to figure things out in Python
####################################
'tom brady'.capitalize()

'  tom brady'
'tom brady'

#######
# bools
#######
team1_pts = 110
team2_pts = 120

# and these are all bools:
team1_won = team1_pts > team2_pts
team2_won = team1_pts < team2_pts
teams_tied = team1_pts == team2_pts
teams_did_not_tie = team1_pts != team2_pts

type(team1_won)
teams_did_not_tie

# error because test for equality is ==, not =
# teams_tied = (team1_pts = team2_pts)  # commented out since it throws an error

shootout = (team1_pts > 150) and (team2_pts > 150)
at_least_one_good_team = (team1_pts > 150) or (team2_pts > 150)
you_guys_are_bad = not ((team1_pts > 100) or (team2_pts > 100))
meh = not (shootout or at_least_one_good_team or you_guys_are_bad)

###############
# if statements
###############
if team1_won:
  message = "Nice job team 1!"
elif team2_won:
  message = "Way to go team 2!!"
else:
  message = "must have tied!"

message

#################
# container types
#################

# lists
my_roster_list = ['tom brady', 'adrian peterson', 'antonio brown']

my_roster_list[0]
my_roster_list[0:2]
my_roster_list[-2:]

# dicts
my_roster_dict = {'qb': 'tom brady',
                  'rb1': 'adrian peterson',
                  'wr1': 'antonio brown'}

my_roster_dict['qb']
my_roster_dict['k'] = 'mason crosby'

# unpacking
qb, rb = ['tom brady', 'todd gurley']

qb = 'tom brady'
rb = 'todd gurley'

# gives an error - n of variables doesn't match n items in list
# qb, rb = ['tom brady', 'todd gurley', 'julio jones']  # commented out w/ error

#######
# loops
#######

# looping over a list
my_roster_list = ['tom brady', 'adrian peterson', 'antonio brown']

my_roster_list_upper = ['', '', '']
i = 0
for player in my_roster_list:
    my_roster_list_upper[i] = player.title()
    i = i + 1

my_roster_list_upper

for x in my_roster_dict:
    print(f"position: {x}")

for x in my_roster_dict:
   print(f"position: {x}")
   print(f"player: {my_roster_dict[x]}")

for x, y in my_roster_dict.items():
    print(f"position: {x}")
    print(f"player: {y}")

################
# comprehensions
################

# lists
my_roster_list
my_roster_list_proper = [x.title() for x in my_roster_list]
my_roster_list_proper

my_roster_list_proper_alt = [y.title() for y in my_roster_list]

type([x.title() for x in my_roster_list])
[x.title() for x in my_roster_list][:2]

my_roster_last_names = [full_name.split(' ')[1] for full_name in my_roster_list]
my_roster_last_names

full_name = 'tom brady'
full_name.split(' ')
full_name.split(' ')[1]

my_roster_a_only = [
    x for x in my_roster_list if x.startswith('a')]
my_roster_a_only

my_roster_a_only_title = [
    x.title() for x in my_roster_list if x.startswith('a')]
my_roster_a_only_title

# dicts
pts_per_player = {
    'tom brady': 20.7, 'adrian peterson': 10.1, 'antonio brown': 18.5}

pts_x2_per_upper_player = {
    name.upper(): pts*2 for name, pts in pts_per_player.items()}

pts_x2_per_upper_player

sum([1, 2, 3])

sum([pts for _, pts in pts_per_player.items()])

###########
# functions
###########
len(['tom brady', 'adrian peterson', 'antonio brown'])

def rec_pts(rec, yds, tds):
    """
    multi line strings in python are between three double quotes

    it's not required, but the convention is to put what the fn does in one of these multi line strings (called "docstring") right away in function

    this function takes number of recieving: yards, receptions and touchdowns and returns fantasy points scored (ppr scoring)
    """
    return yds*0.1 + rec*1 + tds*6

rec_pts(6, 110, 0)

# this gives an error: yds is only defined inside rec_pts
# print(`yds`)

def rec_pts_noisy(rec, yds, tds):
    """
    this function takes number of recieving: yards, receptions and touchdowns and returns fantasy points scored (ppr scoring)

    it also prints out yds
    """
    print(yds)  # works here since we're inside fn
    return yds*0.1 + rec*1 + tds*6

rec_pts_noisy(6, 110, 0)

# side effects
def is_player_on_team(player, team):
    """
    take a player string and team list and check whether the player is on team

    do this by adding the player to the team, then returning True if the player shows up 2 or more times
    """
    team.append(player)
    return team.count(player) >= 2

my_roster_list = ['tom brady', 'adrian peterson', 'antonio brown']
is_player_on_team('gronk', my_roster_list)

my_roster_list
is_player_on_team('gronk', my_roster_list)

my_roster_list

#############################
# default values in functions
#############################

# error: leaving off a function
# rec_pts(4, 54)

def rec_pts_wdefault(rec=0, yds=0, tds=0):
    """
    this function takes number of recieving: yards, receptions and touchdowns
    and returns fantasy points scored (ppr scoring)
    """
    return yds*0.1 + rec*1 + tds*6

rec_pts_wdefault(4, 54)
rec_pts_wdefault()

def rec_pts2(rec=0, yds=0, tds=0, ppr=1):
    """
    takes number of receiving: yards, receptions and touchdowns AND points per
    reception and returns fantasy points scored
    """
    return yds*0.1 + rec*ppr + tds*6

rec_pts2(4, 54, 0.5)  # not doing what we want

54*0.1 + 4*1 + 0.5*6

rec_pts2(4, 54, 0, 0.5)  # solution 1
rec_pts2(4, 54, ppr=0.5)  # solution 2

# error: can't put key word argument before positional
# rec_pts2(ppr=0.5, 4, 54)

#####################################
# functions that take other functions
#####################################

def do_to_list(working_list, working_fn, desc):
    """
    this function takes a list, a function that works on a list, and a
    description

    it applies the function to the list, then returns the result along with
    description as a string
    """

    value = working_fn(working_list)

    return f'{desc} {value}'

def last_elem_in_list(working_list):
    """
    returns the last element of a list.
    """
    return working_list[-1]

positions = ['QB', 'RB', 'WR', 'TE', 'K', 'DST']

do_to_list(positions, last_elem_in_list, "last element in your list:")
do_to_list([1, 2, 4, 8], last_elem_in_list, "last element in your list:")

do_to_list(positions, len, "length of your list:")

do_to_list([2, 3, 7, 1.3, 5], lambda x: 3*x[0], "first element in your list times 3 is:")

# normally imports like this would be at the top of the file
import os

os.cpu_count()

from os import path

# change this to the location of your data
DATA_DIR = '/Users/nathan/fantasybook/data'
path.join(DATA_DIR, 'adp_2017.csv')
os.path.join(DATA_DIR, 'adp_2017.csv')  # alt if we didn't want to import path
