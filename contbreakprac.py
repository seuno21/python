
# number game with break and continue
for i in range(1, 11):
    if i == 5:
      print("skipping number 5(continue)")
      continue 
    if i == 8:
      print("stopping the loop at number 8(breal)")
      break

    print("current nuumber is",i)

print("loop finished")



#TASK 1
"""A teacher is taking attendance for 10 students.

If roll number 5 comes, print "Lunch break! Stop attendance" and use break to end the loop.

Otherwise, print "Present: Student <roll number>".
keep"""

for i in range(1, 10):
   if i == 5:
    print("Lunch break! Stop attendance(BREAK)")
    break

   print("Present: Student <roll number",i)


#Task 2
"""Print days of the week (1–7).

If it’s day 7 (Sunday), print "Skipping Sunday" and use continue.

Print all other days as "Working day <day>"."""
dayName = input("what number is today")
for dayName in range (1,8):
  if dayName == 7:
    print("skipping sunday")
    continue
  print ("working day", dayName)
  


  #TASK 3
  """Ask the user for 5 numbers.

If you find the first even number, print "Found an even number: <number>" and stop using break.

If it’s odd, keep checking."""

for num in range(1,6):
  Num = int(input("give me a number between 1 and 5"))
  if Num %2 == 0 :
    print("found the first even number",Num)
    break 
  else:
      print("its odd keep checking")



for dayName in range (1,8):
  dayName = input("what number is today")
  if dayName == 7:
    print("skipping sunday")
    continue
  
  print("working day", dayName)


  for day in range(1, 8):  
    day = int(input("ENter a number here?"))
    if day == 7:
        print("Skipping Sunday")
        continue
    print("Working day", day)