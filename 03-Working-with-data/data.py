# variables

country = "India"
name = "mano"
mobile_brand = "samsung"

print(country,name,mobile_brand)
print(country+name+mobile_brand)

#data types

name = "John"       #String
age = 23            #Integer - int
bodyTemp = 98.4     #Float
ROI = 2.5           #Float
number = 3+5j       #complex
isLoggedIn = True   #bool
isLoggedOut = False #bool
result = 5>10

print(name,age,bodyTemp,ROI,number)
print(isLoggedIn,isLoggedOut)
print(result)

#multi-line string

quote = """ Lore ipsum  adsfkj asfasdfjkndf adsdsv asdloijlkmae aer vpkj v aesfjkzxcv aesfASDFJNV ASDFJNMADFLKXCasdfgxcv 
asdfklm asdfkmnd  APOEKJCDVM  asefmsdf asdfj PEOFMASDF pomja EPOK A;EMASDFGLK DFSA;PSVC[Pl P;[ASJDF ASDLKMVNMLASEF ASDLK]]
ASDLKMN ;lj;lkm., b;p;olmkas, ;[a;lmdf ;as;dllmads;lm mgp;okja;lmds ;ljmasd;f dscv;lmj., ;lmasd;lm,ac;.,mvjasdf;lmdsf;lmd]
"""

print(quote)

#type() function

print(type(name))
print(type(age))
print(type(bodyTemp))
print(type(number))
print(type(result))
print(type(isLoggedIn))

#input() function

ur_name = input("Enter your name: ")
ur_age = input("Enter your age: ")
print("Your name is " + ur_name)
print("Your age is " + ur_age)
print(type(ur_age)) #accept input as string

#type conversion method

ur_age = int(input("Enter your age: "))
temp = float(input("enter the temperature: "))
print("Your age is ", ur_age)
print(type(ur_age)) #accept input as integer
print(type(temp)) #accept input as float

