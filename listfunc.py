
""" TASK 1:
Create a list of your 5 favorite fruits.
Make a copy of that list using the copy() method.
Change one fruit in the copied list and print both lists"""

favfoods = ["sphagetti", "pizza", "chipotle", "soup"]
copyfavfoods = favfoods.copy()
copyfavfoods [1] = "fried chicken"
print(favfoods)
print(copyfavfoods)

print("TASK 2 ")
"""Make a list of numbers from 1 to 5. Create another list using slicing ([:]). 
Add one more number to the new list and show that the original didn’t change."""

num = [1, 2, 3, 4, 5]
newnum = num[:]
newnum.append(6)
print("original", num)
print("tamperd version", newnum)

print("Task 3")
"""Make a list of colors: ["red", "green", "blue", "yellow"]. Reverse the list using the reverse() method"""

colors = ["red", "green", "blue", "yellow"]
print("originasl", colors)
colors.reverse()
print("reversed", colors)