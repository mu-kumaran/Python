
with open("practice.txt",'r') as file1:
    file_stuff = file1.read()
    
print(file1.closed)
print(file1.mode)
print(file1.name)
print(file_stuff)
