"""Write a Python program to ask a user to enter their age and print their life stage: "Child" (0–12), "Teen" (13–19), "Adult" (20–59), "Senior" (60+)."""
age =int(input("how old are you"))

if age <= 12:
  print("child")
elif age <= 13 or age <= 19:
  print("teen")
elif age <=20 or age <=59:
  print("adult")
elif age <= 60:
  print("senior")
else:
  print("decrepid")


