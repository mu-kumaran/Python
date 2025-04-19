# change collector
import math
coins = [20,10,5,2,1]
amt = int(input("Enter the amount for which you need a change: "))
if(amt>coins[2]):
    coin20 = math.floor(amt/coins[2])
    bal3 = amt%coins[2]
print(coin20,bal3)


# total = 0
# c1=c2=c3 = 0
# while(total<=amt):
#     if total<amt:
#         total  = total + coin1+coin2+coin3
#         c1 = c1 + coin1
#         c2 = c2 + coin2
#         c3 = c3 + coin3
#     elif total == amt:
#         break
# print("Change collected =",total)
# print("1 rupee -",c1/1,"coins")
# print("2 rupee -",c2/2,"coins")
# print("5 rupee -",c3/5,"coins")

# algo:
# eg: 256 rs
# 1st step: if 256>=20
# 256/20   Q = 12 coins bal= 16 rs
# 2nd step: if 16>=10
# 16/10     Q = 1 coin bal = 6 rs
# 3rd step: if 6>=5
# 6/5       Q = 1 coin bal = 1 rupee
# 4th step: if 1>=2
# skip 
# 5th step: if 1>=1 
# 1/1         Q = 1 coin bal = 0 rupee