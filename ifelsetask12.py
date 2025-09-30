
"""Check age and student status

Ask the user for their age and if they are a student (True/False).

If age is less than 18 and student is True, print "School Student".

If age is between 18 and 25 and student is True, print "College Student".

Otherwise, print "Not a Student"."""

age = int(input("how old are you  "))
student = True


if age < 18 and student:
  print("School Student")
elif age >= 18 and age <= 25 and student:
  print("College Student")
else:
  print("Not a Student")
