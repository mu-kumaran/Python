# change collector

coin1 = 1
coin2 = 2
coin3 = 5
amt = int(input("Enter the amount for which you need a change: "))
total = 0
c1=c2=c3 = 0
while(total<=amt):
    if total<amt:
        total  = total + coin1+coin2+coin3
        c1 = c1 + coin1
        c2 = c2 + coin2
        c3 = c3 + coin3
    elif total == amt:
        break
print("Change collected =",total)
print("1 rupee -",c1/1,"coins")
print("2 rupee -",c2/2,"coins")
print("5 rupee -",c3/5,"coins")