import numpy as np

# The shapes can be in form of tuples or lists "doesn't matter"
# All zeros
arr = np.zeros((3, 2))
arr1 = np.zeros([3, 2])
print(arr)
print(arr1)

#  All ones
arr2 = np.ones([2, 2, 3])
print(arr2)

# Identity matrix
identity_matrix = np.eye(3)
print(identity_matrix)

# Fixed value

# Fixed value
fixed_arr = np.full([2, 3], 42)
print(fixed_arr)

# Range with start, end and step
range_arr = np.arange(10, 90, 3)
print(range_arr)

print(range_arr.shape)

# You can also reshape the array
# shape

print(range_arr.reshape(9, 1, 3))

# Equally spaced numbers in a range
# This method will give specified number of digits between specified range
# For ex:, in this example, it gives 50 equally spaced numbers between 10-100
print(np.linspace(10, 100, 20))
