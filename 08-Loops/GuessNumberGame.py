# Guess number game

import random
print("Guess the generated number between 1-10:")
while(True):
    Gen_num = random.randint(1,10)
    user = int(input("Enter your guess: "))
    if(Gen_num==user):
        print("You win... Generated number is ",Gen_num)
        break
    else:
        print("You lose... Generated number is ",Gen_num)