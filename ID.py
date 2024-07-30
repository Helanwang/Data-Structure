"""
id(): id refers to the built-in function id().
This function returns a unique integer that represents the identity of an object.
Represents the memory address of the object.
"""

list1 = [1, 2, 3]
print(id(list1[0]))
print(id(list1[1]))
print(id(list1[2]))

print(id(list1))


a = 12
b = 12
c = 14

print(id(a) == id(b))  # Output: True
print(id(c) == id(a))   # Ouput: False
