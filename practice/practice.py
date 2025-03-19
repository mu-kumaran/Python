first_name = "manoj"
last_name = "kumar"
full_name = " ".join([first_name,last_name])
age = 33
print("Hello",first_name+last_name)
print("Hello","+".join([first_name,last_name]))

string1 = "Hello {}. You are {} years old".format(full_name,age)
string2 = "Hello {fname}. You are {age} years old".format(fname=full_name,age=age)
string3 = "Hello {0}. You are {1} years old".format(full_name,age)
string4 = f"Hello {full_name}. You are {age} years old"
string5 = f"Hello {first_name+" "+last_name}. You are {age+45} years old"

print(string1)
print(string2)
print(string3)
print(string4)
print(string5)

name = full_name
print(name[0],name[1],name[2],name[3],name[4],name[5],name[6])
print(name[-1],name[-2],name[-3],name[-4],name[-5],name[-6])