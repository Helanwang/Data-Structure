# Task: find the lowest value in the list
# list1 = [42, 76, 59, 33, 87, 23, 15, 91, 72, 38, 19, 63, 8, 53, 99, 4, 67, 28, 50, 11]

list1 = [42, 76, 59, 33, 87, 23, 15, 91, 72, 38, 19, 63, 8, 53, 99, 4, 67, 28, 50, 11]

minvalue = list1[0]

for i in list1:  # I refer to each item on the list
    if i < minvalue:
        minvalue = i
        print(minvalue)

print(f"The lowest value is {minvalue}")

# Find the highest value on the given list.

list2 = [5, 12, 7, 45, 22, 9, 34, 56, 18, 29, 47, 3, 67, 23, 89, 14, 31, 21, 37, 41]
highest_value = list2[0]

for i in list2:
    if i > highest_value:
        highest_value = i
        print(highest_value)

print(f"the highest value is {highest_value}")
