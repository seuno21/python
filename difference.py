
set1 = {"aaple", "banana", "kiwi"}
set2 = {"microsoft", "apple", "HP"}

set3 = set1.difference(set2)
print(set3)


set3 = {6, 7, 8, 9}
set4 = {1, 2, "a", "b", "c", 9}

setResult = set3.difference(set4)
print(setResult)


#You can use the - operator instead of the difference() method, and you will get the same result.

setResult2 = set3 - set4
print(setResult)


#The - operator only allows you to join sets with sets, 
#and not with other data types like you can with the difference() method.
#Use the difference_update() method to keep the items that are not present in both sets:

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)

print(set1)

