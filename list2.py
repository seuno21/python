
list1 = ["item1", "item2", "item3", "item 4"]
print(list1)

#lenghth of list
print(len(list1))

list2 = ["item1", "item2", "item3", "item 4"]
#index - address(indexes starts from  zero )- to access the data in the list 

print(list2[3])

#access the list 
grocery = ["milk", "eggs","bread","jam","butter", "grapes",]

#negative indexing 
print(grocery[-2])

#range of indexes
print(grocery[:5])
print("the range from index 1 to 5 ", grocery[:5])

# check if items exist 
if "milk" in grocery:
    print("yes milk is in the list ")


#create dicnationary in python and access their words and whats is the first word and last word.

dictionary = ["apples", "airplanes", "airlines","alleigence", "application", "alteration","auditions", "autism", "alighnment"]
print(dictionary)
print(len(dictionary))
print("the dictionary begins and ends with the words- ", dictionary[0], dictionary[-1])