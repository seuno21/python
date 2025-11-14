"""TASK 1 - 
You have two sets of friends:
Find the students who are friends in both classes.
"""

#Intersection 

"""The intersection() method will return a new set, that only contains 
the items that are present in both sets.

Keep ONLY the duplicates

"""
set1 = {"apple", "banana", "kiwi"}
set2 = {"google", "microsoft", "apple"}  

set3 = set1.intersection(set2)
print(set3)

#You can use the & operator instead of the intersection() method, and you will get the same result.

set1 = {"apple", "banana", "kiwi"}
set2 = {"google", "microsoft", "apple"}  

set3 = set1 & set2
print(set3)


#The & operator only allows you to join sets with sets, 
#and not with other data types like you can with the intersection() method.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)

print(set1)


#The values True and 1 are considered the same value. The same goes for False and 0.
set4 = {"apple", 1,  "banana", 0, "cherry"}
set5 = {False, "google", 1, "apple", 2, True}

set6 = set4.intersection(set5)

print(set6)

"""TASK 1 - 
You have two sets of friends:
Find the students who are friends in both classes.
"""
friends = {"rachel","ross","phoebe","joey","chandler"}
friends2 = {"meredith","christina","phoebe","joey","chandler"}

allMyfreinds = friends.intersection(friends2)
print(allMyfreinds)

"""TASK 2 - 
You have two sets of students:
Find the students who play both sports.
Find the students who play only football.
"""
print("TASK2")

DoubleAthlete = {"william","jashua","becham","cynthia","ashley"}
footballplayers = {"jashua","ryan","landon","cynthia","ashley"}
footballplayers1 = footballplayers.intersection(DoubleAthlete)
print(footballplayers1)
footballplayers.difference_update(DoubleAthlete)
print(footballplayers)


"""TASK 3 - 
Two branches of a library have different book collections:
Find the books available in both branches.
Find the books that are only available in Branch A.
"""

print("TASK3")

branchA ={"harry potter","how to kill a mocking bird","dork diaries","diary of a wimpy kid"}
brancB = {"fancy nancy","harry potter","judie b jones","dork diaries"}
branchs = branchA.intersection(brancB)
print(branchs)
branchA.difference_update(brancB)
print(branchA)

"""TASK 6 - 
Two groups of people were asked about their favorite fruits:
Find fruits liked by both groups.
Find fruits liked only by the first group.
Find fruits liked only by the second group.
"""
print("TASK 6")

group1 = {"plums","bananas","mangos","strawberries"}
group2 ={"pineapple","guava","jackfruit","mangos","strawberries"}
groups = group1.intersection(group2)
print("both groups like- ",groups)
only1 = group1.difference(group2)
print("only group1 likes- ", only1 )
only2 = group2.difference(group1)
print("only group2 likes these- ", only2)

"""TASLK 7 - 
A teacher keeps track of students who submitted each assignment:
Find students who submitted both assignments.
Find students who missed the second assignment.
"""
print("TASK7")

assighnment1  = {"charlie","kennedy","jackson","savannah"}
assighnment2 = {"charlie","jackson"}
goodstudents = assighnment1.intersection(assighnment2)
print("studnets who submitted all there work", goodstudents)
students = assighnment1 - assighnment2 
print("students who didint turn in ass.2- ", students)


"""TASK 8 - 
A university offers several courses. Some students are enrolled in multiple courses.
You have the following sets:

data_science = {"Ali", "Sara", "Hassan", "Fatima", "Omar"}
machine_learning = {"Fatima", "Omar", "Zara", "Bilal"}
ai_course = {"Sara", "Omar", "Hassan", "Zara", "Nida"}

Find students who are enrolled in all three courses.
Find students who are enrolled in Data Science and Machine Learning, but not in AI.
Find students who are in AI only (not in the other two).
"""

print("TASK 8")
data_science = {"Ali", "Sara", "Hassan", "Fatima", "Omar"}
machine_learning = {"Fatima", "Omar", "Zara", "Bilal"}
ai_course = {"Sara", "Omar", "Hassan", "Zara", "Nida"}
enrolled3 = data_science.intersection(machine_learning,ai_course)
print("the students who enrolled in 3 courses: ",enrolled3)
dataAi = data_science.intersection(machine_learning)
print("people only enrolled in data and ai: ", dataAi)
Aionly = ai_course.difference(data_science,machine_learning)
print( "she is in AI only: ",Aionly)

# convert using operators  | , & ,  -