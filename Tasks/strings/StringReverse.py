# String reverse

print("String Reversal")
name = input("Enter the string:")
rev_name = ""
for i in range(1,len(name)+1):
    rev_name += name[-i]
print("Reverse of given string:",rev_name)