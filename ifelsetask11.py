
"""Online shopping discount

Ask the user if they are a member (True/False) and how much they spent.

If they are a member and spent more than 500, print "20% Discount".

If they are a member but spent less than 500, print "10% Discount".

If they are not a member, print "No Discount". """


member = True
spending = int(input("how much did you spend"))

if member and spending > 500:
  print("20% Discount")
elif member and spending < 500:
  print("10% Discount")
else:
  print("no discount")