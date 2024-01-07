import seaborn as sns
import matplotlib.pyplot as plt
"""## Scatter Plot

In a scatter plot, the values of 2 variables are plotted as points on a 2-dimensional grid. Additionally, 
you can also use a third variable to determine the size or color of the points. Let's try out an example.

The [Iris flower dataset](https://en.wikipedia.org/wiki/Iris_flower_data_set) provides sample measurements of sepals 
and petals for three species of flowers. The Iris dataset is included with the Seaborn library and can be loaded as a 
Pandas data frame"""

# Load data into a Pandas dataframe
flowers_df = sns.load_dataset("iris")
print(flowers_df)

# to identify different species
print(flowers_df['species'].unique())

plt.plot(flowers_df.sepal_length, flowers_df.sepal_width)
plt.show()

'''The output is not very informative as there are too many combinations of the two properties within the dataset. 
There doesn't seem to be simple relationship between them.

We can use a scatter plot to visualize how sepal length & sepal width vary using the `scatterplot` function from the 
`seaborn` module (imported as `sns`).'''

sns.scatterplot(x=flowers_df.sepal_length, y=flowers_df.sepal_width)
plt.show()

'''### Adding Hues

Notice how the points in the above plot seem to form distinct clusters with some outliers. We can color the dots 
using the flower species as a `hue`. We can also make the points larger using the `s` argument.'''

sns.scatterplot(x=flowers_df.sepal_length,y=flowers_df.sepal_width,hue=flowers_df.species)
plt.show()

'''### Customizing Seaborn Figures

Since Seaborn uses Matplotlib's plotting functions internally, we can use functions like `plt.figure` and `plt.title` 
to modify the figure.'''

sns.set_style("darkgrid")
plt.figure(figsize=(12, 6))
plt.title('Sepal Dimensions')

sns.scatterplot(x=flowers_df.sepal_length,
                y=flowers_df.sepal_width,
                hue=flowers_df.species,
                s=100)
plt.show()

'''### Plotting using Pandas Data Frames

Seaborn has in-built support for Pandas data frames. Instead of passing each column as a series, you can provide 
column names and use the `data` argument to specify a data frame.'''

plt.title('Sepal Dimensions')
sns.scatterplot(x='sepal_length',
                y='sepal_width',
                hue='species',
                s=100,
                data=flowers_df)
plt.show()
