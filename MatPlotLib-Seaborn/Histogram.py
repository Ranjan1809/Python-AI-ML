import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
# Load data into a Pandas dataframe
flowers_df = sns.load_dataset("iris")

print(flowers_df.sepal_width)

# Histogram is used to show graph of single columns
# Example there will be lot of values in a column and histogram will create range of those values for that column
# Ex Name = Ranjan, Ranjan2 , Rahul , ABc ,Xyz
# histogram will create range of A-to some point, R to some point, x to some point and pull respective values
# in that

sns.set_style("darkgrid")
plt.title("Distribution of Sepal Width")
plt.hist(flowers_df.sepal_width)
plt.show()

# Specifying the number of bins
# bins meaning number of towers in the graph
plt.hist(flowers_df.sepal_width, bins=5)
plt.show()

# Multiple histograms

setosa_df = flowers_df[flowers_df.species == 'setosa']
versicolor_df = flowers_df[flowers_df.species == 'versicolor']
virginica_df = flowers_df[flowers_df.species == 'virginica']

plt.hist(setosa_df.sepal_width, alpha=0.4, bins=np.arange(2, 5, 0.25))
plt.hist(versicolor_df.sepal_width, alpha=0.4, bins=np.arange(2, 5, 0.25))
plt.hist(virginica_df.sepal_width, alpha=0.4, bins=np.arange(2, 5, 0.25))

plt.show()

# We can also stack multiple histograms on top of one another.

plt.title('Distribution of Sepal Width')

plt.hist([setosa_df.sepal_width, versicolor_df.sepal_width, virginica_df.sepal_width],
         bins=np.arange(2, 5, 0.25),
         stacked=True)

plt.legend(['Setosa', 'Versicolor'])

plt.show()
