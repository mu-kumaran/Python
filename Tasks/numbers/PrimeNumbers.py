#Prime Numbers
print("Prime number check")
num = int(input("Enter the number:"))
if(num <= 1):
    print("Its not a prime")
else:
    for i in range(2,num):   
        if(i**2<=num):
            if(num%i==0):
                print(f"Its not a prime. It is divisible by {i}")
                break
    else:
        print("Its a prime number")
    

# else:
#     for i in range(2,int(num**0.5)+1):   

#             if(num%i==0):
#                 print(f"Its not a prime. It is divisible by {i}")
#                 break
#     else:
#         print("Its a prime number")
    