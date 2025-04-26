dataopen = open("data.txt",'r+')
pyopen = open("python.txt","a+")
data = dataopen.read()
lst = data.split("\n")
print(type(data))
print(data)
print(lst)

for i in lst:
    pyopen.write("\n")
    pyopen.write(i)

dataopen.close()
pyopen.close()

pyopen = open("python.txt",'r')
py = pyopen.read()
print(py)