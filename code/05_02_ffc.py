from bs4 import BeautifulSoup as Soup
import requests
from pandas import DataFrame

ffc_response = requests.get('https://fantasyfootballcalculator.com/adp/ppr/12-team/all/2020')

print(ffc_response.text)

adp_soup = Soup(ffc_response.text)

# adp_soup is a nested tag, so call find_all on it

tables = adp_soup.find_all('table')

# find_all always returns a list, even if there's only one element, which is
# the case here
len(tables)

# get the adp table out of it
adp_table = tables[0]

# adp_table another nested tag, so call find_all again
rows = adp_table.find_all('tr')

# this is a header row
rows[0]

# data rows
first_data_row = rows[1]
first_data_row

# get columns from first_data_row
first_data_row.find_all('td')

# comprehension to get raw data out -- each x is simple tag
[str(x.string) for x in first_data_row.find_all('td')]

# put it in a function
def parse_row(row):
    """
    Take in a tr tag and get the data out of it in the form of a list of
    strings.
    """
    return [str(x.string) for x in row.find_all('td')]

# call function
list_of_parsed_rows = [parse_row(row) for row in rows[1:]]

# put it in a dataframe
df = DataFrame(list_of_parsed_rows)
df.head()

# clean up formatting
df.columns = ['ovr', 'pick', 'name', 'pos', 'team', 'adp', 'std_dev', 'high',
              'low', 'drafted', 'graph']

float_cols =['adp', 'std_dev']
int_cols =['ovr', 'drafted']

df[float_cols] = df[float_cols].astype(float)
df[int_cols] = df[int_cols].astype(int)

df.drop('graph', axis=1, inplace=True)

# done
df.head()

