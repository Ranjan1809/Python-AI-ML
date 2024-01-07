import seaborn as sns
import matplotlib.pyplot as plt

"""## Heatmap

A heatmap is used to visualize 2-dimensional data like a matrix or a table using colors. The best way to understand 
it is by looking at an example. We'll use another sample dataset from Seaborn, called `flights`, to visualize monthly 
passenger footfall at an airport over 12 years."""

# old syntax doesn't work
# Use new syntax (this syntax)
flights_df = sns.load_dataset("flights").pivot(index='month', columns='year', values='passengers')
print(flights_df)
plt.title("No. of Passengers (1000s)")
sns.heatmap(flights_df)
plt.show()

'''The brighter colors indicate a higher footfall at the airport. By looking at the graph, we can infer two things:

- The footfall at the airport in any given year tends to be the highest around July & August.
- The footfall at the airport in any given month tends to grow year by year.

We can also display the actual values in each block by specifying `annot=True` and using the `cmap` argument to 
change the color palette.'''

plt.title("No. of Passengers (1000s)")
# by default, format of the values will be some float format
# Hence changed the value to decimal in fmt argument
# cmap gives color palette
# annot = true says that values must be displayed inside the graph
sns.heatmap(flights_df, fmt="d", annot=True, cmap='Blues')
plt.show()


