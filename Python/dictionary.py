dictionary = {
    "Name": "Ranjan",
    "Age": 22,
    "Year": 2023
}

print(dictionary.get("Name"))

# If the key is not available, it will display the message next to the invalid key
print(dictionary.get("company", "Can't find this key. Please enter a valid key"))

Employee = {"Name": "John", "Age": 29, "salary": 25000, "Company": "GOOGLE"}

# displays dict_items([('Name', 'John'), ('Age', 29), ('salary', 25000), ('Company', 'GOOGLE')])
# The below line displays list of tuples
items = Employee.items()
print(items)

# displays dict_keys(['Name', 'Age', 'salary', 'Company'])
# The below line displays list of keys
keys = Employee.keys()
print(keys)

# displays dict_values(['John', 29, 25000, 'GOOGLE'])
# The below line displays list of values
values = Employee.values()
print(values)

for x in Employee.values():
    print(x, type(x))

""" In each iteration, Employee.items() return key-value pair as tuples
 displays
 ('Name', 'John') <class 'tuple'>
 ('Age', 29) <class 'tuple'>
 ('salary', 25000) <class 'tuple'>
 ('Company', 'GOOGLE') <class 'tuple'> """

for x in Employee.items():
    print(x, type(x))

NewEmployee = Employee.popitem()
print(Employee, NewEmployee)
