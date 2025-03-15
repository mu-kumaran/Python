# Traffic light coding
print("Traffic light coding:")
light = input("Enter the colour of the signal: ")
if light=="green" or light=="green" or light=="GREEN":
    print("Please Keep Going")
elif light=="yellow" or light=="Yellow" or light=="YELLOW":
    print("Please go slow")
else:
    print("Please stop")

# Maximum of three

user1 = 9
user2 = 4
user3 = 7
if(user1>user2 and user1>user3):
    print("user1 is maximum")
elif(user2>user1 and user2>user3):
    print("user2 is maximum")
else:
    print("user3 is maximum")

# odd or even check
num = int(input("Enter the number: "))
if(num%2 == 0):
    print("An even number")
else:
    print("An odd number")
