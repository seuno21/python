from pickle import REDUCE
"""Write a Python program to ask a user to enter a traffic light color
 (red, yellow, green) and print the action: "Stop", "Ready", or "Go"."""

trafficLight =input("what color is the traffic light red green or yellow")

if trafficLight == "red":
  print("stop")
elif trafficLight == "green":
  print("go")
elif trafficLight == "yellow":
  print("ready")
else:
  print("try again")


