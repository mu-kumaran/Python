# Workouts

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
print("")

name = full_name
print(name[0],name[1],name[2],name[3],name[4],name[5],name[6])
print(name[-1],name[-2],name[-3],name[-4],name[-5],name[-6])
print("")

print(name)
print(name[0::])
print(name[0:5])
print(name[6:])
print(name[1::2])
print(name[0:5:2])
print("")

name = 'manojkumar890'
name1 = 'MANOJ KUMAR'
alpnum = 'dfkjn123)(*)' 

print(name.capitalize())
print(name1.capitalize())
print(name.upper())
print(name1.lower())
print(name1.count('A'))
print(name1.count('M'))
print(name1.count('N'))
print(name1.index('N'))
print(name1.index('M'))
print(name1.index('A'))
print(name1.find('N'))
print(name1.find('M'))
print(name1.find('A'))
print(name.replace('kumar','harshan'))
print(name.isalpha())
print(name.isalnum())
print(alpnum.isalnum())
print(name1.isalnum())
print(name1.isalpha())
print("")

print(len(name))
print(len(name1))
print(len(alpnum))
print("")

print(name*2)
print(name1*3)
print("")

print("mano" in name)
print("890" not in name)
print("KUM" in name1)
