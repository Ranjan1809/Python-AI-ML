"""## Bar Chart

Bar charts are quite similar to line charts, i.e., they show a sequence of values. However, a bar is shown for each
value, rather than points connected by lines. We can use the `plt.bar` function to draw a bar chart."""
import seaborn as sns
import matplotlib.pyplot as plt

years = range(2000, 2006)
apples = [0.35, 0.6, 0.9, 0.8, 0.65, 0.8]
oranges = [0.4, 0.8, 0.9, 0.7, 0.6, 0.8]

plt.bar(years, oranges)

plt.show()

plt.bar(years, apples)
plt.bar(years, oranges, bottom=apples)
plt.show()

tips_df = sns.load_dataset("tips")
print(tips_df)

sns.barplot(x='day', y='total_bill', data=tips_df)
plt.show()
'''The lines cutting each bar represent the amount of variation in the values. For instance, it seems like the 
variation in the total bill is relatively high on Fridays and low on Saturday.

We can also specify a `hue` argument to compare bar plots side-by-side based on a third feature, e.g., sex.'''