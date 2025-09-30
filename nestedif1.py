
"""Ask for marks.

If marks ≥ 50 → "Pass"

If marks ≥ 85 → "Pass with Distinction"

Else → "Fail" """

marks = int(input("what are your most recent marks") )

if marks >= 50:
  print("pass")
  if marks>= 85:
   print("passed with distinction")
else:
  print("fail")
