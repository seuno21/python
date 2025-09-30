
"""Question 4: Candy Distribution

You have 10 candies to give.
If you reach candy number 7, stop distribution (break) with message "No more candies left".
Skip candy number 3 with message "Candy 3 is broken, skipping" (continue).
Print the rest normally."""

for i in range(1,10):
 if i == 3:
    print("Candy 3 is broken, skipping")
    continue 
 if i == 7:
    print("No more candies left")
    break 
 else:
   print("-", i)

"""Question 5: ATM PIN Entry

A user has 3 chances to enter the correct PIN (say 1234).
If the user enters the correct PIN, print "Access granted" and stop.
If not, continue asking until 3 tries are over.
After 3 wrong tries, print "Card blocked"""


for attempt in range(3):
  pin =int (input("what is security pin? "))
  if pin == 1234:
    print("Access granted")
    break 
  else:
    print("try again")
 
  if attempt == 3:
        print("Card blocked")

"""Reverse Countdown

Print numbers from 10 down to 1 using a loop.

After printing all numbers, print "Blast off!"."""

for i in range(10, 1, -1):
  print(i)
  
print("blast off")