def add(num1=45,num2=63):
    print("Ans:",num1+num2)
    return num1+num2

sum = add(63,44)
sum1 = add(sum,88)
sum2 = add()

addi = lambda num1,num2:num1+num2
sqrt = lambda n: n**(1/2)
pow = lambda n,power: n**(power)
print(addi(23,100))
print(sqrt(81))
print(pow(2,2))

print(list(range(2,10,2)))

print(round(45.668356,3))