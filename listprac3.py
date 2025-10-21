iphones = ["iphone1", "iphone 2","iphone1","iphone 4","iphone 5"]

print(len(iphones))
print(type(iphones))


#changing items in lists

fruits = ["apples", "plums", "cherries", "mangos"]
print(fruits)
fruits[3] = "cantaloupe"

print(fruits)


fruits2 = ["apples", "plums", "cherries", "mangos"]
print(fruits)
fruits[1:2] = ["cantaloupe", "blackberries"]

fruits3 = ["apples", "plums", "cherries", "mangos"]
fruits3.insert(2, "boisenberry")
print(fruits3)


#Task 4 - create a list of your 5 favorite foods.
#change the last food item to "pizza" and print the updated list .

favFoods = ["sphagetti", "chipotle", "rice", "sandwhiches","jalepenos "]
favFoods[-1] = "pizza"
print(favFoods)