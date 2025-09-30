
"""Weather & umbrella

Ask the user if it is raining (True/False) and if they have an umbrella (True/False).

If it is raining and they have an umbrella → print "You can go outside".

If it is raining but no umbrella → print "Better stay inside".

If it is not raining → print "No need for umbrella". """

raining = True
have_umbrella = True
no_umbrella = False

if have_umbrella and raining:
  print("You can go outside")
  if no_umbrella and raining:
    print("Better stay inside")
else:
  print("no need for an umbrella")