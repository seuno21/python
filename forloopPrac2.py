
"""Print a triangle of stars using a loop. Example for 5 rows:

*
**
***
****
*****"""


i = int (input ("give me a number"))

for i in range (6):
 print("*"*i ) 

 """Count Vowels in a Word

Ask the user to enter a word.

Use a for loop to check each character.

Count how many vowels (a, e, i, o, u) are in the word."""
word = input("enter word").lower()
vowels = "aeiou"
count = 0

for ch in word:
  if ch in vowels:
    count += 1

print("count of vowels",count )


"""Sum of Digits

Ask the user for a number.

Use a for loop to calculate the sum of its digits.

Example: 123 → 1 + 2 + 3 = 6"""

num = int (input("give me a number? "))

innum = "123 = 1 2 3 "
count = 0
 
print("add the vowels", innum)