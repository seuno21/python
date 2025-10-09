
"""
list - lists are used to store multiple items in a asingle variable. 
lists is the one of the data types in python
"""

"""list items - list items are orderd ,changeable,and allow duplicate values.

list items are indeed the first item has index [0],
the second item has index[1] etc.

1. Ordered
When we say that lists are ordered, it means that the items have a defined order, 
and that order will not change.
If you add new items to a list, the new items will be placed at the end of the list.

2. Changeable
The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

3. Allow Duplicates
Since lists are indexed, lists can have items with the same value:

Example
Lists allow duplicate values:
"""
fruitlist = ["apple","banana","orange","watermelon"]

print(fruitlist)
print(len(fruitlist))

#TASK 1 - CREATE A LIST OF YOUR FAVORITE SUBJECTS AND CALCULATE LIST LENGHTH 

subjects = ["science","history","music","dance"]
print("my favorite subjects are- ",subjects)
print("subject list is", len(subjects))

#Task 2  - create a shopping list

shoppingList = ["pants","shirts","shoes","hangers"]
print("my shopping list is ",shoppingList )