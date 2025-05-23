# File handling

# Reading files
fp = open("D:/Software/Livewire_notes/Python/14-File-Handling/python.txt",'r')
# fp = open("python.txt",'r')
# print(fp.read())
# print(fp.read(6))
# print(fp.readline())
print(fp.readlines())

# Writing to a file
fp = open("D:/Software/Livewire_notes/Python/14-File-Handling/python.txt",'w')
# fp = open("python.txt",'w')
fp.write("PythonX is the Best. ") # It will overwrite the previous content 

# Appending the file
fp = open("D:/Software/Livewire_notes/Python/14-File-Handling/python.txt",'a')
# fp = open("python.txt",'w')
fp.write("Python has become one among the top languages in the world. ") # It will get added to the previous content 

# closing the file
fp.close()

# File pointer
# tell() method
fp = open("D:/Software/Livewire_notes/Python/14-File-Handling/data.txt",'r')
# fp = open("data.txt",'r')
print("Pointer position before reading:",fp.tell())
fp.read()
print("Pointer position after reading:",fp.tell())
fp.close()

# seek() method
fp = open("D:/Software/Livewire_notes/Python/14-File-Handling/data.txt",'r')
# fp = open("data.txt",'r')
print("Pointer position before seeking:",fp.tell())
fp.seek(5)
print("Pointer position after seeking:",fp.tell())
print(fp.read())
fp.close()

# Reading, list conversion, appending to another file
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

pyopen.close()

# To close file automatically

with open("python.txt",'r') as file1:
        file_stuff = file1.read()
        for line in file1:
            print("Iteration", str(i), ": ", line)
            i = i + 1
    
print(file1.closed)
print(file1.mode)
print(file1.name)
print(file_stuff)

with open("python.txt",'r') as file2:
    i = 0
    for line in file2:
            print("Iteration", str(i), ": ", line)
            i = i + 1
