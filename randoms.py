# Call random using seed
from random import random, seed, randrange, choice, sample, randint

print("Generate random using a seed")
seed(0)
for i in range(5):
    print(random())

print("\nGenerate a random number between 0 and 10")
print(randrange(0, 10))	

print("\nGenerate random int values between 1 and 10")
for i in range(10):
    print(randint(1, 10), end=',')	

print("\n\nUsing choice and sample")
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_list)
print(choice(my_list))  #choose a number from list
print(sample(my_list, 5))	#Choose 5 number from list 