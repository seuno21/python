"""Write a Python program to ask a user to enter a number and print whether it
 is positive, negative, or zero.Write a Python program to ask a user to enter the day number
 (1–7) and print the corresponding day name (Monday, Tuesday … Sunday).
"""
number = int(input("pick a number between 1 and 7:"))

if number == 1:
  print("monday")
elif number == 2:
  print("tuesday")
elif number == 3:
  print("wenesday")
elif number == 4:
  print("thursday")
elif number == 5:
  print("friday")
elif number == 6:
  print("saturday")
elif number == 7:
  print("sunday")
else:
  print("try to enter 1 through 7")

