# multiplication table
print("multiplication table:")
num = int(input("Enter the number for you need multiplication table: "))
for i in range(1,11):
    print(num,"x",i,"=",num*i)


#generating even numbers for the given range
print("Generating even numbers:")
num = int(input("Enter the range within even numbers to be generated:"))
i=0
while(i<=num):
    if((i*2)<=num):
        print(i*2)
        i = i+1
    else:
        break

#Another logic
j=0
while(j<=num):
    if j%2 == 0:
        print(j)
    j=j+1