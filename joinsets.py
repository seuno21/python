
#Union - The union() method returns a new set with all items from both sets.

set1 = {"a", "b", "c", "d"}

set2 = {1, 2, 3}

set3 = set1.union(set2) 
print("Using Union Function ",set3)

set4 = set1 | set2
print("Using | operator ", set4)


#list - Ordered, changable, Duplicated allowed
list1 = (1, 2, 3)
list2 = ("a", "b", "c", "d")

list3 = list1 +list2
print("Adding list1 and 2 hsing + operator: ", list3)


#Join Multiple sets 
set1 = {"a", "b", "c", "d"}

set2 = {1, 2, 3}

set3 = {"John", "Elena"}

set4= {"apple", "banana", "kiwi"}

myset2 = set1.union(set2, set3, set4)
print(myset2)

#When using the | operator, separate the sets with more | operators:
myset2 = set1 | set2 | set3 |set4
print(myset2)

# Join a Set and a list
set1 = {1, 2, 3, 5}
list1 = ("a", "b", "c", "d")

Join = set1.union(list1)
print(Join)


#The update() method inserts the items in set2 into set1:
set1 = {"a", "b" ,"c",  "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

#Both union() and update() will exclude any duplicate items.

"""Task 1: Combine Friend Lists 

You and your best friend have different friend circles.
You want to see all unique friends you both know.

"""
freinds1 = {"allen","lee","gerald","susan","micheal","edgar"}
freinds2 = {"ali","rodrick","benson","sierra","emily"}
print(freinds1)
print(freinds2)
freinds3 =freinds1.union(freinds2)
print(freinds3)

"""TASK 2- Merge Product Categories
An online store has two separate lists of product categories:
existing and new ones.
You want to add the new categories into the existing list.
"""
print("TASK 2")

inventory2020 = {"toys","clothes","baby bottles","food","birthing items"}
print(inventory2020)
new_inventory = {"notebooks","snacks","lunchbags","pencil bags","headphones"}
inventory2020.update(new_inventory)
print(inventory2020)


"""TASK 3 - Two students have different subjects in their semester.
You want to list all unique subjects both are studying."""

print("TASK 3 ")

sheryl = {"algebra","art appreciation","geograoghy"}
print("sheryls classes",sheryl)
jack = {"calculus","choir","history 101"}
print( "jacks classes",jack)
classes = sheryl.union(jack)
print(classes)

"""Task 4: Combine Weekend & Holiday Activities

You have two sets:
Activities planned for the weekend
Activities planned for holidays
Create a single list of all unique activities.
"""
print("TASK 4!!!")
weekendact = {"television","movies","mall","roller skating"}
print(weekendact)
holidayact ={"travel","roadtrip","ski","eat good food"}
print(holidayact)
alluniqueactivities = weekendact.union(holidayact)
print("ALL TOGETHER NOW ",alluniqueactivities)


"""
Task 5: Merge Event Guests
Two events happened this week, each with different guest lists.
You need a final list showing everyone who attended either event."""

print("TASK5")

eventGuest = {"joclyn","katy","rachel","josh"}
eventGuest2 = {"gibril","mathew","jacob"}
allGuests = eventGuest.union(eventGuest2)
print (allGuests)