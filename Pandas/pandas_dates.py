import pandas as pd

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

print("Practice session")
