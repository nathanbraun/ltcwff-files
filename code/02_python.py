##############
# basic python
# v0.0.3
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

my_roster_a_only = [
    x.title() for x in my_roster_list if x.startswith('a')]
my_roster_a_only

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

def over_100_total_yds(rush_yds, rec_yds):
    """
    multi line strings in python are between three double quotes

    it's not required, but the convention is to put what the fn does in one of
    these multi line strings (called "docstring") right away in function

    when you type over_100_total_yds? in the REPL, it shows this docstring

    this function takes rushing, receiving yards, adds them, and returns a bool
    indicating whether they're more than 100 or not
    """
    return rush_yds + rec_yds > 100

# print(rush_yds)  # commented out since it shows an error

def noisy_over_100_total_yds(rush_yds, rec_yds):
    """
    this function takes rushing, recieving yards, adds them, and returns a bool
    indicating whether they're more than 100 or not

    it also prints rush_yds
    """
    print(rush_yds)
    return rush_yds + rec_yds > 100

over_100_total_yds(60, 39)
noisy_over_100_total_yds(84, 32)

def over_100_total_yds_wdefault(rush_yds=0, rec_yds=0):
    """
    this function takes rushing, receiving yards, adds them, and returns a bool
    indicating whether they're more than 100 or not

    if a value for rushing or receiving yards is not entered, it'll default to 0
    """
    return rush_yds + rec_yds > 100

over_100_total_yds_wdefault(92)
over_100_total_yds(92)

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
