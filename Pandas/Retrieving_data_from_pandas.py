import pandas as pd

# To read the file, we can use the read_csv method from Pandas.
covid_df = pd.read_csv('italy-covid-daywise.csv')

print(covid_df)

# Pandas format is similar to this
# They store data in this format. Hence to access something from dataframe , keep this format in mind.
covid_data_dict = {
    'date': ['2020-08-30', '2020-08-31', '2020-09-01', '2020-09-02', '2020-09-03'],
    'new_cases': [1444, 1365, 996, 975, 1326],
    'new_deaths': [1, 4, 6, 8, 6],
    'new_tests': [53541, 42583, 54395, None, None]
}

'''# Pandas format is not similar to this
covid_data_list = [
    {'date': '2020-08-30', 'new_cases': 1444, 'new_deaths': 1, 'new_tests': 53541},
    {'date': '2020-08-31', 'new_cases': 1365, 'new_deaths': 4, 'new_tests': 42583},
    {'date': '2020-09-01', 'new_cases': 996, 'new_deaths': 6, 'new_tests': 54395},
    {'date': '2020-09-02', 'new_cases': 975, 'new_deaths': 8 },
    {'date': '2020-09-03', 'new_cases': 1326, 'new_deaths': 6},
]'''

# Keeping the above analogy in mind , you can now retrieve the required data in following ways

print("To access new_cases column from data_frame\n", covid_df['new_cases'])

'''Each column is represented using a data structure called Series, 
   which is essentially a numpy array with some extra methods and properties.'''

'''Each column is represented using a data structure called Series, which is essentially a numpy array with some 
extra methods and properties.'''

# Each column has a series datatype
print(type(covid_df['new_cases']))

# to access any index
print(covid_df['new_cases'][243])
print(covid_df['new_cases'][246])

# Pandas also provides the .at method to retrieve the element at a specific row & column directly.
print(covid_df.at[246, 'new_cases'])

'''Instead of using the indexing notation `[]`, Pandas also allows accessing columns as properties of the dataframe 
using the `.` notation. However, this method only works for columns whose names do not contain spaces or special 
characters.'''
print(covid_df.new_cases)

# Further, you can also pass a list of columns within the indexing notation `[]`
# to access a subset of the data frame with just the given columns.

# displays dataframe of just given columns and all of it's rows
cases_df = covid_df[['date', 'new_cases']]
print(cases_df)

# Even though we have used another df to hold data that is cases_df , both will be pointing to same location
# in memory.
# In order to prevent actual df from getting affected by modifying this df,
# we have to use some technique like spreading objects into another object in js
# This can be done by copy method in python

covid_df_copy = covid_df.copy()
# Now, The data within covid_df_copy is completely separate from covid_df, and changing values inside one of them
# will not affect the other.

# To access a specific row of data, Pandas provides the `.loc` method.
# This entire row will be series object
print(covid_df.loc[243])

# We can use the .head and .tail methods to view the first or last few rows of data.
print(covid_df.head(50), "\n", covid_df.tail(10))

# We can find the first index that doesn't contain a NaN value using a column's first_valid_index method.
print(covid_df.new_tests.first_valid_index())

# aWe can pick sample rows from df using smaple method
# even though it picks random rows, we will still get their exact indexes
# this feature is more advantageous compared to lists properties which returns indexes as 0, 1, 2 ...

# Notice that even though we have taken a random sample, each row's original index is preserved - this is a useful
# property of data frames.
print(covid_df.sample(5))

# to calculate sum of the given column
print(covid_df['new_cases'].sum())
print(covid_df.new_cases.sum())

total_cases = covid_df['new_cases'].sum()
total_deaths = covid_df['new_deaths'].sum()

death_rate = total_deaths/total_cases
print("The death rate is {:.2f} percent.".format(death_rate*100))

