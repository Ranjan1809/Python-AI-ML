import pandas as pd

# To read the file, we can use the read_csv method from Pandas.
covid_df = pd.read_csv('italy-covid-daywise.csv')

print(covid_df)

'''Data from the file is read and stored in a DataFrame object - one of the core data structures in Pandas for 
storing and working with tabular data. We typically use the _df suffix in the variable names for dataframes.'''

# displays <class 'pandas.core.frame.DataFrame'>
print(type(covid_df))

# We can view some basic information about the data frame using the .info method.
print("Info about the covid dataframe")
print(covid_df.info())

'''It appears that each column contains values of a specific data type. You can view statistical information for 
numerical columns (mean, standard deviation, minimum/maximum values, and the number of non-empty values) using the 
`.describe` method.'''

print(covid_df.describe())
