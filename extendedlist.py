
#extend list 
fruit =["apple","banana","kiwi"]
print(fruit)

tropical = ["mango","pineapple","papaya"]
fruit.extend(tropical)
print(fruit)

print("PRACTICING REMOVE NOW ")
#remove 
fruit = ["apple","banana","kiwi"]
print(fruit)

fruit.remove("banana")
print(fruit)

print("PRAC.remove function occurence  ")
#remove function occurence 

fruit = ["apple","banana","kiwi","banana"]
print(fruit)

fruit.remove("banana")
print(fruit)


print("ndex ---> address of items ")
#index ---> address of items 
fruit = ["apple","banana","kiwi","banana"]
print(fruit)

fruit.pop(1)
print(fruit)

print("pop()")
fruit = ["apple","banana","kiwi","banana"]
print(fruit)

print("del")
fruit = ["apple","banana","kiwi","banana"]
del fruit[1:5]
print(fruit)
 
 #clear list 
fruit = ["apple","banana","kiwi","banana"]
fruit.clear()
print(fruit )

print("task time")
#TASKS 
"""TASK 1: 
You went grocery shopping and made this list:
grocery = ["milk", "bread", "eggs", "chips", "butter"]
You realize you already have "chips" at home.
Remove "chips" from the list and print the updated grocery list."""

grocery = ["milk", "bread", "eggs", "chips", "butter"]
grocery.remove("chips")
print(grocery)


print("TASK 2")
"""TASK 2: You created a to-do list:

tasks = ["study", "exercise", "cook", "watch TV"]
You finished "study", so remove it from the list and print what’s left to do.
"""
tasks = ["study", "exercise", "cook", "watch TV"]
tasks.remove("study")
print(tasks)

print("TASK 3")
"""Task 3:
Your list of friends going to a party:
friends = ["Ali", "Sara", "Ahmed", "Fatima"]
One friend, the last one, cancels."""

friends = ["Ali", "Sara", "Ahmed", "Fatima"]
friends.pop(-1)
print(friends)

print("TASK 4")
"""You have a list of weekend plans:

plans = ["movie", "shopping", "picnic", "gym"]


You decide not to go to the second plan (index 1).
Use pop(1) to remove it and print the updated plans."""

plans = ["movie", "shopping", "picnic", "gym"]
plans.pop(1)
print(plans)

print("TASK 5")
"""TASK 5: 

You have a list of your favorite songs:

songs = ["Perfect", "Faded", "Believer", "Shape of You"
Remove the last song and store it in a variable called removed_song.

Then print:  Removed song: Shape of You"""

songs = ["Perfect", "Faded", "Believer", "Shape of You"]
removed_songs = songs.pop()
print(songs)
print(removed_songs)

print("task6")
"""TASK 6:
You have a list of school subjects:
subjects = ["Math", "Science", "English"]

Your teacher adds a new subject "Computer" after "Math".
Add it in the correct position."""
subjects = ["Math", "Science", "English"]
subjects.insert(1, "computers")
print(subjects)

print("TASK 7")
"""You are creating a playlist:

playlist = ["song1", "song2", "song4"]

You forgot to add "song3" after "song2".
Use LIST functions to fix your playlist.
keep"""
playlist = ["song1", "song2", "song4"]
playlist.insert(2, "song3")
print(playlist)

print("TASK 8 ")
"""Task 8:
In your team list:

team = ["Ali", "Sara", "Omar"]
A new member "Fatima" joins and should be at the start of the list.
Use appr. LIST funtion and print the updated team."""
team = ["Ali", "Sara", "Omar"]
team.insert(0,"fatima")
print(team)


print("TASK 9")
"""Task 9:
You made a shopping cart:

cart = ["shoes", "bag", "dress", "watch"]
After checkout, you want to empty the cart."""
cart = ["shoes", "bag", "dress", "watch"]
print("before shopping", cart)
cart.clear()
print("after shopping", cart)


print("task 9")
"""Task 10:
You created a list of tasks for today:
tasks = ["email client", "finish report", "clean desk"]
At the end of the day, clear all tasks and print a message like:
All tasks completed!"""
tasks = ["email client", "finish report", "clean desk"]
print("before", tasks)
tasks.clear()
print("All tasks completed!!", tasks)

print("TASK 11")
"""Task 11:
Create a list of books you want to read.
Add two new books using insert()
Remove one using remove()
Use pop() to take the last one as the book you’ll read today
Clear the list after finishing all books
Sample Output:
After inserting new books: ['The Alchemist', 'Deep Work', 'Atomic Habits', 'Think Like a Monk', 'The Power of Now']
After removing one book: ['The Alchemist', 'Deep Work', 'Atomic Habits', 'Think Like a Monk']
Book to read today: Think Like a Monk
Book list after clearing: []"""
books = ["harry potter", "dork diaries","wimx club"]
print("original", books )
books.insert(1, "dr.suess")
books.insert(2, "red queen")
print("insert function-", books )
books.remove("dr.suess")
print(books)
readToday = books.pop() 
print(readToday)
