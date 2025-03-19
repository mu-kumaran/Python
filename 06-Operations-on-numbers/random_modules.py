# Random modules
import random
print("Random functions")
print(random.random())
print(random.randint(1,100))
print(random.randint(100,150))
print(random.randrange(1,10))
print(random.randrange(1,10,2))
print(random.randrange(100,150,5))

# understanding step size in randrange
# values are kept apart by step size w
# Here 10 is the limit where output always produced lesser than the limit
print("With step size 2") # possible values 1,3,5,7,9
print(random.randrange(1,10,2))
print(random.randrange(1,10,2))
print(random.randrange(1,10,2))
print(random.randrange(1,10,2))
print("With step size 3") # possible values 1,4,7
print(random.randrange(1,10,3))
print(random.randrange(1,10,3))
print(random.randrange(1,10,3))
print(random.randrange(1,10,3))

lst = [12,34,45,67,89,92]
print(l)
print(random.choice(lst))
random.shuffle(lst)     #This method changes the original list, it does not return a new list.
print(l)

