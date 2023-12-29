import urllib.request
import numpy as np

# Urllib is a module in python that is used for handling urls and their responses like get,post responses
# urlretrieve of request is used to download required file from required url
# request.urlopen only opens the required url and doesn't download the file from url
urllib.request.urlretrieve(
    'https://gist.github.com/BirajCoder/a4ffcb76fd6fb221d76ac2ee2b8584e9/raw/4054f90adfd361b7aa4255e99c2e874664094cea'
    '/climate.csv',
    'climate.txt')

# genfromtxt converts the datapoints from climate.txt file to numpy array
# we need to specify delimiter which separates the datapoints
# If delimiter prop is not specified , then the output will be nan values
# skip header is used to indicate that we don't need 1 line of the file
# climate.txt contains temperature,rainfall,humidity at first line which is not required

# You can also use loadtxt method
# But to use loadtxt method all datapoints in a file must be of same data type
# while genfromtxt supports mixed datatypes as well
climate_data = np.genfromtxt("climate.txt", delimiter=",", skip_header=1)
print(climate_data, climate_data.shape)

weights = np.array([0.3, 0.2, 0.5])

yields = climate_data @ weights

print(yields, yields.shape)

# Let's add the yields to climate_data as a fourth column using the np.concatenate function.

# both the arrays in concatenate method must have same dimensions or else you will get this error ValueError: all the
'''input arrays must have same number of dimensions, but the array at index 0 has 2 dimension(s) and the array at 
   index 1 has 1 dimension(s)'''

# axis = 1 means you want to concatenate here [[...here],[...here],[..here]...for all 10000 rows]
# axis = 0 means you want to concatenate here [[],[]... here]
climate_results = np.concatenate((climate_data, yields.reshape(10000, 1)), axis=1)
print(climate_results)

# write the output to new file

# fmt is used because by default this code creates all datapoints with many digits after the decimal points
# hence fmt '%.2f' rounds of all datapoints to 2 digits after the decimal point

# delimiter puts , between all datapoints of a row

# header will generate header in the file

'''comments is used because by default header generates header in the file as comments
   # temperature,rainfall,humidity,apple_yield '''
# Hence to remove this comment , we give comment prop as '' empty

np.savetxt('climate_results.txt',
           climate_results,
           fmt='%.2f',
           delimiter=',',
           header='temperature,rainfall,humidity,apple_yield',
           comments='')
