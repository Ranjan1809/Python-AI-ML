import matplotlib.markers
import matplotlib.pyplot as plt
import seaborn as sns

# Line chart
yield_apples = [0.895, 0.91, 0.919, 0.926, 0.929, 0.931]
plt.plot(yield_apples)

# used to show graphs. May not be required in case of jupyter notebooks
plt.show()

'''### Customizing the X-axis
The X-axis of the plot currently shows list element indexes 0 to 5. The plot would be more informative if we could 
display the year for which we're plotting the data. We can do this by two arguments `plt.plot`.'''

years = [2010, 2011, 2012, 2013, 2014, 2015]
yield_apples = [0.895, 0.91, 0.919, 0.926, 0.929, 0.931]

plt.plot(years, yield_apples)
plt.show()

'''### Axis Labels

We can add labels to the axes to show what each axis represents using the `plt.xlabel` and `plt.ylabel` methods.'''

plt.plot(years, yield_apples)
plt.xlabel('Year')
plt.ylabel('Yield (tons per hectare)')
plt.show()

'''### Plotting Multiple Lines

You can invoke the `plt.plot` function once for each line to plot multiple lines in the same graph. Let's compare the 
yields of apples vs. oranges in Kanto.'''

years = range(2000, 2012)
apples = [0.895, 0.91, 0.919, 0.926, 0.929, 0.931, 0.934, 0.936, 0.937, 0.9375, 0.9372, 0.939]
oranges = [0.962, 0.941, 0.930, 0.923, 0.918, 0.908, 0.907, 0.904, 0.901, 0.898, 0.9, 0.896, ]

plt.plot(years, apples)
plt.plot(years, oranges)
plt.xlabel('Year')
plt.ylabel('Yield (tons per hectare)')

'''### Chart Title and  Legend

To differentiate between multiple lines, we can include a legend within the graph using the `plt.legend` function. We 
can also set a title for the chart using the `plt.title` function.'''

plt.title("Crop Yields in Kanto")
plt.legend(['Apples', 'Oranges'])
plt.show()

'''### Line Markers

We can also show markers for the data points on each line using the `marker` argument of `plt.plot`. Matplotlib 
provides many different markers, like a circle, cross, square, diamond, etc. You can find the full list of marker 
types here: https://matplotlib.org/3.1.1/api/markers_api.html .'''

plt.plot(years, apples, marker="x")
plt.plot(years, oranges,marker="o")
plt.xlabel('Year')
plt.ylabel('Yield (tons per hectare)')
plt.title("Crop Yields in Kanto")
plt.legend(['Apples', 'Oranges'])
plt.show()

'''### Styling Lines and Markers

The `plt.plot` function supports many arguments for styling lines and markers:

- `color` or `c`: Set the color of the line ([supported colors](https://matplotlib.org/3.1.0/gallery/color/named_colors.html))
- `linestyle` or `ls`: Choose between a solid or dashed line
- `linewidth` or `lw`: Set the width of a line
- `markersize` or `ms`: Set the size of markers
- `markeredgecolor` or `mec`: Set the edge color for markers
- `markeredgewidth` or `mew`: Set the edge width for markers
- `markerfacecolor` or `mfc`: Set the fill color for markers
- `alpha`: Opacity of the plot


Check out the documentation for `plt.plot` to learn more: [
https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot](
https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot) .'''

plt.plot(years, apples, marker='s', c='b', ls='-', lw=2, ms=8, mew=2, mec='navy')
plt.plot(years, oranges, marker='o', c='r', ls='--', lw=3, ms=10, alpha=.5)

plt.xlabel('Year')
plt.ylabel('Yield (tons per hectare)')

plt.title("Crop Yields in Kanto")
plt.legend(['Apples', 'Oranges'])
plt.show()

'''The `fmt` argument provides a shorthand for specifying the marker shape, line style, and line color. It can be provided as the third argument to `plt.plot`.

```
fmt = '[marker][line][color]'
```
'''

plt.plot(years, apples, 's-b')
plt.plot(years, oranges, 'o--r')

plt.xlabel('Year')
plt.ylabel('Yield (tons per hectare)')

plt.title("Crop Yields in Kanto")
plt.legend(['Apples', 'Oranges'])
plt.show()

'''### Improving Default Styles using Seaborn

An easy way to make your charts look beautiful is to use some default styles from the Seaborn library. These can be 
applied globally using the `sns.set_style` function. You can see a full list of predefined styles here: 
https://seaborn.pydata.org/generated/seaborn.set_style.html .'''

sns.set_style("whitegrid")
plt.plot(years, apples, 's-b')
plt.plot(years, oranges, 'o--r')

plt.xlabel('Year')
plt.ylabel('Yield (tons per hectare)')

plt.title("Crop Yields in Kanto")
plt.legend(['Apples', 'Oranges'])
plt.show()

# with dark grid

sns.set_style("darkgrid")
plt.plot(years, apples, 's-b')
plt.plot(years, oranges, 'o--r')

plt.xlabel('Year')
plt.ylabel('Yield (tons per hectare)')

plt.title("Crop Yields in Kanto")
plt.legend(['Apples', 'Oranges'])
plt.show()

