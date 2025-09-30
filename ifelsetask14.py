
"""
Write a Python program using the boolean data type to check if a student can sit in an exam.

Use two boolean variables:

paid_fees → True if the student has paid exam fees, otherwise False.
has_admit_card → True if the student has an admit card, otherwise False.

If the student has paid fees and has the admit card, print "You can sit in the exam".
If the student has paid fees but does not have the admit card, print "Collect your admit card".
Otherwise, print "You are not allowed to sit in the exam"."""


paid_fees = input("Have paid exam fee? ")

if paid_fees == "True":
  paid_fees = True
else:
  paid_fees = False


has_admit_card = input("do you have an admit card? ")

#convert teh string into boolean
if has_admit_card == "True":
  has_admit_card = True
else:
  has_admit_card = False

if paid_fees and has_admit_card:
  print("You can sit in the exam")
elif paid_fees and not has_admit_card:
  print("Collect your admit card")
else:
  print("You are not allowed to sit in the exam")