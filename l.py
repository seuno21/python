
"""sheryl = {"algebra","art appreciation","geograoghy"}
jack = {"calculus","choir","history 101"}
sheryl_jack = sheryl.union(jack)
print(sheryl_jack)"""


sheryl = {"algebra","art appreciation","geograoghy"}
print("sheryls classes",sheryl)
jack = {"calculus","choir","history 101"}
print( "jacks classes",jack)
classes = sheryl.union(jack)
print(classes)

print("TASK 4!!!")
weekendact = {"television","movies","mall","roller skating"}
print(weekendact)
holidayact ={"travel","roadtrip","ski","eat good food"}
print(holidayact)
alluniqueactivities = weekendact.union(holidayact)
print("ALL TOGETHER NOW ",alluniqueactivities)



assighnment1  = {"charlie","kennedy","jackson","savannah"}
assighnment2 = {"charlie","jackson"}
goodstudents = assighnment1.intersection(assighnment2)
print(goodstudents)