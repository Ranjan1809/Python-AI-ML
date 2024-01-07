import pandas as pd
import matplotlib.pyplot as plt

# To read the file, we can use the read_csv method from Pandas.
covid_df = pd.read_csv('italy-covid-daywise.csv')

# by default pandas doesn't recognize date column as date. Instead it treats it has a plain object
print(covid_df['date'])

# To convert object into date, we can use pandas method
# Now the type is datetime64[ns]
covid_df['date'] = pd.to_datetime(covid_df['date'])
print(covid_df['date'])

# extract year , month, day, weekday
covid_df['year'] = pd.DatetimeIndex(covid_df.date).year
covid_df['month'] = pd.DatetimeIndex(covid_df.date).month
covid_df['day'] = pd.DatetimeIndex(covid_df.date).day
covid_df['weekday'] = pd.DatetimeIndex(covid_df.date).weekday

print(covid_df)

# Query the rows for May
covid_df_may = covid_df[covid_df.month == 5]
print(covid_df_may)

# Extract the subset of columns to be aggregated
covid_df_may_metrics = covid_df_may[['new_cases', 'new_deaths', 'new_tests']]

# Get the column-wise sum
covid_may_totals = covid_df_may_metrics.sum()
print(covid_may_totals)

# Overall average
covid_df.new_cases.mean()

# Average for Sundays
covid_df[covid_df.weekday == 6].new_cases.mean()

covid_month_df = covid_df.groupby('month')[['new_cases', 'new_deaths', 'new_tests']].sum()
print(covid_month_df)

covid_df['total_cases'] = covid_df.new_cases.cumsum()

covid_df['total_deaths'] = covid_df.new_deaths.cumsum()

covid_df['total_tests'] = covid_df.new_tests.cumsum()

import pandas as pd

locations_df = pd.read_csv('locations.csv')

print(locations_df[locations_df['location'] == "Italy"])

'''We can merge this data into our existing data frame by adding more columns. However, to merge two data frames, 
we need at least one common column. Let's insert a `location` column in the `covid_df` dataframe with all values set 
to `"Italy"`.'''

covid_df['location'] = "Italy"
print(covid_df)

# merging is done on the basis of location column which is common column (on = 'location')
merged_df = covid_df.merge(locations_df, on="location")

print("Merged_df", merged_df)
print("covid_df", covid_df)
print("location_df", locations_df)

merged_df['cases_per_million'] = merged_df.total_cases * 1e6 / merged_df.population

merged_df['deaths_per_million'] = merged_df.total_deaths * 1e6 / merged_df.population

merged_df['tests_per_million'] = merged_df.total_tests * 1e6 / merged_df.population

# writing back to file with only required columns
result_df = merged_df[['date',
                       'new_cases',
                       'total_cases',
                       'new_deaths',
                       'total_deaths',
                       'new_tests',
                       'total_tests',
                       'cases_per_million',
                       'deaths_per_million',
                       'tests_per_million']]

print(result_df)

# in order to avoid index column 0,1,2 .. of pandas into the file, we put index = none
result_df.to_csv('results.csv', index=None)


'''
print(result_df.new_cases.plot())
plt.show()

While this plot shows the overall trend, it's hard to tell where the peak occurred, as there are no dates on the 
X-axis. We can use the `date` column as the index for the data frame to address this issue.
print(result_df)

Notice that the index of a data frame doesn't have to be numeric. Using the date as the index also allows us to 
get the data for a specific data using `.loc`.
print(result_df.loc['2020-09-01'])

# Let's plot the new cases & new deaths per day as line graphs.
print(result_df.new_cases.plot())
print(result_df.new_deaths.plot())
plt.show()'''

result_df.set_index('date', inplace=True)
result_df.new_cases.plot()
result_df.new_deaths.plot()

plt.show()
