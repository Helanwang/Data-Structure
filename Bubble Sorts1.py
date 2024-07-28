"""Principle"""

# Swapping two numbers
# Essentially: x, y = y, x

list1 = [34, 25, 12, 22, 11, 64, 90, 5]

j = 0

if list1[j] > list1[j+1]:
    list1[j], list1[j+1] = list1[j+1], list1[j]

print(list1)

"""
if list1[0] > list1[1]:  # compare index number 0 & 1
    list1[0], list1[1] = list1[1], list1[0]  # if index's number value of 0 is greater than index 1, then swap.

if list1[1] > list1[2]:
    list1[1], list1[2] = list1[2], list1[1]

print(list1)
"""

my_array = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(my_array)

for i in range(n-1):  # how many times the loops will go. for outer loops
    for j in range(n-i-1):  # the loops less, bc the highest values of the lists have been arranged in correct order.
        if my_array[j] > my_array[j+1]:
            my_array[j], my_array[j+1] = my_array[j+1], my_array[j]
            print(my_array[j], my_array[j+1])  # show the process

print(my_array)
