
"""ATM Withdrawal

Ask user for PIN.

If PIN is correct:

Ask withdrawal amount.

If amount ≤ balance → "Transaction Successful"

Else → "Insufficient Balance"

Else → "Wrong PIN" """

pin = int(input("what is your  4 digit pincopde "))
balance = 1000
withdrawlAmount = int(input("what is your withdrawl amount"))

if pin == 2323:
  print("what is your withdrawl amount")
  if withdrawlAmount <= 1000 or withdrawlAmount >= 1:
    print("withdrawl succesful  ",withdrawlAmount)
else:
 print("insufficient balance")
 