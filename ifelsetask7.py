from typing import OrderedDict
#Write a Python program that asks the user to enter a number.
#The program should check whether the number is even or odd and then print the result.

number = int(input("please enter a number?: "))

if number % 2 == 0:
  print("even number")
else:
  print("odd number")
