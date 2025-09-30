
"""Write a Python program to ask a user to enter a month number (1–12) and print the season: "Winter", "Spring", "Summer", or "Autumn"."""

month = int(input("what is a month number: "))

if month >=1 and month <=3:
  print("winter")
elif month >= 3 and month <= 6:
  print("spring")
elif month >= 6 and month <= 9:
  print("summer")
elif month >= 9 and month <= 12:
  print("fall")
else:
  print("try again")

  month
