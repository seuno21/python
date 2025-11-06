
list1 = ["a","b", "c", "d "]
list2 = [1, 2, 3, 4 ]

list3 = list1 + list2
print(list3)

#check for both list are both are characters 

list1 = ["a","b", "c", "d "]
list2 = [1, 2, 3, 4 ]

for x in list2:
    list1.append(x)
print(list1)

list1 = ["a","b", "c", "d "]
list2 = [1, 2, 3, 4 ]

list1.extend(list2)
print(list1)

list1 = ["a","b", "c", "d "]
list2 = [1, 2, 3, 4 ]

list.extend
print(list2)

print("TASK 5")
""" TASK 5:
Sort Numbers (Ascending & Descending)

Question:
Create a list of numbers: [12, 4, 8, 2, 10]. 
Sort the list in ascending order, then in descending order.
"""
numbers = [12, 4, 8, 2, 10]
numbers.sort()
print(numbers)
numbers.sort(reverse = True)
print(numbers)