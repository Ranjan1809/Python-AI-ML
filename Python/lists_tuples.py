List = [1, 2, 3, 4, 5, 6, 7]
List2 = [8, 9, 10]
List3 = [11, 12, 13, 14, 15]

print(List[0])
print(List[1])
print(List[2])
print(List[3])
# Slicing the elements
print(List[0:6])
# By default, the index value is 0 so its starts from the 0th element and go for index -1 (displays [1,2,3,4,5,6])

# displays all elements
print(List[:])

# displays [3, 4, 5]
print(List[2:5])

# Here, 1 is starting index , 6 is ending index, 2 is the gap
# displays [2, 4, 6]
print(List[1:6:2])

# displays last element
# negative indexing
# displays 7 6
print(List[-1], List[-2])

# displays [5, 6, 7]
print(List[-3:])

# displays [1, 2, 3, 4, 5, 6]
print(List[:-1])

# displays [5, 6]
print(List[-3:-1])

# reverses the list
print("After reversing", List[::-1])

List.append(List2)

# displays After appending List2 to List, List has [1, 2, 3, 4, 5, 6, 7, [8, 9, 10]]
print("After appending List2 to List, List has", List)

# Here this works since we appended List2 to List. Hence, List2 will be present as whole in List.
List.remove(List2)

# displays [1, 2, 3, 4, 5, 6, 7]
print(List)

List.extend(List2)

# displays [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(List)

# you can also append list using + operator
List += List3
print("Adding List3 elements to List using + operator", List)

# This will throw error since List2 will be de-structured and added as individual elements to List while using extend
# List.remove(List2)

# Insert value at given index
List.insert(0, 1000)

print(List)

# removes the last element
# displays [8, 9]
List2.pop()
print(List2)

# removes 9
List2.remove(9)
print(List2)

# clears the list
# displays []
List2.clear()
print(List2)

''' tuples are similar to lists
 Difference is that tuples are immutable meaning they can't be modified once created
 While Lists are mutable meaning they can be modified once created '''

t1 = (2, 3)
print(t1)
print(type(t1))

# displays tuple' object doesn't support item deletion
# del t1[1]

# entire tuple can be deleted
del t1

# after deleting tuple, displays name 't1' is not defined when trying to print
# deleted tuple
# print(t1)

# This is built in function called sorted. Used to sort list and tuples
L = ["cccc", "b", "dd", "aaa"]
print("Normal sort :", sorted(L))
# Sorts based on length
print("Sort with len :", sorted(L, key=len))

T = ("Ranjan", "apple", "ball", "great")
# Sorts based on length
print(sorted(T, key=len))
