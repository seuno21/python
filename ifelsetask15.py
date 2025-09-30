
"""Gym Entry

Ask if the user has a membership (yes/no).

Ask if the user has paid the monthly fee (yes/no).

If both are yes → "Welcome to the gym".

If membership is yes but fee not paid → "Please pay your fee".

If no membership → "You need to register first".
keep
Pinned"""


gym_mem = input("do you have a gym membership true/false? ")
month_fee = input("have you paid the monthly free true/false")

if gym_mem == True and month_fee == True:
  print ("welcome to the gym!!!")
  if gym_mem == True and month_fee == False:
    print("please pay your fee")
else:
  print("you need to register first")
  