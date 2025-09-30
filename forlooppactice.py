
for counter in range(1,11):
    print(counter)

#Print squares of numbers 1–5
 
for counter in range(1,5): 
    print(counter*counter)

for counter in range (2,20):
    print(counter % 2 )

word = "happyday"
for letter in word:
    print(letter)

    """Print numbers 1 to 10

1. Print numbers 1 to 10
2. Print squares of numbers 1–5
3. Print even numbers between 2 and 20
4. Print each letter of a word """
#repeats a block of code a fixed number of times.
for num in range (1,20):
    if num %2 == 0:
     print ("even number", num)


#Task 2: Print numbers from 1 to N (user input)

N = int(input("give me a number any number"))
for N in range(1,N):
    print("-", N)     

#Task 3: Print multiplication table of a number (user input)

Num = int(input("give me another number"))
for counter in range (1,12):
    print(Num, "X", counter, "=",Num*counter)
