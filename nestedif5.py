
"""Library access

Ask the user if they are a student (True/False) and if they have a library card (True/False).

If both are True, print "You can borrow books".

If student is True but no card, print "Get a library card first".

If not a student, print "Library access denied"."""

student = False
libraryCard = False

if student and libraryCard:
  print("you can borrow books")
elif student and not libraryCard:
  print("get a library card first")
else:
  print("library access denied")