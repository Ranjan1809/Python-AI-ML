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

# positive_rate = 0.05206657403227681

'''We can also formulate more complex queries that involve multiple columns. As an example, let's try to determine 
the days when the ratio of cases reported to tests conducted is higher than the overall positive_rate'''

# We can also add new column using below code
covid_df['positive_rate'] = covid_df.new_cases / covid_df.new_tests
print(covid_df)

# You can also remove column if not required
# if you use inplace = true , it modifies the original df and returns none
# if you use inplace = false (default) , it returns a new df which is modified but doesn't effect the old df
c = covid_df.drop(columns="positive_rate")

print(covid_df)
print(c)

covid_df.drop(columns="positive_rate", inplace=True)
print(covid_df)

# sorting
print(covid_df.sort_values('new_deaths', ascending=False).head(10))
print(covid_df.sort_values('new_cases').head(10))

# we need to modify negative value -148.0 for new_cases sort
# .at method can be used for modification
covid_df.at[172, 'new_cases'] = (covid_df.at[171, 'new_cases'] + covid_df.at[173, 'new_cases'])/2
print(covid_df.sort_values('new_cases').head(10))

