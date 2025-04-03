#palindrome check

print("Palindrome Check :")
name = input("Enter the string:")
rev_name = ""
for i in range(1,len(name)+1):
    rev_name += name[-i]
print("Given name on reverse:",rev_name)
if(name == rev_name):
    print("Its a palindrome")
else:
    print("Its not a palindrome")