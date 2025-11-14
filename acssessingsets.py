#accessing sets 

fruit_set = {"apple", "banana", "grapes", "kiwi"}
#access the set item 
for x in fruit_set:
    print(x)

#check is banan item?
print("strawbery" in fruit_set )#false
print("banana" in fruit_set )#true
print("banana" not in fruit_set)

#change item once set is created but you can not change its items 
#but you can add new items 

#adding items in set 

fruit_set  ={"apple", "banana", "grapes", "kiwi"}
print("original set- ",fruit_set)

fruit_set.add("orange")
print("added to the set- ",fruit_set)

fruit_set1= {"apple", "banana"}

fruit_set2 = {"grapes", "kiwi"}

fruit_set1.update(fruit_set2)
print("printing updated fruitset- ", fruit_set1)


"""Task 1: Library Book Check
A librarian wants to make sure no book is entered twice in the library record.
If the book is already there, show a message saying it’s available; otherwise, add it.

Hint: Use a condition to check membership before adding."""


library1= (input("which book would you like to check out today "))
libraryrec = {"avatar", "biography", "fancy nancy","harry potter "}
if library1 in libraryrec:
    print("it’s available")
else: 
    libraryrec.add(library1) 
    print(libraryrec)
    print("book added to library")


print("TASK2")
"""Task 2: Course Enrollment

A student’s record already contains the courses they’ve completed.
Before adding a new course, the system must check whether they’ve already taken it or not.
If not, add it to their record."""

studentcourse = (input("what course will you be adding today?"))
studentcourse1 = {"math", "science", "english", "history"}
if studentcourse in studentcourse1:
    print("class already taken, try again")
else:
    studentcourse1.add(studentcourse)
    print("approved-good luck with your course!")

print("TAST 3")
"""Task 5: Attendance Check

The teacher wants to find out which students were absent today.
You are given the list of all students and the list of students who were present."""

studentt = (input("which student are we checking for?"))
                  
students = {"abigail", "ryan", "seun", "lope", "germine","taylor"}#present students 
students1 ={"abigail", "ryan", "seun", "lope", "germine","taylor","katy", "borris", "nelson","harry "}#full list of students 
if studentt in students:
    print("stuent present")
else:
    print("student absent/missing ")