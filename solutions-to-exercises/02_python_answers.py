"""
Answers to the end of chapter exercises for Python chapter.

Questions with written (not code) answers are inside triple quotes.
"""

###############################################################################
# 2.1
###############################################################################
"""
a) Valid. Python programmers often start variables with `_` if they're
throwaway or temporary, short term variables.
b) Valid.
c) Not valid. Can't start with a number.
d) Valid, though convention is to split words with _, not camelCase.
e) `rb1_name`. Valid. Numbers OK as long as they're not in the first spot
f) `flex spot name`. Not valid. No spaces
g) `@home_or_away`. Not valid. Only non alphnumeric character allowed is `_`
h) `'pts_per_rec_yd'`. Not valid. A string (wrapped in quotes), not a
variable name. Again, only non alphnumeric character allowed is `_`
"""

###############################################################################
# 2.2
###############################################################################
weekly_points = 100
weekly_points = weekly_points + 28
weekly_points = weekly_points + 5

weekly_points # 133

###############################################################################
# 2.3
###############################################################################
def for_the_td(player1, player2):
    return f'{player1} to {player2} for the td!'

for_the_td('Dak', 'Zeke')

###############################################################################
# 2.4
###############################################################################
"""
It's a string method, so what might `islower()` in the context of a string?
I'd say it probably returns whether or not the string is lowercase.

A function "is *something*" usually returns a yes or no answer (is it
something or not), which would mean it returns a boolean.

We can test it like:
"""

'tom brady'.islower()  # should return True
'Tom Brady'.islower()  # should return False

###############################################################################
# 2.5
###############################################################################
def is_leveon(player):
    return player.replace("'", '').lower() == 'leveon bell'

is_leveon('tom brady')
is_leveon("Le'Veon Bell")
is_leveon("LEVEON BELL")

###############################################################################
# 2.6
###############################################################################
def commentary(score):
    if score >= 100:
        return f'{score} is a good score'
    else:
        return f"{score}'s not that good"

commentary(90)
commentary(200)

###############################################################################
# 2.7
###############################################################################
giants_roster = ['Daniel Jones', 'Saquon Barkley', 'Evan Engram', 'OBJ']

giants_roster[0:3]
giants_roster[:3]
giants_roster[:-1]
[x for x in giants_roster if x != 'OBJ']
[x for x in giants_roster if x in ['Daniel Jones', 'Saquon Barkley',
                                   'Evan Engram']]

###############################################################################
# 2.8
###############################################################################
league_settings = {'number_of_teams': 12, 'ppr': True}

# a
league_settings['number_of_teams'] = 10
league_settings

# b
def toggle_ppr(settings):
    settings['ppr'] = not settings['ppr']
    return settings

toggle_ppr(league_settings)

###############################################################################
# 2.9
###############################################################################
"""
a) No. `'has_a_flex'` hasn't been defined.
b) No, `number_of_teams` is a variable that hasn't been defined, the key is
`'number_of_teams'`.
c) Yes.
"""

###############################################################################
# 2.10
###############################################################################
my_roster_list = ['tom brady', 'adrian peterson', 'antonio brown']

# a
for x in my_roster_list:
  print(x.split(' ')[-1])

# b
{player: len(player) for player in my_roster_list}

###############################################################################
# 2.11
###############################################################################
my_roster_dict = {
    'qb': 'tom brady', 'rb1': 'adrian peterson', 'wr1': 'davante adams', 'wr2':
    'john brown'}

# a
[pos for pos in my_roster_dict]

# b
[player for _, player in my_roster_dict.items()
    if player.split(' ')[-1][0] in ['a', 'b']]

###############################################################################
# 2.12
###############################################################################
# a
def mapper(my_list, my_function):
  return [my_function(x) for x in my_list]

# b
list_of_rushing_yds = [1, 110, 60, 4, 0, 0, 0]

mapper(list_of_rushing_yds, lambda x: x*0.1)
