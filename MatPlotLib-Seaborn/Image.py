# Before displaying an image, it has to be read into memory using the `PIL` module.
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img = Image.open('chart.jpg')

'''An image loaded using PIL is simply a 3-dimensional numpy array containing pixel intensities for the red, 
green & blue (RGB) channels of the image. We can convert the image into an array using `np.array`.'''

img_array = np.array(img)
print(img_array.shape)
print(img_array)
plt.imshow(img)
plt.show()

# To display a part of the image, we can simply select a slice from the numpy array.
plt.imshow(img_array[125:325, 105:305])
plt.show()