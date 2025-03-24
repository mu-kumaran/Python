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

# seek() method
fp = open("D:/Software/Livewire_notes/Python/14-File-Handling/data.txt",'r')
# fp = open("data.txt",'r')
print("Pointer position before seeking:",fp.tell())
fp.seek(5)
print("Pointer position after seeking:",fp.tell())
print(fp.read())
fp.close()

