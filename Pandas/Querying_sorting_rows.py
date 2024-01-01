import pandas as pd

# To read the file, we can use the read_csv method from Pandas.
covid_df = pd.read_csv('italy-covid-daywise.csv')

print(covid_df)

# find out the day having greater than 1000 cases
# returns complete list with true or false flag
high_new_cases = covid_df['new_cases'] > 1000
print(high_new_cases)

# in order to get desired output in form of subset of df
print(covid_df['new_cases'])
print(covid_df[high_new_cases])
# or
print(covid_df[covid_df['new_cases'] > 1000])

positive_rate = 0.05206657403227681

'''We can also formulate more complex queries that involve multiple columns. As an example, let's try to determine 
the days when the ratio of cases reported to tests conducted is higher than the overall positive_rate'''




