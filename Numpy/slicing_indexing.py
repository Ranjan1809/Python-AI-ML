import numpy as np

arr3 = np.array([
    [[11, 12, 13, 14],
     [13, 14, 15, 19]],

    [[15, 16, 17, 21],
     [63, 92, 36, 18]],

    [[98, 32, 81, 23],
     [17, 18, 19.5, 43]]])

print(arr3.shape)

# accessing the required elements
print(arr3[2])
print(arr3[1][1])
# or
print(arr3[1, 1])

print(arr3[1][1][2])
# or
print(arr3[1, 1, 2])

print(arr3[1:, 0:1, :2])

print(arr3[:2, 1])

# gives error
# displays IndexError: too many indices for array: array is 3-dimensional, but 4 were indexed
# print(arr3[1, 3, 2, 1])
