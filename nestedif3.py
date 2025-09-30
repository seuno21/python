
"""Movie Ticket Discount

Input age.

If age < 18:

If age < 5 → "Free Ticket"

Else → "Child Discount Ticket"

Else if age ≥ 60 → "Senior Citizen Discount"

Otherwise → "Normal Ticket Price" """


ticketAge = int (input("how old are you "))

if ticketAge > 18 or ticketAge <60:
  print("adult")
  if ticketAge < 5:
    print("free ticket")
elif ticketAge > 60:
   print("senior citizen discount")
elif ticketAge <18:
   print("child discount ticket")
else:
  print("normal ticket price ")
