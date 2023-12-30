import numpy as np

kanto = np.array([73, 67, 43])
weights = np.array([0.3, 0.2, 0.5])

print(kanto.shape, weights.shape)

print(np.matmul(kanto, weights))
# displays [73 67 43] <class 'numpy.ndarray'>
print(kanto, type(kanto))

# performs dot product of 2 matrices
print(np.dot(kanto, weights))

# The above operation can also be done by another way using numpy
# performs element wise multiplication
# ex: [73*3 67*0.2 43*0.5]
matrix = kanto * weights

# displays [21.9 13.4 21.5]
print(matrix)

# displays 56.8
print(matrix.sum())

# using matmul
# displays 56.8
print("You can also perform above operation using matmul function instead of dot function", np.matmul(kanto, weights))

# 2D numpy arrays
climate_data = np.array([[73, 67, 43],
                         [91, 88, 64],
                         [87, 134, 58],
                         [102, 43, 37],
                         [69, 96, 70]])
print("2D numpy array\n", climate_data)

# displays Shape gives dimension of the numpy array and the dimensions will be in form of tuples (5, 3) <class 'tuple'>
print("Shape gives dimension of the numpy array and the dimensions will be in form of tuples",
      climate_data.shape, type(climate_data.shape))

# 3D numpy arrays

# 3D array
arr3 = np.array([
    [[11, 12, 13],
     [13, 14, 15]],
    [[15, 16, 17],
     [17, 18, 19.5]]])

print(arr3.shape, type(arr3.shape))

print("All the elements in a numpy array have the same data type.")
print("If an array contains even a single floating point number, all the other elements are also converted to floats.")
print("Using dtype, you can find out the data type of values in numpy arrays", arr3.dtype, climate_data.dtype)

print("All the below 3 ways give same result")

# There are some differences in matmul , @ and dot functions
# For now 1 difference is @ and matmul doesn't allow scalar multiplication while dot does
print(np.dot(climate_data, weights))
print(np.matmul(climate_data, weights))
print(climate_data @ weights)
# displays ValueError: matmul: Input operand 1 does not have enough dimensions (has 0, gufunc core with signature (
# n?,k),(k,m?)->(n?,m?) requires 1)
# print(np.matmul(weights, 5))

# displays ValueError: matmul: Input operand 1 does not have enough dimensions (has 0, gufunc core with signature (n?,k),(k,
# m?)->(n?,m?) requires 1)
# print(weights @ 5)

# But dot product does scalar multiplication
print(np.dot(weights, 5))
