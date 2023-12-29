import numpy as np

arr2 = np.array([[1, 2, 3, 4],
                 [5, 6, 7, 8],
                 [9, 1, 2, 3]])

arr3 = np.array([[11, 12, 13, 14],
                 [15, 16, 17, 18],
                 [19, 11, 12, 13]])

arr4 = np.array([4, 5, 6, 7])

# Adding a scalar
print(arr2 + 3)

# Element-wise subtraction
# Also supports +, %, /
print(arr3 - arr2)

# Array broadcasting
'''Numpy arrays also support broadcasting, allowing arithmetic operations between two arrays with different 
numbers of dimensions but compatible shapes.'''

print("Shape of arr2 and arr4", arr2.shape, arr4.shape)

'''When the expression arr2 + arr4 is evaluated, arr4 (which has the shape (4,)) is replicated three times to match 
the shape (3, 4) of arr2. Numpy performs the replication without actually creating three copies of the smaller 
dimension array, thus improving performance and using lower memory.'''

print("Sum of two arrays of different shapes is", arr2 + arr4)

# arr6 can be broadcasted
arr6 = np.array([7, 8, 9, 10])
print(arr2 + arr6)

# Broadcasting only works if one of the arrays can be replicated to match the other array's shape.
# Here the broadcasting is not possible since (2, ) shape can't be broadcast  to (3,4)
# displays ValueError: operands could not be broadcast together with shapes (3,4) (2,)
arr5 = np.array([7, 8])
print("Array 5 shape is", arr5.shape)
# print(arr2 + arr5)

#  comparisons
arr1 = np.array([[1, 2, 3], [3, 4, 5]])
arr2 = np.array([[2, 2, 3], [1, 2, 5]])

print(arr1 == arr2)
print(arr1 >= arr2)

# gives 3 as output since False evaluates to 0 and True evaluates to 1 in boolean
# sum gives number of True + number of False
# True + False = 3 + 0 = 3
'''Array comparison is frequently used to count the number of equal elements in two arrays using the sum method. 
Remember that True evaluates to 1 and False evaluates to 0 when booleans are used in arithmetic operations.'''
print((arr1 == arr2).sum())
print((arr1 >= arr2).sum())

