
"""Write a Python code to:

Ask the user to enter their marks (0-100).

Print "Grade: A" if marks are 90 or above.

Print "Grade: B" if marks are 80-89.

Print "Grade: C" if marks are 70-79.

Otherwise, print "Grade: F"""

Grade= int(input("what score did yiu receive on this most recent exam "))

if Grade >= 91:
  print("Grade A")
elif Grade >= 81 and Grade <= 89 :
  print("Grade B")
elif Grade <= 80 and Grade >= 70 :
  print("Grade C")
elif Grade < 50 :
  print("Grade F")
else:
  print("please input valid number")



